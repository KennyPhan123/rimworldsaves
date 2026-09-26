# 🧰 tools/ — công cụ đọc file save RimWorld

Hai script Python thuần (**không cần `pip install` gì cả**, chỉ cần Python 3.8+).

## 1. `rw_state.py` — biến 1 file save thành "STATE FULL" (khuyến nghị dùng cái này)

```bash
# cách dùng cơ bản (xuất ra file .md)
python3 rw_state.py Hateria.rws STATE.md

# thêm sơ đồ ASCII khu căn cứ + đánh dấu ô mái sắp sập
python3 rw_state.py Hateria.rws STATE.md --ascii

# bỏ phần giải mã lưới cho nhanh
python3 rw_state.py Hateria.rws --no-grid --stdout
```

Trên Windows (nếu `python` không có trong PATH thì dùng `py`):

```bat
py rw_state.py Hateria.rws STATE.md --ascii
```

**Kết quả:** một file `.md` ~25–30 KB (≈0,2% dung lượng save, khoảng 1–2 giây cho save 15 MB) gồm 21 mục:

| Mục | Nội dung |
|---|---|
| 0–4 | phiên bản + mod, thời gian/storyteller/adaptation, danh sách map, phe & quan hệ, tổng quan vật thể |
| **5** | **từng colonist chi tiết**: nhu cầu, thoughts (kèm hệ số & tuổi), kỹ năng + đam mê, đặc điểm, hediff từng phần cơ thể + chảy máu/chưa băng, trang bị, job, giường, quan hệ |
| 6–7 | thú/mech kèm khoảng cách; **xác chết + ai đang ăn** |
| 8–11 | tài nguyên (kèm vị trí + Forbidden), công trình/blueprint, điện & phòng thủ, bill, zone/area |
| **12/12b** | **lưới đã giải mã** (ô mái sắp sập kèm khoảng cách, cụm sương mù, mỏ sâu, ô đá) + **sơ đồ ASCII căn cứ** (`!` = mái sắp sập) |
| 13–19 | nghiên cứu, tôn giáo + nghĩa vụ đang mở, nhiệm vụ, thư (chưa đọc + nội dung), lord/raid/đe doạ ngủ đông, Anomaly, thế giới |
| **20–21** | **cảnh báo tự động** (đói, mood thấp, vết thương chưa xử lý, không vũ khí, hết đồ ăn, chưa có điện/phòng thủ, xác chưa chôn…) và danh sách thứ không parse được |

Đưa file kết quả này cho AI (hoặc đọc trực tiếp) là đủ để phân tích tình hình và lập kế hoạch — không cần gửi file save 15 MB.

## 2. `digest.py` — bản tóm tắt ngắn hơn (bản cũ, ít mục hơn)

```bash
python3 digest.py Hateria.rws DIGEST.txt
```

## Ghi chú

- Chạy được cho save **bất kì** miễn là XML của RimWorld: tự dò kích thước map, số map, phe người chơi; thiếu DLC/mod lạ, file hỏng đều không làm script sập (xem mục 21 trong kết quả).
- **Chỉ đọc** file save, không sửa gì — an toàn tuyệt đối với save gốc.
- Giới hạn: không kèm định nghĩa gốc của game (script in `moodPowerFactor`/`age` chứ không tự suy ra "−3 mood"); mod nặng có khối riêng thì script bỏ qua và ghi vào mục 21.
