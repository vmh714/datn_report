# Kế hoạch chuẩn bị số liệu "xịn" → Bài báo Q1 (Elsevier *Internet of Things*)

## Context

Đóng gói phần TinyML của đồ án (mô hình `v30_optimize`: DS-1D-CNN, 26,629 params, INT8 trên ESP32-S3,
**Acc 95.40% · Fall-Recall 97.50% · 11.20 ms · 55.8 KB · arena 28.3 KB**) thành bài Elsevier IoT.
Đã chốt: tạp chí *Internet of Things*; đóng khung **TinyML co-design là trọng tâm**, viết **hướng giả
thuyết**; tác giả chạy được cross-dataset + đo năng lượng thật (INA2xx, loop-invoke RAM) + pilot +
**bổ sung board ARM Cortex-M + CMSIS-NN**.

**Luận đề trung tâm cần số liệu chứng minh:** việc chọn `v30_optimize` phải được quyết bởi **Pareto
năng lượng–độ chính xác**, không phải chỉ latency. Số liệu năng lượng (P2) là mảnh khóa: nó biến
"chọn model nhanh" thành "chọn model tối ưu năng lượng/ngày pin ở cùng mức accuracy".

Tài liệu này = **kế hoạch thực thi (WBS) chuẩn bị số liệu**. Định vị/cấu trúc bài đã thống nhất ở các
vòng trước; ở đây tập trung vào *việc cần làm để có số liệu*.

---

## Giả thuyết bài kiểm định (mỗi số liệu phục vụ 1 giả thuyết)

- **H1** — Trên MCU có accelerator, **operator-coverage** (tỉ lệ MAC nằm trên op được tăng tốc) chi
  phối latency, KHÔNG phải MACs/params. *(số liệu: D-A1, D-E1, D-E3)*
- **H2** — Head tĩnh (Flatten + dual-pool) giữ thông tin thời gian ngang recurrent/dilated ở phần nhỏ
  latency. *(số liệu: D-A2 ablation head)*
- **H3** — Generalization đa trục: subject (LSO) · population (young/elderly) · dataset (cross-dataset)
  · platform (ESP↔ARM). *(số liệu: D-B, D-D, D-E3, D-F)*

---

## Bản đồ "reviewer bắt lỗi → task bịt lỗ"

| Điểm reviewer | Task bịt |
|---|---|
| M1 Chọn v30_optimize chưa biện minh | **D-C (energy Pareto)** |
| M2 Dữ liệu ngã người già (0/375) | D-D3 young/elderly breakdown + Discussion trung thực |
| M3 Oracle windowing | **D-D2 streaming/event-level** |
| M4 Thiếu ESP-NN ON/OFF | **D-E1** |
| M5 Nhầm inference vs detection latency | D-D2 (đo detection-to-alert) |
| M6 Precision/FPR bị bỏ | D-D2 (FPR/giờ) + D-D4 (PR/ROC) |
| M7 Sim-to-real cảm biến | D-F3 (khớp phân phối) |
| M8 Single-platform | **D-E3 (ARM+CMSIS-NN)** |
| Minor (variance, baseline, mâu thuẫn) | D-A3, D-D5, D-G |

---

# WBS — CÁC TASK CHUẨN BỊ SỐ LIỆU

Ký hiệu: **[⭐ critical path]**, effort ~ (S<1 ngày / M vài ngày / L 1–2 tuần). Mỗi task ghi:
mục tiêu · bước · output artifact · phụ thuộc.

## Track A — Tái công cụ hóa model & training (nền cho H1/H2)

**D-A1 — Trích MACs + op-composition cho 15 phiên bản** ⭐ (S)
- Mục tiêu: biến độc lập trung tâm của H1.
- Bước: (1) với mỗi model, đếm MACs/FLOPs (keras-flops hoặc TF profiler). (2) Parse `.tflite` bằng
  `tf.lite.Interpreter._get_ops_details()` (hoặc schema `tflite`), liệt kê từng op + kích thước tensor.
  (3) Đối chiếu danh sách op **được ESP-NN accelerate** (đã có bảng 2.1/3.2) → tính **% MAC accelerated**.
