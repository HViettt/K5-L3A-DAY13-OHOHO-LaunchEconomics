# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83% (994/1.200)** |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12% (48/177)** |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25% (51/1.200)** |
| Dùng (tự đề xuất) | Tỉ lệ gợi ý được nhân viên giữ nguyên | `quyet_dinh_xem_lai` là `giu`, chia số yêu cầu được xem lại | Chưa tính thành tiêu chí quyết định; sẽ ghi nhận trong đợt pilot |
| An toàn (tự đề xuất) | Tỉ lệ đơn hoàn sai tiền phát hiện bằng kiểm tra mẫu | Số mẫu có `so_tien_da_hoan` khác `so_tien_dung`, chia tổng số mẫu kiểm tra | Chưa tính thành tiêu chí quyết định; sẽ lấy mẫu 100 đơn mỗi tuần |

Các chỉ số trong đợt chạy thử lần lượt là **82,83%, 27,12% và 4,25%**; đợt chạy thử không có nhóm đối chứng nên không kết luận trợ lý đã làm tăng chỉ số.

## Danh sách event

Mỗi event có `trace_id` để nối với trace của agent và truy ngược một yêu cầu.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, arm, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Trợ lý agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra |
| `staff_review_decision` | Nhân viên | quyet_dinh_xem_lai, phut_xem_lai_do_thu, trace_id | Khi bấm giữ, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai_do_thu, ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ cái |
| `handoff_to_staff` | Trợ lý agent | reason, tom_tat, trace_id | Khi chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | closed_at, trace_id | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần khi kiểm tra mẫu |

**Kiểm tra chéo:** mỗi chỉ số phải có event tính được.

- Chỉ số chính **82,83%**: tính từ `refund_request_created`, `ticket_closed` và `ticket_reopened`.
- Chỉ số dùng **27,12%**: tính từ `staff_review_decision`, mẫu số là các lần nhân viên xem lại.
- Chỉ số an toàn **4,25%**: tính từ `ticket_reopened`, mẫu số là số yêu cầu đã tạo.
- Chỉ số dùng tự đề xuất: tính từ `staff_review_decision` với quyết định `giu`.
- Chỉ số an toàn tự đề xuất: tính từ `audit_sample_checked` khi hai số tiền khác nhau.

## E2 · Rủi ro kinh tế

Các số trong bảng lấy từ B1–B4 của `bang_chi_phi.md`; số phụ thuộc cột `*_simulated` được ghi nhãn `simulated`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| R1: Số ca làm lại tăng gấp đôi | CPS lên **6.787 đ, +51,8%** (`simulated`) | Tỉ lệ làm lại theo tuần vượt **7%** | Giới hạn tối đa **2 lần chạy**, thu hẹp về `noi_dia` và rà **20 trace** làm lại | PM trợ lý hoàn phí |
| R2: Tỉ lệ xem lại tăng gấp đôi | CPS lên **6.292 đ, +40,7%** (`simulated`) | Tỉ lệ yêu cầu được xem lại vượt **50%** cuối bước 0,25 | Giảm xem lại theo bậc khi tỉ lệ sửa hoặc bỏ dưới **15%** | Trưởng nhóm CSKH |
| R3: Phải xem lại 100% kéo dài | CPS lên **11.743 đ = 0,98×**; nếu làm lại 15,3 phút/ca thì **12.415 đ = 1,03×** (`simulated`) | Thời gian xem lại thực tế vượt **5 phút/lần** | Dừng mở rộng, đo lại thời gian thực tế trong tuần đầu và giảm tỉ lệ xem lại | Kế toán trưởng |
