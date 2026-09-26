# 🎯 PHÂN TÍCH TÌNH HÌNH HIỆN TẠI — RIMWORLD 1.6.4871
## Thuộc địa "Hateria" · Hành tinh Tureis · Ngày 13 Septober, năm 5500 · ~05:00 sáng
### Bản save mới nhất: `Hateria.rws` (tick 432.519) — bản cũ hơn: `Autosave-5.rws` (tick 423.521)

---

# ⚡ PHẦN 1 — TÓM TẮT TRONG 60 GIÂY

| | |
|---|---|
| 🕐 **Đang là** | Ngày 13/9 (Septober), **~5 giờ sáng** (mới rạng đông), trời **Clear** (quang đãng), **còn ~2,5 ngày nữa là sang mùa đông (Decembary)** |
| 👥 **Còn lại** | **2 người**: Nicole (51t, nữ, tay súng + nhà nghiên cứu) và Nate "Hairy" (38t, nam, thợ mỏ). Cả 2 đang **nằm trên giường** |
| 💀 **Vừa mất** | **Kory Smith (51t)** — bị **mái nhà sập đè chết** lúc **~4:39 sáng nay**, chỉ **21 phút trước** khi save |
| 🍽️ **Thức ăn** | **0 món ăn trong toàn bộ thuộc địa.** Nicole đang **đói 0%** (mức chết đói) |
| 🩸 **Y tế** | Nicole bị **vết cắt ở đầu 21/25 HP chưa băng**, đang chảy máu (3,8%) + suy dinh dưỡng 6,8% |
| 🏚️ **Nguy hiểm trước mắt** | **8 ô mái nhà ở khu ruộng sẽ sập tiếp** — y hệt ô đã giết Kory |
| ⚰️ **Nghi lễ** | Lễ tang cho Kory **sẽ hết hạn sau 9 ngày (7 Decembary)** — nhưng **chưa có cái mộ nào** |
| ⚔️ **Đe doạ ngủ đông** | 5 Fleshbeast + 1 Centipede trong 2 khu di tích cổ (còn nguyên sương mù, chưa lộ) |
| 💰 **Tài sản** | 1.961 thép · 800 bạc · **32 linh kiện** (30 công nghiệp + 2 spacer) · 360 Gravlite · **không có điện, không turret** |
| 🎯 **Mục tiêu dài hạn** | Đã có **GravEngine + 360 Gravlite** ⇒ mở khoá kết thúc game kiểu **Odyssey (đóng Gravship)** |

> **3 việc phải làm ngay khi bấm Play:** ① Xóa vùng xây mái khu ruộng ② Cho Nicole ăn + băng đầu ③ Xây mộ, chôn Kory.

---

# ⚡ PHẦN 2 — CHUYỆN GÌ ĐÃ XẢY RA? (dòng thời gian 7,2 ngày)

| Ngày | Sự kiện |
|---|---|
| 0,00 | 3 người tỉnh dậy từ khoang ngủ đông, rơi xuống bằng khoang thoát hiểm (scenario hướng dẫn) |
| 0,49 | Nate phát hiện **Void Monolith** (Anomaly) |
| 1,56 | **⚔️ Raid #1** — phe "Chất độc society" (Pirate Waster) tấn công |
| 2,50 | Khách từ bộ lạc **Ascamlán** ghé thăm |
| 3,40 | Chuột phát điên |
| 4,02 | Người ăn xin tới (nhiệm vụ "Vagabond Desires Resources") → **thất bại** |
| 4,20 | Một lữ khách bị hại (làm giảm tâm trạng cả đội) |
| 4,36 | **Nicole và Kory thành người yêu** 💕 |
| 4,40 | Một con quạ **tự thuần hoá** |
| 5,40 | **⚔️ Raid #2** — Waster tấn công lần 2; cả đội bị thương, **một nữ cướp bị hạ (Ded Skarad — xác còn ở (94,205))** |
| 6,02 | Nhận nhiệm vụ **"Mechanoid Signal"** (Odyssey) |
| 6,09 | **Tàu mech rơi** → thu được **GravEngine** + **360 Gravlite** |
| **7,19** | **💀 MÁI NHÀ SẬP — KORY CHẾT.** Nicole bị thương đầu. 14 lần "CollapseDodged" trong cùng 1 tick |
| **7,21** | **HIỆN TẠI** — save mới nhất. 3 lá thư chưa đọc |

**Điểm mấu chốt:** thuộc địa mới 7,2 ngày tuổi, đã bị 2 raid, và **chưa từng có thức ăn dự trữ**. Đây là vấn đề hệ thống, không phải vận rủi.

---

# ⚡ PHẦN 3 — SỰ CỐ CHÍNH: CÁI CHẾT CỦA KORY & NGUY CƠ SẬP TIẾP

## 3.1. Chuyện đã xảy ra
- Lá thư #15 *"Roof collapse"*: *"A roof has collapsed because it was too far from any support. These things were crushed: **-Steel, -Kory (Math prof), -Revolver (normal 81%), -Nicole (Dancer), -Wooden fence (0%)**"*
- Kory bị **đè vào cổ** → chết ngay. Nicole bị **đè vào đầu** → vết cắt 21/25.
- Trong cùng tick đó có **14 lần `CollapseDodged`** (14 lần suýt bị đè chết) — nghĩa là **cả một vùng mái sập cùng lúc**.

## 3.2. Vì sao sập — nguyên nhân gốc (rất quan trọng, vì còn 8 ô nữa sắp sập y hệt)
Bạn đã **quét vùng "Xây mái" (Build roof)** lên khu ruộng lúa / chuồng ở phía nam căn cứ (tổng **431 ô** chỉ định mái).

> **Luật của RimWorld: một ô mái chỉ đứng vững nếu cách một điểm tựa (tường / cửa / cột) không quá 6 ô.** Các ô mái phía bắc khu ruộng tựa vào **tường nam nhà kho ở z=128**; đi xa hơn về phía nam thì **chỉ còn 2 cây cửa ở (120,130) và (121,130)** làm điểm tựa. **Hàng rào (dù là blueprint hay đã xây) KHÔNG đỡ được mái.**

Kết quả giải mã lưới mái trong save — **8 ô mái đang ở ngoài ngưỡng 6 ô và sẽ sập tiếp**:

```
Vị trí 8 ô mái SẮP SẬP (⚠), đều nằm NGAY TRÊN ruộng lúa:
   (116,135)  (125,135)              ← cách điểm tựa 6,4 ô
   (117,136)  (118,136)  (119,136)   ← 6,1 – 6,7 ô
   (122,136)  (123,136)  (124,136)   ← 6,1 – 6,7 ô

Ô đã sập lúc Kory chết: (121,139) — cách điểm tựa gần nhất 9,0 ô
   (đúng như hiện trạng: z=137–139 hiện không còn ô mái nào)
```

## 3.3. Hậu quả kép đang chồng lên nhau
1. **Nguy hiểm sinh mạng:** 8 ô mái kia sẽ sập bất cứ lúc nào, đúng vào lúc Nicole/Nate ra ruộng hái lúa. Với 2 người, mất thêm 1 người là mất cả thuộc địa.
2. **Sập cái này lại xây cái khác:** mái sập → game tự đặt lại blueprint mái (vì vùng "Build roof" vẫn còn) → pawn chạy ra xây → lại sập. **Vòng lặp vô tận cho tới khi bạn xoá vùng chỉ định.**
3. **Ruộng lúa bị chặn sáng:** 58/75 cây lúa nằm **dưới mái** → ánh sáng = 0 → **không lớn thêm được**. 17 cây còn lại ngoài trời cũng mới ở 0,31 độ lớn (cần 1,0 mới thu hoạch). **Vụ lúa này không thể cứu đói trong 2–3 ngày tới.**

---

# ⚡ PHẦN 4 — NHÂN SỰ: 2 NGƯỜI CÒN LẠI

## 🔴 Nicole Squid — 51 tuổi, nữ — ⚠️ NGUY KỊCH, CẦN CỨU NGAY
| Mục | Chi tiết |
|---|---|
| **Sinh lực** | **Food = 0%** (đói chết) · Rest 79% · Joy 46% · Comfort 36% |
| **Tâm trạng** | **45,3%** — đang trên bờ vực "khủng hoảng tinh thần" (35%). **Nguy cơ nổi loạn/khủng hoảng cao** |
| **Đang buồn vì** | 💔 Người yêu qua đời (`MyLoverDied`) · 🌫️ Không có mái che khi ngủ · 🍽️ Ăn không bàn · 🛏️ Ngủ tập thể · 😞 Bị từ chối tình cảm (Kory từ chối cô ấy 3,2 ngày trước) · 🤢 Suy dinh dưỡng |
| **Đang vui vì** | 👨‍🚀 Cùng rơi xuống hành tinh với Kory & Nate · 💬 Nói chuyện sâu với Kory nhiều lần |
| **Sức khoẻ** | **Cut (vết cắt) ở ĐẦU — 21/25 HP, CHƯA BĂNG** · BloodLoss 3,8% · Malnutrition 6,8% |
| **Kỹ năng** | Trí tuệ **12** · Xã hội **10** · Bắn súng **7** · Nghệ thuật 7 · Nấu ăn 5 · Y học 4 · Cây cối 4 · Chế tạo 3 |
| **Trang bị** | 🔫 **Bolt-action rifle 98%** · Áo Synthread (không giáp) |
| **Đặc điểm** | **Gourmand (Háu ăn)** — ăn nhanh gấp đôi, nhưng mau đói hơn |
| **Tuổi** | 51 sinh học — **nguy cơ đau lưng/viêm khớp**, nên tránh lao động nặng |

