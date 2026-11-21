# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | Đang chạy thử trên dữ liệu logix 1.200 req |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | Đang chạy thử trên dữ liệu logix 1.200 req |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | Đang chạy thử trên dữ liệu logix 1.200 req |
| Dùng | Nhóm tự đề xuất: Tỉ lệ yêu cầu được xem lại và chấp nhận gợi ý đầu tiên | `quêt_dinh_xem_lai` là `sua` và kết quả là `thanh_cong`, chia số yêu cầu xem lại | Không cần tính - ghi nhận từ đợt chạy thử |
| An toàn | Nhóm tự đề xuất: Tỷ lệ lỗi do hệ thống gây ra sau khi xem lại | `mo_lai_trong_7_ngay` do lỗi hệ thống, chia số yêu cầu xem lại | Không cần tính - ghi nhận từ đợt chạy thử |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| E1: Agent nhận yêu cầu mới | Trợ lý agent | request_id, loai, depot, ghi điểm bắt đầu xử lý | T: t0 khi agent nhận request |
| E2: Agent kiểm tra kết quả thành công | Trợ lý agent | ket_qua = thanh_cong, trace_id | T: t1 khi agent hoàn thành xử lý |
| E3: Agent quyết xem lại do quyết định | Trợ lý agent | duoc_xem_lai = sua/bo, quyêt_dinh_xem_lai | T: t2 khi agent chọn xem lại |
| E4: Agent xem lại yêu cầu | Trợ lý agent | phut_xem_lai_simulated, lý do xem lại | T: t3 khi agent bắt đầu xem lại |
| E5: Agent làm lại yêu cầu | Trợ lý agent | phut_lam_lai_simulated, ket_qua = lam_lai | T: t4 khi agent bắt đầu làm lại |
| E6: Hệ thống ghi lỗi lọt khách | Hệ thống | mo_lai_trong_7_ngay = 1, loai lỗi | T: t5 khi lỗi lọt đến khách |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số Chính (% đóng 24h/không mở lại 7d): tính từ E1 (thanh_cong ∧ ¬mo_lai_7ngay)
- Chỉ số Dùng (bỏ qua gợi ý): tính từ E3 (quyet_dinh_xem_lai ∈ {sua, bo})
- Chỉ số An toàn (lỗi lọt khách): tính từ E6 (mo_lai_trong_7_ngay = 1)

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| R1: Chi phí mỗi yêu cầu cao do nhiều lan chay lai | CPS [sim] tăng lên đến 18.500đ (gấp 1,5x so với cơ sở 12.000đ) | Giá token gấp đôi, he_so_xem_lai > 1, so_lan_chay cao | Giới hạn max_lan_chay, tối ưu he_so_xem_lai | TV2 - Mảng Pilot |
| R2: Tỷ lệ lỗi lọt khách vượt ngưỡng an toàn | mo_lai_trong_7_ngay có thể đạt 3-5% khi hệ thống overloaded | Tăng he_so_lam_lai, gioi han 3 lan chay | Giới hạn so_lan_chay ≤ 2, giám sát real-time | TV2 - Mảng Pilot |
