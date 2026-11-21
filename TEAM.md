# Team

## Thông tin nhóm

- Tên nhóm: OHOHO
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-OHOHO-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/HViettt/K5-L3A-DAY13-OHOHO-LaunchEconomics · `main` · (commit chốt ghi sau lần push cuối)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Hoàng Việt | 2A202603487 | hoangviet1824qsqn@gmail.com | HViettt | Người viết code (A, B) |
|   2 | Đỗ Hoàng Minh | 2A202603507 | hoangminh.word@gmail.com | MazzDh | Người kiểm số, người gắn nhãn 2 (D, chỉ số và rủi ro E) |
|   3 | Đoàn Gia Long | 2A202603443 | doanlong932004@gmail.com | ... | Người gắn nhãn 1, kiêm giữ hồ sơ (C, hồ sơ launch v0, tổng hợp) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-

## NguyenHoangViet-2A202603487

### Phần việc phụ trách

- Nhiệm vụ A và B: `src/lab13.py` (phần A, B), `report/team/bang_chi_phi.md`.

### Đóng góp cụ thể

- Ba phép thử A1 ĐẠT (1,20 · 1,25 · 1,25); chi phí mỗi việc thành công 4.472 đ `simulated`, gấp 16,3 lần hoá đơn; bảng A3 theo loại, A4 chi phí cố định.
- Bảng độ nhạy B1 đủ 9 kịch bản, B2 đổi một cặp (+46,3%), B3 giới hạn chạy lại (2 lần rẻ nhất cho hệ thống), B4 xem lại 100% (0,98–1,03×, `simulated`).

### Bằng chứng

- Commit `e4a9267`; `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/2A202603487_NguyenHoangViet.md`.

## DoHoangMinh-2A202603507

### Phần việc phụ trách

- Nhiệm vụ D (`report/team/pilot_plan.yaml`, khối D1 trong `src/lab13.py`), chỉ số, event và rủi ro của E (`report/team/chi_so.md`), bộ nhãn 2 của Nhiệm vụ C.

### Đóng góp cụ thể

- D1 đủ 5 câu (1.251 · 3.103 · 1.000 · 300 · 299), chọn chia theo nhân viên 20 + 20 với MDE 6 điểm, nêu power 0,64; 3 luật dừng đủ bốn vế.
- Ba chỉ số tính thử 82,83% · 27,12% · 4,25%, 2 chỉ số tự đề xuất, 10 event có `trace_id`, 3 dòng rủi ro kinh tế lấy số từ B1–B4.

### Bằng chứng

- Commit `fd5c1a7`, `7386d46`, `0c739f5`; `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/2A202603507_DoHoangMinh.md`.

## DoanGiaLong-2A202603443

### Phần việc phụ trách

- Nhiệm vụ C (`report/team/bang_loi.md`), hồ sơ launch v0 (`report/team/ho_so_launch_v0.md`), tổng hợp `group_report.md`, `TEAM.md`, `phieu_cham.md`, soát checklist nộp bài.

### Đóng góp cụ thể

- Bộ nhãn 1 cho 20 ca lỗi; đồng thuận 16/20 = 80%; quy tắc cho 4 ca lệch; quy tắc cho ca không trùng; bảng khắc phục 5 ca đủ năm loại (ca 1, 20, 16, 11, 5).
- Hồ sơ launch v0 đủ bảy mục và đề xuất Go có điều kiện (4 điều kiện, mỗi điều kiện có người phụ trách và ngày kiểm tra); báo cáo nhóm; soát checklist nộp bài.

### Bằng chứng

- `report/team/bang_loi.md`, `report/team/ho_so_launch_v0.md`, `report/team/2A202603443_DoanGiaLong.md`; commit `4c451cc`, `d4fc1df` và commit hoàn thiện hồ sơ.