👉 **Nicole là bộ não của thuộc địa** (Trí tuệ 12 = nhà nghiên cứu chính, Xã hội 10 = dàn xếp tốt nhất). **Mất cô ấy = mất tương lai nghiên cứu.**

## 🟠 Nate "Hairy" Sanders — 38 tuổi, nam
| Mục | Chi tiết |
|---|---|
| **Sinh lực** | Food 60% · Rest 92% · **Joy 24% (rất thấp)** · **Beauty 23% (rất thấp)** |
| **Tâm trạng** | 60% — ổn nhưng Joy thấp sẽ kéo xuống dần |
| **Sức khoẻ** | 5 vết bầm (từ đánh nhau với Ded Skarad) · không nguy hiểm |
| **Kỹ năng** | **Đào mỏ 11 (đam mê lớn!)** · Y học 8 · Trí tuệ 5 · Nghệ thuật 4 · Bắn súng 3 · Xây dựng 1 |
| **Trang bị** | 🛡️ **Flak Vest + Advanced Helmet (plasteel)** — nhưng ❌ **KHÔNG CÓ VŨ KHÍ** |
| **Đặc điểm** | **Bloodlust (Khát máu)** — vui khi giết địch · **CreepyBreathing** (mọi người ghét) · **Jealous** (ghen tị) |
| **Tuổi** | 38 — còn trẻ, làm việc nặng tốt |

👉 **Nate là lao động chính**: Đào mỏ 11 + Y học 8. Nhưng anh ấy **tay không** — nếu raid ập tới lúc này thì vô dụng. **Đưa súng lục của Kory cho anh ấy NGAY.**

## ⚫ Kory Smith — 51 tuổi, nam — ĐÃ CHẾT
- Là **thợ xây + giáo viên toán**, người yêu của Nicole.
- Xác ở **(122,138)**, độ phân huỷ 1000/1000, **chưa bị đánh dấu `Forbidden`**.
- **6 con quạ hoang (`Crow36810`, `Crow36837`, `Crow36838`, `Crow36839`, `Crow36869`, `Crow36870`) đã đăng ký ăn xác này** trong sổ reservation của save. Nếu không chôn gấp, xác sẽ bị ăn/hư và **lễ tang sẽ không thể thực hiện** (phải chuyển sang loại "không có xác").

---

# ⚡ PHẦN 5 — CĂN CỨ & TÀI SẢN

## 5.1. Sơ đồ căn cứ (giải mã từ lưới mái + danh sách vật thể)
```
    000000000011111111112222222222333333   ← toạ độ X
    012345678901234567890123456789012345
112                                     
113          ####     #######D######       ← tường bắc: LỖ HỔNG 5 ô (x113–117) · CỬA (125,113)
114          #          #..........#       ← KHU TÂY x110–119 KHÔNG MÁI (sân/lab) │ PHÒNG ĐÔNG x121–130 CÓ MÁI
115          #          #..........#    
116          #          #........F.#       ← Bếp nấu (129,116)
117          # r        #....o.....#       ← bàn NC (111,117) │ Đuốc (125,117)
118          #          #......r...#       ← bàn NC (127,118)
119          #          #bbb......a#       ← 3 giường (121–123,119) · đệm thú (130,119)
120          #######################       ← tường nam khối bắc
121                      ########          ← dải z=121 (x≤120) là HÀNH LANG HỞ NGOÀI TRỜI giữa 2 khối nhà
122  #############D#######......# sss ss   ← NHÀ KHO: CỬA (114,122) — lối vào DUY NHẤT
123  #..........................# s        ← kho 26×5 ô CÓ MÁI (2 stockpile chứa toàn bộ tài nguyên)
124  #..........................# s     
125  #..........................#       
126  #..........................# s     
127  #..........................# s     
128  ############################ sss ss   ← tường nam nhà kho z=128 = điểm tựa chính của mái khu ruộng
129                                     
130                =====DD=====            ← HÀNG RÀO chỉ là BLUEPRINT chưa xây + 2 CỬA (120,130),(121,130)
131                =**********=            ← '*' = lúa (x116–125) · '=' = cọc rào blueprint (x115 & x126)
132                =**********=            ← MÁI XÂY phủ z130–134 (x116–126), z135–136 hẹp dần
133                =**********=         
134                =**********=         
135                =**********=            ← 2 ô mái NGUY HIỂM: (116,135),(125,135)
136                =**********=            ← 6 ô mái NGUY HIỂM: (117,136),(118,136),(119,136),(122,136),(123,136),(124,136)
137                =**********=         
138                =     *K***=            ← K = XÁC KORY (122,138) — 6 quạ đang nhắm ăn
139                ============            ← ranh giới nam vùng quy hoạch
140                                     
```

**Điểm cần lưu ý về thiết kế căn cứ:**
- ✅ Căn cứ **có tường bao quanh** (gỗ + thép), 4 cửa (125,113), (114,122), (120,130), (121,130) và 2 khối nhà lớn đều có mái.
- ⚠️ **Khối bắc bị chia làm 2 nửa KHÔNG thông nhau** (tường x=120, không có cửa): nửa **tây (x110–119) hoàn toàn KHÔNG MÁI** và có **lỗ hổng 5 ô ở z=113 (x113–117)** — vừa là lỗ hổng phòng thủ, vừa khiến bàn nghiên cứu (111,117) nằm ngoài trời; nửa **đông (x121–130)** mới là phòng ngủ-bếp có mái.
- ✅ Bãi bao cát hình vành khuyên ở (130–136, z122–128) — có **3 lỗ hổng: (133,122) phía bắc, (130,125) phía tây, (136,125) phía đông** — **hoàn toàn trống, không có lính, không có turret**.
- ⚠️ **Phòng ngủ và kho ngăn cách bằng dải z=121 hở ngoài trời** → nếu bị tấn công, 2 người bị chia cắt ở 2 toà nhà khác nhau và phải chạy qua sân. Cần bịt/bố trí lại.
- ⚠️ **Nhà kho chỉ có 1 cửa duy nhất ở (114,122)**, hướng ra sân z=121 → nếu cửa này bị chặn, toàn bộ tài nguyên bị khoá trong kho.
- ⚠️ **Trong phòng ngủ có 1 xác thú thối (128,117 — xác thỏ)** → vừa mất vệ sinh vừa giảm tâm trạng mỗi ngày. Dọn ngay.
- ⚠️ **Không có lối đi vòng quanh an toàn** giữa ruộng và kho — đi từ kho ra ruộng phải vòng qua sân hở.

## 5.2. Tài sản & vật tư (số liệu chính xác từ save)
| Loại | Số lượng | Ghi chú |
|---|---|---|
| **Thép (Steel)** | **1.961** | Rất dồi dào, đủ xây 300+ tường |
| **Bạc (Silver)** | **800** | Đủ mua ~8 món tốt khi có Comms console |
| Gravlite Panel | **360** | Vật liệu đóng Gravship (Odyssey) |
| Vải (Cloth) | 200 | May quần áo, áo giáp vải |
| **Linh kiện (Component)** | 30 | Quan trọng — dành cho điện/nghiên cứu |
| Thuốc công nghiệp | 22 | Dùng băng bó |
| Thuốc herbal | 1 | |
| Thuốc Ultratech | 8 ⚠️ | **Đang bị Forbidden** — ở khu cổ phía tây (17,195) |
| Component Spacer | 2 ⚠️ | **Đang bị Forbidden** — ở khu cổ phía tây (16,193) |
| Cần sa (Smokeleaf) | 12 (bị Forbidden) + 11 | Ở khu xác Ded Skarad (94,205) |
| Gỗ (WoodLog) | 22 | Rất ít — cần chặt thêm |
| **THỰC PHẨM** | **0** ⛔ | **Không có một món nào trong toàn map** |
| Nhiên liệu bếp | 35,6 | Còn đủ nấu vài bữa |

**Vũ khí trên bản đồ:** 1 khẩu bolt-action (Nicole đang cầm) · 1 **Revolver 81%** (của Kory, rơi ở (123,138) — **đang bị Forbidden**) · 3 dao · 1 dùi cui.
**Phòng thủ:** 20 bao cát — **0 turret, 0 bẫy, 0 súng phụ**.
**Điện:** **KHÔNG CÓ** — không generator, không ắc-quy, **dù đã nghiên cứu xong Điện và Máy điều hoà**. Đây là lãng phí rất lớn.

---

# ⚡ PHẦN 6 — THỨC ĂN & NÔNG NGHIỆP (trọng tâm số 1)

## 6.1. Vì sao hết sạch thức ăn?
1. **Bill nấu ăn bị kẹt**: bếp `FueledStove` (129,116) vẫn còn bill `CookMealSimple`, nhưng **không có nguyên liệu thô** nào → không nấu được.
2. **Không có bàn mổ thịt (Butcher Table)** → dù có giết được thú cũng **không xẻ thịt được** thành nguyên liệu nấu ăn.
3. **Ruộng lúa bị mái che 58/75 cây** → 0 ánh sáng → không lớn.
4. **Chưa tận dụng thức ăn hoang dã**: toàn bản đồ có **130 bụi dâu (88 bụi đã chín)** và **141 cây cỏ y tế (healroot)** mà không ai hái.