- Output: `ops_profile.csv` (version, MACs, params, #ops, %MAC_accelerated, danh sách op không-accel).
- Phụ thuộc: các model đã lưu (đã có).

**D-A2 — Ablation head có kiểm soát (H2)** (M)
- Mục tiêu: cô lập đúng biến "head", chứng minh Flatten thay được recurrent.
- Bước: giữ backbone cố định, hoán 3 head: {pool-only (v30), Flatten+dual-pool (v30_optimize),
  TCN/recurrent}. Train cùng seed/split. Ghi Trans-F1, Macro-F1, latency.
- Output: bảng ablation head (T2 phụ).
- Phụ thuộc: pipeline train (đã có).

**D-A3 — Retrain multi-seed + LSO chuẩn hóa** ⭐ (M)
- Mục tiêu: variance thống kê (bịt Minor) + số liệu sạch, cùng test set (giải mâu thuẫn 95.33 vs 95.40).
- Bước: chạy ≥5 seed cho v30_optimize + các baseline chính; cùng LSO splits; log per-fold.
- Output: `runs_metrics.csv` (seed, fold, acc, fall-recall, fall-precision, trans-f1, macro-f1) →
  mean±std + CI.
- Phụ thuộc: —.

**D-A4 — Export INT8 chuẩn cho mọi ứng viên deploy** (S)
- Mục tiêu: đảm bảo mọi model so sánh energy/latency dùng cùng quy trình PTQ + cùng representative set.
- Output: thư mục `.tflite` INT8 versioned + hash; ghi size Flash/arena thực.
- Phụ thuộc: D-A3.

## Track B — Cross-dataset (H3-dataset, đòn bẩy Q1 lớn nhất)

**D-B1 — Harmonization pipeline tái sử dụng** ⭐ (M)
- Mục tiêu: đưa KFall/UMAFall/FallAllD về cùng không gian với SisFall.
- Bước: resample→100 Hz; chọn subset cảm biến **thắt lưng/hông**; rescale accel→±8g, gyro→±500 dps;
  cửa sổ 200×6; ánh xạ nhãn ADL/fall → 5-lớp theo cùng tiêu chí gyro-RMS>20/SVM-peak.
- Output: loader thống nhất + `dataset_stats.md` (số subject/ADL/fall mỗi bộ sau harmonize).

**D-B2 — Hai kịch bản đánh giá** ⭐ (M)
- (i) **Transfer**: train SisFall → test KFall/UMAFall/FallAllD (generalization thật).
- (ii) **Within-dataset LSO** mỗi bộ (mô hình có ổn định khi train lại).
- Output: **T6** Acc/Fall-Recall/Macro-F1/Trans-F1 × dataset × kịch bản (mean±std).
- Phụ thuộc: D-B1, D-A3.

## Track C — Năng lượng (⭐ MẢNH KHÓA — biện minh chọn v30_optimize, M1)

**D-C1 — Dựng rig đo công suất** ⭐ (M)
- Mục tiêu: đo dòng/điện năng tin cậy, tách được từng trạng thái.
- Lựa chọn: **INA226** (I2C, 16-bit, high-side) + **MCU logger riêng** đọc INA226 (không để DUT tự đo
  nguồn của chính nó). *Khuyến nghị mạnh nếu có: Nordic PPK II hoặc Otii Arc* — reviewer tin hơn, có
  sẵn sampling µs + tách baseline. Ghi rõ Vsupply, Rshunt, tần số lấy mẫu.
- Output: mô tả rig + ảnh sơ đồ (cho Methodology) + script log dòng.

**D-C2 — Firmware "benchmark mode" với GPIO markers** ⭐ (M)
- Mục tiêu: tách 4 pha năng lượng bằng cạnh GPIO đánh dấu trên power trace.
- Pha: (a) **idle/light-sleep**; (b) **sampling-only** (PCNT 100 Hz, không inference); (c)
  **inference loop-invoke**: nạp K window vào RAM, invoke interpreter M lần (M≥1000) đo cửa sổ ổn định;
  (d) **4G-TX burst** (một cảnh báo MQTT/TLS).
- Output: firmware benchmark (ESP) + log thời điểm marker.
- Phụ thuộc: D-A4.

**D-C3 — Tính năng lượng & thời lượng pin (protocol INA219 loop-invoke)** ⭐ (S)
- Mục tiêu: các con số vào bảng T7 + Pareto.
- **Phương pháp:** loop-invoke M≥1000 lần trên window nạp sẵn RAM (pha active kéo dài giây → bù
  bandwidth thấp của INA219); tích phân P=V·I trên cửa sổ steady-state, chia M.
  `E_per_inf = (P̄_loop − P̄_baseline)·T_window / M` với T_window cắt bằng **GPIO marker** bao đúng M invoke.
- **Điều kiện bắt buộc:** khóa clock 240 MHz (tắt DVFS/light-sleep trong lúc đo) · cô lập vòng lặp
  (không I2C sensor/Serial/4G) · bỏ warm-up · INA219 cấu hình dải hẹp (~±400 mA, LSB ~0.05 mA) +
  averaging 64–128 · logger riêng đọc INA219 (không để DUT tự đo) · ≥3–5 lần → **mean±std**.
- **Báo cả hai:** *marginal µJ/inference* (trừ baseline — so model công bằng) và *total power* (mô hình pin).
- Lặp cho **mỗi ứng viên** {v30, v31, v30_optimize, v30_resnet1d, v30_tcn_opt, v30_tcn}. Đo light-sleep,
  sampling, 4G-TX ở pha **riêng**. Ghép duty-cycle → **mWh/ngày** + **giờ pin** theo mAh thật.
- *Nâng độ tin cậy (tùy chọn):* cross-check 1–2 điểm bằng Nordic PPK II/Otii/Joulescope để đối chứng INA219.
- Output: **T7** (mA idle/sample/infer/TX; µJ/inf; mWh/ngày; giờ pin) + **F6 Energy–Accuracy–Latency
  Pareto** (figure chủ đạo).
- Phụ thuộc: D-C1, D-C2.

**D-C4 — Lập luận chọn model từ Pareto** ⭐ (S)
- Mục tiêu: câu chốt M1. So `v30_optimize` vs `v30_tcn_opt`: +0.2% acc nhưng ~12× t_inf ⇒ định lượng
  chênh mWh/ngày & giờ pin mất đi. Chỉ ra v30_optimize nằm trên frontier accuracy–energy.
- Output: đoạn Discussion + annotate trên F6.
- Phụ thuộc: D-C3, D-B2 (accuracy) .

## Track D — Đánh giá thực tế (streaming, event-level, FPR, PR/ROC)

**D-D1 — Bộ đánh giá event-level** ⭐ (M)
- Mục tiêu: thoát "oracle windowing" (M3). Định nghĩa fall-event, cửa sổ khớp, tiêu chí TP/FP/FN theo thời gian.
- Output: script eval event-level tái dùng cho SisFall & pilot.

**D-D2 — Streaming eval trên bản ghi nguyên gốc** ⭐ (M)
- Bước: sliding-window liên tục trên SisFall gốc (chưa cắt) → event-level sens/spec + **false-alarm/giờ**;
  đo **detection-to-alert latency** (window + FSM 4 s) tách khỏi inference latency (M5).
- Output: bảng streaming + phân phối độ trễ.
- Phụ thuộc: D-D1, D-A4.

**D-D3 — Young/elderly breakdown** ⭐ (S)
- Mục tiêu: minh bạch M2. Tách mọi chỉ số theo SA (young) / SE (elderly); nêu rõ giới hạn dữ liệu ngã
  người già (0/375) + diễn giải (học chữ ký va chạm tổng quát; elderly ADL để test false-alarm).
- Output: **T9** + đoạn Limitations.
- Phụ thuộc: D-A3.

**D-D4 — PR/ROC/AUC lớp Fall + chọn ngưỡng** (S)
- Output: **F8** PR+ROC, bảng ngưỡng theo trade-off recall–FPR.
- Phụ thuộc: D-A3.

**D-D5 — Baselines cùng protocol** (M)
- Mục tiêu: so sánh công bằng (Minor). Chạy dưới cùng LSO: **threshold/SVM-magnitude** (đối thủ thực
  của deployed system) + feature-ML (RF/SVM) + 1D-CNN thuần + CNN-LSTM + TCN (từ bảng version).
- Output: cột baseline trong T2 + **McNemar** v30_optimize vs từng baseline.
- Phụ thuộc: D-A3.

## Track E — Co-design evidence & cross-platform (H1, M4, M8)

**D-E1 — Ablation ESP-NN OFF vs ON** ⭐ (M)
- Bước: build TFLM với ESP-NN tắt (reference kernels) vs bật; đo latency **cùng v30_optimize** +
  **một model non-friendly** (có SE/sigmoid hoặc dilated) để lộ op rơi về reference kernel.
- Output: **T5** (per-op & end-to-end ON/OFF), input củng cố H1.
- Phụ thuộc: D-A4.

**D-E2 — Bảng ánh xạ operator ESP-NN ↔ CMSIS-NN** (S)
- Mục tiêu: lập luận cơ chế cho generalization (cả hai accelerate depthwise/pointwise/FC/pool; đều
  không accelerate reshape tùy ý/sigmoid).
- Output: một phần **T10**.

**D-E3 — Port ARM Cortex-M + CMSIS-NN, đo thật** ⭐ (L)
- Mục tiêu: kiểm chứng **H1 lặp lại** trên nền khác (M8). Board gợi ý: STM32H7/F7 (Nucleo) hoặc
  nRF52840 / RP2040; TFLM + CMSIS-NN, cùng `.tflite` INT8.
- Bước: đo latency (+energy nếu rig cho phép) cho vài phiên bản; vẽ lại latency-vs-op-coverage trên ARM.
- Output: **F9** ESP vs ARM replication + phần **T10** (latency ARM).
- Phụ thuộc: D-A4, (D-C1 nếu đo energy ARM).

## Track F — Pilot đeo thật (H3-population, M7, FPR thực địa)

**D-F1 — Chuẩn bị đạo đức & giao thức** (S) — IRB/consent, kịch bản ADL + ngã có kiểm soát trên đệm.
**D-F2 — Thu dữ liệu** (M) — 3–8 người, đeo thắt lưng, MPU6050 100 Hz; log raw + nhãn thời gian.
**D-F3 — Phân tích** ⭐ (M) — FPR/giờ, sens/spec thực địa; **khớp phân phối tín hiệu MPU6050 vs
  SisFall** (sim-to-real, M7). Output: **T8** + F sim-to-real. Phụ thuộc: D-D1.

## Track G — Làm sạch & thống kê xuyên suốt

**D-G1 — Thống nhất số liệu mâu thuẫn** (S): 95.33 vs 95.40 (ghi rõ Float32/PC vs INT8/device, cùng
test set) · size 25 vs 55.8 KB · gyro ±500 vs ±2000 · sampling 100/200 Hz.
**D-G2 — Gói thống kê** (S): mean±std, CI 95%, McNemar — áp cho mọi bảng.
**D-G3 — Repo tái lập** (M): script + `.tflite` + firmware (ESP & ARM) + số liệu thô + "Data & Code
Availability".

---

## Critical path & thứ tự đề xuất

```
D-A1 ─┐
D-A3 ─┼─► D-A4 ─┬─► D-C2 ─► D-C3 ─► D-C4 (chốt M1) ⭐
      │        ├─► D-E1 (ESP-NN on/off)
      │        └─► D-E3 (ARM port)          [L, khởi động sớm vì lead-time board]
D-B1 ─► D-B2 (cross-dataset accuracy) ──────► feed D-C4
D-D1 ─► D-D2 (streaming) / D-D3 / D-D4 / D-D5
D-C1 (rig) ── song song, làm sớm ──► D-C2
D-F1 ─► D-F2 ─► D-F3   [pilot: bắt đầu IRB/lịch NGAY vì phụ thuộc con người]
D-G* xuyên suốt
```

**Làm sớm nhất (lead-time dài / mở khóa nhiều thứ):** D-A1, D-A3/A4, D-C1 (rig), đặt mua **board ARM**,
khởi động **IRB + lịch pilot**. Khối energy (D-C2→C4) là mảnh chốt luận đề — ưu tiên sau khi có A4.

---

## Deliverables số liệu (đầu vào cho lúc viết Results)
`ops_profile.csv` · `runs_metrics.csv` · thư mục `.tflite` INT8 versioned · **T5** ESP-NN on/off ·
**T6** cross-dataset · **T7** energy + giờ pin · **T8** pilot FPR · **T9** young/elderly · **T10**
ESP↔ARM/CMSIS-NN · **F6** Energy–Acc–Latency Pareto · **F8** PR/ROC · **F9** ESP vs ARM.

## Verification — coi là "số liệu xịn, đủ Q1" khi:
- [ ] **F6 Energy Pareto** + **D-C4** biện minh dứt khoát việc chọn v30_optimize (định lượng mWh/ngày, giờ pin) — bịt M1.
- [ ] H1: latency-vs-MACs-vs-opcoverage thuyết phục **và lặp lại trên ARM** (D-E3) — bịt M8.
- [ ] Streaming/event-level + **FPR/giờ**, tách inference vs detection-to-alert — bịt M3/M5/M6.
- [ ] ≥2 dataset ngoài SisFall (D-B2); young/elderly breakdown trung thực (D-D3) — bịt M2.
- [ ] ESP-NN on/off (D-E1); pilot MPU6050 khớp phân phối (D-F3) — bịt M4/M7.
- [ ] Multi-seed + CI + McNemar; baseline threshold/feature-ML cùng protocol; mâu thuẫn số liệu đã thống nhất.
