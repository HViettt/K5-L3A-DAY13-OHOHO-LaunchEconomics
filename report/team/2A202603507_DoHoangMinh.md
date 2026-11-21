# Báo cáo cá nhân — DoHoangMinh-2A202603507

## 1. Thông tin thành viên

- Họ tên: Đỗ Hoàng Minh
- MSSV: 2A202603507
- Email: hoangminh.word@gmail.com
- Vai trò trong nhóm: TV2 — người kiểm số và người gắn nhãn 2; phụ trách Nhiệm vụ D, chỉ số/event của E và đoạn code CP4 trong `src/lab13.py`

## 2. Phần việc phụ trách

- Nhiệm vụ D: tính đủ **5 câu D1**, trả lời **5 câu D2**, hoàn thiện `pilot_plan.yaml` và thêm code cỡ mẫu vào `src/lab13.py`.
- Nhiệm vụ E1–E2: hoàn thiện `chi_so.md` gồm **3 chỉ số tính thử, 2 chỉ số tự đề xuất, 10 event có `trace_id`** và **3 dòng rủi ro kinh tế**.
- Nhiệm vụ C: gắn độc lập bộ nhãn 2 cho **20 ca lỗi** và bàn giao số thô cho người giữ hồ sơ; đồng thuận sau khi so là **16/20 = 80%**.

## 3. Đóng góp cụ thể

- D1: chia theo yêu cầu cần **1.251** mỗi nhóm; chia theo nhân viên `m=75` có DE **2,48**, cần **3.103** yêu cầu mỗi nhóm; 20 nhân viên mỗi nhóm có trần **1.000**; 6 depot mỗi nhóm có trần **300**; mức chênh 6 điểm cần **859** yêu cầu mỗi nhóm, `m ≥ 299`, DE **6,96**.
- D2: chọn phương án **20 + 20 nhân viên** để tách tốt tác động; chấp nhận MDE **6 điểm**, nêu rõ nếu tác động thật chỉ **5 điểm** thì power chỉ còn **0,64**.
- Pilot plan: đặt ngưỡng mở lại hiện tại **4,25%** toàn bộ và **3,97%** trong phạm vi; viết **3 luật dừng** đủ NẾU–TRONG–THÌ–KHÔNG THÌ, có người quyền dừng và thời hạn.
- E1: tính thử trên **1.200** yêu cầu: chỉ số chính **82,83%**, bỏ qua gợi ý **27,12%**, lỗi lọt khách **4,25%**; đề xuất thêm **2 chỉ số** có event đo được.
- E2: nêu rủi ro tăng làm lại lên **6.787 đ (+51,8%, `simulated`)**, tăng xem lại lên **6.292 đ (+40,7%, `simulated`)** và xem lại 100% lên **11.743–12.415 đ (0,98–1,03×, `simulated`)**.

## 4. Bằng chứng

- `src/lab13.py`: khối `D1 · Cỡ mẫu` in đủ **5 câu**, power **0,64** và tỉ lệ mở lại **4,25% / 3,97%**; lệnh chạy từ `src` đã hoàn tất.
- `report/team/pilot_plan.yaml`: YAML đọc bằng `yaml.safe_load`, đủ **5 câu D1 + 5 câu D2**, **3 luật dừng** và các trường pilot.
- `report/team/chi_so.md`: **3 chỉ số tính thử + 2 chỉ số tự đề xuất**, **10 event có `trace_id`**, **3 dòng rủi ro** lấy số từ B1–B4.
- `report/team/bang_loi.md`: bộ nhãn 2 độc lập cho **20 ca**; đồng thuận **16/20 = 80%**.
- Commit nền của TV2: `fd5c1a7` (`update TV2`); commit hoàn thiện CP4/E1–E2 được tạo sau khi kiểm tra đầy đủ và ghi trong lịch sử Git.

## 5. Công cụ AI đã dùng

- OpenCode/ChatGPT: dùng để giải thích công thức cỡ mẫu và hệ số thiết kế, gợi ý cách tổ chức YAML/Markdown, cùng soát lỗi cấu trúc; không dùng AI để bịa số hay thay kết quả kiểm tra độc lập.
- Tự kiểm tra: chạy `cd src && python lab13.py` và đối chiếu **1.251, 3.103, 1.000, 300, 299** với công thức; kiểm tra YAML bằng `yaml.safe_load`; đếm lại **3 chỉ số, 10 event, 3 dòng rủi ro**; đối chiếu mọi số `simulated` với `bang_chi_phi.md`.

## 6. Tự đánh giá

- Đã hoàn thành đúng **3 nhóm sản phẩm** của TV2: code CP4, `pilot_plan.yaml`, `chi_so.md`, đồng thời hoàn thiện báo cáo cá nhân; các kiểm tra tự động đều chạy thành công.
- Hạn chế còn lại: bộ nhãn đồng thuận **80%** chỉ đạt ngưỡng, và kế hoạch MDE **6 điểm** phải được Giám đốc vận hành ký nhận vì power ở tác động **5 điểm** chỉ **0,64**.
- Hướng cải thiện: sau tuần đầu pilot, thay số phút `simulated` bằng số đo thực tế và kiểm tra lại tỉ lệ làm lại/xem lại trước khi mở rộng.