## 6.2. Nguồn thức ăn khẩn cấp — có sẵn, MIỄN PHÍ, cách căn cứ rất gần
**Dâu hoang đã chín (88 bụi)** — 10 bụi gần nhất (đơn vị: ô):
| Vị trí | Khoảng cách |
|---|---|
| **`(111,135)`** | **15 ô** ← GẦN NHẤT, hái được trước khi làm gì khác |
| `(124,149)` | 24 ô |
| `(147,132)` | 26 ô |
| `(147,141)` | 30 ô |
| `(126,87)` | 38 ô |
| `(110,164)` | 41 ô |
| `(78,125)` | 44 ô |
| `(161,104)` | 44 ô |
| `(155,156)` | 45 ô |
| `(116,173)` | 48 ô |

→ **Chỉ 10 bụi này đã cho khoảng 88–160 quả dâu = đủ ăn 3–5 ngày cho 2 người.** Toàn bộ 88 bụi ≈ **~900 quả dâu ≈ 44 điểm dinh dưỡng ≈ 27 ngày ăn.**
(Trên quả, dâu là `Plant_Berry` — thu hoạch bằng công cụ **Harvest (🔨)** hoặc để pawn tự hái.)

**2 nguồn phụ trợ:**
- **141 cây cỏ y tế (healroot)** → chế thuốc herbal, giảm phụ thuộc thuốc công nghiệp.
- **Động vật hoang gần nhất**: Thổ Nhĩ Kỳ `(130,161)` cách 37 ô · Thỏ `(74,165)` cách 62 ô · Chim sẻ `(154,51)` cách 81 ô · Gấu mèo (Raccoon) `(64,99)` cách 64 ô · **⚠️ 1 con WARG (chó sói đen) ở `(90,154)` cách 43 ô** → **nếu bạn cho Nicole ra săn, phải cho cô ấy cầm súng trường và để Nate đi cùng, hoặc đừng lại gần con Warg.**
- **Yak "Venus"** (con vật duy nhất của thuộc địa, trong chuồng (156–158, 164–168)): nếu bí quá, giết lấy thịt (~300 đơn vị thịt) — nhưng mất con vật duy nhất.

## 6.3. Kế hoạch nông nghiệp dài hạn
| Vấn đề hiện tại | Cách sửa |
|---|---|
| Ruộng nằm dưới mái, bị rào blueprint bao quanh | **XOÁ vùng "Xây mái" trên ruộng**, xoá luôn 38 blueprint hàng rào, để ruộng **lộ thiên hoàn toàn** |
| Lúa cần 3 ngày mới chín mà mùa đông còn 2,5 ngày | **Đổi cây trồng**: trồng **Potato** (chịu lạnh tốt, để lâu) hoặc **Corn** (năng suất cao) thay vì lúa gạo |
| Mùa đông không thể trồng ngoài trời | Nghiên cứu **Hydroponics (Thuỷ canh)** → nhà kính có **Sun Lamp** = trồng quanh năm |
| Không có kho lạnh | Nghiên cứu **Air Conditioning (đã xong!) `Cooler`** + Pin (Batteries) → dựng phòng lạnh. **Mùa đông thì chỉ cần phòng kín** |
| Thức ăn không để lâu | Làm **Pemmican** (đã nghiên cứu Pemmican) — để được hàng tháng trời mà không cần tủ lạnh |

> **Chiến lược đúng cho 2 người:** 3–4 ruộng lớn (khoai tây + ngô) ở khu đất màu mỡ + 1 nhà kính thuỷ canh + 1 kho lạnh + 1 bàn mổ thịt. Đó là "an ninh lương thực".

---

# ⚡ PHẦN 7 — ĐE DOẠ & AN NINH

## 7.1. Mối đe doạ đang tồn tại trên bản đồ

| Mối đe doạ | Vị trí | Trạng thái |
|---|---|---|
| **5 Fleshbeast** (Bulbfreak ×3, Toughspike, Trispike) | Khu cổ phía tây (7–17, 193–196) | Ở trong chế độ **`LordJob_FleshbeastAssault` (sẽ tấn công thuộc địa)** nhưng **đang bị nhốt trong khu cổ còn nguyên sương mù**. Sẽ tung ra nếu bạn mở cửa/khoét tường khu đó. |
| **1 Centipede Gunner** (mech hạng nặng) | Khu cổ phía bắc (72, 216) | **Ngủ đông** (`CompCanBeDormant`) — thức dậy khi bị nhìn thấy/đánh. |
| **Void Monolith** (Anomaly) | **(167,114)** — cách căn cứ ~45 ô về phía đông | Chưa kích hoạt — mức Anomaly hiện là **"Inactive"** ✅ |
| **1 Warg** (chó sói) | (90, 154) — 43 ô | Lang thang gần căn cứ |
| 1 Megasloth, 3 Tê giác, 7 Lợn rừng, 2 Boomrat | Xa (117–160 ô) | Chỉ nguy nếu lại gần |
| **2 raid đã xảy ra** (đều từ phe Pirate Waster "Chất độc society") | Ngày 1,56 và 5,40 | Lần 2 hạ 1 nữ cướp — Ded Skarad, xác còn ở (94,205) |
| **1 Faction_10 fleshbeast** và 1 **Faction_8 mech** đang có lord job | — | Đang "dormant/contained" |
| **Storyteller: Cassandra Classic / Easy** | `adaptDays = −31,5` | **Đang ở giai đoạn "nợ" bạn sự kiện dễ — nghĩa là raid tiếp theo sẽ mạnh hơn bình thường.** |

## 7.2. Vấn đề an ninh của căn cứ
- ❌ **0 turret** — bãi bao cát xây xong mà không có gì trong đó.
- ❌ **Không có tường bao quanh toàn bộ thuộc địa** (chỉ có 2 khối nhà có tường). Ruộng và sân hoàn toàn hở.
- ❌ **Phòng ngủ ↔ nhà kho bị ngăn cách** → không thể hỗ trợ nhau khi bị tấn công.
- ❌ **Nate không có vũ khí.**
- ❌ **Chưa có điện** → không thể xây turret (turret cần điện).

---

# ⚡ PHẦN 8 — TÍN NGƯỠNG, THẾ GIỚI & NHIỆM VỤ

## 8.1. Đạo "Astropolitan 2" (Ideology — đang chạy chế độ ẩn/hidden)
Các luật đang ảnh hưởng đến bạn:
- 🍖 **Ăn thịt người: được CHẤP NHẬN** (`Cannibalism_Classic`) — về mặt luật tôn giáo, đây **không phải tội**. (Có 6 xác người trên map — nhưng tất nhiên tôi không khuyến khích dùng cách đó khi còn dâu rừng.)
- 💀 **Xác chết bị coi là ghê tởm** (`Corpses_Ugly`) → đừng để xác trong nhà, và **nhớ chôn/dọn xác Kory**.
- 🪲 **Thịt côn trùng bị khinh** · 🥣 **Bột dinh dưỡng kinh tởm** · 💑 **Tình yêu tự do (Lovin_Free)** · ⛓️ **Chấp nhận nô lệ** · 🏛️ **Nghi lễ: lễ tang, tử hình công khai, phiên toà, liên kết cây Anima, phóng Gravship...**
- ⚠️ **KHÔNG có work priority thủ công** (bạn chưa bao giờ mở tab Work để set priority) → pawn làm việc theo mặc định.

## 8.2. Thế giới
- **16 phe**: thù địch gồm 6 phe man rợ/cướp, **Mechanoid, Insect, Entities (thực thể), AncientsHostile, HoraxCult**. Trung lập: **Ascamlán (bộ lạc), Empire (Đế chế), TradersGuild, Salvagers**.
- **247 khu định cư** trên hành tinh, **12 tiểu hành tinh** (có Vàng Jade & Plasteel).
- Thù địch mạnh nhất về lâu dài: **Mechanoid** (vì 2 người, thiếu súng chống giáp) và **Entities/Anomaly**.

## 8.3. Nhiệm vụ đang mở
- ✅ **"Mechanoid Signal"** (mở) — đây là **mục tiêu endgame của Odyssey**: bạn đã có **GravEngine** (36,109) + **360 Gravlite** ⇒ có thể đóng **Gravship** và phóng lên quỹ đạo.
- ❌ "Vagabond Desires Resources" — thất bại (người ăn xin bị hại) → để lại dư âm tâm trạng.

## 8.4. Môi trường & thời tiết
- **Rừng ôn đới (Temperate Forest)**, mùa hiện tại: **Septober** (cuối thu) → **Decembary (Đông) bắt đầu sau ~2,5 ngày**.
- **Nhiệt độ hiện tại ~11,6 °C** ở khu căn cứ. Rừng có **1.437 cây sồi già + 1.381 cây dương** (nguồn gỗ khổng lồ — chặt thêm ngay).
- **15 hồ nước ngọt**, hồ gần nhất ở **(173,130) cách 52 ô** — cá nước ngọt, nhưng phải nghiên cứu `Fishing` (Odyssey) mới đánh bắt được.
- **5 mạch nước ngầm (Steam Geyser)** → tiềm năng điện địa nhiệt (Geothermal) — mạnh hơn cả pin mặt trời, chạy 24/7.

