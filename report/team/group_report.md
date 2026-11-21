# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: OHOHO
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để hội đồng Gate 2a quyết định có duyệt kế hoạch pilot hay không. Nhóm 3 người chia việc theo file để không ai sửa trùng file của người khác: Việt làm A + B (`src/lab13.py`, `bang_chi_phi.md`); Minh làm D + chỉ số và event của E (`pilot_plan.yaml`, `chi_so.md`, đoạn D1 trong `lab13.py`); Long làm C, hồ sơ launch v0 và tổng hợp. Ba điểm bàn giao: 20 nhãn thô của Minh cho Long (CP3), Việt push số A và B, Minh push pilot và chỉ số lúc 16:45 để chốt đề xuất trước 17:00.

## 3. Giải pháp

Tóm tắt cách nhóm làm từng nhiệm vụ A–E và link tới file hồ sơ tương ứng.

- **A · Mô hình chi phí** ([bang_chi_phi.md](bang_chi_phi.md)): tử số tính mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm `ket_qua == 'thanh_cong'`; cộng giờ xem lại và làm lại (`simulated`); tách theo loại và cộng chi phí cố định cho phạm vi noi_dia + hang_nang.
- **B · Độ nhạy** ([bang_chi_phi.md](bang_chi_phi.md)): đổi từng yếu tố trong 9 kịch bản, một cặp, giới hạn 1–3 lần chạy và kịch bản xem lại 100%.
- **C · Bảng lỗi** ([bang_loi.md](bang_loi.md)): hai người gắn nhãn độc lập 20 ca theo năm loại PAIR, so nhãn, thống nhất ca lệch, chọn 5 ca để gán cách phát hiện đo được và vai trò phụ trách.
- **D · Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): tính 5 câu cỡ mẫu trước, rồi chọn chia ngẫu nhiên theo nhân viên 20 + 20; tính tỉ lệ mở lại hiện tại trước khi đặt luật an toàn.
- **E · Chỉ số, rủi ro, hồ sơ** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): tính thử ba chỉ số, liệt kê event có `trace_id`, lấy rủi ro từ bảng độ nhạy, ghép thành hồ sơ một trang.

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo nhóm nhận được từ hội đồng.

- Chi phí mỗi việc thành công **4.472 đ** (`simulated`), gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu; chi phí cả hệ thống **5.865 đ/yêu cầu = 0,49×** mức nhân viên tự làm 12.000 đ (`simulated`).
- Ba yếu tố nhạy nhất: làm lại (+51,8%), xem lại (+40,7%), lương (+23,1%) (`simulated`); `quoc_te` 1,88× nên loại khỏi pilot.
- Bảng lỗi: đồng thuận **16/20 = 80%**.
- Chỉ số trong đợt chạy thử: chính **82,83%**, bỏ qua gợi ý **27,12%**, mở lại 7 ngày **4,25%**.
- Pilot: 20 + 20 nhân viên, MDE 6 điểm, 859 yêu cầu/nhóm; con số bất lợi là power **0,64** nếu tác động thật chỉ 5 điểm.
- **Đề xuất: Go có điều kiện** cho pilot noi_dia + hang_nang, 4 điều kiện có người phụ trách và ngày kiểm tra.
- **Kết quả duyệt chéo nhóm nhận được từ hội đồng (nhóm 4AE):** **26 / 30 điểm** (Đề xuất khớp bằng chứng: 9/10 · Số giả lập và phạm vi: 8/10 · Pilot ra được quyết định: 9/10) — **Quyết định hội đồng: Go có điều kiện**. Hội đồng đánh giá cao đề xuất khớp bằng chứng, nêu đủ số bất lợi (xem lại 100% lên 0,98–1,03×, power 0,64) và 3 luật dừng rõ ngưỡng/người dừng; đồng thời góp ý 3 điểm cần làm rõ (chênh lệch baseline 0,70 vs 82,83%, ngày bắt đầu/thời lượng pilot, và CPS cộng cố định 40 triệu/tháng ở đúng quy mô pilot 20 nhân viên). Nhóm đã phản hồi đầy đủ tại buổi (dùng baseline từ nhóm đối chứng cùng kỳ, nền ~0,83 cần ít mẫu hơn nên 859 vẫn thận trọng; chạy 2 tuần 2026-12-22 → 2027-01-05; ở 5.980 yc pilot thì CPS + cố định là ~10.712 đ = 0,89× `simulated`, chạy đủ 1 tháng giảm còn ~6.647 đ = 0,55× `simulated`).

## 5. Khó khăn và cách xử lý

- Nhóm chỉ có 3 người cho 4 vai: chia việc theo file (mỗi file một người sở hữu) và chỉ đồng bộ ở 3 điểm bàn giao để tránh xung đột Git.
- Xung đột Git ở `bang_loi.md` khi hai người cùng sửa: giữ cột nhãn của từng người, gộp lại bằng tay.
- Bản nháp đầu của `pilot_plan.yaml` và `chi_so.md` còn thiếu D1, D2, số chỉ số và luật dừng chưa đủ vế: người giữ hồ sơ rà soát, TV2 sửa lại trước khi điền hồ sơ.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Số phút xem lại và làm lại là `simulated`: chi phí mỗi việc thành công phải tính lại bằng phút đo thật sau tuần 1 pilot.
- 40 nhân viên không đủ cho MDE 5 điểm; pilot chỉ thấy được mức chênh 6 điểm (power 0,64 ở mức 5 điểm).
- Đồng thuận nhãn 80% chỉ vừa đạt ngưỡng; nên viết thêm ví dụ cho các cặp loại dễ lẫn (Hệ thống / Giới hạn, Hệ thống / Ngữ cảnh).

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure"
- Tài liệu statsmodels, `NormalIndPower`
- `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`
