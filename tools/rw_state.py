#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rw_state.py — Đọc MỘT file save RimWorld (.rws) bất kì và in ra "STATE FULL":
bản mô tả tình trạng đầy đủ, có phân tích, đủ để một AI (hoặc người) hiểu 100%
chuyện gì đang xảy ra và lập kế hoạch — mà không phải mở game.

Dùng:
    python3 rw_state.py <save.rws> [out.md]
    python3 rw_state.py <save.rws> --stdout      # in thẳng ra màn hình
    python3 rw_state.py <save.rws> --no-grid      # bỏ phần giải mã lưới (nhanh hơn)

Nguyên tắc:
  * KHÔNG hard-code map này: tự dò kích thước map, số map, phe người chơi, mod, DLC.
  * Mọi khối đều bọc try/except: save lạ/thiếu DLC/v1.4–1.6 đều không làm sập script.
  * Giữ nguyên văn mọi thứ "đổi được quyết định"; phần thừa (cỏ, rác, thú hoang,
    lịch sử vụn) thì hợp nhất thành bảng đếm/toạ độ.
"""
import base64
import math
import os
import re
import statistics
import struct
import sys
import zlib
from collections import Counter, defaultdict

# ----------------------------------------------------------------- tiện ích
def block(s, tag):
    """Nội dung (đã gồm thẻ) của khối <tag> ... </tag> đầu tiên."""
    i = s.find('<%s>' % tag)
    if i < 0:
        return ''
    j = s.find('</%s>' % tag, i)
    return s[i:j + len(tag) + 3] if j > 0 else ''


def block_in(s, tag, lo=0, hi=None):
    i = s.find('<%s>' % tag, lo, hi)
    if i < 0:
        return ''
    j = s.find('</%s>' % tag, i, hi)
    return s[i:j + len(tag) + 3] if j > 0 else ''


def spans(s, tag):
    """Danh sách (start,end) của mọi phần tử <tag ...>…</tag> (kể cả lồng nhau)."""
    out, depth, cur = [], 0, 0
    op = re.compile(r'<%s[ >]' % tag)
    cl = '</%s>' % tag
    for m in re.finditer(r'<%s[ >]|</%s>' % (tag, tag), s):
        if m.group().startswith('<%s' % tag):
            if depth == 0:
                cur = m.start()
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                out.append((cur, m.end()))
    return out


def clean(txt, limit=None):
    t = (txt or '').replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&') \
                   .replace('&quot;', '"').replace('&#39;', "'")
    t = re.sub(r'<[^>]*>', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t[:limit] if limit else t


def first(s, pat, grp=1, default='?'):
    m = re.search(pat, s, re.S)
    return clean(m.group(grp)) if m else default


def decode_grid(txt):
    return zlib.decompress(base64.b64decode(''.join(txt.split())), -15)


def num(x, default=0.0):
    try:
        return float(x)
    except Exception:
        return default


WARN = []


def warn(msg):
    WARN.append(msg)


# ----------------------------------------------------------------- nạp file
if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)
path = sys.argv[1]
args = [a for a in sys.argv[2:]]
out_path = next((a for a in args if not a.startswith('--')), None)
do_grid = '--no-grid' not in args
stdout = '--stdout' in args or not out_path
src = open(path, encoding='utf-8', errors='replace').read()
O = []
say = lambda x='': O.append(x)

say('---')
say('# STATE FULL — %s' % os.path.basename(path))
say('*Sinh bởi rw_state.py · %s bytes · %s dòng*' % (f'{len(src):,}', f'{src.count(chr(10)):,}'))
say('')

# ================================================================ 0. META
say('## 0. META / MÔI TRƯỜNG')
try:
    meta = block(src, 'meta')
    say('- gameVersion: `%s`' % first(meta, r'<gameVersion>([^<]+)'))
    mods = re.findall(r'<li>([^<]+)</li>', block(meta, 'modIds'))
    names = re.findall(r'<li>([^<]+)</li>', block(meta, 'modNames'))
    say('- mods (%d): %s' % (len(mods), ', '.join(names or mods)))
    say('- save của: %s' % ('MULTIPLAYER (rwmt) — phải giữ mod Multiplayer khi load'
                            if any('multiplayer' in m for m in mods) else 'chơi đơn'))
except Exception as e:
    warn('meta: %s' % e)
say('')

# ================================================================ 1. THỜI GIAN & LUẬT CHƠI
say('## 1. THỜI GIAN / LUẬT CHƠI / THỜI TIẾT')
try:
    tm = block(src, 'tickManager')
    tick = int(first(tm, r'<ticksGame>(\d+)', default='0') or 0)
    gs = first(src, r'<gameStartAbsTick>(\d+)', default='')
    say('- ticksGame: **%d** → **ngày %d, %02d:%02d**%s' % (
        tick, tick // 60000, (tick % 60000) // 2500, int((tick % 2500) / 2500 * 60),
        (' | ngày tuyệt đối %d' % (int(gs) + tick)) if gs.isdigit() else ''))
    st = block(src, 'storyteller')
    say('- storyteller: **%s / %s**%s' % (first(st, r'<def>([^<]+)'),
                                          first(st, r'<difficulty>([^<]+)'),
                                          ' (chế độ %) ' % first(st, r'<randomPlusChance>([\d.]+)') if '<randomPlusChance>' in st else ''))
    sw = block(src, 'storyWatcher')
    say('- storyWatcher: raid=%s, threat đang xếp hàng=%s, colonist đã chết=%s | adaptation(độ khó)=%s, (dân số)=%s' % (
        first(sw, r'<numRaidsEnemy>(\d+)'), first(sw, r'<numThreatsQueued>(\d+)'),
        first(sw, r'<colonistsKilled>(\d+)'),
        first(sw, r'<watcherAdaptation>\s*<adaptDays>([-\d.]+)'),
        first(sw, r'<watcherPopAdaptation>\s*<adaptDays>([-\d.]+)')))
    say('- scenario: %s' % clean(block(src, 'scenario'), 300))
    sc = block(src, 'playSettings')
    say('- playSettings: ' + ', '.join('%s=%s' % (k, v) for k, v in re.findall(r'<(\w+)>([^<]{0,24})</\1>', sc)[:10]))
except Exception as e:
    warn('time: %s' % e)
say('')

# ================================================================ 2. MAPS
maps = []          # mỗi map: dict(idx, block, size, x0..)
try:
    maps_blk = block(src, 'maps')
    mobj = list(re.finditer(r'<li>\s*<uniqueID>', maps_blk))
    for k, m in enumerate(mobj):
        a = m.start()
        b = mobj[k + 1].start() if k + 1 < len(mobj) else len(maps_blk)
        mb = maps_blk[a:b]
        size = re.search(r'<size>\((\d+), (\d+), (\d+)\)</size>', mb)
        maps.append(dict(idx=k, block=mb, sx=int(size.group(1)) if size else 0,
                         sz=int(size.group(3)) if size else 0))
except Exception as e:
    warn('maps: %s' % e)

say('## 2. CÁC BẢN ĐỒ TRÊN MAP (%d)' % len(maps))
for mp in maps:
    mb = mp['block']
    say('- **map %d**: %d×%d | parent=%s | weather=%s' % (
        mp['idx'], mp['sx'], mp['sz'], first(mb, r'<parent>([^<]+)'),
        first(mb, r'<curWeather>([^<]+)')))
    cond = block_in(mb, 'gameConditionManager')
    kinds = re.findall(r'<li Class="(GameCondition_\w+)">', cond)
    if kinds:
        say('    - điều kiện môi trường đang chạy: %s' % ', '.join(kinds))
    elif '<conditions>' in cond and '<li>' in cond:
        say('    - điều kiện môi trường: (có mục nhưng không nhận diện được class)')
say('')

# ================================================================ 3. PHE
say('## 3. PHE / QUAN HỆ NGOẠI GIAO')
fac_def, fac_name, player_fid = {}, {}, None
try:
    fm = block(src, 'factionManager')
    for li in re.finditer(r'<li>(.*?)</li>\s*(?=<li>|$)', block_in(fm, 'allFactions'), re.S):
        b = li.group(1)
        fid = first(b, r'<loadID>(\d+)', default=first(b, r'<def>([A-Za-z]+)', default=''))
        d = first(b, r'<def>([A-Za-z]+)')
        n = first(b, r'<name>([^<]*)', default='')
        if d:
            fac_def[d] = n
    # nối Faction_N ↔ def
    order = re.findall(r'<def>([A-Za-z]+)</def>', block_in(fm, 'allFactions'))
    for i, d in enumerate(order):
        fac_name['Faction_%d' % i] = '%s (%s)' % (fac_def.get(d, d), d)
        if d == 'PlayerColony':
            player_fid = 'Faction_%d' % i
    if not player_fid:
        # dự phòng: phe của pawn khởi đầu
        sp = first(src, r'<startingAndOptionalPawns>\s*<li>([^<]+)</li>')
        mm = re.search(r'<thing Class="Pawn">.*?<id>%s</id>.*?<faction>(Faction_\d+)</faction>' % re.escape(sp.replace('Thing_', '')), src, re.S)
        player_fid = mm.group(2) if mm else 'Faction_16'
    say('- **phe người chơi: %s = %s**' % (player_fid, fac_name.get(player_fid, '?')))
    say('- tất cả phe: ' + '; '.join('%s=%s' % (k, v) for k, v in fac_name.items()))
    relmap = {}
    for li in re.finditer(r'<li>\s*<other>(Faction_\d+)</other>(.*?)</li>', block_in(fm, 'allFactions'), re.S) or []:
        pass
    for m2 in re.finditer(r'<relations>(.*?)</relations>', fm, re.S):
        rb = m2.group(1)
        if player_fid and player_fid not in fm[max(0, m2.start() - 3000):m2.start() + 3000]:
            continue
        for li in re.finditer(r'<li>\s*<other>(Faction_\d+)</other>(.*?)</li>', rb, re.S):
            kind = first(li.group(2), r'<kind>([^<]+)', default='Neutral')
            gw = first(li.group(2), r'<goodwill>([-\d]+)', default='0')
            relmap[li.group(1)] = (kind, gw)
    rels = ['%s (%s)' % (fac_name.get(f, f), '%s, %s' % v) for f, v in sorted(relmap.items())]
    say('- quan hệ của phe người chơi: ' + (', '.join(rels) if rels else '(không đọc được)'))
except Exception as e:
    warn('faction: %s' % e)
say('')

# ================================================================ 4. THINGS (cache chung)
things = []
try:
    for a, b in spans(src, 'thing'):
        head = src[a:a + 400]
        cm = re.search(r'<thing Class="([^"]+)"', head)
        dm = re.search(r'<def>([^<]+)</def>', head)
        pm = re.search(r'<pos>\((\d+), (\d+), (\d+)\)</pos>', head)
        body = src[a:b]
        outer = body.split('<thing ', 1)[0]        # bỏ phần vật thể lồng bên trong
        things.append(dict(
            cls=cm.group(1) if cm else '(none)',
            defn=dm.group(1) if dm else (cm.group(1) if cm else '?'),
            pos=(int(pm.group(1)), int(pm.group(3))) if pm else None,
            forb='<forbidden>True</forbidden>' in outer,
            n=int(first(outer, r'<stackCount>(\d+)', default='1') or 1),
            s=a, e=b, body=body,
            fac=first(body[:700], r'<faction>(Faction_\d+)', default=''),
            bdef=first(block_in(body, 'buildDef'), r'<def>([^<]+)</def>', default=''),
            mapidx=int(first(head, r'<map>(\d+)', default='-1') or -1),
        ))
except Exception as e:
    warn('things: %s' % e)

say('## 4. TỔNG QUAN VẬT THỂ')
try:
    cls = Counter(t['cls'] for t in things)
    say('- tổng: **%d** vật thể' % len(things))
    say('- theo class: ' + ', '.join('%s=%d' % (k, v) for k, v in cls.most_common(14)))
    plants = [t for t in things if t['cls'] == 'Plant']
    filth = [t for t in things if t['cls'] == 'Filth']
    say('- thực vật hoang: %d (đã lược chi tiết) | rác: %d (đã lược)' % (len(plants), len(filth)))
    pl = Counter(t['defn'] for t in plants)
    say('- thực vật theo loài: ' + ', '.join('%s=%d' % (k, v) for k, v in pl.most_common(12)))
except Exception as e:
    warn('overview: %s' % e)
say('')

# ================================================================ 5. NGƯỜI CỦA THUỘC ĐỊA (đầy đủ)
say('## 5. NGƯỜI CỦA THUỘC ĐỊA — CHI TIẾT ĐẦY ĐỦ')
BASE = None
PAWN_NAME = {}


def parse_pawn(b):
    d = {}
    d['id'] = first(b, r'<id>([^<]+)')
    d['first'] = first(b, r'<first>([^<]*)', default='')
    d['nick'] = first(b, r'<nick>([^<]*)', default='')
    d['last'] = first(b, r'<last>([^<]*)', default='')
    d['gender'] = first(b, r'<gender>([^<]+)', default='')
    if not d['gender'] or d['gender'] == '?':
        mm = re.search(r'<pawn>Thing_%s</pawn>.{0,4000}?<gender>([^<]+)</gender>' % re.escape(d['id']), src, re.S)
        d['gender'] = mm.group(1) if mm else '(không rõ)'
    abt = first(b, r'<ageBiologicalTicks>(\d+)', default='')
    d['age'] = '%.0f' % (int(abt) / 3600000.0) if abt.isdigit() else first(b, r'<age>(\d+)')
    d['kind'] = first(b, r'<kindDef>([^<]+)')
    d['faction'] = first(b, r'<faction>([^<]+)')
    # nhu cầu
    needs = {}
    for nm in re.finditer(r'<li Class="Need_(\w+)">(.*?)</li>', b, re.S):
        cv = re.search(r'<curLevel>([\d.]+)</curLevel>', nm.group(2))
        if cv:
            needs[nm.group(1)] = float(cv.group(1))
    d['needs'] = needs
    # suy nghĩ (có hệ số + tuổi)
    th = []
    tb = block(b, 'thoughts')
    for tm2 in re.finditer(r'<li[^>]*>\s*<def>([^<]+)</def>(.*?)(?=<li|</thoughts>)', tb, re.S):
        bt = tm2.group(2)
        th.append((tm2.group(1),
                   num(first(bt, r'<moodPowerFactor>([\d.]+)', default='1'), 1),
                   int(num(first(bt, r'<age>(\d+)', default='0'))),
                   first(bt, r'<otherPawn>([^<]+)', default='')))
    d['thoughts'] = th
    # kỹ năng + đam mê
    sk = []
    for sm in re.finditer(r'<li>\s*<def>([^<]+)</def>\s*<level>(\d+)</level>(.*?)</li>', block(b, 'skills'), re.S):
        pas = first(sm.group(3), r'<passion>([^<]+)', default='')
        sk.append((sm.group(1), int(sm.group(2)), pas))
    d['skills'] = sorted(sk, key=lambda x: -x[1])
    # đặc điểm
    d['traits'] = [x for x in re.findall(r'<def>([^<]+)</def>', block(b, 'traits'))]
    d['backstories'] = re.findall(r'<(childhood|adulthood)>([^<]+)</\1>', b)
    # sức khoẻ: hediff + phần cơ thể
    hd = []
    for hm in re.finditer(r'<li Class="(Hediff_\w+)">(.*?)</li>(?=\s*<li Class="Hediff|\s*</hediffs>)', block(b, 'hediffs'), re.S):
        hb = hm.group(2)
        pt = block(hb, 'part')
        hd.append(dict(cls=hm.group(1), defn=first(hb, r'<def>([^<]+)'),
                       sev=first(hb, r'<severity>([\d.]+)', default='-'),
                       part=first(pt, r'<def>([^<]+)', default=''),
                       bleed=first(hb, r'<isBleeding>([A-Za-z]+)', default=''),
                       ctxt=clean(first(hb, r'<combatLogText>(.*?)</combatLogText>', default=''), 110),
                       tend=first(hb, r'<tended>([A-Za-z]+)', default='')))
    d['health'] = hd
    # trang bị
    d['gear'] = [x for x in re.findall(r'<def>([A-Za-z_][\w]*)</def>',
                                       block(block(b, 'equipment'), 'innerList') +
                                       block(block(b, 'wornApparel'), 'innerList'))]
    d['inventory'] = [x for x in re.findall(r'<def>([A-Za-z_][\w]*)</def>',
                                            block(block(b, 'inventory'), 'innerList'))]
    # công việc / giường / tín ngưỡng
    jb = block(b, 'jobs')
    d['job'] = first(jb, r'<def>([^<]+)')
    tgt = first(jb, r'<targetA>([^<]+)', default='')
    ob = first(b, r'<ownedBed>([^<]+)', default='')
    d['bed'] = ob if ob.startswith('Thing_') else tgt
    d['certainty'] = first(b, r'<certainty>([\d.]+)', default='')
    # quan hệ
    d['relations'] = [(first(rr, r'<def>([^<]+)'), first(rr, r'<otherPawn>([^<]+)'))
                      for rr in re.findall(r'<li Class="DirectPawnRelation">(.*?)</li>', b, re.S)]
    return d


colonists = [t for t in things if t['cls'] == 'Pawn' and t['defn'].startswith('Human')
             and (t['faction'] if 'faction' in t else True)]
# lọc theo phe người chơi (đúng hơn)
col_bodies = []
for t in things:
    if t['cls'] != 'Pawn' or not t['defn'].startswith('Human'):
        continue
    b = src[t['s']:t['e']]
    if '<faction>%s</faction>' % player_fid in b:
        col_bodies.append(b)
if not col_bodies:
    warn('không nhận diện được colonist theo phe %s — thử mọi Human' % player_fid)
    col_bodies = [src[t['s']:t['e']] for t in things if t['cls'] == 'Pawn' and t['defn'].startswith('Human')]

for b in col_bodies:
    p = parse_pawn(b)
    PAWN_NAME[p['id']] = '%s %s' % (p['first'], p['last'])
    say('### %s "%s" %s — %s, %s tuổi, %s' % (p['first'], p['nick'], p['last'], p['gender'], p['age'], p['kind']))
    say('- **id**: `%s` | tín ngưỡng: certainty=%s' % (p['id'], p['certainty'] or '?'))
    if p['backstories']:
        say('- backstory: ' + ', '.join('%s=%s' % (k, v) for k, v in p['backstories']))
    if p['traits']:
        say('- đặc điểm: **%s**' % ', '.join(p['traits']))
    say('- kỹ năng: ' + ', '.join('%s %d%s' % (n, l, {'Major': ' ⭐⭐', 'Minor': ' ⭐', 'None': '', '': ''}.get(pa, ''))
                                  for n, l, pa in p['skills'][:12] if l > 0 or pa))
    nd = ', '.join('%s=%.0f%%' % (k, v * 100) for k, v in p['needs'].items())
    say('- nhu cầu: %s' % nd)
    if p['thoughts']:
        pos = [x for x in p['thoughts'] if x[1] >= 1]
        neg = [x for x in p['thoughts'] if x[1] < 1]
        say('- suy nghĩ tích cực/cần chú ý (%d): %s' % (len(p['thoughts']),
            ', '.join('%s(×%.2f, %dh)' % (d, f, a // 2500) for d, f, a, o in p['thoughts'][:16])))
    if p['health']:
        say('- sức khoẻ:')
        for h in p['health']:
            say('    - %s%s%s%s%s %s' % (h['defn'], '(%s)' % h['sev'] if h['sev'] != '-' else '',
                                         ' @%s' % h['part'] if h['part'] else '',
                                         ' [CHẢY MÁU]' if h['bleed'] == 'True' else '',
                                         ' [đã băng]' if h['tend'] == 'True' else ' [CHƯA BĂNG]' if h['tend'] == 'False' else '',
                                         ('← ' + h['ctxt']) if h['ctxt'] else ''))
    else:
        say('- sức khoẻ: không có hediff nào (khoẻ)')
    say('- trang bị: %s%s' % (', '.join(p['gear']) or 'không',
                              (' | trong người: ' + ', '.join(p['inventory'])) if p['inventory'] else ''))
    say('- công việc hiện tại: `%s` | giường: %s' % (p['job'], p['bed'] or '?'))
    if p['relations']:
        say('- quan hệ: ' + ', '.join('%s→%s' % (d, PAWN_NAME.get(o.replace('Thing_', ''), o))
                                      for d, o in p['relations']))
    say('')

# ================================================================ 6. PAWN KHÁC
say('## 6. PAWN KHÁC (thú nuôi / thú hoang / mech / thực thể)')
try:
    if col_bodies:
        BASE = (int(first(col_bodies[0], r'<pos>\((\d+),', default='0')),
                int(first(col_bodies[0], r'<pos>\(\d+, \d+, (\d+)\)', default='0')))
    if not BASE:
        BASE = (125, 125)
    counts, near, pawn_rows = Counter(), [], []
    for t in things:
        if t['cls'] != 'Pawn' or t['defn'].startswith('Human'):
            continue
        b = src[t['s']:t['e']]
        fac = first(b, r'<faction>([^<]+)', default='')
        counts[(t['defn'], fac)] += 1
        if t['pos']:
            row = dict(defn=t['defn'], pos=t['pos'], fac=fac,
                       d=math.dist(t['pos'], BASE) if BASE else 0,
                       hp=first(b, r'<summaryHealth>([\d.]+)', default=''),
                       downed='<Downed>True</Downed>' in b or '<healthState>Downed' in b,
                       lord=first(b, r'<lord>([^<]+)', default=''))
            pawn_rows.append(row)
    say('- theo loài: ' + ', '.join('%s%s ×%d' % (d, '[nuôi]' if f == player_fid else '', n)
                                    for (d, f), n in counts.most_common(30)))
    say('- **con trong bán kính 70 ô quanh căn cứ** (sắp theo khoảng cách):')
    for r in sorted([r for r in pawn_rows if r['d'] <= 70], key=lambda x: x['d'])[:25]:
        say('    - %-18s %-12s cách %3d ô %s%s%s' % (r['defn'], str(r['pos']), r['d'],
                                                     'NUÔI ' if r['fac'] == player_fid else ('PHE %s ' % r['fac'] if r['fac'] else 'hoang '),
                                                     'HP=%s ' % r['hp'] if r['hp'] else '',
                                                     'GỤC ' if r['downed'] else ''))
    foes = [r for r in pawn_rows if r['fac'] and r['fac'] != player_fid]
    if foes:
        say('- **phe địch / mech trên map**: ' + ', '.join('%s@%s' % (r['defn'], r['pos']) for r in foes[:20]))
except Exception as e:
    warn('pawns: %s' % e)
say('')

# ================================================================ 7. XÁC
say('## 7. XÁC CHẾT')
try:
    pnames = {}
    for m in re.finditer(r'<id>(Human\d+)</id>', src):
        win = src[m.end():m.end() + 900]
        f, l = first(win, r'<first>([^<]*)', default=''), first(win, r'<last>([^<]*)', default='')
        k = first(win, r'<kindDef>([^<]+)')
        pnames[m.group(1)] = (' '.join(x for x in (f, l) if x), k)
    resv = block(src, 'reservationManager') + block(src, 'physicalInteractionReservationManager')
    for t in things:
        if t['cls'] != 'Corpse':
            continue
        b = src[t['s']:t['e']]
        refs = re.findall(r'<li>Thing_([^<]+)</li>', block(b, 'innerList'))
        who = ', '.join('%s (%s)' % pnames.get(r, ('?', '?')) for r in refs)
        eaters = re.findall(r'<target>Thing_%s</target>\s*<claimant>([^<]+)</claimant>'
                            % re.escape(first(b, r'<id>([^<]+)')), resv)
        ec = Counter(re.sub(r'\d+$', '', x.replace('Thing_', '')) for x in eaters)
        say('- %-30s %-18s @%s rot=%s %s%s' % (
            clean(who, 30) or '(không rõ)', t['defn'], t['pos'],
            first(b, r'<rotProg>([\d.]+)', default='-'),
            'FORBIDDEN' if t['forb'] else '', ' ← đang bị ăn: %s' % dict(ec) if ec else ''))
except Exception as e:
    warn('corpses: %s' % e)
say('')

# ================================================================ 8. TÀI NGUYÊN / ĐỒ
say('## 8. TÀI NGUYÊN / ĐỒ ĐẠC (đã lọc, giữ vị trí)')
SKIP = {'Plant', 'Filth', 'Pawn', 'Corpse', 'Blueprint_Build', 'Building', 'Building_Door',
        'Building_Bed', 'Building_AncientCryptosleepCasket', 'MinifiedThing',
        'DeadPlant', 'SmashedStump', 'TreeStump', 'DeadTree', 'FilthWithSources'}
try:
    items = defaultdict(lambda: dict(n=0, stacks=0, forb=0, pos=[]))
    for t in things:
        if t['cls'] in SKIP or t['defn'].startswith(('Plant_', 'Filth_')):
            continue
        if t['cls'].startswith('Building'):
            continue
        it = items[t['defn']]
        it['n'] += t['n']
        it['stacks'] += 1
        it['forb'] += 1 if t['forb'] else 0
        if t['pos']:
            it['pos'].append((t['pos'], t['n'], t['forb']))
    for d, v in sorted(items.items(), key=lambda kv: -kv[1]['n']):
        ps = ' @' + '; '.join('%s×%d%s' % (p, n, '[F]' if f else '') for p, n, f in v['pos'][:8]) \
             if (v['n'] < 4000 or d in ('Gun_Revolver', 'MedicineUltratech', 'ComponentSpacer')) else ''
        say('- **%s**: %d (%d stack, %d bị Forbidden)%s' % (d, v['n'], v['stacks'], v['forb'], ps))
except Exception as e:
    warn('items: %s' % e)
say('')

# ================================================================ 9. CÔNG TRÌNH
say('## 9. CÔNG TRÌNH / BLUEPRINT')
try:
    bld = defaultdict(list)
    for t in things:
        if not (t['cls'].startswith('Building') or t['cls'] == 'Blueprint_Build'):
            continue
        name = t['defn']
        if t['cls'] == 'Blueprint_Build':
            name = 'BLUEPRINT:' + (first(src[t['s']:t['e']], r'<def>([^<]+)</def>', default=t['defn'])
                                   if '<buildDef>' in src[t['s']:t['e']] else t['defn'])
        bld[name].append(t['pos'])
    for d, ps in sorted(bld.items(), key=lambda kv: -len(kv[1])):
        xs = [p[0] for p in ps if p]
        zs = [p[1] for p in ps if p]
        bb = 'bbox x%d-%d z%d-%d' % (min(xs), max(xs), min(zs), max(zs)) if xs else ''
        show = ', '.join(str(p) for p in ps[:12]) + (' ...' if len(ps) > 12 else '') if len(ps) <= 20 else ''
        say('- %-34s ×%-4d %-26s %s' % (d, len(ps), bb, show))
    power = [t for t in things if t['defn'] in
             ('PowerConduit', 'Battery', 'SolarGenerator', 'WoodFiredGenerator', 'FueledGenerator',
              'GeothermalGenerator', 'WatermillGenerator', 'WindTurbine', 'PowerSwitch')]
    defs = [t for t in things if 'Turret' in t['defn'] or t['defn'] in ('TrapSpike', 'Sandbags', 'Barricade', 'DeadfallTrap')]
    say('- **điện**: %s' % (', '.join('%s×%d' % (k, v) for k, v in Counter(x['defn'] for x in power).items()) or 'KHÔNG CÓ GÌ'))
    say('- **phòng thủ**: %s' % (', '.join('%s×%d' % (k, v) for k, v in Counter(x['defn'] for x in defs).items()) or 'KHÔNG CÓ GÌ'))
except Exception as e:
    warn('buildings: %s' % e)
say('')

# ================================================================ 10. BILL
say('## 10. BILL SẢN XUẤT')
try:
    n_bill = 0
    for t in things:
        b = src[t['s']:t['e']]
        if '<billStack>' not in b:
            continue
        for bm in re.finditer(r'<li Class="(Bill_\w+)">(.*?)(?=<li Class="|</bills>)', b, re.S):
            bb = bm.group(2)
            n_bill += 1
            say('- %s @%s: recipe=%s target=%s %s%s%s' % (
                t['defn'], t['pos'], first(bb, r'<recipe>([^<]+)'),
                first(bb, r'<targetCount>(\d+)', default='-'), first(bb, r'<repeatMode>([^<]+)', default=''),
                ' [TREO]' if '<suspended>True</suspended>' in bb else '',
                ' chặn: ' + ','.join(re.findall(r'<li>(Allow\w+)</li>', block(bb, 'disallowedSpecialFilters')))))
    if not n_bill:
        say('- (không có bill nào)')
except Exception as e:
    warn('bills: %s' % e)
say('')

# ================================================================ 11. ZONE / AREA
say('## 11. ZONE / AREA')
try:
    zm = block(src, 'zoneManager')
    for m in re.finditer(r'<li Class="(Zone_\w+)">(.*?)(?=<li Class="Zone_|</allZones>)', zm, re.S):
        zb = m.group(2)
        cells = re.findall(r'<li>\((\d+), \d+, (\d+)\)</li>', zb)
        xs = [int(a) for a, _ in cells]
        zs = [int(b) for _, b in cells]
        say('- %-16s %-24s %5d ô %s %s' % (
            m.group(1), clean(first(zb, r'<label>([^<]*)', default=''), 24), len(cells),
            'x%d-%d z%d-%d' % (min(xs), max(xs), min(zs), max(zs)) if cells else '',
            'gieo=%s' % first(zb, r'<plantDefToSow>([^<]+)') if '<plantDefToSow>' in zb else ''))
    am = block(src, 'areaManager')
    for m in re.finditer(r'<li Class="(Area_\w+)">(.*?)</li>', am, re.S):
        say('- %-18s %s ô' % (m.group(1), first(m.group(2), r'<trueCount>(\d+)')))
except Exception as e:
    warn('zones: %s' % e)
say('')

# ================================================================ 12. LƯỚI
if do_grid:
    say('## 12. LƯỚI ĐÃ GIẢI MÃ (mái / sương mù / đất / mỏ sâu)')
    NATURAL = {6699, 10820}
    for mp in maps:
        mb = mp['block']
        SX, SZ = mp['sx'] or 250, mp['sz'] or 250
        N = SX * SZ
        say('### map %d (%d×%d)' % (mp['idx'], SX, SZ))
        try:
            roof_raw = None
            m = re.search(r'<roofsDeflate>\s*([A-Za-z0-9+/=\s]+?)\s*</roofsDeflate>', mb)
            if m:
                roof_raw = decode_grid(m.group(1))
            if roof_raw:
                roof = struct.unpack('<%dH' % (len(roof_raw) // 2), roof_raw)
                supports = [t['pos'] for t in things
                            if t['defn'] in ('Wall', 'Door', 'Column') and t['mapidx'] == mp['idx'] and t['pos']]
                sbuck = defaultdict(list)
                for sx, sz in supports:
                    sbuck[(sx // 8, sz // 8)].append((sx, sz))

                def nsup(p):
                    x, z = p
                    best = 99.0
                    for bx in range(x // 8 - 1, x // 8 + 2):
                        for bz in range(z // 8 - 1, z // 8 + 2):
                            for sx, sz in sbuck.get((bx, bz), ()):
                                best = min(best, math.hypot(x - sx, z - sz))
                    return best
                risky = []
                ncons = 0
                for i, v in enumerate(roof):
                    if not v or v in NATURAL:
                        continue
                    ncons += 1
                    x, z = i % SX, i // SX
                    dd = nsup((x, z))
                    if dd > 6.0:
                        risky.append((x, z, round(dd, 2)))
                say('- mái khối xây: %d ô | điểm tựa: %d | **mái NGUY HIỂM (>6 ô): %d ô**'
                    % (ncons, len(supports), len(risky)))
                for r in sorted(risky)[:60]:
                    say('    - (%d,%d) cách %.2f ô' % r)
                if len(risky) > 60:
                    say('    - … và %d ô nữa' % (len(risky) - 60))
        except Exception as e:
            warn('roof map%d: %s' % (mp['idx'], e))
        try:
            m = re.search(r'<fogGridDeflate>\s*([A-Za-z0-9+/=\s]+?)\s*</fogGridDeflate>', mb)
            if m:
                fog = decode_grid(m.group(1))
                fogn = sum(1 for i in range(N) if (fog[i // 8] >> (i % 8)) & 1)
                say('- sương mù: %d ô (%.1f%%)' % (fogn, 100.0 * fogn / N))
                seen, clusters = set(), []
                for i in range(N):
                    if not ((fog[i // 8] >> (i % 8)) & 1) or i in seen:
                        continue
                    st, pts = [i], []
                    seen.add(i)
                    while st:
                        k = st.pop()
                        pts.append(k)
                        x, z = k % SX, k // SX
                        for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nx, nz = x + dx, z + dz
                            if 0 <= nx < SX and 0 <= nz < SZ:
                                nk = nz * SX + nx
                                if nk not in seen and ((fog[nk // 8] >> (nk % 8)) & 1):
                                    seen.add(nk)
                                    st.append(nk)
                    clusters.append(pts)
                clusters.sort(key=len, reverse=True)
                for pts in clusters[:6]:
                    xs = [k % SX for k in pts]
                    zs = [k // SX for k in pts]
                    say('    - cụm %d ô: x%d-%d z%d-%d' % (len(pts), min(xs), max(xs), min(zs), max(zs)))
        except Exception as e:
            warn('fog map%d: %s' % (mp['idx'], e))
        try:
            m = re.search(r'<topGridDeflate>\s*([A-Za-z0-9+/=\s]+?)\s*</topGridDeflate>', mb)
            if m:
                terr = struct.unpack('<%dH' % (len(decode_grid(m.group(1))) // 2), decode_grid(m.group(1)))
                say('- đất (top 6 hash): %s' % ', '.join('h%d=%d' % (k, v) for k, v in Counter(terr).most_common(6)))
        except Exception as e:
            warn('terrain map%d: %s' % (mp['idx'], e))
        try:
            d = block_in(mb, 'deepResourceGrid')
            mm = re.search(r'<defGridDeflate>\s*([A-Za-z0-9+/=\s]+?)\s*</defGridDeflate>', d)
            if mm:
                raw = decode_grid(mm.group(1))
                vals = struct.unpack('<%dH' % (len(raw) // 2), raw)
                say('- **mỏ sâu**: %d/%d ô có tài nguyên%s'
                    % (sum(1 for v in vals if v), len(vals),
                       ' ⇒ ĐỪNG nghiên cứu DeepDrilling/GroundPenetratingScanner' if not any(vals) else ''))
        except Exception as e:
            warn('deepres: %s' % e)
        try:
            mm = re.search(r'<compressedThingMapDeflate>\s*([A-Za-z0-9+/=\s]+?)\s*</compressedThingMapDeflate>', mb)
            if mm:
                raw = decode_grid(mm.group(1))
                vals = struct.unpack('<%dH' % (len(raw) // 2), raw)
                mine = [(i % SX, i // SX) for i, v in enumerate(vals) if v]
                say('- ô đá/mineable tĩnh: %d' % len(mine))
        except Exception as e:
            warn('ctm: %s' % e)
        mineables = [t for t in things if t['cls'] == 'Mineable' and t['mapidx'] == mp['idx']]
        if mineables:
            say('- vật thể Mineable (cách cũ): %d — %s' % (len(mineables), Counter(t['defn'] for t in mineables).most_common(6)))
    say('')

# ---- (tuỳ chọn) sơ đồ ASCII khu căn cứ
if '--ascii' in args:
    say('## 12b. SƠ ĐỒ ASCII KHU CĂN CỨ (khu vực Area_Home)')
    CORE = {'Wall', 'Door', 'Sandbags', 'Fence', 'FenceGate', 'Bed', 'SimpleResearchBench',
            'FueledStove', 'TorchLamp', 'HorseshoesPin', 'AnimalSleepingSpot', 'PenMarker',
            'Table2x2c', 'Grave', 'Sarcophagus', 'PowerConduit', 'Battery', 'Autodoor',
            'Blueprint_Fence', 'Blueprint_Wall', 'Blueprint_Door'}
    for mp in maps:
        try:
            SX, SZ = mp['sx'] or 250, mp['sz'] or 250
            core = [t['pos'] for t in things if t['mapidx'] == mp['idx'] and t['pos']
                    and (t['defn'] in CORE or t['bdef'] in CORE) and t['fac'] == player_fid
                    and BASE and math.dist(t['pos'], BASE) <= 45]
            if not core:
                continue
            xs = [p[0] for p in core]
            zs = [p[1] for p in core]
            x0, x1 = max(0, min(xs) - 3), min(SX - 1, max(xs) + 3)
            z0, z1 = max(0, min(zs) - 3), min(SZ - 1, max(zs) + 3)
            # điểm tựa + mái + nguy hiểm
            roof = []
            rm2 = re.search(r'<roofsDeflate>\s*([A-Za-z0-9+/=\s]+?)\s*</roofsDeflate>', mp['block'])
            if rm2:
                roof = struct.unpack('<%dH' % (len(decode_grid(rm2.group(1))) // 2), decode_grid(rm2.group(1)))
            supports = [t['pos'] for t in things if t['defn'] in ('Wall', 'Door', 'Column')
                        and t['mapidx'] == mp['idx'] and t['pos']]
            sbuck = defaultdict(list)
            for sx, sz in supports:
                sbuck[(sx // 8, sz // 8)].append((sx, sz))

            def nsup(p):
                x, z = p
                best = 99.0
                for bx in range(x // 8 - 1, x // 8 + 2):
                    for bz in range(z // 8 - 1, z // 8 + 2):
                        for sx, sz in sbuck.get((bx, bz), ()):
                            best = min(best, math.hypot(x - sx, z - sz))
                return best
            ch_of = {'Wall': '#', 'Door': 'D', 'Autodoor': 'D', 'Bed': 'b', 'SimpleResearchBench': 'r',
                     'FueledStove': 'F', 'TorchLamp': 'o', 'Sandbags': 's', 'Fence': 'f', 'FenceGate': 'G',
                     'Blueprint_Fence': '=', 'PenMarker': 'P', 'HorseshoesPin': 'h', 'AnimalSleepingSpot': 'a',
                     'Table2x2c': 'T2', 'Grave': 'g', 'Sarcophagus': 'S'}
            sym, rank = {}, {}
            PRI = {'x': 5, '#': 4, 'D': 4, '=': 3, 's': 3, 'b': 3, 'r': 3, 'F': 3, 'o': 3, 'g': 3,
                   'T': 2, '*': 1}
            for t in things:
                if t['mapidx'] != mp['idx'] or not t['pos']:
                    continue
                x, z = t['pos']
                if not (x0 <= x <= x1 and z0 <= z <= z1):
                    continue
                ch = ch_of.get(t['defn'])
                if t['cls'] == 'Corpse':
                    ch = 'x'
                elif t['defn'].startswith('Plant_') and t['defn'] not in ('Plant_Grass', 'Plant_TallGrass', 'Plant_Brambles'):
                    ch = 'T' if t['defn'] in ('Plant_TreeOak', 'Plant_TreePoplar') else '*'
                if not ch:
                    continue
                ch = ch[0]
                r = PRI.get(ch, 3)
                if r >= rank.get((x, z), -1):
                    sym[(x, z)] = ch
                    rank[(x, z)] = r
            # tập ô mái NGUY HIỂM để tô đè bằng '!'
            risky = set()
            if roof:
                for (rx, rz) in list(sym) + [(x, z) for x in range(x0, x1 + 1) for z in range(z0, z1 + 1)]:
                    v = roof[rz * SX + rx] if 0 <= rz < SZ and 0 <= rx < SX else 0
                    if v and v not in (6699, 10820) and nsup((rx, rz)) > 6.0:
                        risky.add((rx, rz))
            say('### map %d — vùng lõi căn cứ (x%d–%d, z%d–%d)' % (mp['idx'], x0, x1, z0, z1))
            say('```')
            say('    ' + ''.join(str(x // 10 % 10) for x in range(x0, x1 + 1)))
            say('    ' + ''.join(str(x % 10) for x in range(x0, x1 + 1)))
            for z in range(z0, z1 + 1):
                row = ''
                for x in range(x0, x1 + 1):
                    ch = sym.get((x, z))
                    if ch is None:
                        v = roof[z * SX + x] if roof else 0
                        ch = '.' if v and v not in (6699, 10820) else ' '
                    if (x, z) in risky:
                        ch = '!'              # ô mái SẮP SẬP (ưu tiên hiển thị)
                    row += ch
                say('%3d %s' % (z, row))
            say('```')
            say('`#`tường `D`cửa `b`giường `r`bàn NC `F`bếp `o`đuốc `s`bao cát `=`rào(blueprint) `f`rào '
                '`x`xác `*`cây trồng `T`cây to `.`mái `!`**mái sắp sập**')
        except Exception as e:
            warn('ascii map%d: %s' % (mp['idx'], e))
    say('')

# ================================================================ 13. NGHIÊN CỨU / IDEO / QUEST
say('## 13. NGHIÊN CỨU')
try:
    rm = block(src, 'researchManager')
    keys = re.findall(r'<li>([A-Za-z_]+)</li>', block(block(rm, 'progress'), 'keys'))
    vals = re.findall(r'<li>([\d.]+)</li>', block(block(rm, 'progress'), 'values'))
    fin = [k for k, v in zip(keys, vals) if num(v) >= 1]
    nz = [(k, v) for k, v in zip(keys, vals) if 0 < num(v) < 1]
    say('- đang nghiên cứu: **%s**' % first(rm, r'<currentProj>([^<]+)', default='-'))
    say('- đã xong (%d): %s' % (len(fin), ', '.join(fin)))
    say('- đang dở: %s' % (', '.join('%s=%s' % (k, v) for k, v in nz) or 'không'))
    say('- CHƯA nghiên cứu: %d công nghệ' % (len(keys) - len(fin) - len(nz)))
except Exception as e:
    warn('research: %s' % e)
say('')

say('## 14. TÔN GIÁO (Ideology)')
try:
    im = block(src, 'ideoManager')
    if not im:
        say('- (save không có Ideology hoặc không có ideo)')
    anchors = [m.start() for m in re.finditer(r'<foundation Class="', im)]
    for ai, a0 in enumerate(anchors):
        a1 = anchors[ai + 1] if ai + 1 < len(anchors) else len(im)
        ib = im[a0:a1]
        say('- **%s**: member=%s, foundation=%s, hidden=%s, certainty=%s' % (
            first(ib, r'<name>([^<]+)', default='(không tên)'),
            first(ib, r'<memberName>([^<]*)', default=''),
            first(ib, r'<foundation Class="(\w+)"', default='-'),
            'True' if '<hiddenIdeoMode>True' in ib else 'False',
            first(ib, r'<certainty>([\d.]+)', default='-')))
        mem = re.findall(r'<li>([^<]+)</li>', block(ib, 'memes'))
        say('    - memes: %s' % (', '.join(mem) if mem else '(không có/ẩn)'))
        pb = block(ib, 'precepts')
        pre = ['%s=%s' % (d, clean(n, 20)) for n, d in
               re.findall(r'<name>([^<]*)</name>\s*<def>([^<]+)</def>', pb)]
        say('    - precepts (%d): %s' % (len(pre), ', '.join(dict.fromkeys(pre))))
        obl = re.findall(r'<activeObligations>(.*?)</activeObligations>', ib, re.S)
        for o in obl:
            for li in re.finditer(r'<li>(.*?)</li>', o, re.S):
                ob = li.group(1)
                say('    - **NGHĨA VỤ ĐANG MỞ**: triggeredTick=%s targetA=%s onlyFor=%s' % (
                    first(ob, r'<triggeredTick>(\d+)'), first(ob, r'<targetA>([^<]+)'),
                    re.findall(r'<li>(Thing_\w+)</li>', block(ob, 'onlyForPawns'))))
except Exception as e:
    warn('ideo: %s' % e)
say('')

say('## 15. NHIỆM VỤ (Quests)')
try:
    qm = block(src, 'questManager')
    qblk = block(qm, 'quests')
    anchors = [m.start() for m in re.finditer(r'<li>\s*(?:<id>\d+</id>\s*)?<name>', qblk)]
    qs = []
    for ai, a0 in enumerate(anchors):
        a1 = anchors[ai + 1] if ai + 1 < len(anchors) else len(qblk)
        qb = qblk[a0:a1]
        qs.append((first(qb, r'<name>([^<]*)', default='(không tên)'), qb))
    if not qs:
        say('- (không có nhiệm vụ)')
    for nm, qb in qs:
        say('- **%s**: ended=%s outcome=%s | tick=%s' % (
            clean(nm, 60), first(qb, r'<ended>([^<]+)', default='?'),
            first(qb, r'<endOutcome>([^<]+)', default='-'),
            first(qb, r'<appearanceTick>(\d+)', default='-')))
        desc = clean(first(qb, r'<description>(.*?)</description>', default=''), 400)
        if desc:
            say('    - %s' % desc)
except Exception as e:
    warn('quests: %s' % e)
say('')

# ================================================================ 16. THƯ
say('## 16. THƯ (chưa đọc + gần nhất)')
try:
    unread = set(re.findall(r'<li>Letter_(\d+)</li>', block(src, 'letterStack')))
    lets = []
    for lm in re.finditer(r'<li Class="(StandardLetter|DeathLetter|NewQuestLetter|ChoiceLetter|Message)">(.*?)(?=<li Class="|</archivables>)', src, re.S):
        lb = lm.group(2)
        tick = first(lb, r'<arrivalTick>(\d+)', default=first(lb, r'<startingTick>(\d+)', default='0'))
        lets.append((int(num(tick)), first(lb, r'<ID>(\d+)', default='?'), lm.group(1),
                     clean(first(lb, r'<label>(.*?)</label>', default='?'), 80),
                     clean(first(lb, r'<text>(.*?)</text>', default=''), 300)))
    lets.sort(key=lambda x: -x[0])
    say('- thư CHƯA ĐỌC trong stack: %s' % (sorted(unread, key=int) if unread else 'không'))
    for tk, i, cl, lab, tx in lets[:18]:
        say('- [%d] #%s %-14s **%s**%s' % (tk, i, cl, lab, '  ← CHƯA ĐỌC' if i in unread else ''))
        if tx:
            say('    > %s' % tx)
except Exception as e:
    warn('letters: %s' % e)
say('')

# ================================================================ 17. ĐE DOẠ
say('## 17. ĐE DOẠ ĐANG HOẠT ĐỘNG (lordManager)')
try:
    lm = block(src, 'lordManager')
    lab = {t['s']: t['defn'] for t in things}
    if lm and '<lordJob' in lm:
        for m in re.finditer(r'<lordJob Class="([\w.]+)"\s*(?:/>|>(.*?)</lordJob>)', lm, re.S):
            jb = m.group(2) or ''
            starts = [m2.start() for m2 in re.finditer(r'<li>\s*(?:<loadID>\d+</loadID>\s*)?<faction>Faction_\d+</faction>', lm)
                      if m2.start() <= m.start()]
            li0 = starts[-1] if starts else -1
            pre = lm[li0:m.start()] if li0 >= 0 else lm[max(0, m.start() - 1500):m.start()]
            own = re.findall(r'<li>(Thing_[^<]+)</li>', block(pre, 'ownedPawns'))
            fac = first(pre, r'<faction>(Faction_\d+)', default='-')
            flags = ', '.join('%s=%s' % (k, v) for k, v in
                              re.findall(r'<(wakeOnPawnUnfogged|assaultColony|canSteal|interruptCurrentJob)>([^<]*)</\1>', jb))
            names = [x.replace('Thing_', '') for x in own]
            say('- **%s** | phe=%s | %d pawn%s%s' % (m.group(1), fac, len(own),
                                                     (' (' + ', '.join(names[:8]) + ')') if own else '',
                                                     (' | ' + flags) if flags else ''))
    else:
        say('- (không có lord nào đang hoạt động)')
except Exception as e:
    warn('lords: %s' % e)
say('')

# ================================================================ 18. ANOMALY
say('## 18. ANOMALY (nếu có)')
try:
    comp = block(src, 'components')
    if 'Anomaly' in src[:200000] or '<entityCodex' in src:
        cx = block(src, 'entityCodex')
        ents = re.findall(r'<def>([A-Za-z_]+)</def>', cx) or re.findall(r'<li>([A-Za-z_]+)</li>', cx)
        say('- entityCodex: %d mục%s' % (len(ents), (' — ' + ', '.join(dict.fromkeys(ents))[:300]) if ents else ''))
        lvl = re.findall(r'<li>([A-Za-z]+)</li>', block(src, 'anomalyKnowledgeGained'))
        ent = [t for t in things if t['cls'] in ('Entity', 'EntityWithComps') or t['defn'].startswith('Entity')]
        say('- thực thể trên map: %s' % (Counter(t['defn'] for t in ent).most_common(10) or 'không'))
        say('- VoidMonolith: %s' % ('CÓ' if 'VoidMonolith' in src else 'không'))
    else:
        say('- (không có Anomaly)')
except Exception as e:
    warn('anomaly: %s' % e)
say('')

# ================================================================ 19. THẾ GIỚI
say('## 19. THẾ GIỚI')
try:
    inf = block(src, 'info')
    say('- tile thuộc địa: %s | pawn khởi đầu: %s' % (
        first(inf, r'<startingTile>(\d+)'), re.findall(r'<li>([^<]+)</li>', block(inf, 'startingAndOptionalPawns'))))
    wo = block(src, 'worldObjects')
    stl = []
    for m in re.finditer(r'<li Class="Settlement">(.*?)</li>', wo, re.S):
        b = m.group(1)
        t = first(b, r'<tile>(\d+),', default='')
        if t.isdigit():
            stl.append((int(t), first(b, r'<faction>(Faction_\d+)'), clean(first(b, r'<nameInt>([^<]*)', default=''), 26)))
    start = first(inf, r'<startingTile>(\d+)', default='')
    SX = 500
    if stl and start.isdigit():
        s = int(start)
        say('- khu định cư trên hành tinh: %d | tiểu hành tinh: %d' % (len(stl), wo.count('BasicAsteroidMapParent')))
        for t, f, n in sorted(stl, key=lambda x: math.dist((x[0] % SX, x[0] // SX), (s % SX, s // SX)))[:10]:
            dd = int(math.dist((t % SX, t // SX), (s % SX, s // SX)))
            say('    - %-22s %-26s cách ~%d tile' % (n or '(không tên)', fac_name.get(f, f), dd))
    lm2 = block(src, 'landmarks') + block(src, 'features')
    if lm2:
        say('- địa danh (landmarks/features): ' + ', '.join(
            '%s×%d' % (k, v) for k, v in Counter(re.findall(r'<def>([A-Za-z_]+)</def>', lm2)).most_common(12)))
except Exception as e:
    warn('world: %s' % e)
say('')

# ================================================================ 20. CẢNH BÁO TỰ ĐỘNG
say('## 20. CẢNH BÁO TỰ ĐỘNG (máy tính suy ra từ dữ liệu trên)')
try:
    for b in col_bodies:
        p = parse_pawn(b)
        nm = p['first']
        if p['needs'].get('Food', 1) < 0.15:
            say('- 🔴 **%s ĐÓI (Food=%.0f%%)** — nguy cơ ngất/chết' % (nm, p['needs']['Food'] * 100))
        if p['needs'].get('Mood', 1) < 0.35:
            say('- 🔴 **%s tâm trạng thấp (%.0f%%)** — nguy cơ khủng hoảng tinh thần' % (nm, p['needs']['Mood'] * 100))
        for h in p['health']:
            if h['bleed'] == 'True' or h['tend'] == 'False':
                say('- 🩸 %s có %s%s chưa xử lý' % (nm, h['defn'], ' @%s' % h['part'] if h['part'] else ''))
        if not p['gear'] or all(g.startswith('Apparel') for g in p['gear']):
            say('- ⚔️ %s KHÔNG có vũ khí' % nm)
    food = [t for t in things if t['defn'] in ('MealSimple', 'MealFine', 'MealLavish', 'Pemmican',
                                               'MealNutrientPaste', 'Berries', 'MeatRaw', 'RawRice', 'RawPotatoes')]
    if not food:
        say('- 🍽️ **KHÔNG có thức ăn/dược liệu ăn được nào trên map** (kiểm tra cây trồng + săn/hái)')
    if not any(t['defn'] in ('PowerConduit', 'Battery', 'WoodFiredGenerator', 'SolarGenerator') for t in things):
        say('- ⚡ Chưa có hệ thống điện nào (dù có thể đã nghiên cứu Điện)')
    if not any('Turret' in t['defn'] or 'Trap' in t['defn'] for t in things):
        say('- 🛡️ Chưa có turret/bẫy phòng thủ')
    graves = [t for t in things if t['defn'] in ('Grave', 'Sarcophagus')]
    dead_humans = [t for t in things if t['cls'] == 'Corpse' and t['defn'].startswith('Corpse_Human')]
    if dead_humans and not any(t['defn'] == 'Grave' for t in things):
        say('- ⚰️ Có %d xác người nhưng KHÔNG có Grave nào' % len(dead_humans))
    if BASE:
        wolves = [t for t in things if t['defn'] in ('Warg', 'Bear_Grizzly', 'Bear_Polar', 'Cougar', 'Megasloth')
                  and t['pos'] and math.dist(t['pos'], BASE) < 60]
        for w in wolves:
            say('- 🐺 %s ở %s (cách %.0f ô)' % (w['defn'], w['pos'], math.dist(w['pos'], BASE)))
except Exception as e:
    warn('alerts: %s' % e)
say('')

# ================================================================ 21. LỖI/CHƯA HỖ TRỢ
if WARN:
    say('## 21. GHI NHẬN KHI PHÂN TÍCH (không parse được / cần để ý)')
    for w in WARN:
        say('- ⚠️ %s' % w)
    say('')

# ----------------------------------------------------------------- xuất
text = '\n'.join(O) + '\n'
if out_path and not stdout:
    open(out_path, 'w', encoding='utf-8').write(text)
    n = len(text.encode('utf-8'))
    print('OK -> %s' % out_path)
    print('gốc   : %s bytes' % f'{len(src):,}')
    print('state : %s bytes (%.3f%% file gốc, ~%s token)' % (f'{n:,}', 100.0 * n / len(src), f'{int(n/3.5):,}'))
else:
    print(text)
