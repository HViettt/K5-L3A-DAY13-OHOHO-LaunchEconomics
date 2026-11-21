"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import sys
from statistics import NormalDist

import pandas as pd

# Windows Terminal cũ có thể dùng cp1252; ép UTF-8 để lệnh chạy không dừng ở dấu tiếng Việt.
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    hoa_don_moi_yc = (tien_token.sum() + tien_tool.sum()) / len(reqs)

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=chay_lai,
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=hoa_don_moi_yc,
    )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()

    # ---------- A2 · Mô hình chi phí từ trace ----------
    print('\n=== A2 · Mô hình chi phí từ trace ===')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        if ten == 'hoa_don_moi_yc':
            print(f'{ten:16s} {gia_tri:>14,.1f}')
        else:
            print(f'{ten:16s} {gia_tri:>14,.0f}')
    print(f'So lan goi tool: {int(runs["tool_calls"].sum()):,}')
    print(f'Phut xem lai [simulated]: {reqs["phut_xem_lai_simulated"].sum():,.1f}')
    print(f'Phut lam lai [simulated]: {reqs["phut_lam_lai_simulated"].sum():,.1f}')
    print(f'Gap hoa don/yc:  {ket_qua["cps"] / ket_qua["hoa_don_moi_yc"]:.1f}x')
    print(f'Ti trong lam lai [simulated]: {ket_qua["lam_lai"] / ket_qua["tong"] * 100:.1f}%')
    print(f'Ti trong xem lai [simulated]: {ket_qua["xem_lai"] / ket_qua["tong"] * 100:.1f}%')
    he_thong_moi_yc = (ket_qua['tong'] + (len(reqs) - ket_qua['thanh_cong']) * BASELINE) / len(reqs)
    print(f'Chi phi ca he thong/yc [simulated]: {he_thong_moi_yc:,.0f} đ ({he_thong_moi_yc / BASELINE:.2f}x)')

    # ---------- A3 · Tách theo loại yêu cầu ----------
    print('\n=== A3 · Tách theo loại yêu cầu ===')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        kq_loai = mo_hinh(runs, sub)
        ti_le_tc = kq_loai['thanh_cong'] / len(sub) * 100
        tb_chay = sub['so_lan_chay'].mean()
        print(
            f'{loai:10s} | n={len(sub):3d} | TC={ti_le_tc:5.1f}% | '
            f'chay/yc={tb_chay:.2f} | CPS [sim]={kq_loai["cps"]:8,.0f} đ | '
            f'so 12k={kq_loai["cps"] / BASELINE:.2f}x'
        )
    runs_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    runs_loai['is_ok'] = (runs_loai['status'] == 'ok').astype(int)
    print('\nTi le status=ok theo loai va lan thu (attempt):')
    print((runs_loai.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100).round(1))

    # ---------- A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ----------
    print('\n=== A4 · Chi phí cố định (noi_dia + hang_nang) ===')
    CHI_PHI_CO_DINH = 40_000_000
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi)
    ti_le_pv = kq_pv['thanh_cong'] / len(reqs)
    print(f'Trong pham vi: n={len(pham_vi)}, thanh_cong={kq_pv["thanh_cong"]}, tong={kq_pv["tong"]:,.0f} đ, CPS [sim]={kq_pv["cps"]:,.0f} đ')
    for ten_kl, khoi_luong in [('45.000 yc/thang', 45_000), ('Mot nua (22.500 yc/thang)', 22_500)]:
        viec_thang = khoi_luong * ti_le_pv
        co_dinh_viec = CHI_PHI_CO_DINH / viec_thang
        cps_co_dinh = kq_pv['cps'] + co_dinh_viec
        print(
            f'{ten_kl:26s} | TC/thang={viec_thang:8,.0f} | '
            f'co_dinh={co_dinh_viec:6,.0f} đ | CPS+CD [sim]={cps_co_dinh:6,.0f} đ | '
            f'so 12k={cps_co_dinh / BASELINE:.2f}x'
        )

    # ---------- B1 · Bảng độ nhạy (đổi từng yếu tố) ----------
    print('\n=== B1 · Bảng độ nhạy ===')
    kich_ban = {
        'Giá token gấp đôi':         dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':    dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi':     dict(he_so_xem_lai=2.0),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi':     dict(he_so_lam_lai=2.0),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%':  dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần':        dict(max_lan_chay=1),
    }
    goc = ket_qua['cps']
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:28s} | CPS [sim]={cps:8,.0f} đ | {(cps / goc - 1) * 100:+6.1f}%')

    # ---------- B2 · Đổi một cặp ----------
    print('\n=== B2 · Đổi một cặp ===')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    print(f'Token x2 + Xem lai x2: CPS [sim]={cps_cap:,.0f} đ ({(cps_cap / goc - 1) * 100:+.1f}%)')

    # ---------- B3 · Giới hạn chạy lại (chi phí cả hệ thống) ----------
    print('\n=== B3 · Giới hạn chạy lại ===')
    for gioihan in [1, 2, 3]:
        kq_gh = mo_hinh(runs, reqs, max_lan_chay=gioihan)
        khong_tc = len(reqs) - kq_gh['thanh_cong']
        ca_he_thong = kq_gh['tong'] + khong_tc * BASELINE
        print(
            f'{gioihan} lan | tong_tro_ly [sim]={kq_gh["tong"]:10,.0f} đ | '
            f'khong_TC={khong_tc:3d} | ca_he_thong [sim]={ca_he_thong:10,.0f} đ | '
            f'CPS [sim]={kq_gh["cps"]:6,.0f} đ'
        )

    # ---------- B4 · Xem lại 100% (phạm vi noi_dia + hang_nang) ----------
    print('\n=== B4 · Xem lại 100% (noi_dia + hang_nang) ===')
    runs_pv = runs[runs['request_id'].isin(pham_vi['request_id'])]
    so_co_ok = int(runs_pv[runs_pv['status'] == 'ok']['request_id'].nunique())
    so_lam_lai = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    token_tool_pv = kq_pv['token'] + kq_pv['tool']
    xem_lai_100 = so_co_ok * 5 * LUONG_PHUT
    lam_lai_9p = so_lam_lai * 9 * LUONG_PHUT
    tong_b4_9p = token_tool_pv + xem_lai_100 + lam_lai_9p
    cps_b4_9p = tong_b4_9p / kq_pv['thanh_cong']
    hoa_von_9p = (BASELINE * kq_pv['thanh_cong'] - token_tool_pv - lam_lai_9p) / (so_co_ok * LUONG_PHUT)

    tb_phut_lam_lai_all = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    lam_lai_thuc = so_lam_lai * tb_phut_lam_lai_all * LUONG_PHUT
    tong_b4_thuc = token_tool_pv + xem_lai_100 + lam_lai_thuc
    cps_b4_thuc = tong_b4_thuc / kq_pv['thanh_cong']
    hoa_von_thuc = (BASELINE * kq_pv['thanh_cong'] - token_tool_pv - lam_lai_thuc) / (so_co_ok * LUONG_PHUT)

    print(f'So yc co it nhat 1 lan ok: {so_co_ok}, so ca lam_lai: {so_lam_lai}, token+tool: {token_tool_pv:,.0f} đ')
    print(f'Voi 9 phut/ca lam lai:      tong={tong_b4_9p:,.0f} đ | CPS [sim]={cps_b4_9p:,.0f} đ ({cps_b4_9p / BASELINE:.2f}x) | hoa von <= {hoa_von_9p:.1f} phut/lan xem')
    print(f'Voi {tb_phut_lam_lai_all:.1f} phut/ca (TB data): tong={tong_b4_thuc:,.0f} đ | CPS [sim]={cps_b4_thuc:,.0f} đ ({cps_b4_thuc / BASELINE:.2f}x) | hoa von <= {hoa_von_thuc:.1f} phut/lan xem')

    # ---------- D1 · Cỡ mẫu cho kế hoạch pilot ----------
    def co_mau(p1, p2, alpha=0.05, power=0.8):
        """Cỡ mẫu mỗi nhóm khi so sánh hai tỉ lệ theo công thức NormalDist."""
        za = NormalDist().inv_cdf(1 - alpha / 2)
        zb = NormalDist().inv_cdf(power)
        pb = (p1 + p2) / 2
        return math.ceil(
            (
                za * math.sqrt(2 * pb * (1 - pb))
                + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
            ) ** 2 / (p2 - p1) ** 2
        )

    print('\n=== D1 · Cỡ mẫu ===')
    alpha, power, icc = 0.05, 0.80, 0.02
    n_5pp = co_mau(0.70, 0.75, alpha=alpha, power=power)
    de_m75 = 1 + (75 - 1) * icc
    n_5pp_m75 = math.ceil(n_5pp * de_m75)
    n_max_20_staff = 20 / icc
    n_max_6_depot = 6 / icc
    n_6pp = co_mau(0.70, 0.76, alpha=alpha, power=power)
    m_6pp_20_staff = math.ceil(n_6pp * (1 - icc) / (20 - n_6pp * icc))
    de_m6pp = 1 + (m_6pp_20_staff - 1) * icc
    n_effective_6pp = 20 * m_6pp_20_staff / de_m6pp

    print(f'a) Chia theo yeu cau: {n_5pp:,} yeu cau moi nhom')
    print(
        f'b) Theo nhan vien, m=75: DE={de_m75:.2f}; n={n_5pp * de_m75:,.2f} '
        f'-> {n_5pp_m75:,} yeu cau moi nhom; can '
        f'{math.ceil(n_5pp_m75 / 75)} nhan vien moi nhom (>40, khong du)'
    )
    print(f'c) 20 nhan vien moi nhom: toi da {n_max_20_staff:,.0f} < {n_5pp:,} yeu cau')
    print(f'd) 6 depot moi nhom: toi da {n_max_6_depot:,.0f} yeu cau')
    print(
        f'e) Chenh 6 diem: n={n_6pp:,} yeu cau moi nhom; can m>={m_6pp_20_staff} '
        f'yeu cau/nguoi voi 20 nhan vien (DE={de_m6pp:.2f}; '
        f'n_effective={n_effective_6pp:,.1f})'
    )

    # Power thực tế nếu kế hoạch được thiết kế cho 6 điểm nhưng tác động chỉ 5 điểm.
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower

    effect_size_5pp = abs(proportion_effectsize(0.70, 0.75))
    power_5pp = NormalIndPower().power(
        effect_size=effect_size_5pp,
        nobs1=n_6pp,
        alpha=alpha,
        ratio=1,
        alternative='two-sided',
    )
    print(f'Power thuc te o che do 6 diem neu tac dong chi 5 diem: {power_5pp:.2f}')

    # ---------- D3 · Tỉ lệ mở lại hiện tại trước khi đặt luật dừng ----------
    mo_lai_hien_tai = reqs['mo_lai_trong_7_ngay'].mean()
    mo_lai_pham_vi = pham_vi['mo_lai_trong_7_ngay'].mean()
    print(
        f'Ty le mo lai hien tai: {mo_lai_hien_tai:.2%} toan bo; '
        f'{mo_lai_pham_vi:.2%} trong pham vi noi_dia + hang_nang'
    )