---

# ⚡ PHẦN 9 — KẾT LUẬN VỀ "SỨC KHOẺ" CỦA BẢN SAVE

| Hạng mục | Đánh giá |
|---|---|
| 💾 File save | ✅ Lành mạnh, không lỗi, đúng phiên bản 1.6.4871 rev591 |
| 🧩 Mod | ⚠️ **Cần 9 mod** — nếu thiếu bất kỳ mod nào (đặc biệt **Anomaly/Odyssey/Multiplayer**) thì phải bật lại cho đúng |
| 👥 Nhân sự | ⚠️ Chỉ còn **2 người** — mọi sai lầm đều đắt |
| 🚨 Vấn đề cấp bách | **3 cái chết tiềm tàng:** Nicole (đói + thương + mood 45%), 8 ô mái sập, raid sắp tới |
| 🌱 Tiềm năng | **Rất cao**: 1.961 thép, 800 bạc, GravEngine, 5 geyser, 2.800 cây gỗ, 88 bụi dâu chín, 2 khu di tích chưa khai thác |

> **Chẩn đoán 1 câu:** Bạn đang chơi nhanh và bỏ qua nền tảng — thuộc địa 7 ngày tuổi nhưng **chưa có bàn mổ thịt, chưa có điện, chưa có nông nghiệp hoạt động, chưa có mộ**. Kết quả là cái chết của Kory và nguy cơ mất Nicole. Cần "sửa nền móng" trong 2 ngày tới trước khi nghĩ tới mở rộng.

---
---

# 🛠️ PHẦN 10 — GIẢI PHÁP NGẮN HẠN (làm trong 30 phút tới, theo ĐÚNG thứ tự)

## 🥇 VIỆC 0 (10 giây) — Bấm **PAUSE** và mở 3 lá thư chưa đọc
Góc dưới-phải màn hình có 3 lá thư:
1. **"Lễ tang opportunity for Kory"** — nói rõ bạn cần làm gì.
2. **"Death: Kory"**.
3. **"Roof collapse"**.

Đọc hết để bạn nắm được thông tin, rồi bấm Play ở tốc độ **1x (không dùng 3x trong 30 phút đầu)**.

---

## 🥈 VIỆC 1 (2 phút) — **XOÁ MÁI KHU RUỘNG** (làm TRƯỚC cả ăn, vì nó có thể giết người)
Đây là việc quan trọng nhất. Thao tác:

1. Mở **Architect → Zones/Areas → Manage areas** (hoặc bấm nút **"Areas"** trên thanh dưới).
2. Chọn **"Clear roof area" (Xoá mái)** — *hoặc* dùng công cụ **`Build roof`** rồi **quét xoá vùng cũ**.
3. **Quét toàn bộ hình chữ nhật `x = 114 → 127`, `z = 129 → 140`** (trùm cả ruộng, chuồng, và 8 ô nguy hiểm).
4. **Bắt buộc bước 4:** mở **Area "Build roof"** (vùng xây mái) → **quét xoá luôn chính vùng đó** → **nếu không xoá, game sẽ TỰ ĐẶT LẠI blueprint mái và vòng lặp sập/xây lại tiếp tục.**
5. Kiểm tra: bấm phím nóng xem overlay **Mái (Roof)** — vùng ruộng phải **không còn ô mái nào**.

**Kết quả mong đợi:**
- 8 ô mái nguy hiểm bị gỡ **an toàn** (không sập, không đè ai).
- **58 cây lúa được sáng trở lại** → bắt đầu lớn (nhưng xem mục 6 để biết vì sao vụ này vẫn khó cứu).
- **Nguy cơ chết người biến mất.**

> 💡 **Muốn giữ mái ở khu đó?** Bắt buộc phải xây **tường/cột mỗi 6 ô**. Nhưng nhà kính cần **Sun Lamp** (chưa nghiên cứu) → bây giờ **bỏ mái hoàn toàn là đúng nhất**.

---

## 🥉 VIỆC 2 (5 phút) — **CỨU NICOLE NGAY**
1. Chọn **Nicole** → chuột phải vào chính cô ấy → **Tend (Băng bó)** — hoặc mở tab Health → ấn **Tend**.
   - **Dùng `MedicineIndustrial` (thuốc công nghiệp, 22 viên)**. Vết đầu 21/25 + chảy máu: nếu để lâu sẽ nhiễm trùng/chết.
   - Mở **Assign → Medical** đảm bảo đã chọn **"Best"** (đã đặt sẵn) và **self-tend = Yes** (đã bật).
2. Nếu cô ấy đã **gục (downed)**: chọn Nate → chuột phải vào Nicole → **Rescue** → đưa vào giường → rồi băng.
3. **Đưa cô ấy vào giường nghỉ**: chọn Nicole → chuột phải vào giường `Bed41026` (122,119) → **Rest until healed**.
4. **Cho ăn NGAY:** cô ấy cần thức ăn trong vòng ~10 phút game. Xem việc 3.

---

## 🏅 VIỆC 3 (10 phút) — **KIẾM THỨC ĂN TRONG NGÀY**
### Cách nhanh nhất (làm ngay):
1. Bấm **Architect → Orders → Harvest (Cây cối)** và **quét vùng rộng quanh căn cứ** để hái hết dâu + cỏ y tế.
   - Hoặc **chọn từng bụi dâu chín** (bụi nào có icon quả chín) và ấn **Harvest** — chỉ cần **10 bụi gần nhất** là đủ ăn nhiều ngày.
   - **Bụi gần nhất: `(111,135)` — chỉ 15 ô từ căn cứ!**
2. **Mở tab Work và set priority:** cho Nicole + Nate **`Grow` (Plant cut/Harvest) = 1** — hiện tại priority đang để mặc định nên họ có thể không ưu tiên hái.
3. **Xây ngay 1 Bàn mổ thịt (Butcher Table)**: **Architect → Production → Butcher Table** = 1 linh kiện + 1 nút gỗ/thép. **Không có nó thì không xẻ thịt được** → mãi không có nguyên liệu nấu ăn.
4. **Bật lại bill nấu ăn cho bếp (129,116)**: chọn bếp → **Bills** → đảm bảo bill `Cook Meal (Simple)` có nút xanh (allowed) và có **nguyên liệu thô**.
5. **Câu giờ bằng dâu:** trong lúc chờ, chọn Nicole → chuột phải vào chồng dâu → **Consume (Ăn)** — pawn sẽ ăn quả trực tiếp, **không cần nấu**.

> ⚠️ **Tuyệt đối không** để Nicole chạy ra `(90,154)` hay bất cứ chỗ nào quá xa — cô ấy đang ở 0% food + chấn thương đầu, ngất giữa đường là chết.

---

## 🏅 VIỆC 4 (10 phút) — **CHÔN KORY & LÀM LỄ TANG** (giải quyết tâm trạng + nghi lễ)
1. **Xây 1 NGÔI MỘ:** **Architect → Furniture → Grave (Mộ)** — **5 thép**. Đặt ở **trong sân căn cứ** (ví dụ gần (110,119) hoặc trong khu đất phía nam).
   - ⚠️ **Đây là bắt buộc**, vì nghi lễ yêu cầu "một ngôi mộ **có chứa xác Kory**".
2. **Chôn xác Kory (122,138):**
   - Chọn Nate (hoặc Nicole) → chuột phải vào **xác Kory** → **Prioritize Hauling/Bury** (ưu tiên chôn).
   - **Làm gấp:** 6 con quạ hoang đã đăng ký ăn xác — nếu để vài giờ đồng hồ game, xác sẽ hỏng và **bạn mất luôn khả năng làm lễ tang** (chuyển thành nghi lễ "không có xác", phần thưởng tâm trạng thấp hơn).
3. **Tổ chức LỄ TANG:** chọn ngôi mộ (đã có xác Kory) → bấm nút **"Begin lễ tang"** → chọn Nicole + Nate tham dự.
   - **Deadline: 9 ngày — ngày 7 tháng Decembary.** Làm sớm được thì làm.
   - **Lợi ích:** giảm mạnh suy nghĩ `MyLoverDied`/`KnowColonistDied` và **hồi tâm trạng cho cả 2**.
4. **DỌN XÁC CÒN LẠI** (5 xác người + 9 xác thú thối đang rải rác):
   - **Xác thú thối ở (128,117) — NẰM NGAY TRONG PHÒNG NGỦ** → khiêng ra ngoài rồi đốt/hủy.
   - Với các xác khác: khoét **hố chôn tập thể** (grave) hoặc để xa căn cứ. **Đừng để xác gần chỗ ngủ** — sẽ trừ mood liên tục.
   - **KHIÊNG XÁC DED SKARAD Ở (94,205) VỀ KHO trước khi chôn**: quanh xác đó có **1 dùi cui + 1 thuốc herbal + 12 cần sa đang bị Forbidden** — bỏ Forbidden rồi thu gom.

---

