# Báo cáo cá nhân — NguyenHoangViet-2A202603487

## 1. Thông tin thành viên

- Họ tên: Nguyễn Hoàng Việt
- MSSV: 2A202603487
- Email: hoangviet1824qsqn@gmail.com
- Vai trong nhóm: Người viết code (thành viên 1/3 của nhóm OHOHO — phụ trách Nhiệm vụ A và B)

## 2. Phần việc phụ trách

- Nhiệm vụ A (CP1): viết ba hàm phép thử đáp án biết trước (A1), xây dựng hàm mô hình chi phí `mo_hinh` từ trace (A2), tách chi phí theo 4 loại yêu cầu và tỉ lệ `ok` theo lần thử (A3), tính bổ sung chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` (A4) trong `src/lab13.py`.
- Nhiệm vụ B (CP2): chạy 9 kịch bản độ nhạy đổi từng yếu tố (B1), kịch bản đổi cặp và xếp hạng top 3 yếu tố ảnh hưởng mạnh nhất (B2), so sánh chi phí cả hệ thống theo giới hạn 1/2/3 lần chạy (B3), phân tích kịch bản xem lại 100% ở cả mức 9 phút và 15,3 phút trung bình dữ liệu (B4).
- Điền đầy đủ `report/team/bang_chi_phi.md`, gắn nhãn `simulated` cho mọi con số từ hai cột `_simulated`, và kiểm tra chạy chéo sau khi nhóm ghép phần D1.

## 3. Đóng góp cụ thể

- **A1:** Hoàn thành 3 hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`, đạt cả 3 phép thử (`1,20 · 1,25 · 1,25`).
- **A2:** Tính chi phí mỗi việc thành công = **4.472 đ** (`simulated`), gấp **16,3×** hoá đơn token + tool mỗi yêu cầu (274,7 đ); làm lại chiếm **51,8%**, xem lại **40,7%** (`simulated`); chi phí cả hệ thống = **5.865 đ/yêu cầu = 0,49×** mức 12.000 đ (`simulated`).
- **A3–A4:** Chỉ ra `quoc_te` không đáng xử lý (**22.515 đ = 1,88×**, `simulated`; tỉ lệ `ok` tụt từ 30,0% → 11,4% → 2,2% nên chạy lại không giúp) và `doi_tac` sát ngưỡng (**10.215 đ = 0,85×**); đề xuất thu hẹp phạm vi pilot về `noi_dia` + `hang_nang` (**4.599 đ = 0,38×** ở 45.000 yc/tháng và **5.784 đ = 0,48×** ở nửa khối lượng, đã cộng cố định 40 triệu/tháng, `simulated`).
- **B1–B4:** Xếp hạng top 3 yếu tố nhạy nhất (**1. Số ca làm lại +51,8% · 2. Tỉ lệ xem lại +40,7% · 3. Lương +25% → +23,1%**, `simulated`); xác định giới hạn **2 lần chạy** rẻ nhất cho cả hệ thống (**6.901.220 đ**, `simulated`), khác với mức CPS thấp nhất ở 1 lần (4.111 đ); tính kịch bản xem lại 100% lên **11.743 đ (0,98×)** ở 9 phút làm lại và **12.415 đ (1,03×)** ở 15,3 phút trung bình dữ liệu (`simulated`).

## 4. Bằng chứng

- `src/lab13.py`: các hàm A1, `mo_hinh` (A2) và toàn bộ khối tính toán A2, A3, A4, B1, B2, B3, B4.
- `report/team/bang_chi_phi.md`: đầy đủ các bảng A1–A4, B1–B4, câu trả lời ngắn ($\le 3$ dòng, có số) và nhãn `simulated`.
- Commit: `e4a9267` (`feat(CP1-CP2): hoan thanh mo hinh chi phi (A) va bang do nhay (B)`).

## 5. Công cụ AI đã dùng

- Antigravity (Gemini): dùng để đọc cấu trúc đề bài, chia việc không chồng chéo cho nhóm 3 người, gợi ý cấu trúc code A1–B4 trong `src/lab13.py` và rà soát trình bày bảng `report/team/bang_chi_phi.md`.
- Cách tự kiểm tra: tự chạy trực tiếp `cd src && python lab13.py` trên dữ liệu CSV thật của lab, xác nhận 3 phép thử A1 in `ĐẠT`, đối chiếu từng con số A2–B4 với công thức trong `docs/du_lieu_va_cong_thuc.md` và tính chất đối xứng của bảng độ nhạy (giảm nửa = nửa mức tăng), kiểm tra không còn từ cấm và đủ nhãn `simulated`.

## 6. Tự đánh giá

- Hoàn thành đúng hạn và chính xác toàn bộ phần A, B để bàn giao sớm số liệu cho TV2 (làm rủi ro kinh tế `chi_so.md` và `pilot_plan.yaml`) và TV3 (điền `ho_so_launch_v0.md`), không gây xung đột Git.
- Nắm chắc bản chất kinh tế của mô hình (vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm `thanh_cong`, vì sao tối ưu CPS khác tối ưu tổng chi phí hệ thống, và rủi ro khi xem lại 100%).
- Điểm cần lưu ý thêm: cần cài đủ `statsmodels` trong môi trường local để chạy trọn vẹn phần D1 sau khi pull code của TV2, và chủ động rà soát cùng nhóm trước buổi duyệt chéo Gate 2a.
