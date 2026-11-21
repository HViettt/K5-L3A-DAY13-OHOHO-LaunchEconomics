# Báo cáo cá nhân — DoanGiaLong-2A202603443

## 1. Thông tin thành viên

- Họ tên: Đoàn Gia Long
- MSSV: 2A202603443
- Email: doanlong932004@gmail.com
- Vai trong nhóm: Người gắn nhãn 1 kiêm giữ hồ sơ (thành viên 3/3 của nhóm OHOHO)

## 2. Phần việc phụ trách

- Nhiệm vụ C: gắn bộ nhãn 1 cho 20 ca lỗi, tính tỉ lệ đồng thuận với bộ nhãn 2, viết quy tắc cho ca không trùng, lập bảng khắc phục 5 ca (`report/team/bang_loi.md`).
- Hồ sơ launch v0: dựng khung 7 mục từ đầu buổi, điền số khi các thành viên khác commit (`report/team/ho_so_launch_v0.md`).
- Tổng hợp: `report/team/group_report.md`, `TEAM.md`, `report/team/phieu_cham.md` khi nhóm làm hội đồng Gate 2a.
- Soát checklist nộp bài: không có từ cấm, đủ nhãn `simulated`, người phụ trách là vai trò.

## 3. Đóng góp cụ thể

- Gắn bộ nhãn 1 độc lập cho 20 ca: 3 do người dùng (1, 6, 9), 7 hệ thống (2, 7, 8, 12, 15, 18, 20), 4 ngữ cảnh (3, 10, 13, 16), 4 giới hạn hệ thống (4, 11, 14, 19), 2 ngầm (5, 17).
- Bảng khắc phục 5 ca, mỗi loại một ca (ca 1, 20, 16, 11, 5); mỗi dòng có event hoặc kiểm tra mẫu, ngưỡng, tần suất và một vai trò phụ trách.
- Dựng khung hồ sơ launch v0 với người phụ trách cho cả 7 mục.
- So với bộ nhãn 2 (Minh): trùng 16/20 = 80%; viết quy tắc phân biệt và thống nhất 4 ca lệch (17, 18, 19, 20).
- Điền hồ sơ launch v0 mục 1, 2, 3 từ số A/B của Việt (4.472 đ, 16,3×, 0,49×, xếp hạng độ nhạy, `simulated`) và mục 5.
- Đề xuất cuối của nhóm: ...

## 4. Bằng chứng

- `report/team/bang_loi.md`: cột "Nhãn người 1", tỉ lệ đồng thuận, quy tắc 4 ca lệch, bảng khắc phục 5 ca.
- `report/team/ho_so_launch_v0.md`: khung 7 mục, mục 1, 2, 3, 5.
- Commit: ...

## 5. Công cụ AI đã dùng

- Claude Code: trích 20 ca lỗi từ file đề `.docx`, tính tỉ lệ đồng thuận giữa hai bộ nhãn, nháp quy tắc cho ca lệch và bảng khắc phục, đối chiếu số A/B khi điền hồ sơ.
- Bộ nhãn 1 do tôi tự gắn, không dùng AI. Cách tự kiểm tra: đếm lại số ca trùng bằng tay (16/20), đọc lại từng dòng khắc phục để chắc có event, ngưỡng, tần suất và một vai trò phụ trách; số trong hồ sơ đối chiếu với output của `python lab13.py`.

## 6. Tự đánh giá

...