## 🏅 VIỆC 5 (5 phút) — **SỬA NHỮNG THỨ BỊ BỎ QUÊN**
1. **Trang bị súng cho Nate:** tìm **`Gun_Revolver` ở (123,138)** — bấm vào nó, **bỏ chọn "Forbidden" (biểu tượng 🔒/dấu X)**, rồi cho Nate trang bị (chọn Nate → chuột phải → Equip).
2. **Thu hồi 8 thuốc Ultratech + 2 Spacer Component** ở khu vực `(16–17, 193–195)` (phía tây, ngay SÁT mép khu cổ — bỏ Forbidden rồi lấy nếu an toàn) — **bỏ Forbidden** cho phần nằm **ngoài** khu cổ rồi mang về.
   - ⚠️ **KHÔNG khoét tường vào khu cổ** — bên trong có 3 quan tài ngủ đông + **5 fleshbeast**. Chỉ lấy phần rơi vãi bên ngoài.
3. **Bỏ Forbidden cho 5 chồng Gravlite** ở `(37,104)`, `(10,107)`, `(20,123)`, `(11,117)`, `(22,105)` → mang về kho (nếu để ngoài đồng, chúng có thể bị mất/coi là của hoang).
4. **Đặt `Forbidden` cho tất cả xác động vật** để pawn không tự động ăn thịt thối.

---

## 🏅 VIỆC 6 (5 phút, trước khi hết ngày) — **MỞ ĐIỆN ĐỂ SƯỞI ẤM**
Vì mùa đông tới trong **~2,5 ngày**:
1. **Chặt gỗ:** chọn nhiều cây sồi/cây dương quanh căn cứ → **Chop (Chặt cây)**. Cần ~100–150 gỗ.
2. **Xây Máy phát điện gỗ (Wood-fired generator)**: ~2 linh kiện + ~100 thép.
3. **Kéo dây điện (Power conduit)** tới phòng ngủ và nhà kho.
4. **Xây Heater (Máy sưởi)** trong phòng ngủ và nhà kho — **đã nghiên cứu Air Conditioning rồi**.
5. **Xây 1 Standing Lamp / đèn dầu** để tăng ánh sáng (đỡ buồn chán ban đêm).
6. **Đặt đủ nhiên liệu gỗ vào generator** — nếu hết gỗ là hết điện giữa mùa đông.

---

# 🛠️ PHẦN 11 — GIẢI PHÁP TRUNG HẠN (3 – 10 ngày game tới)

## 11.1. Nông nghiệp & an ninh lương thực (ưu tiên số 1)
| Việc | Chi tiết |
|---|---|
| **Trồng lại ruộng mới, ngoài trời** | Chọn khu có **fertility cao** (xem chỉ số khi rê chuột) — thường là đất ven hồ. Trồng **Potato** (chín nhanh, chịu lạnh) và **Corn** (năng suất cao) |
| **Bỏ hẳn lúa gạo** | Lúa cần đất màu mỡ + thời gian dài, không phù hợp khí hậu này khi vừa lâm mùa đông |
| **Làm 40–60 Pemmican** | Nguyên liệu: thịt + ngũ cốc. Để được rất lâu, ăn được khi đi caravan |
| **Xây kho lạnh** | Phòng kín + **2 máy Cooler** (cần điện + pin) → bảo quản thịt. Hoặc tận dụng mùa đông: **để thực phẩm ngoài trời đông** |
| **Xây bàn mổ thịt + bàn nấu ăn nâng cấp** | `Butcher Table` + `Stove` (đã có). Thêm `Fermenting Barrel` nếu muốn bia |
| **Gia tăng dàn thú** | Mua/bắt thêm gia súc (Boomalope cho nhiên liệu, Muffalo cho sữa, Chicken cho trứng) từ trader |

## 11.2. Nhà ở & tâm trạng (Nicole đang 45% — nguy hiểm)
| Việc | Chi tiết |
|---|---|
| **Chia phòng ngủ** | Xây **2 phòng ngủ riêng** (mỗi người 1 phòng, có giường đôi + bàn + giá) → hết `SleptInBarracks` |
| **Bàn ăn tập thể** | Xây **Table (2x2) + 4 ghế** ở nhà kho → hết `AteWithoutTable` (−3 mood) |
| **Nâng cấp nội thất** | Sàn gỗ đá, đèn, tượng nghệ thuật (Nicole có Nghệ thuật 7 → tự tạc tượng!) → tăng Beauty (Nate đang 23%) |
| **Khu giải trí** | TV (cần điện + nghiên cứu), bàn bi-a, đàn hạc → tăng `Joy` (Nate đang 24%!) |
| **Quần áo ấm** | May **Parka / Jacket** cho mùa đông. Nicole cần 1 bộ, Nate cần 1 bộ |

## 11.3. Phòng thủ (cấp thiết vì `adaptDays` đang nghiêng về raid mạnh)
1. **Nghiên cứu `GunTurrets`** → xây **2–3 Mini-turret** đặt vào bãi bao cát đã có ở (130–136, 122–128). Đây là "người lính thứ 3" của bạn.
2. **Hoàn thiện vòng tường:** xây tường đá bao quanh toàn bộ khu dân cư + ruộng (dùng thép có sẵn) → tạo 1 hoặc 2 lối vào duy nhất, đặt turret/bẫy ở đó (**kill-box**).
3. **Xây bẫy (Traps)** dọc các hướng tiếp cận — spike trap = 2 gỗ, cực rẻ.
4. **Trang bị giáp cho Nicole**: `Flak Vest + Flak Helmet` (nghiên cứu FlakArmor) — đừng để cô ấy bị thương đầu thêm lần nào nữa.
5. **Nghiên cứu `Mortars`** → 1–2 khẩu súng cối để đối phó raid đông người + mechanoid từ xa.

## 11.4. Công nghệ & kinh tế
| Việc | Chi tiết |
|---|---|
| **Nghiên cứu theo thứ tự** | `Batteries` (đang 34%) → `SolarPanels` → `Microelectronics` → `GunTurrets` → `Hydroponics` → `FlakArmor` → `Mortars` → `DeepDrilling`/`Fabrication` |
| **Comms Console + Orbital Trade Beacon** | Bán **800 bạc + thép dư + vải** để mua: **súng, giáp, thuốc, linh kiện, thức ăn** |
| **Đoàn caravan** | Gửi 1 người tới **khu định cư của Ascamlán/Empire** gần nhất để mua bán + mang thư từ |
| **Khai thác mỏ** | Nate (Đào mỏ 11) — bản đồ còn **3.897 ô đá có thể đào**, nhiều dải đá gần căn cứ (quanh (150–170, 115–125)). Đá = vật liệu xây tường miễn phí |
| **Nghiên cứu `Hydroponics`** | Đây là "bullet-proof" lương thực cho mùa đông dài |

---

# 🛠️ PHẦN 12 — GIẢI PHÁP DÀI HẠN (15+ ngày, hướng tới kết thúc game)

## 12.1. Lộ trình ưu tiên (theo mốc)
### Giai đoạn 1 (ngày 10–20): Ổn định & sống sót qua mùa đông
- ✅ 1 nhà kính thuỷ canh (Hydroponics + Sun Lamp + pin + sưởi) = **không bao giờ chết đói**
- ✅ 4–5 người (tuyển thêm từ tù binh/khách/escape pod) — **1–2 người là quá mỏng**
- ✅ Điện ổn định: 2 pin mặt trời + 2 ắc-quy + **1 máy địa nhiệt tại geyser gần nhất** (chạy 24/7)
- ✅ 4–6 turret + kill-box ⇒ chống raid ổn định
- ✅ Tất cả mọi người có súng + giáp Flak

### Giai đoạn 2 (ngày 20–40): Mở rộng & chuyên môn hoá
- ✅ Chia **phòng nghiên cứu riêng** có Multi-Analyzer + bàn Hi-tech (Nicole Trí tuệ 12 sẽ chạy cực nhanh)
- ✅ **Xưởng chế tạo** (Fabrication) → sản xuất component, vũ khí, giáp
- ✅ **Chăn nuôi quy mô lớn** (Yak/Boomalope/Muffalo) + trồng cỏ làm thức ăn gia súc
- ✅ **Bệnh viện** với giường y tế + máy theo dõi sinh hiệu → giảm tỷ lệ chết khi bị thương
- ✅ Bắt đầu **khai thác 2 khu di tích cổ** (sau khi có đủ 5+ người + giáp + turret) → lấy đồ quý

### Giai đoạn 3 (ngày 40+): Endgame Odyssey / Anomaly
- ✅ **Gravship:** bạn đã có GravEngine + 360 Gravlite → nghiên cứu nhánh **BasicGravtech → StandardGravtech → AdvancedGravtech** → chế **Gravlite Hull** → đóng tàu → **nghi lễ "Phóng Gravship"** → bay lên quỹ đạo, ghé 12 tiểu hành tinh (Vàng Jade, Plasteel) hoặc kết thúc game kiểu Odyssey
- ✅ **Anomaly (nếu muốn):** sau khi có 6 người + turret + súng chống giáp, hãy "nuôi" Void Monolith để mở khoá công nghệ Anomaly (bioferrite, súng insanity) — nhưng đây là **nguy hiểm cấp cao**; hãy để cuối cùng
- ✅ Có thể chọn hướng cổ điển: đóng **tàu ngôi sao** (`ShipBasics` → `ShipReactor` → `ShipEngine` → `ShipComputerCore`) rồi phóng

