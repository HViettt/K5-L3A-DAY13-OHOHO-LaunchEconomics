# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: OHOHO · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ `simulated` (4.373.585 đ ÷ 978 việc), gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); giờ nhân viên chiếm 92,5% | Giả lập | Kế toán trưởng |
| 2 · Ba yếu tố nhạy nhất | Số ca làm lại gấp đôi +51,8% · tỉ lệ xem lại gấp đôi +40,7% · lương +25% → +23,1% (`simulated`); giá token gấp đôi chỉ +5,6% | Giả lập | Kỹ sư trưởng agent |
| 3 · So với nhân viên tự làm | Cả hệ thống 5.865 đ/yêu cầu = 0,49× mức 12.000 đ (`simulated`); phạm vi noi_dia + hang_nang kèm cố định 40 triệu/tháng: 4.599 đ = 0,38×; quoc_te 1,88× nên loại khỏi pilot. Bất lợi: xem lại 100% đẩy lên 11.743–12.415 đ = 0,98–1,03× (`simulated`) | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử: chính 82,83% (994/1.200) · bỏ qua gợi ý 27,12% (48/177) · mở lại trong 7 ngày 4,25% (51/1.200); 10 event có `trace_id`. Đợt chạy thử không có đối chứng nên chưa kết luận về tác động | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 16/20 = 80%, thống nhất 4 ca lệch (17, 18, 19, 20); nhãn chốt: 3 do người dùng · 6 hệ thống · 5 ngữ cảnh · 4 giới hạn · 2 ngầm; 5 ca khắc phục đủ năm loại (ca 1, 20, 16, 11, 5), mỗi ca có ngưỡng đo được | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 6 · Pilot plan | Chia ngẫu nhiên theo nhân viên 20 + 20, phạm vi noi_dia + hang_nang; MDE 6 điểm cần 859 yêu cầu/nhóm, ≥ 299 yêu cầu/nhân viên (DE 6,96). Bất lợi: 20 + 20 tối đa 1.000 < 1.251 nên không thấy được 5 điểm, power chỉ 0,64; 3 luật dừng, quyết định 2027-01-05 | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi → 6.787 đ (+51,8%) · xem lại gấp đôi → 6.292 đ (+40,7%) · xem lại 100% kéo dài → 11.743–12.415 đ = 0,98–1,03× (`simulated`); mỗi rủi ro có ngưỡng theo dõi và người phụ trách | Giả lập | Kế toán trưởng |

**Đề xuất:** Go có điều kiện, cho pilot chỉ noi_dia + hang_nang (loại quoc_te 1,88× và doi_tac 0,85×, `simulated`). Các điều kiện:

- Khoá chống trùng và đối soát sổ cái hằng giờ (ca 7, 20) chạy thử đạt 0 ca hoàn trùng trước ngày bắt đầu · Kỹ sư trưởng agent · kiểm tra 2026-12-01.
- Ký chấp nhận MDE 6 điểm (power 0,64 nếu tác động thật chỉ 5 điểm) và cam kết mỗi nhân viên nhóm trợ lý xử lý ≥ 299 yêu cầu · Giám đốc vận hành · kiểm tra 2026-12-01.
- Bật đủ 10 event có `trace_id`; sau tuần 1 thay số phút `simulated` bằng phút đo thật và tính lại chi phí mỗi việc thành công · PM trợ lý hoàn phí · kiểm tra 2026-12-15.
- Có kế hoạch giảm xem lại theo bậc; thời gian xem lại đo thật phải ≤ 5 phút/lần, nếu không thì dừng mở rộng vì xem lại 100% đã ở mức 0,98–1,03× (`simulated`) · Trưởng nhóm CSKH · kiểm tra 2026-12-22.
