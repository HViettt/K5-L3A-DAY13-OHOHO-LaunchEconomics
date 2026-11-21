# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Đoàn Gia Long · Người gắn nhãn 2: Đỗ Hoàng Minh (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Lý do chọn nhãn (người 1) | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- | --- |
| 1 | Do người dùng | Khách nhập thiếu số tài khoản; trợ lý làm đúng theo đầu vào sai | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Gọi tool sai tham số (hàng thường thay hàng nặng), sai chính sách và khách đã thấy | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Hoàn về ví đúng thiết kế, chỉ khác kỳ vọng của khách nên không phải Hệ thống | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Không có dữ liệu chặng hãng nước ngoài, cố mấy cũng không tra được | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Hoàn thừa nhưng không khách nào báo, không cảnh báo nào kích; chỉ lộ khi kiểm tra mẫu | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Khách chọn sai mục; trợ lý xử lý đúng luồng khách đã chọn | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Sổ cái lỗi mà vẫn báo "đã hoàn", trợ lý làm sai thiết kế | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Trích điều khoản không tồn tại; sai nhìn thấy được nên không phải Ngầm | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Khách nhập mã sàn thay mã vận đơn; thiếu gợi ý là chỗ cần sửa, không phải gốc lỗi | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Từ chối đúng chính sách, khách thấy sai vì ứng dụng hiện "cam kết 24 giờ" | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Trợ lý không xử lý được âm thanh, đầu vào ngoài định dạng hỗ trợ | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Hệ thống | Lỗi nằm ở tool tra đơn của hệ thống (trả thiếu trường), không do khách hay hoàn cảnh | Hệ thống | Có | Hệ thống |
| 13 | Ngữ cảnh | Trợ lý trả lời theo kịch bản phí vận chuyển, không khớp câu hỏi bảo hiểm của khách | Ngữ cảnh | Có | Ngữ cảnh |
| 14 | Giới hạn hệ thống | Yêu cầu bị đóng sau thao tác nhầm, trợ lý không có cách hoàn tác | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 15 | Hệ thống | Tính 100% thay vì 50%, sai chính sách; nhân viên bắt được nên không phải Ngầm | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Gửi ngay đúng thiết kế, nhưng 2:14 sáng không hợp hoàn cảnh khách | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Dùng bảng giá cũ, 212 đơn lệch mà không ai mở lại; không phải lỗi của khách | Do người dùng | Không | Ngầm |
| 18 | Hệ thống | Tin nhắn thiếu cách tính là lỗi mẫu tin của trợ lý, khách thấy và mở lại | Ngữ cảnh | Không | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Chỉ truy cập được dữ liệu 12 tháng, đơn 14 tháng ngoài dữ liệu; trợ lý đã chuyển đúng | Hệ thống | Không | Giới hạn hệ thống |
| 20 | Hệ thống | Thiếu khoá chống trùng nên hoàn hai lần, sai thiết kế chứ không phải không làm được | Giới hạn hệ thống | Không | Hệ thống |

**Tỉ lệ đồng thuận:** 16 / 20 = 80%

Phân bố nhãn thống nhất: Do người dùng 3 (1, 6, 9) · Hệ thống 6 (2, 7, 8, 12, 15, 20) · Ngữ cảnh 5 (3, 10, 13, 16, 18) · Giới hạn hệ thống 4 (4, 11, 14, 19) · Ngầm 2 (5, 17).

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận đạt 80% nên giữ định nghĩa năm loại như đề bài.

- **Ca 17 → Ngầm, không phải Do người dùng:** khách không nhập sai gì; trợ lý dùng bảng giá cũ trong bộ nhớ đệm, lệch 212 đơn trong 9 ngày mà không ai mở lại, chỉ lộ ra khi kiểm tra.
- **Ca 18 → Ngữ cảnh, không phải Hệ thống:** trợ lý tính đúng chính sách (30.000 đ × 50% = 15.000 đ), không vi phạm thiết kế; chỉ giả định "khách hiểu cách tính" là không khớp hoàn cảnh của khách.
- **Ca 19 → Giới hạn hệ thống, không phải Hệ thống:** trợ lý chỉ truy cập được dữ liệu 12 tháng, đơn 14 tháng nằm ngoài dữ liệu; trợ lý đã báo rõ và chuyển nhân viên đúng thiết kế.
- **Ca 20 → Hệ thống, không phải Giới hạn hệ thống:** hoàn hai lần vì thiếu khoá chống trùng là trợ lý làm sai thiết kế trong phạm vi, không phải việc trợ lý không thể làm.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `bank_transfer_failed` với `reason = invalid_account`, nối theo `trace_id`; cảnh báo khi quá 1% số lệnh hoàn trong ngày | Kiểm tra độ dài số tài khoản theo ngân hàng và tra tên chủ tài khoản trước khi tạo lệnh; khách xác nhận tên rồi mới hoàn | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát sổ cái mỗi giờ: số bút toán hoàn trên cùng một mã vận đơn lớn hơn 1; ngưỡng 0 ca | Thêm khoá chống trùng (mã vận đơn + loại hoàn) cho lệnh hoàn; yêu cầu gửi lại trả về trạng thái "đang xử lý" thay vì tạo lệnh mới | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | Event `notification_sent` có giờ gửi trong 22:00–07:00, đếm theo ngày; ngưỡng 0 tin, kèm số phản ánh gắn thẻ "làm phiền" theo tuần | Vẫn hoàn tiền ngay, nhưng tin Zalo trong khung 22:00–07:00 được xếp hàng tới 07:00; trạng thái trong ứng dụng cập nhật ngay | Trưởng nhóm CSKH |
| 11 | Giới hạn hệ thống | Event `unsupported_input` với `input_type = audio`, nối theo `trace_id`, đếm theo ngày; cảnh báo khi quá 2% số yêu cầu | Trả lời rõ trợ lý chưa nghe được tin nhắn thoại, đưa mẫu nhập nhanh (mã vận đơn, lý do hoàn) và nút chuyển nhân viên kèm file thoại | PM trợ lý hoàn phí |
| 5 | Ngầm | Kiểm tra mẫu 100 đơn có mã giảm giá mỗi tuần, so số tiền hoàn với giá sau giảm, ngưỡng 1% đơn lệch; cảnh báo hằng ngày khi số tiền hoàn lớn hơn số khách thực trả | Tool tính hoàn lấy giá khách thực trả (sau giảm); chặn lệnh hoàn vượt số khách thực trả và chuyển nhân viên xem lại | Kế toán trưởng |