## 12.2. Những thứ nên làm sớm (vì rất dễ bỏ quên)
| Việc | Lợi ích |
|---|---|
| **Bật `Work priorities` thủ công** | Hiện chưa bật → pawn làm việc kém hiệu quả. Vào **Work → Custom priorities**, set: Nate = Mining/Construction/Y hạng 1; Nicole = Research/Cooking/Y hạng 1 |
| **Đặt `Outfit` & `Drug policy`** | Tránh pawn mặc rách khi vào đông, tránh tự ăn cần sa |
| **Đặt `Food restriction`** | Cấm ăn thịt người để tránh mood, cấm ăn nguyên liệu thô |
| **Bật `Auto-rebuild` ở Home Area** | Tự sửa tường bị raid phá |
| **Xây Tủ lạnh / bảo quản** | Tránh hỏng thức ăn khi ít |
| **Đặt Graveyard riêng** | Để không phải nhìn xác người chết gần nhà |

---

# ⚡ PHẦN 13 — CHECKLIST ĐỂ IN RA (làm theo thứ tự)

```
TRONG 10 PHÚT ĐẦU (pause rồi làm)
☐ 1. Xoá vùng "Build roof" trên khu ruộng (x114–127, z129–140)  ← QUAN TRỌNG NHẤT
☐ 2. Băng vết thương đầu cho Nicole (dùng thuốc Industrial)
☐ 3. Cho Nicole ăn (dâu hoang hoặc Rest until healed + ăn)
☐ 4. Harvest 10 bụi dâu gần nhất — bụi đầu tiên ở (111,135)

TRONG 30 PHÚT
☐ 5. Xây Bàn mổ thịt (Butcher Table)
☐ 6. Xây 1 cái Mộ (Grave) — 5 thép
☐ 7. Khiêng xác Kory vào mộ (ưu tiên Haul, làm GẤP vì quạ đang ăn)
☐ 8. Tổ chức "Lễ tang cho Kory" (hạn 9 ngày = 7 Decembary)
☐ 9. Bỏ Forbidden khẩu súng lục (123,138) → đưa cho Nate
☐ 10. Dọn xác thú thối trong phòng ngủ (128,117)

TRONG NGÀY ĐẦU
☐ 11. Bỏ Forbidden + mang về: 8 thuốc Ultratech, 2 Spacer Component, 360 Gravlite,
      12 cần sa + dùi cui + thuốc herbal ở (94,205)
☐ 12. Chặt cây → xây Máy phát điện gỗ (2 linh kiện + 100 thép)
☐ 13. Kéo dây điện → đặt Heater (máy sưởi) ở phòng ngủ + nhà kho
☐ 14. Bật Work priorities: Grow/Harvest = 1 cho cả 2 người
☐ 15. Nghiên cứu xong Batteries → chuyển sang SolarPanels

TRONG 3 NGÀY (mùa đông!)
☐ 16. Trồng ruộng mới (Potato + Corn) ở đất màu mỡ, ngoài trời
☐ 17. Nấu 40+ Pemmican
☐ 18. Xây bàn ăn + ghế (hết mood "ate without table")
☐ 19. Xây 2 phòng ngủ riêng
☐ 20. May Parka cho cả 2 người (200 vải có sẵn)
☐ 21. Nghiên cứu Microelectronics → Comms Console + Trade Beacon
☐ 22. Nghiên cứu GunTurrets → đặt 2 turret vào bãi bao cát (130–136, 122–128)

TRONG 1–2 TUẦN
☐ 23. Nghiên cứu Hydroponics → nhà kính thuỷ canh (Sun Lamp + pin)
☐ 24. Xây tường bao quanh toàn bộ thuộc địa (dùng 1.961 thép + đá khai thác)
☐ 25. Nghiên cứu FlakArmor → trang bị giáp cho cả 2 người
☐ 26. Tuyển thêm người (ít nhất lên 4 người trước khi mở khu cổ)
☐ 27. Nghiên cứu GeothermalPower → xây 1 nhà máy địa nhiệt ở mạch nước ngầm
☐ 28. Xây Gravship Workshop → bắt đầu lộ trình Gravtech (endgame)
```

---

# ⚡ PHẦN 14 — CÁC LỖI CẦN TRÁNH (bài học từ chính save này)

| ❌ Lỗi | Hậu quả đã xảy ra |
|---|---|
| **Quét "Build roof" lên vùng rộng không có tường/cột** | **GIẾT CHẾT KORY.** Mái sập đè chết người + nghiền nát súng + hàng rào |
| **Để ruộng nằm dưới mái** | 58/75 cây lúa bị chặn sáng → 7 ngày không thu được gì |
| **Không xây bàn mổ thịt trước** | Không thể xẻ thịt → cả thuộc địa chỉ ăn thực vật hoang, hết thức ăn |
| **Không set Work priorities** | Pawn làm việc chậm, không hái dâu dù dâu chín đầy rừng |
| **Không xây mộ trước khi ai đó chết** | Kory chết → không có chỗ chôn → quạ đang ăn xác → nguy cơ mất luôn lễ tang |
| **Bỏ quên điện dù đã nghiên cứu** | Điện + Điều hoà đã có nhưng 0% sử dụng → không sưởi, không turret, không kho lạnh |
| **Để Nicole (đói + thương + mood 45%) tự do đi lại** | Cô ấy có thể ngất hoặc khủng hoảng tinh thần bất cứ lúc nào |
| **Chưa mở Work/Assign/Health tabs bao giờ** | Nhiều cơ chế quan trọng đang bỏ trống (outfit, drug policy, food restriction) |

---

# 📌 PHỤ LỤC A — SỐ LIỆU KỸ THUẬT CỦA SAVE

| Chỉ số | Giá trị |
|---|---|
| Phiên bản | **1.6.4871 rev591** |
| Mod cần có | **Harmony, Prepatcher, Core, Royalty, Ideology, Biotech, Anomaly, Odyssey, Multiplayer (RWMT)** |
| **GameComponent đặc biệt** | **`Multiplayer.Client.Comp.BootstrapCoordinator`** → **đây là save của phiên chơi MULTIPLAYER** (nếu bạn chơi 1 mình, đừng tắt mod Multiplayer hoặc save có thể hỏng) |
| Kích thước map | 250 × 250, 1 map duy nhất (không có map con) |
| Số vật thể trong map | **27.358** (rất nhiều, chủ yếu là cây cối hoang) |
| Số pawn trên map | 2 người + 2 động vật nuôi (Yak "Venus", Crow "Crow 1") + 6 quạ hoang + ~60 thú hoang + 6 quái/mech |
| Nhiệt độ | Ngoài trời 11,6 °C (mùa **Septober → Decembary** chuyển mùa trong ~2,5 ngày) |
| Thời tiết | `Clear`, không mưa, không sương mù ở căn cứ |
| Số thư chưa đọc | 3 (`Letter_13`, `Letter_14`, `Letter_15`) |

# 📌 PHỤ LỤC B — GHI CHÚ VỀ MOD MULTIPLAYER (RWMT)
Save này có component `Multiplayer.Client.Comp.BootstrapCoordinator` → **save được tạo trong phiên chơi Multiplayer**. Khi load lại:
- **Giữ nguyên mod list** — đặc biệt **Multiplayer (rwmt.multiplayer)** — nếu tắt, save có thể lỗi hoặc mất đồng bộ.
- Nếu load mà không có ai kết nối (chơi solo), game vẫn chạy bình thường; **chỉ cần đảm bảo không bật chế độ khác biệt** (vd. thay đổi tốc độ/hành vi mod).
- Nếu báo lỗi "mod list mismatch": bật lại đúng 9 mod và load thử lần nữa.

# 📌 PHỤ LỤC C — CÁCH TÔI ĐỌC ĐƯỢC NHỮNG CHỈ SỐ NÀY
Toàn bộ số liệu trên được trích trực tiếp từ XML bên trong `Hateria.rws` và `Autosave-5.rws`, bao gồm cả các **lưới dữ liệu nén** mà game lưu ở dạng base64 + deflate:

| Lưới | Cách giải mã | Dùng để trả lời |
|---|---|---|
| `roofGrid.roofsDeflate` | base64 → deflate → 2 byte/ô (250×250) | **Xác định chính xác 8 ô mái sắp sập và các ô mái đã sập** |
| `fogGrid.fogGridDeflate` | base64 → deflate → 1 bit/ô | Xác nhận 2 khu di tích cổ **còn nguyên sương mù** (chưa bị lộ) |
| `areaManager (Area_BuildRoof, Area_Home, Area_1)` | bit-packed | Vùng Xây mái (431 ô) & vùng Home |
| `zoneManager` | trực tiếp | 2 kho (132 ô) + 1 ruộng lúa (80 ô) |
| `terrainGrid` | base64 → deflate → 2 byte/ô | Loại đất từng ô (giải thích "đá trong nhà kho") |
| `compressedThingMapDeflate` | base64 → deflate → 2 byte/ô | **3.897 ô đá/ore tĩnh còn lại** |
| `deepResourceGrid` | như trên | **Toàn bộ = 0** → không có mỏ sâu ⇒ không cần DeepDrilling |
| `waterBodyTracker` | trực tiếp | 15 hồ nước ngọt + quần thể cá |
| `hediffSet`, `healthTracker` | trực tiếp | Vết thương, phần cơ thể bị ảnh hưởng, mức độ |
| `needs`, `thoughts`, `mood` | trực tiếp | Nicole 45,3% — liệt kê đủ mọi suy nghĩ tích cực/tiêu cực |
| `taleManager` | trực tiếp | 14 lần `CollapseDodged` + `KilledBy` trong cùng 1 tick |
| `letterStack`, `questManager`, `lordManager`, `storyWatcher` | trực tiếp | 3 thư chưa đọc, nhiệm vụ mở, quái đang "ngủ", mức adapt của Cassandra |
| `reservationManager` | trực tiếp | **6 con quạ hoang đã đặt chỗ ăn xác Kory** |

