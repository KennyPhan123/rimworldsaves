#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
digest.py — Nén file save RimWorld (.rws) thành bản "tóm tắt trạng thái" đủ để một AI
hiểu 100% tình hình và lập kế hoạch, mà không cần đọc 14 MB XML.

Cách dùng:
    python3 digest.py Hateria.rws            > DIGEST.txt
    python3 digest.py Hateria.rws out.txt

Nguyên tắc lọc:
  - GIỮ nguyên văn: pawn của thuộc địa, xác, thư, tài nguyên, công trình, zone/area,
    nghiên cứu, tôn giáo, nhiệm vụ, đe doạ, lịch sử đã lọc, lưới đã giải mã.
  - BỎ/HỢP NHẤT: thực vật hoang (23.293 vật thể ≈ 8,4 MB), rác (3.020 ≈ 1,0 MB),
    pawn hoang chỉ giữ tổng hợp + con gần căn cứ, log/database mặc định không dùng
    cho kế hoạch, lưới lãnh thổ hành tinh chỉ giữ phần liên quan.
"""
import base64
import math
import re
import struct
import sys
import zlib
from collections import Counter, defaultdict

SIZE = 250
TILE = SIZE * SIZE


# ---------------------------------------------------------------- helpers
def decode_grid(text):
    return zlib.decompress(base64.b64decode(''.join(text.split())), -15)


def blk(src, tag):
    i = src.find('<%s>' % tag)
    if i < 0:
        return ''
    j = src.find('</%s>' % tag, i)
    return src[i:j + len(tag) + 3]


def inner_deflate(src, outer, inner):
    seg = blk(src, outer)
    m = re.search(r'<%s>\s*([A-Za-z0-9+/=\s]+?)\s*</%s>' % (inner, inner), seg)
    return decode_grid(m.group(1)) if m else b''


def thing_spans(src):
    """Trả về list (start, end) của mọi <thing ...> ... </thing> (tính cả lồng nhau)."""
    out, depth, cur = [], 0, 0
    for m in re.finditer(r'<thing[ >]|</thing>', src):
        if m.group().startswith('<thing'):
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
    t = re.sub(r'<[^>]+>', '', t)          # bỏ thẻ màu <color=...>
    t = re.sub(r'\s+', ' ', t).strip()
    return t[:limit] if limit else t


def pos_of(body):
    m = re.search(r'<pos>\((\d+), (\d+), (\d+)\)</pos>', body)
    return (int(m.group(1)), int(m.group(3))) if m else None


# ---------------------------------------------------------------- load
path = sys.argv[1] if len(sys.argv) > 1 else 'Hateria.rws'
out_path = sys.argv[2] if len(sys.argv) > 2 else None
src = open(path, encoding='utf-8').read()
O = []
say = O.append

say('#### DIGEST SAVE RIMWORLD — sinh tự động bởi digest.py')
say('#### file gốc: %s | %s bytes | tỉ lệ nén sẽ in ở cuối' % (path, f'{len(src):,}'))
say('')

# ---------------------------------------------------------------- 1. meta
say('== 1. SAVE / CÀI ĐẶT ==')
m = re.search(r'<gameVersion>([^<]+)</gameVersion>', src)
say('version: %s' % (m.group(1) if m else '?'))
say('modIds: ' + ', '.join(re.findall(r'<li>([^<]+)</li>', blk(src, 'modIds'))))
tm = blk(src, 'tickManager')
tk = re.search(r'<ticksGame>(\d+)</ticksGame>', tm)
abs_t = re.search(r'<absTick>(\d+)</absTick>', tm)
tk = int(tk.group(1)) if tk else 0
say('ticksGame: %d  => ngày %d, giờ ~%d:00' % (tk, tk // 60000, (tk % 60000) // 2500))
gs = re.search(r'<gameStartAbsTick>(\d+)</gameStartAbsTick>', src)
say('absTick: %s | gameStartAbsTick: %s | (ngày tuyệt đối của save: %s)' % (
    abs_t.group(1) if abs_t else '?', gs.group(1) if gs else '?',
    (int(gs.group(1)) + tk) if gs else '?'))
st = blk(src, 'storyteller')
say('storyteller: %s / %s' % (re.search(r'<def>([^<]+)</def>', st).group(1) if '<def>' in st else '?',
                              clean(re.search(r'<difficulty>([^<]*)</difficulty>', st).group(1) if '<difficulty>' in st else '')))
sw = blk(src, 'storyWatcher')
say('storyWatcher: ' + ', '.join('%s=%s' % (t, v) for t, v in
     re.findall(r'<(numRaidsEnemy|numThreatsQueued|colonistsKilled)>([^<]*)</\1>', sw))
    + ' | adapt(độ khó)=%s | adapt(dân số)=%s' % (
        (re.search(r'<watcherAdaptation>\s*<adaptDays>([^<]*)', sw).group(1) if '<watcherAdaptation>' in sw else '?'),
        (re.search(r'<watcherPopAdaptation>\s*<adaptDays>([^<]*)', sw).group(1) if '<watcherPopAdaptation>' in sw else '?')))
inf = blk(src, 'info')
say('startingTile: %s' % (re.search(r'<startingTile>(\d+),', inf).group(1) if '<startingTile>' in inf else '?'))
say('scenario: %s' % clean(blk(src, 'scenario'), 400))
w = blk(src, 'weatherManager')
say('weather now: %s' % clean(re.search(r'<curWeather>([^<]+)</curWeather>', w).group(1) if '<curWeather>' in w else w, 120))
gc = blk(src, 'gameConditionManager')
say('gameConditions: %s' % clean(gc, 400))
say('')

# ---------------------------------------------------------------- 2. pawns + things
spans = thing_spans(src)
BUCKET = {}
for s, e in spans:
    head = src[s:s + 420]
    cm = re.search(r'<thing Class="([^"]+)"', head)
    dm = re.search(r'<def>([^<]+)</def>', head)
    cls = cm.group(1) if cm else '(none)'
    dfn = dm.group(1) if dm else '?'
    BUCKET.setdefault((cls, dfn), []).append((s, e))

def bodies(cls, dfn=None):
    out = []
    for (c, d), lst in BUCKET.items():
        if c == cls and (dfn is None or d == dfn):
            out += [src[s:e] for s, e in lst]
    return out

# ---- colonists
say('== 2. NGƯỜI CỦA THUỘC ĐỊA (chi tiết đầy đủ) ==')
col = []
for b in bodies('Pawn', 'Human'):
    if '<faction>Faction_16</faction>' not in b and 'player' not in b:
        continue
    col.append(b)
for b in col:
    f = re.search(r'<first>([^<]*)</first>', b)
    nk = re.search(r'<nick>([^<]*)</nick>', b)
    ls = re.search(r'<last>([^<]*)</last>', b)
    gd = re.search(r'<gender>([^<]*)</gender>', b)
    abt = re.search(r'<ageBiologicalTicks>(\d+)</ageBiologicalTicks>', b)
    agv = '%.0f' % (int(abt.group(1)) / 3600000.0) if abt else '?'
    idm = re.search(r'<id>([^<]+)</id>', b) or re.search(r'Thing_(Human\d+)', b)
    say('--- %s %s%s | %s | %s tuổi | id=%s | kind=%s' % (
        f.group(1) if f else '?', '"%s" ' % nk.group(1) if nk and nk.group(1) else '',
        ls.group(1) if ls else '', gd.group(1) if gd else '?', agv,
        idm.group(1) if idm else '?', clean(re.search(r'<kindDef>([^<]+)</kindDef>', b).group(1) if '<kindDef>' in b else '', 20)))
    # nhu cầu
    needs = re.findall(r'<li Class="Need_(\w+)">(.*?)</li>', b, re.S)
    ns = []
    for name, nb in needs:
        cv = re.search(r'<curLevel>([\d.]+)</curLevel>', nb)
        if cv:
            ns.append('%s=%.2f' % (name, float(cv.group(1))))
    say('    needs: ' + ', '.join(ns))
    # tâm trạng + suy nghĩ
    th = blk(b, 'thoughts') or blk(b, 'memory')
    defs = re.findall(r'<def>([^<]+)</def>', th)
    say('    thoughts(%d): %s' % (len(defs), ', '.join(defs[:14]) + (' ...' if len(defs) > 14 else '')))
    # kỹ năng
    sk = blk(b, 'skills')
    skills = re.findall(r'<def>([^<]+)</def>\s*<level>(\d+)</level>', sk) or \
             re.findall(r'<li>\s*<def>([^<]+)</def>[^<]*<level>(\d+)</level>', sk)
    skills = sorted(skills, key=lambda x: -int(x[1]))
    say('    skills: ' + ', '.join('%s %s' % (a, c) for a, c in skills[:8]))
    # đặc điểm
    tr = blk(b, 'traits')
    say('    traits: ' + ', '.join(dict.fromkeys(re.findall(r'<def>([^<]+)</def>', tr))))
    bs = re.findall(r'<(childhood|adulthood)>([^<]+)</\1>', b) or \
         re.findall(r'<(childhood|adulthood)>([^<]+)</\1>', blk(b, 'story'))
    say('    backstories: ' + ', '.join('%s=%s' % (k, v) for k, v in bs))
    # sức khoẻ
    hs = blk(b, 'hediffSet') or blk(b, 'healthTracker')
    hd = []
    for hm in re.finditer(r'<li Class="(Hediff_\w+)">(.*?)</li>', hs, re.S):
        hb = hm.group(2)
        d = re.search(r'<def>([^<]+)</def>', hb)
        sv = re.search(r'<severity>([\d.]+)</severity>', hb)
        pt = blk(hb, 'part')
        ptd = re.search(r'<def>([^<]+)</def>', pt)
        cl = re.search(r'<combatLogText>(.*?)</combatLogText>', hb, re.S)
        hd.append('%s%s%s%s' % (d.group(1) if d else '?',
                                '(%s)' % sv.group(1) if sv else '',
                                ' @%s' % ptd.group(1) if ptd else '',
                                ' [%s]' % clean(cl.group(1), 90) if cl else ''))
    say('    health: ' + (' | '.join(hd) if hd else 'khoẻ'))
    # trang bị
    eqd = re.findall(r'<def>([^<]+)</def>', blk(blk(b, 'equipment'), 'innerList'))
    apd = re.findall(r'<def>([^<]+)</def>', blk(blk(b, 'wornApparel'), 'innerList'))
    say('    gear: ' + (', '.join(dict.fromkeys([x for x in eqd + apd if x[0].isupper()])) or 'không'))
    # công việc + giường
    jb = blk(b, 'jobs')
    tgt = re.search(r'<targetA>([^<]+)</targetA>', jb)
    say('    job: %s | giường: %s' % (
        clean(re.search(r'<def>([^<]+)</def>', jb).group(1) if '<def>' in jb else '', 40),
        (lambda ob: ob if ob.startswith('Thing_') else (tgt.group(1) if tgt else ''))(
            re.search(r'<ownedBed>([^<]+)</ownedBed>', b).group(1) if '<ownedBed>' in b else '')))
    # quan hệ
    rel = []
    for rm in re.finditer(r'<li Class="DirectPawnRelation">(.*?)</li>', b, re.S):
        rb = rm.group(1)
        d = re.search(r'<def>([^<]+)</def>', rb)
        o = re.search(r'<otherPawn>([^<]+)</otherPawn>', rb)
        rel.append('%s->%s' % (d.group(1) if d else '?', o.group(1) if o else '?'))
    if rel:
        say('    relations: ' + ', '.join(rel[:10]))
    ct = re.search(r'<certainty>([\d.]+)</certainty>', b)
    say('    tín ngưỡng: %s' % ('certainty=%.3f' % float(ct.group(1)) if ct else '?'))
    say('')

# ---- other pawns
say('== 3. PAWN KHÁC (động vật nuôi / hoang / quái) ==')
BASE = None
for b in col:
    BASE = pos_of(b) or BASE
    if BASE:
        break
BASE = BASE or (121, 119)
say('điểm tham chiếu căn cứ: %s' % (BASE,))
counts = Counter()
near = []
for (c, d), lst in BUCKET.items():
    if c != 'Pawn':
        continue
    for s, e in lst:
        b = src[s:e]
        counts[d] += 1
        p = pos_of(b)
        fac = re.search(r'<faction>(Faction_\d+)</faction>', b)
        if p and math.dist(p, BASE) <= 70 and d != 'Human':
            hp = re.search(r'<summaryHealth>([\d.]+)</summaryHealth>', b)
            near.append((round(math.dist(p, BASE)), d, p, fac.group(1) if fac else 'hoang',
                         'HP=%s' % hp.group(1) if hp else ''))
say('tổng theo loài: ' + ', '.join('%s x%d' % (k, v) for k, v in counts.most_common()))
say('con Ở GẦN căn cứ (<=70 ô) — sắp theo khoảng cách:')
for r, d, p, f, hp in sorted(near)[:22]:
    say('    %-16s %-14s cách %3d ô  %s %s' % (d, str(p), r, f, hp))
say('')

# ---------------------------------------------------------------- 4. corpses
say('== 4. XÁC CHẾT ==')
# bảng tên: quét MỌI <id>HumanN</id> (pawn sống nằm trong <things>, pawn chết nằm trong
# worldPawns dạng <li Class="Pawn">) rồi lấy tên trong ~900 ký tự ngay sau đó
pname = {}
for m in re.finditer(r'<id>(Human\d+|Animal_\w+)</id>', src):
    win = src[m.end():m.end() + 900]
    f = re.search(r'<first>([^<]*)</first>', win)
    l = re.search(r'<last>([^<]*)</last>', win)
    k = re.search(r'<kindDef>([^<]+)</kindDef>', win)
    nm = ' '.join(x for x in [(f.group(1) if f else ''), (l.group(1) if l else '')] if x)
    pname[m.group(1)] = (nm or '?', k.group(1) if k else '?')
reservations = blk(src, 'reservationManager') + blk(src, 'physicalInteractionReservationManager')
for b in bodies('Corpse'):
    p = pos_of(b)
    inn = blk(b, 'innerList')
    refs = re.findall(r'<li>Thing_([^<]+)</li>', inn)
    who_p = ', '.join('%s (%s)' % (pname.get(r, ('?', '', ''))[0], pname.get(r, ('', '?', ''))[1]) for r in refs)
    rot = re.search(r'<rotProg>([\d.]+)</rotProg>', b)
    tod = re.search(r'<timeOfDeath>(\d+)</timeOfDeath>', b)
    forb = '<forbidden>True</forbidden>' in b
    tid = re.search(r'<id>([^<]+)</id>', b)
    who = []
    if tid:
        for rm in re.finditer(r'<target>Thing_%s</target>\s*<claimant>([^<]+)</claimant>' % re.escape(tid.group(1)), reservations):
            who.append(rm.group(1))
    if who:
        who = ['%d × %s' % (len(who), clean(who[0]).replace('Thing_', '').rstrip('0123456789'))]
    say('    %-24s %-16s pos=%s rotProg=%s chết@%s%s%s' % (
        clean(who_p, 24), re.search(r'<def>([^<]+)</def>', b).group(1), p,
        rot.group(1) if rot else '-', tod.group(1) if tod else '-',
        ' FORBIDDEN' if forb else '',
        ' | đang bị ăn bởi: ' + ', '.join(who) if who else ''))
say('')

# ---------------------------------------------------------------- 5. letters
say('== 5. THƯ (thư CHƯA ĐỌC trước, rồi tới các thư gần nhất) ==')
# thư nằm trong <history><archive><archivables> — quét toàn file
unread_ids = set(re.findall(r'<li>Letter_(\d+)</li>', blk(src, 'letterStack')))
lets = []
for lm in re.finditer(r'<li Class="(StandardLetter|DeathLetter|NewQuestLetter|ChoiceLetter|Message|TextMote)">(.*?)(?=<li Class="|</archivables>)', src, re.S):
    lb = lm.group(2)
    idm = re.search(r'<ID>(\d+)</ID>', lb)
    lab = re.search(r'<label>(.*?)</label>', lb, re.S)
    tick = re.search(r'<arrivalTick>(\d+)</arrivalTick>', lb) or re.search(r'<startingTick>(\d+)</startingTick>', lb)
    txt = re.search(r'<text>(.*?)</text>', lb, re.S)
    lets.append((int(tick.group(1)) if tick else 0, lm.group(1), idm.group(1) if idm else '?',
                 clean(lab.group(1) if lab else '?', 90), clean(txt.group(1) if txt else '', 260)))
lets.sort(key=lambda x: -x[0])
say('tổng số thư lưu trong archive: %d | đang nằm trong stack (chưa đọc): %s' % (len(lets), sorted(unread_ids) or 'không'))
for t, cl, i, lab, tx in lets[:14]:
    mark = ' <<< CHƯA ĐỌC' if i in unread_ids else ''
    say('    [%s] #%s %-16s %-44s tick=%d%s' % (t, i, cl, lab, t, mark))
    if tx:
        say('        "%s"' % tx)
say('')

# ---------------------------------------------------------------- 6. items
say('== 6. TÀI NGUYÊN / ĐỒ ĐẠC ==')
items = defaultdict(lambda: [0, 0])   # def -> [số lượng, số stack forbidden]
itempos = defaultdict(list)
for (c, d), lst in BUCKET.items():
    if c not in ('ThingWithComps', 'Medicine', 'MinifiedThing', 'Item', 'Apparel', 'Weapon') and not d.startswith(('Medicine', 'Gun_', 'MeleeWeapon')):
        continue
    for s, e in lst:
        b = src[s:e]
        sc = re.search(r'<stackCount>(\d+)</stackCount>', b)
        n = int(sc.group(1)) if sc else 1
        items[d][0] += n
        f = '<forbidden>True</forbidden>' in b
        items[d][1] += 1 if f else 0
        p = pos_of(b)
        if p:
            itempos[d].append((p, n, f))
for d, (n, nf) in sorted(items.items(), key=lambda kv: -kv[1][0]):
    ps = ''
    if d.startswith(('Gun_', 'MeleeWeapon', 'Medicine', 'Component', 'Gravlite')) or d in ('Silver', 'Gold', 'Steel'):
        ps = ' @' + '; '.join('%s×%d%s' % (p, cnt, ' [F]' if f else '') for p, cnt, f in itempos[d][:8])
    say('    %-26s tổng %-6d (%d stack bị Forbidden)%s' % (d, n, nf, ps))
say('')

# ---------------------------------------------------------------- 7. buildings
say('== 7. CÔNG TRÌNH ==')
bld = defaultdict(list)
for (c, d), lst in BUCKET.items():
    if not c.startswith('Building') and c != 'Blueprint_Build':
        continue
    for s, e in lst:
        p = pos_of(src[s:e])
        d0 = d
        if c == 'Blueprint_Build':
            d0 = 'BLUEPRINT:' + (re.search(r'<def>([^<]+)</def>', blk(src[s:e], 'buildDef')).group(1)
                                 if '<buildDef>' in src[s:e] else d)
        bld[d0].append(p)
for d, ps in sorted(bld.items(), key=lambda kv: -len(kv[1])):
    xs = [p[0] for p in ps if p]; zs = [p[1] for p in ps if p]
    bb = 'bbox x%d-%d z%d-%d' % (min(xs), max(xs), min(zs), max(zs)) if xs else ''
    show = ', '.join(str(p) for p in ps[:10]) + (' ...' if len(ps) > 10 else '')
    say('    %-30s x%-5d %-26s %s' % (d, len(ps), bb, show if len(ps) <= 14 else ''))
say('')

say('')
say('== 7b. BILL SẢN XUẤT (bếp/xưởng) ==')
for (c, d), lst in BUCKET.items():
    if not c.startswith('Building'):
        continue
    for s0, e0 in lst:
        b = src[s0:e0]
        if '<billStack>' not in b:
            continue
        pos = pos_of(b)
        for bm in re.finditer(r'<li Class="(Bill_\w+)">(.*?)</li>', b, re.S):
            bb = bm.group(2)
            rc = re.search(r'<recipe>([^<]+)</recipe>', bb)
            tg = re.search(r'<targetCount>(\d+)</targetCount>', bb)
            rp = re.search(r'<repeatMode>([^<]+)</repeatMode>', bb)
            sus = '<suspended>True</suspended>' in bb
            dis = re.findall(r'<li>(AllowCorpses\w+|AllowRotten|AllowPlantFood)</li>', blk(bb, 'disallowedSpecialFilters'))
            say('    %-16s @%-12s %-22s x%-4s %-12s%s%s' % (
                d, str(pos), rc.group(1) if rc else '?', tg.group(1) if tg else '-',
                rp.group(1) if rp else '', ' [ĐANG TREO]' if sus else '',
                ' chặn: ' + ','.join(dis) if dis else ''))
say('')

# ---------------------------------------------------------------- 8. zones/areas
say('== 8. VÙNG / KHU VỰC ==')
zm = blk(src, 'zoneManager')
for zm2 in re.finditer(r'<li Class="(Zone_\w+)">(.*?)(?=<li Class="Zone_|</allZones>)', zm, re.S):
    zb = zm2.group(2)
    lab = re.search(r'<label>([^<]*)</label>', zb)
    cells = re.findall(r'<li>\((\d+), \d+, (\d+)\)</li>', zb)
    plant = re.search(r'<plantDefToSow>([^<]+)</plantDefToSow>', zb)
    if cells:
        xs = [int(a) for a, _ in cells]; zs = [int(b) for _, b in cells]
        bb = 'x%d-%d z%d-%d' % (min(xs), max(xs), min(zs), max(zs))
    else:
        bb = ''
    say('    %-18s %-22s %4d ô  %s %s' % (zm2.group(1), clean(lab.group(1) if lab else ''), len(cells), bb,
                                          'gieu/cây trồng=%s' % plant.group(1) if plant else ''))
am = blk(src, 'areaManager')
for am2 in re.finditer(r'<li Class="(Area_\w+)">(.*?)</li>', am, re.S):
    ab = am2.group(2)
    tc = re.search(r'<trueCount>(\d+)</trueCount>', ab)
    say('    %-18s %s ô' % (am2.group(1), tc.group(1) if tc else '?'))
say('')

# ---------------------------------------------------------------- 9. grids
say('== 9. LƯỚI ĐÃ GIẢI MÃ (mái / sương mù / đất / mỏ) ==')
roof = struct.unpack('<%dH' % TILE, inner_deflate(src, 'roofGrid', 'roofsDeflate')) if 'roofsDeflate' in src else [0] * TILE
fog = inner_deflate(src, 'fogGrid', 'fogGridDeflate')
terr = struct.unpack('<%dH' % TILE, inner_deflate(src, 'terrainGrid', 'topGridDeflate'))
NATURAL = {6699, 10820}
construct = [i for i, v in enumerate(roof) if v and v not in NATURAL]
supports = []
for (c, d), lst in BUCKET.items():
    if d in ('Wall', 'Door', 'Column'):
        for s, e in lst:
            p = pos_of(src[s:e])
            if p:
                supports.append(p)
def fog_at(p):
    x, z = p
    k = z * SIZE + x
    return (fog[k // 8] >> (k % 8)) & 1
sbuck = defaultdict(list)
for sx, sz in supports:
    sbuck[(sx // 8, sz // 8)].append((sx, sz))
def near_support_dist(p):
    x, z = p
    best = 99.0
    for bx in range(x // 8 - 1, x // 8 + 2):
        for bz in range(z // 8 - 1, z // 8 + 2):
            for sx, sz in sbuck.get((bx, bz), ()):
                best = min(best, math.hypot(x - sx, z - sz))
    return best
risky = []
for i in construct:
    x, z = i % SIZE, i // SIZE
    d = near_support_dist((x, z))
    if d > 6.0:
        risky.append((x, z, round(d, 2)))
say('mái: %d ô có mái (khối xây) | %d điểm tựa (tường/cửa/cột)' % (len(construct), len(supports)))
say('mái NGUY HIỂM (cách tựa > 6 ô — sẽ sập): %d ô' % len(risky))
for r in sorted(risky):
    say('    (%d,%d) cách %.2f ô' % r)
fogn = sum(1 for i in range(TILE) if (fog[i // 8] >> (i % 8)) & 1)
say('sương mù: %d ô (%.1f%% bản đồ)' % (fogn, 100.0 * fogn / TILE))
# cụm sương mù lớn
seen = set(); clusters = []
for i in range(TILE):
    if not ((fog[i // 8] >> (i % 8)) & 1) or i in seen:
        continue
    st = [i]; seen.add(i); pts = []
    while st:
        k = st.pop(); pts.append(k)
        x, z = k % SIZE, k // SIZE
        for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, nz = x + dx, z + dz
            if 0 <= nx < SIZE and 0 <= nz < SIZE:
                nk = nz * SIZE + nx
                if nk not in seen and ((fog[nk // 8] >> (nk % 8)) & 1):
                    seen.add(nk); st.append(nk)
    clusters.append(pts)
clusters.sort(key=len, reverse=True)
for pts in clusters[:5]:
    xs = [k % SIZE for k in pts]; zs = [k // SIZE for k in pts]
    say('    cụm sương mù %d ô: x%d-%d z%d-%d' % (len(pts), min(xs), max(xs), min(zs), max(zs)))
th = Counter(terr)
say('đất: ' + ', '.join('hash%s=%d' % (k, v) for k, v in th.most_common(8)))
dsg = blk(src, 'deepResourceGrid')
dg = inner_deflate(src, 'deepResourceGrid', 'defGridDeflate') if 'defGridDeflate' in dsg else b''
if dg:
    dvals = struct.unpack('<%dH' % (len(dg) // 2), dg)
    nz = sum(1 for v in dvals if v)
    say('mỏ sâu (deepResourceGrid): %d/%d ô có tài nguyên' % (nz, len(dvals)))
ctm = blk(src, 'compressedThingMapDeflate')
if '<compressedThingMapDeflate>' in src:
    raw = decode_grid(re.search(r'<compressedThingMapDeflate>\s*([A-Za-z0-9+/=\s]+?)\s*</compressedThingMapDeflate>', src).group(1))
    cv = struct.unpack('<%dH' % (len(raw) // 2), raw)
    mine = [(i % SIZE, i // SIZE, v) for i, v in enumerate(cv) if v]
    say('ô đá/mineable (compressedThingMapDeflate): %d ô' % len(mine))
    nm = sorted(mine, key=lambda t: math.dist((t[0], t[1]), BASE))[:10]
    say('    gần căn cứ nhất: ' + '; '.join('(%d,%d)h%d cách %.1f' % (x, z, v, math.dist((x, z), BASE)) for x, z, v in nm))
say('')

# ---------------------------------------------------------------- 10. research/ideo/quests
say('== 10. NGHIÊN CỨU ĐÃ XONG ==')
rm = blk(src, 'researchManager')
proj = re.search(r'<currentProj>([^<]*)</currentProj>', rm)
keys = re.findall(r'<li>([A-Za-z_]+)</li>', blk(blk(rm, 'progress'), 'keys'))
vals = re.findall(r'<li>([\d.]+)</li>', blk(blk(rm, 'progress'), 'values'))
pairs = list(zip(keys, vals))
fin = [k for k, v in pairs if float(v) >= 1.0]
prog = [(k, v) for k, v in pairs if float(v) < 1.0]
say('    đang nghiên cứu: %s' % (proj.group(1) if proj else '-'))
say('    đã xong (%d): %s' % (len(fin), ', '.join(fin)))
if prog:
    say('    CHƯA nghiên cứu: %d công nghệ' % len(prog))
    nz = [(k, v) for k, v in prog if float(v) > 0]
    if nz:
        say('    đang làm dở: ' + ', '.join('%s=%.0f%%' % (k, float(v) * 100) for k, v in nz))
say('')
say('== 11. TÔN GIÁO ==')
ideo = blk(src, 'ideoManager')
if ideo:
    nm = re.search(r'<name>([^<]*)</name>', ideo)
    cert = re.search(r'<certainty>([\d.]+)</certainty>', ideo)
    mem = re.search(r'<memberName>([^<]*)</memberName>', ideo)
    say('    ideo: %s (member=%s, certainty=%s, hidden=%s)' % (
        nm.group(1) if nm else '?', mem.group(1) if mem else '?', cert.group(1) if cert else '?',
        'True' if '<hiddenIdeoMode>True' in ideo else 'False'))
    pblk = blk(ideo, 'precepts')
    prec = ['%s=%s' % (d, clean(n, 20)) for n, d in re.findall(r'<name>([^<]*)</name>\s*<def>([^<]+)</def>', pblk)]
    say('    precepts (%d): ' % len(prec) + ', '.join(dict.fromkeys(prec)))
    mm = blk(ideo, 'memes')
    mem = re.findall(r'<li>([^<]+)</li>', mm)
    say('    memes: ' + (', '.join(mem) if mem else '(không có / ẩn)'))
say('')
say('== 12. NHIỆM VỤ ==')
qm = blk(src, 'questManager')
for qm2 in re.finditer(r'<li>(.*?)(?=<li>\s*<name>|</quests>)', qm, re.S):
    qb = qm2.group(1)
    nm = re.search(r'<name>([^<]*)</name>', qb)
    if not nm:
        continue
    say('    %-40s ended=%s outcome=%s tick=%s' % (
        clean(nm.group(1), 40),
        clean(re.search(r'<ended>([^<]*)</ended>', qb).group(1) if '<ended>' in qb else '?', 6),
        clean(re.search(r'<endOutcome>([^<]*)</endOutcome>', qb).group(1) if '<endOutcome>' in qb else '', 12),
        re.search(r'<appearanceTick>(\d+)</appearanceTick>', qb).group(1) if '<appearanceTick>' in qb else '?'))
say('')

# ---------------------------------------------------------------- 13. threats / lords
say('== 13. ĐE DOẠ ĐANG HOẠT ĐỘNG (lordManager) ==')
lm = blk(src, 'lordManager')
for lm2 in re.finditer(r'<lordJob Class="([\w.]+)">(.*?)(?=<lordJob Class=|</lordManager>)', lm, re.S):
    lb = lm2.group(2)
    fac = re.search(r'<faction>(Faction_\d+)</faction>', lb)
    own = re.findall(r'<li>(Thing_[^<]+)</li>', blk(lb, 'ownedPawns'))
    extra = re.findall(r'<(wakeOnPawnUnfogged|canSteal|assaultColony)>([^<]*)</\1>', lb)
    say('    %-34s %-12s pawns=%d %s %s' % (lm2.group(1), fac.group(1) if fac else '-', len(own),
                                            ', '.join(own[:4]), dict(extra)))

say('    (lord = nhóm AI đang hoạt động: raid, quái ngủ đông, caravan…)')
say('')
say('== 14. LỊCH SỬ ĐÃ LỌC (taleManager: chỉ sự kiện quan trọng) ==')
tal = blk(src, 'taleManager')
KEEP = ('CollapseDodged', 'KilledBy', 'Wounded', 'LandedInPod', 'Raid', 'RaidArrived', 'Bonded', 'BecameLover',
        'Marriage', 'PawnKilled', 'Death', 'KilledLeader', 'Ritual', 'Funeral', 'Recruited', 'Escaped',
        'Captured', 'Downed', 'Berserk', 'MentalBreak', 'ChangedIdeo', 'GaveBirth', 'Surgery', 'Anomaly')
tales = []
for tm2 in re.finditer(r'<li Class="(Tale_\w+)">(.*?)</li>', tal, re.S):
    tb = tm2.group(2)
    d = re.search(r'<def>([^<]+)</def>', tb)
    if not d or d.group(1) not in KEEP:
        continue
    date = re.search(r'<date>(\d+)</date>', tb)
    names = re.findall(r'<first>([^<]*)</first>', tb) + re.findall(r'<name>([^<]+)</name>', tb)
    txt = re.search(r'<customLabel>([^<]*)</customLabel>', tb)
    tales.append((int(date.group(1)) if date else 0, d.group(1), ', '.join(dict.fromkeys(names))[:60],
                  clean(txt.group(1) if txt else '', 60)))
tales.sort()
c = Counter(t[1] for t in tales)
say('    tổng: %d tale | theo loại: %s' % (len(tales), ', '.join('%s×%d' % (k, v) for k, v in c.most_common())))
say('    --- 25 sự kiện cuối (absTick) ---')
for dt, d, nm, tx in tales[-25:]:
    say('    %-8d %-16s %-30s %s' % (dt, d, nm, tx))
say('')

# ---------------------------------------------------------------- 15. world
say('== 15. THẾ GIỚI ==')
fm = blk(src, 'factionManager')
names = re.findall(r'<def>([^<]+)</def>\s*<name>([^<]*)</name>', fm)
say('    phe: ' + '; '.join('%s=%s' % (a, b) for a, b in names))
wo = blk(src, 'worldObjects')
stl = []
for sm in re.finditer(r'<li Class="Settlement">(.*?)</li>', wo, re.S):
    sb = sm.group(1)
    t = re.search(r'<tile>(\d+),', sb)
    f = re.search(r'<faction>(Faction_\d+)</faction>', sb)
    n = re.search(r'<nameInt>([^<]*)</nameInt>', sb)
    if t:
        stl.append((int(t.group(1)), f.group(1) if f else '?', clean(n.group(1) if n else '', 24)))
say('    khu định cư: %d | tiểu hành tinh: %d' % (len(stl), wo.count('BasicAsteroidMapParent')))
fidx = {('Faction_%d' % i): n for i, (d, n) in enumerate(names)}
SX = 500  # heuristic: bản đồ hành tinh ~500x500 (tile id < 250000)
def txy(t):
    return (t % SX, t // SX)
start = re.search(r'<startingTile>(\d+),', inf)
st_tile = int(start.group(1)) if start else None
if st_tile:
    say('    tile thuộc địa: %d (x=%d,z=%d theo giả định %dx%d)' % (st_tile, st_tile % SX, st_tile // SX, SX, SX))
    for t, f, n in sorted(stl, key=lambda x: math.dist(txy(x[0]), txy(st_tile)))[:8]:
        say('        %-24s %-22s %-26s cách ~%d tile' % (n, f, fidx.get(f, f), math.dist(txy(t), txy(st_tile))))
say('')

# ---------------------------------------------------------------- 16. area "home" details
say('== 16. GHI CHÚ CẦN THIẾT CHO KẾ HOẠCH ==')
res = blk(src, 'reservationManager')
say('    reservation (đang tranh nhau dùng): %d mục' % len(re.findall(r'<li>', res)))
ds = blk(src, 'designationManager')
say('    designation đang treo: %s' % Counter(re.findall(r'<def>([^<]+)</def>', ds)).most_common())
pp = blk(src, 'playSettings')
keys = re.findall(r'<(\w+)>([^<]{0,40})</\1>', pp)
say('    playSettings: ' + ', '.join('%s=%s' % (k, v) for k, v in keys[:14]))
say('')

# ---------------------------------------------------------------- output
text = '\n'.join(O) + '\n'
if out_path:
    open(out_path, 'w', encoding='utf-8').write(text)
    nbytes = len(text.encode('utf-8'))
    print('OK -> %s' % out_path)
    print('gốc : %s bytes' % f'{len(src):,}')
    print('digest: %s bytes (%.2f%% file gốc)' % (f'{nbytes:,}', 100.0 * nbytes / len(src)))
    print('ước lượng token: ~%s' % f'{int(nbytes/3.5):,}')
else:
    print(text)