---

# 📌 PHỤ LỤC D — BẢN ĐỒ CÁC KHỐI TRONG FILE `.rws` (số liệu thật của `Hateria.rws`)

Toàn file: **14.790.292 bytes (~14,1 MB), 442.768 dòng**, bọc trong `<savegame>` với **đúng 2 nhánh**:
`<meta>` (dòng 3–38, 0,8 KB: phiên bản game + danh sách 9 mod) và `<game>` (dòng 39 → hết, 14,4 MB).

**Bên trong `<game>` — 39 khối** (liệt kê các khối đáng chú ý):

| Khối | Dòng | KT | Chứa gì |
|---|---|---|---|
| scenario / info / rules | 41–201 | 5,2 KB | kịch bản 3 người rơi xuống, quy tắc game |
| tickManager | 202 | 0,2 KB | ngày giờ (`ticksGame`) |
| storyWatcher | 217 | 0,4 KB | số raid, adaptation |
| letterStack | 231 | 0,1 KB | **thư chưa đọc (#13 Lễ tang, #14 Death, #15 Roof collapse)** |
| researchManager | 239 | 7,9 KB | công nghệ đã/chưa nghiên cứu |
| storyteller | 606 | 0,7 KB | Cassandra Classic + độ khó Easy |
| history / taleManager / playLog / battleLog | 624–9031 | ~277 KB | toàn bộ lịch sử diễn biến |
| foodRestriction / drugPolicy / outfit | 9032–12644 | ~112 KB | chính sách ăn / mặc / dùng thuốc |
| questManager | 12699 | 13,7 KB | nhiệm vụ (Mechanoid Signal, Vagabond…) |
| components | 13226 | 1,4 KB | Anomaly level, Multiplayer Bootstrap |
| **world** | **13274–68326** | **3,2 MB** | bản đồ hành tinh + phe + tôn giáo + pawn ngoài map |
| **maps** | **68327–442761** | **11,1 MB** | toàn bộ map 0 |

**Bên trong `<world>` (12 khối):** `grid` 2,25 MB (62.500 ô thế giới) · `factionManager` 39,3 KB · **`ideoManager` 43,6 KB** · `worldPawns` 637,6 KB (pawn ngoài map/caravan) · `worldObjects` 120,8 KB (khu định cư, tiểu hành tinh) · `features` / `landmarks` / `storyState` / `components`.

**Bên trong `<maps><li>` — 48 khối:**

| Khối | Dòng | KT | Chứa gì |
|---|---|---|---|
| weatherManager | 68339 | 0,3 KB | thời tiết hiện tại (Clear) |
| reservationManager + physicalInteraction | 68346–68398 | 1,4 KB | **6 con quạ đang đặt chỗ ăn xác Kory** |
| designationManager | 68402 | 3,5 KB | lệnh chặt cây/hái/đào còn treo |
| lordManager | 68603 | 1,9 KB | nhóm AI đang hoạt động (raid, 5 fleshbeast) |
| fogGrid / roofGrid / terrainGrid | 68681 / 68693 / 68711 | 0,9 / 1,4 / 9,2 KB | lưới **NÉN base64** (sương mù, mái, đất) |
| zoneManager | 68813 | 66,2 KB | 2 kho (132 ô) + ruộng lúa (80 ô) |
| temperatureCache / snowGrid / pollutionGrid / waterBodyTracker | 70728–70901 | ~6 KB | nhiệt độ, tuyết, ô nhiễm, 15 hồ cá |
| **areaManager** | 70902 | 2,0 KB | Home (1.504 ô) + **BuildRoof (431 ô — thủ phạm vụ sập mái)** |
| deepResourceGrid | 70981 | 0,5 KB | mỏ sâu (RỖNG — không có gì) |
| compressedThingMapDeflate | 71443 | 3,8 KB | bảng tra ô đá/mineable (~3.900 ô) |
| **things** | **71483** | **11,03 MB (74,6% cả file)** | **27.358 vật thể — mỗi vật thể 1 phần tử (~413 bytes)** |

**4 điều cần lưu ý về cách "state" nằm rải rác:**

1. **`<things>` là danh sách phẳng 27.358 phần tử, xếp theo thứ tự spawn — KHÔNG theo toạ độ.** Muốn xem ô (122,138) có gì phải **lọc theo `<pos>`**, không thể đọc tuần tự. Mỗi pawn là **một phần tử to** duy nhất (chứa đủ nhu cầu, thương tích, kỹ năng, trang bị, công việc, quan hệ).
2. **Một sự kiện để lại dấu ở nhiều khối.** Vụ Kory chết: `letterStack` (2 lá thư) + `taleManager` (14 dòng `CollapseDodged`, dòng "bashing his neck") + `battleLog` + `things` (xác `Corpse_Human71411` + khẩu revolver) + quan hệ trong pawn Nicole. Muốn dựng lại đầy đủ **phải gom 4–5 khối**.
3. **Lưới (grid) bị nén — không đọc bằng mắt được.** `fogGrid` chỉ 0,9 KB nhưng chứa trọn 62.500 ô; phải `base64 → zlib.decompress(bytes, -15)`.
4. **Vị trí khối không như tên gợi ý:** `ideoManager`, `factionManager`, `worldPawns` nằm trong **`<world>`**, không phải `<game>` — tìm sai chỗ sẽ ra `None` (đây chính là lỗi mình gặp khi tìm `ideoManager`).

**Mẹo thao tác nhanh (không cần đọc từng dòng):** cắt 1 khối bằng `sed -n '/^\t<researchManager>/,/^\t<\/researchManager>/p' Hateria.rws`; tra theo khoá bằng `grep -n "Corpse_Human71411" Hateria.rws`; parse bằng Python `xml.etree.ElementTree` (~2–5 giây cho 14 MB) hoặc regex. ⚠️ **Chỉ nên ĐỌC** — sửa tay file `.rws` rất dễ hỏng save; muốn sửa thì dùng dev mode hoặc save editor.

---

# 📌 PHỤ LỤC E — NÉN FILE SAVE THÀNH "BẢN TÓM TẮT CHO AI" (đo bằng số thật)

Đo trên chính `Hateria.rws` (14.790.292 B, 442.768 dòng). Script: `analysis/digest.py` → xuất ra **`DIGEST-HATERIA.txt`**.

## E.1. Cái gì chiếm chỗ trong file

| Nhóm | Số đo | % file |
|---|---|---|
| Thực vật hoang (23.293 vật thể: cỏ, bụi gai, cây…) | 8.389 KB | **58,1%** |
| Rác / sản phẩm bẩn (3.020: Filth_RubbleRock, vết máu…) | 1.074 KB | 7,4% |
| `world.grid` (62.500 ô bản đồ hành tinh) | 2.200 KB | **15,2%** |
| `worldPawns` (pawn ngoài map) | 623 KB | 4,3% |
| Nội tâm/nhu cầu 65 con thú hoang | 658 KB | 4,6% |
| `battleLog` + `taleManager` + `playLog` + `history` (nhật ký) | 271 KB | 1,9% |
| Database mặc định (food/outfit/drug policy) | 115 KB | 0,8% |
| Ký tự thụt lề + xuống dòng (XML pretty-print) | 3.021.595 ký tự | **20,4%** |
| **Tổng phần có thể BỎ hoặc HỢP NHẤT** | **13,2 MB** | **93,6%** |
| Phần bắt buộc giữ nguyên văn (pawn, thư, lưới, vùng, nghiên cứu, tôn giáo, nhiệm vụ, đe doạ…) | **140 KB** | **0,9%** |

## E.2. Quy tắc lọc (4 tầng)

| Tầng | Việc làm | Kết quả |
|---|---|---|
| **0. Format** | Bỏ thụt lề/xuống dòng, gộp khoảng trắng | −20,4% (miễn phí, không mất gì) |
| **1. Bỏ nhiễu** | Thực vật hoang, rác, `DeadPlant` → thay bằng **bảng đếm theo loài + vị trí gần căn cứ**; thú hoang → chỉ giữ loài/vị trí/máu, bỏ nhu cầu–tâm trí | −70% |
| **2. Hợp nhất lịch sử** | `taleManager` → chỉ giữ sự kiện trong danh sách trắng (CollapseDodged, KilledBy, Raid, BecameLover…); `battleLog` → chỉ vết thương/chết của người nhà; `worldPawns`/`grid` → chỉ giữ phần liên quan (khu định cư gần, phe, ô đang ở) | −7% |
| **3. Diễn giải** | Lưới nén (mái/sương mù/đất/mỏ) → **giải mã rồi kết luận bằng chữ** (8 ô mái sập, 2 cụm sương mù, 0 mỏ sâu…); zone/area bit-packed → mô tả + bbox | −0,9% |

## E.3. Kết quả đo được
- **14.790.292 B → 22.940 B = 0,155% dung lượng gốc (giảm 645 lần)**, ~**6.550 token** — vừa một lần đọc của AI.
- **Kiểm tra độ phủ:** 25/25 sự thật then chốt (Nicole đói 0%, Kory bị mái sập, 6 quạ ăn xác, hạn lễ tang 7 Decembary, **đúng 8 ô mái nguy hiểm kèm khoảng cách 6,08–6,71**, deepResourceGrid rỗng, 3.897 ô đá, 1.961 thép/800 bạc, súng lục bị Forbidden, 5 fleshbeast ngủ đông, Centipede, Warg, bill `CookMealSimple`, Cassandra/Easy, adaptDays −31,5…) **đều có mặt**.

## E.4. TUYỆT ĐỐI không được cắt (nếu cắt là AI sẽ "mù")
1. **Pawn của thuộc địa** — nhu cầu, tâm trạng + thoughts, thương tích (định vị từng phần cơ thể), kỹ năng, đặc điểm, trang bị, quan hệ, công việc.
2. **`letterStack` + thư trong `<history><archive>`** — nguồn duy nhất nói *chuyện gì vừa xảy ra* và *hạn chót nghi lễ*.
3. **`roofGrid` / `fogGrid` / `areaManager`** (giải mã) — nguồn duy nhất phát hiện **nguy cơ sập mái**; cắt là bỏ mất nguyên nhân cái chết.
4. **`things` đã lọc** (xác, tài nguyên, công trình, item, blueprint) — gồm cả cờ `forbidden`.
5. **`researchManager` + `ideoManager` + `questManager` + `lordManager` + `storyWatcher`** — biết cái gì đã mở, luật tôn giáo nào đang phạt, nhiệm vụ nào treo, raid nào sắp tới.
6. **`reservationManager` + `designationManager`** — biết ai đang tranh nhau cái gì (6 quạ đang ăn xác Kory) và còn việc gì treo (33 lệnh HarvestPlant).

## E.5. Cái digest CHẤP NHẬN mất (và cách lấy lại khi cần)
| Mất gì | Khi nào cần | Cách thêm lại |
|---|---|---|
| Toạ độ 62.500 ô hành tinh | Khi lập kế hoạch caravan/khai phá hành tinh | Giữ nguyên `<world><grid>` (2,2 MB) hoặc chỉ lọc quanh ô thuộc địa |
| Chất lượng/độ bền từng món đồ (`quality`, `hitPoints`) | Khi muốn so sánh trang bị | Thêm 3 trường vào khối item |
| Số liệu thẩm mỹ phòng ốc (`roomStats`, beauty) | Khi sửa tâm trạng bằng nội thất | Thêm `<roomStats>` của phòng ngủ |
| Nhu cầu/tâm trí từng con thú hoang | Gần như không bao giờ | Bỏ hẳn |
| Toàn bộ lịch sử hành tinh (`landmarks`, `features`) | Khi muốn cướp khu cổ ở nơi khác | Lọc theo khoảng cách ≤ 100 tile |

> **Nguyên tắc:** cắt được hay không phải đo bằng *"thông tin này có đổi được quyết định nào không?"*. Cỏ ở (30,200) không đổi quyết định nào → bỏ. Ô mái (119,136) cách điểm tựa 6,08 ô → **giết người**, phải giữ.

---

# 📌 PHỤ LỤC F — CÔNG CỤ `rw_state.py`: BIẾN SAVE BẤT KÌ THÀNH "STATE FULL"

## F.1. Kết luận: KHẢ THI (đã làm và đã kiểm chứng)
Script: **`/home/user/analysis/rw_state.py`** — chạy `python3 rw_state.py <save.rws> [out.md] [--ascii] [--no-grid]`.
Đã test thật trên 3 tình huống:

| Test | Kết quả |
|---|---|
| `Hateria.rws` (14.790.292 B) | ✅ 27.357 B, **0,19% file gốc**, ~7.850 token, **~0,9 giây** |
| `Autosave-5.rws` (14.754.312 B, mốc cũ hơn 8.998 tick, Kory còn sống) | ✅ 27.357 B, đọc đúng "Kory đang Research, mood 86%, có revolver, khoẻ" |
| Save bị **cắt cụt** 3 MB (giả lập file hỏng) | ✅ Không crash, xuất phần đọc được + cảnh báo |
| Save **"đời cũ"** (đã xoá `compressedThingMapDeflate` + `deepResourceGrid`) | ✅ Chạy bình thường, không cảnh báo |

## F.2. Tool sinh ra gì (21 mục, có phân tích sẵn)
`0` meta/mod · `1` thời gian–storyteller–storyWatcher · `2` danh sách map · `3` phe + quan hệ · `4` tổng quan vật thể · **`5` từng colonist chi tiết** (nhu cầu, thoughts ×hệ số×tuổi, kỹ năng + đam mê, đặc điểm, backstory, hediff từng phần cơ thể + chảy máu/chưa băng, trang bị, job, giường, quan hệ) · `6` thú/mech kèm khoảng cách · **`7` xác + ai đang ăn** · `8` tài nguyên kèm vị trí + cờ Forbidden · `9` công trình/blueprint + điện + phòng thủ · `10` bill sản xuất · `11` zone/area · **`12` lưới giải mã** (mái sắp sập kèm khoảng cách, cụm sương mù, mỏ sâu, ô đá) · **`12b` sơ đồ ASCII căn cứ** (có đánh dấu `!` ô mái sắp sập) · `13` nghiên cứu · `14` tôn giáo + **nghĩa vụ đang mở (hạn lễ tang)** · `15` nhiệm vụ + mô tả · `16` thư (chưa đọc + text) · `17` lord/raid/đe doạ ngủ đông · `18` Anomaly · `19` thế giới (phe, khu định cư theo khoảng cách, địa danh) · `20` **cảnh báo tự động** (đói, mood thấp, vết thương chưa xử lý, không vũ khí, hết thức ăn, mất điện, không phòng thủ, xác chưa chôn, thú dữ gần nhà) · `21` danh sách thứ không parse được.

## F.3. Vì sao chạy được với save "bất kì"
| Rủi ro | Cách xử lý trong script |
|---|---|
| Map to ≠ 250×250 | đọc `<mapInfo><size>` từng map |
| Nhiều map (thuộc địa phụ, pocket map) | lặp qua **mọi** `<maps><li>` |
| Không biết phe người chơi | dò def `PlayerColony`; nếu không có thì lấy phe của pawn khởi đầu |
| Thiếu DLC (không Ideology/Anomaly/Odyssey) | mọi khối đều "có thì đọc, không thì bỏ", bọc try/except |
| Mod thêm class/def lạ | phần lạ chỉ hiện dưới dạng "class/def chưa biết", không làm sập |
| v1.4/1.5: đá nằm trong `<things>` class `Mineable`, không có `compressedThingMapDeflate` | **có cả hai đường**: đọc lưới nén 1.6 *hoặc* đếm vật thể `Mineable` |
| Multiplayer (RWMT) | vẫn đọc bình thường, có cảnh báo phải giữ mod khi load |
| File hỏng/cắt cụt | xuất phần đọc được + mục `21. GHI NHẬN` |

## F.4. Giới hạn cần biết (nói thẳng)
1. **Không thay thế được việc đọc def của game.** Script chỉ đọc *dữ liệu save*; các giá trị gốc (mood −3 của `AteWithoutTable`, công thức mái 6 ô…) là kiến thức của người/AI đọc kết quả. Vì vậy script in `moodPowerFactor` và `age` chứ không tự bịa ra "−3".
2. **Mod nặng có thể thêm khối lạ** (vd. Save Our Ship, Combat Extended) — script sẽ bỏ qua hoặc đưa vào mục 21; muốn đọc sâu thì phải bổ sung nhánh riêng.
3. **Save khổng lồ** (mod + nhiều năm, 50–200 MB): vẫn chạy nhưng chậm hơn (tuyến tính theo dung lượng, 15 MB ≈ 0,9 s ⇒ 100 MB ≈ 6–8 s, RAM ~1–2 GB vì đọc cả file vào bộ nhớ).
4. **Không đọc được**: nội dung hầm mộ/container đóng, `records` (wealth dạng nén), chính sách mặc định (outfit/drug/food) — đã cố ý lược; muốn có thì thêm nhánh.
5. **Caravan đang đi** nằm trong `worldPawns` (chỉ có tên/id) — muốn chi tiết phải parse thêm khối đó.

## F.5. Ví dụ thực tế: 2 save đọc ra khác nhau đúng như mong đợi
| | `Autosave-5.rws` (tick 423.521) | `Hateria.rws` (tick 432.519) |
|---|---|---|
| Thời điểm | ngày 7, 01:24 | ngày 7, 05:00 |
| Kory | **SỐNG**, `Research`, mood 86%, khoẻ, có `Gun_Revolver` | **CHẾT** — `Corpse_Human` @(122,138), 6 quạ đang ăn |
| Nicole | Food 0%, **khoẻ** | Food 0%, **Cut 21 ở đầu chưa băng** |
| Mái nguy hiểm | 8 ô | 8 ô (y hệt) |
⇒ Chỉ cần đưa file save, tool cho ra đủ ngữ cảnh để AI trả lời "chuyện gì đang xảy ra + nên làm gì" như báo cáo này.

---

*Báo cáo lập ngày 26/09/2026 · Phân tích từ `Hateria.rws` (mới nhất, tick 432.519) · Mọi toạ độ ghi theo định dạng `(x, z)` đúng như giao diện game hiển thị ở góc dưới-trái khi rê chuột.*
