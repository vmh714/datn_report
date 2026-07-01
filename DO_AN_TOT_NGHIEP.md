# ĐỒ ÁN TỐT NGHIỆP
> Nguon: `ĐỒ ÁN TỐT NGHIỆP.pdf` — 84 trang


---

## Trang 1

ĐẠI HỌC BÁCH KHOA HÀ NỘI
ĐỒÁN TỐT NGHIỆP
Nghiên cứu và xây dựng hệthống giám sát hành vi người già và phát
hiện té ngã ứng dụng IoT và TinyML
VŨ MẠNH HƯNG
hung.vm225198@sis.hust.edu.vn
Chương trình đào tạo: Kỹthuật máy tính
Giảng viên hướng dẫn:
PGS. TS. Nguyễn Hồng Quang
Chữký GVHD
Khoa:
Kỹthuật máy tính
Trường:
Công nghệThông tin và Truyền thông
HÀ NỘI, 06/2026
Đã ký số ngày 30/06/2026


---

## Trang 2

ĐẠI HỌC BÁCH KHOA HÀ NỘI
ĐỒÁN TỐT NGHIỆP
Nghiên cứu và xây dựng hệthống giám sát hành vi người già và phát
hiện té ngã ứng dụng IoT và TinyML
VŨ MẠNH HƯNG
hung.vm225198@sis.hust.edu.vn
Chương trình đào tạo: Kỹthuật máy tính
Giảng viên hướng dẫn:
PGS. TS. Nguyễn Hồng Quang
Chữký GVHD
Khoa:
Kỹthuật máy tính
Trường:
Công nghệThông tin và Truyền thông
HÀ NỘI, 06/2026


---

## Trang 3

LỜI CẢM ƠN
Lời đầu tiên, em xin gửi lời cảm ơn chân thành và sâu sắc nhất tới PGS. TS. Nguyễn Hồng Quang, người
đã trực tiếp hướng dẫn, dìu dắt và định hướng cho em trong suốt quá trình nghiên cứu và thực hiện đồán
tốt nghiệp này. Nhờcó sựchỉbảo tận tình và những lời khuyên chuyên môn quý báu của Thầy, em đã có thể
vượt qua những khó khăn và hoàn thành tốt đềtài được giao.
Em cũng xin bày tỏlòng biết ơn sâu sắc đến Thầy Nguyễn Đức Tiến, người đã nhiệt tình giúp đỡ, định
hướng và tư vấn chuyên môn cho em trong khâu thiết kếphần cứng cũng như xây dựng kiến trúc hệthống
IoT tổng thể.
Bên cạnh đó, em xin gửi lời tri ân tới Ban lãnh đạo cùng các anh chịđồng nghiệp tại Công ty Cổphần
VTI (VTI Group) đã tạo mọi điều kiện thuận lợi đểem có thểtập trung hoàn thành đồán trong thời gian
thực tập tại công ty.
Đặc biệt, con xin gửi lời tri ân sâu sắc nhất tới bốmẹ, những người đã luôn là hậu phương vững chắc,
vất vảlo toan, không ngừng động viên và ủng hộcon trong suốt 4 năm học đại học. Anh cũng muốn dành
một lời cảm ơn đặc biệt đến người con gái anh yêu vì đã luôn đồng hành, thấu hiểu và san sẻnhững áp lực
cùng anh trong suốt chặng đường học tập cùng với quá trình thực hiện đồán tốt nghiệp này.
Bên cạnh đó, mình xin gửi lời cảm ơn chân thành đến những người bạn thân thiết đã không quản ngại
vất vả, trực tiếp giúp đỡmình trong quá trình thu thập bộdữliệu (dataset) cũng như luôn sát cánh và hỗtrợ
trong suốt quá trình hoàn thiện đềtài.
Tuy đã nỗlực hết mình, nhưng do hạn chếvềmặt kiến thức và thời gian, đồán chắc chắn không tránh
khỏi những thiếu sót. Em rất mong nhận được sựquan tâm, đánh giá và góp ý của các thầy cô trong Hội
đồng bảo vệđểđồán được hoàn thiện hơn.


---

## Trang 4

TÓM TẮT NỘI DUNG ĐỒÁN
Internet vạn vật trong y tế(IoMT) đang tạo ra những bước tiến lớn trong việc chăm sóc sức khỏe và giám
sát người cao tuổi tại các viện dưỡng lão. Tuy nhiên, các giải pháp phát hiện té ngã hiện tại thường gặp hạn
chếlớn: hệthống dựa trên điện toán đám mây (Cloud) gây ra độtrễcảnh báo và rủi ro quyền riêng tư, trong
khi các thiết bịnhúng truyền thống sửdụng thuật toán máy học đơn giản lại kém chính xác và dễbỏsót
các chuyển động động học phức tạp (như trạng thái chuyển tiếp tư thế). Nhằm lấp đầy khoảng trống này,
đồán đềxuất giải pháp "Nghiên cứu và xây dựng hệthống giám sát hành vi người già và phát hiện té ngã
ứng dụng IoT và TinyML". Hệthống sửdụng thiết bịđeo tích hợp trí tuệnhân tạo tại biên (Edge AI) dựa
trên kiến trúc Mạng Nơ-ron Tích chập (CNN) được tối ưu hóa đặc biệt cho vi điều khiển ESP32, kết hợp
kỹthuật lấy mẫu đếm xung (PCNT) nhằm tiết kiệm năng lượng. Đóng góp cốt lõi của nghiên cứu là việc
định nghĩa lại nhãn động học (Trans/Idle) và tối ưu hóa kiến trúc mạng đểkhắc phục giới hạn lọt bộnhớ
đệm 64KB của phần cứng, cho phép duy trì thông tin chuỗi thời gian mà không cần tới các mạng hồi quy
nặng nề. Kết quảthực nghiệm trên bộdữliệu chuẩn SisFall cho thấy mô hình đềxuất (v30_optimize) đạt độ
chính xác (Accuracy) lên tới 95,40%, độnhạy phát hiện té ngã (Fall Recall) đạt 97,50%, với thời gian suy
luận siêu tốc chỉmất 11,20 ms trực tiếp trên vi điều khiển. Hệthống kết nối với nền tảng Web Dashboard
thời gian thực sửdụng đa cơ sởdữliệu (PostgreSQL và InfluxDB) qua giao thức MQTT bảo mật TLS, tạo
thành một hệsinh thái khép kín giúp phản hồi y tếkhẩn cấp tức thời, giảm tải áp lực cho nhân viên y tếvà
có khảnăng mởrộng quy mô lớn.
Sinh viên thực hiện
(Ký và ghi rõ họtên)


---

## Trang 5

MỤC LỤC
CHƯƠNG 1. GIỚI THIỆU ĐỀTÀI .......................................................................
1
1.1 Đặt vấn đề..................................................................................................
1
1.2 Các giải pháp hiện tại và hạn chế.........................................................................
1
1.2.1 Hiện trạng các sản phẩm thương mại...........................................................
1
1.2.2 Các phương pháp nghiên cứu giải quyết bài toán ..............................................
3
1.3 Mục tiêu và định hướng giải pháp ........................................................................
7
1.4 Đóng góp của đồán .......................................................................................
8
1.5 Bốcục đồán ...............................................................................................
8
CHƯƠNG 2. CƠ SỞLÝ THUYẾT VÀ CÔNG NGHỆSỬDỤNG..................................... 10
2.1 Cơ sởlý thuyết vềNhận diện hành vi và Phát hiện té ngã dựa trên cảm biến quán tính (IMU) ....... 10
2.1.1 Cơ chếnhận diện hành vi con người (HAR) ................................................... 10
2.1.2 Cơ chếphát hiện té ngã (Fall Detection) ....................................................... 11
2.1.3 Bộdữliệu thực nghiệm SisFall ................................................................. 12
2.2 Nhóm Công nghệPhần cứng và Giao thức mạng........................................................ 12
2.2.1 Vi điều khiển ESP32-S3 (Module Seeed Studio XIAO)....................................... 12
2.2.2 Cảm biến quán tính MPU6050.................................................................. 14
2.2.3 Module truyền thông 4G LTE A7680C ........................................................ 14
2.2.4 Giao thức truyền thông PPPoS.................................................................. 15
2.2.5 Giao thức truyền tải MQTT ..................................................................... 15
2.3 Công nghệNhận diện hành vi (TinyML)................................................................. 16
2.3.1 Mạng nơ-ron tích chập tách kênh 1 chiều (Depthwise Separable 1D CNN).................. 16
2.3.2 Kỹthuật lượng tửhóa (Quantization) cho TinyML ............................................ 16
2.4 Nền tảng Phần mềm và Hệthống......................................................................... 17
2.4.1 Bộlọc Kalman 1D cho Dung hợp Cảm biến (Sensor Fusion)................................. 17
2.4.2 Nền tảng phát triển Nhúng ESP-IDF và FreeRTOS ........................................... 17
2.4.3 Nền tảng triển khai mô hình học máy (TinyML Pipeline)..................................... 17
2.4.4 Thư viện suy luận nhúng: TensorFlow Lite Micro và ESP-NN ............................... 18
2.4.5 Các thông sốđặc trưng khi triển khai mô hình TinyML lên vi điều khiển ................... 19


---

## Trang 6

2.5 Hệquản trịCơ sởdữliệu.................................................................................. 20
2.5.1 Cơ sởdữliệu chuỗi thời gian InfluxDB ........................................................ 20
2.5.2 Cơ sởdữliệu quan hệPostgreSQL ............................................................. 21
2.6 Nền tảng Web và Dịch vụBackend....................................................................... 21
2.6.1 Framework phát triển Backend FastAPI........................................................ 21
2.6.2 Framework Frontend Next.js và Tailwind CSS ................................................ 21
CHƯƠNG 3. PHƯƠNG PHÁP VÀ GIẢI PHÁP ĐỀXUẤT ............................................ 23
3.1 Quy Trình Tiền XửLý và Phân Tích Phân BốDữLiệu ................................................. 23
3.1.1 Tiền xửlý và chuẩn hóa đầu vào................................................................ 23
3.1.2 Phân tích phân bốdữliệu và lựa chọn ngưỡng cắt............................................. 23
3.1.3 Kỹthuật trích xuất cửa sổvà tăng cường dữliệu............................................... 25
3.2 Chiến Lược Thiết KếNhãn Phân Loại Nhằm Giảm Thiểu Cảnh Báo Sai.............................. 25
3.2.1 Bài toán .......................................................................................... 25
3.2.2 Giải pháp......................................................................................... 26
3.2.3 Kết quả........................................................................................... 26
3.3 Chiến Lược Kiểm Soát ĐộTin Cậy và Tần Suất Cảnh Báo Ngã........................................ 26
3.3.1 Cơ chếxác nhận ngã hai pha (Post-Impact Confirmation) .................................... 26
3.3.2 Điều Chỉnh Ngưỡng Kích Hoạt và Kiểm Soát Tần Suất Cảnh Báo ........................... 27
3.4 Tiến Trình Tối Ưu Hóa Kiến Trúc Mô Hình Học Sâu Tương Thích TinyML .......................... 28
3.4.1 Bài toán .......................................................................................... 28
3.4.2 Giải pháp......................................................................................... 28
3.4.3 Kết quả........................................................................................... 29
3.5 Phương Pháp Lấy Mẫu IMU Chính Xác SửDụng Ngắt Phần Cứng PCNT ............................ 31
3.5.1 Bài toán .......................................................................................... 31
3.5.2 Giải pháp......................................................................................... 31
3.5.3 Kết quảvà Định hướng phát triển............................................................... 32
3.6 Đếm Bước Chân Thông Minh Gating Theo Nhận Dạng Hoạt Động ................................... 32
3.6.1 Bài toán .......................................................................................... 32
3.6.2 Giải pháp......................................................................................... 32
3.6.3 Lý do và Kết quả................................................................................. 33
ii


---

## Trang 7

3.7 Giải Pháp Đảm Bảo Toàn Vẹn DữLiệu Thu Thập Qua Lựa Chọn Đường Truyền..................... 34
3.7.1 Bài toán .......................................................................................... 34
3.7.2 Giải pháp......................................................................................... 34
3.7.3 Kết quảvà Định hướng phát triển............................................................... 35
CHƯƠNG 4. PHÂN TÍCH VÀ THIẾT KẾHỆTHỐNG ............................................... 36
4.1 Tổng quan chức năng ...................................................................................... 36
4.1.1 Biểu đồuse case tổng quát ...................................................................... 36
4.1.2 Biểu đồuse case phân rã Giám sát thời gian thực ............................................. 37
4.1.3 Biểu đồuse case phân rã Xửlý cảnh báo té ngã ............................................... 37
4.1.4 Biểu đồuse case phân rã Gán thiết bịcho bệnh nhân ......................................... 38
4.1.5 Biểu đồuse case phân rã Xem thống kê vận động ............................................. 39
4.1.6 Quy trình nghiệp vụ(Activity Diagram) ....................................................... 39
4.1.7 Tựđộng đăng ký thiết bị(Auto-provisioning).................................................. 40
4.2 Đặc tảchức năng .......................................................................................... 42
4.2.1 Đặc tảUse case: Giám sát thời gian thực....................................................... 43
4.2.2 Đặc tảUse case: Xửlý cảnh báo té ngã ........................................................ 43
4.2.3 Đặc tảUse case: Gán thiết bịcho bệnh nhân................................................... 43
4.2.4 Đặc tảUse case: Xem thống kê vận động ...................................................... 44
4.2.5 Đặc tảUse case: Tựđộng đăng ký thiết bị(Auto-provisioning) .............................. 44
4.3 Yêu cầu phi chức năng .................................................................................... 44
4.4 Phân tích và thiết kếhệthống............................................................................. 45
4.4.1 Kiến trúc tổng thểhệthống ..................................................................... 45
4.4.2 Kiến trúc phần mềm Firmware ................................................................. 45
4.4.3 Thiết kếcơ sởdữliệu............................................................................ 47
4.4.4 Thiết kếgiao thức truyền thông................................................................. 49
4.4.5 Thiết kếFSM phụxác nhận ngã trong svc_ai ............................................... 49
4.4.6 Tối ưu hóa Firmware và Độổn định mạng ..................................................... 50
4.4.7 Tựđộng xửlý cảnh báo tồn đọng (Auto-resolve) .............................................. 50
4.4.8 Tối ưu hóa Thiết kếPhần cứng và Giao tiếp Ngoại vi ......................................... 50
iii


---

## Trang 8

CHƯƠNG 5. TRIỂN KHAI VÀ ĐÁNH GIÁ THỰC NGHIỆM........................................ 52
5.1 Triển khai và Xây dựng ứng dụng ........................................................................ 52
5.1.1 Triển khai thuật toán xửlý tín hiệu IMU (Bộlọc Kalman).................................... 52
5.1.2 Phân tích kiến trúc phần cứng ESP32-S3 định hướng thiết kếmô hình ...................... 53
5.1.3 Huấn luyện và triển khai mô hình học máy (TinyML)......................................... 53
5.1.4 Quá trình phát triển lặp và tối ưu kiến trúc hướng phần cứng................................. 55
5.1.5 Mô hình triển khai đềxuất cuối cùng (v30_optimize)......................................... 56
5.1.6 Triển khai hạtầng giao tiếp MQTT............................................................. 56
5.1.7 Triển khai phần mềm máy chủ(Backend)...................................................... 57
5.1.8 Triển khai giao diện giám sát (Frontend)....................................................... 58
5.2 Kết quảđạt được và Kiểm thử............................................................................ 63
5.2.1 Đánh giá hiệu năng mô hình phân loại ......................................................... 63
5.2.2 Đánh giá hiệu năng suy luận trên vi điều khiển................................................ 65
5.2.3 Kiểm thửtích hợp hệthống đầu cuối ........................................................... 68
CHƯƠNG 6. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN.................................................. 69
6.1 Kết luận .................................................................................................... 69
6.2 Hướng phát triển........................................................................................... 69


---

## Trang 9

DANH MỤC HÌNH VẼ
Hình 1.1
Các sản phẩm thiết bịđeo phát hiện té ngã thương mại tiêu biểu, phân loại theo đối
tượng sửdụng và cơ chếbảo vệ.
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
Hình 2.1
Tín hiệu gia tốc đặc trưng của các hành vi Đứng yên (Idle), Đi bộ(Walk) và Chạy
(Run) trong cửa sổ2 giây. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
Hình 2.2
Bốn giai đoạn động học của một sựkiện té ngã (Fall) điển hình trên tín hiệu gia tốc:
Pre-fall (Trước khi ngã), Free-fall (Rơi tựdo), Impact (Va chạm) và Post-fall (Sau khi ngã).
12
Hình 2.3
Mặt trước và mặt sau của module Seeed Studio XIAO ESP32S3 (chú ý 2 chân BAT
cấp nguồn pin ởmặt sau) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
Hình 2.4
Cảm biến quán tính MPU6050 đo gia tốc và vận tốc góc . . . . . . . . . . . . . . . .
14
Hình 2.5
Module truyền thông mạng di động 4G LTE A7680C (Mặt trước và mặt sau) . . . . .
15
Hình 2.6
Kiến trúc giao thức PPPoS ánh xạmạng 4G thành giao diện mạng trên ESP32S3
. .
15
Hình 2.7
Mô hình giao tiếp Publish/Subscribe của MQTT trong hệthống giám sát . . . . . . .
16
Hình 2.8
Giao diện tài liệu API Swagger tựsinh từFastAPI . . . . . . . . . . . . . . . . . . .
21
Hình 3.1
Phân bốcác trục gia tốc của bộdữliệu SisFall và ngưỡng cắt tối ưu. . . . . . . . . .
24
Hình 3.2
Phân bốcác trục vận tốc góc của bộdữliệu SisFall và ngưỡng cắt tối ưu. . . . . . . .
25
Hình 3.3
Minh họa sựphân rã tích chập tách kênh (Depthwise Separable 1D CNN)
. . . . . .
29
Hình 3.4
Sơ đồkhối kiến trúc mạng nơ-ron v30_optimize (tổng tham số: 26.629)
. . . . . . .
30
Hình 3.5
Pipeline đếm bước chân gating theo nhận dạng hoạt động HAR (lib_pedometer
trong svc_imu) — D-010 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
33
Hình 3.6
Luồng tựnhận diện đường truyền theo hoạt động bus UART — D-026. . . . . . . . .
35
Hình 4.1
Biểu đồuse case tổng quát của hệthống . . . . . . . . . . . . . . . . . . . . . . . .
36
Hình 4.2
Biểu đồuse case phân rã "Giám sát thời gian thực"
. . . . . . . . . . . . . . . . . .
37
Hình 4.3
Biểu đồuse case phân rã "Xửlý cảnh báo té ngã" . . . . . . . . . . . . . . . . . . .
38
Hình 4.4
Biểu đồuse case phân rã "Gán thiết bịcho bệnh nhân"
. . . . . . . . . . . . . . . .
38
Hình 4.5
Biểu đồuse case phân rã "Xem thống kê vận động" . . . . . . . . . . . . . . . . . .
39
Hình 4.6
Biểu đồhoạt động (Activity Diagram) luồng xửlý sựcốté ngã khẩn cấp . . . . . . .
40
Hình 4.7
Biểu đồuse case phân rã "Tựđộng đăng ký thiết bị" . . . . . . . . . . . . . . . . . .
41
Hình 4.8
Biểu đồhoạt động luồng tựđộng đăng ký thiết bị(Auto-provisioning) . . . . . . . .
42
Hình 4.9
Sơ đồKiến trúc Tổng thểHệthống IoT Eldercare . . . . . . . . . . . . . . . . . . .
45
Hình 4.10 Sơ đồChuyển trạng thái (FSM) của Firmware trên thiết bịESP32 (FSM phụxác nhận
ngã của svc_ai được trình bày riêng tại Hình 4.12)
. . . . . . . . . . . . . . . . . . . .
47
Hình 4.11 Sơ đồThực thể- Mối quan hệ(ERD) của cơ sởdữliệu PostgreSQL
. . . . . . . . .
48
Hình 4.12 Sơ đồFSM phụxác nhận ngã hậu va chạm trong svc_ai (D-021) . . . . . . . . . .
49
Hình 5.1
Mạch phần cứng sau khi lắp ráp hoàn thiện
. . . . . . . . . . . . . . . . . . . . . .
52
Hình 5.2
Thiết bịgiám sát đeo trên người thực tế
. . . . . . . . . . . . . . . . . . . . . . . .
52
Hình 5.3
Sơ đồTuần tựcủa Cơ chếĐồng bộcảnh báo lai (Hybrid Alert Sync) trên Frontend
.
59
Hình 5.4
Giao diện bảng điều khiển trung tâm (Dashboard) giám sát đa thiết bị
. . . . . . . .
59
Hình 5.5
Lớp phủcảnh báo ngã khẩn cấp toàn màn hình với độtin cậy của AI . . . . . . . . .
60
Hình 5.6
Lịch sửtrạng thái và nhật ký hoạt động . . . . . . . . . . . . . . . . . . . . . . . . .
60
Hình 5.7
Biểu đồsinh hiệu (Pin và sóng 4G) . . . . . . . . . . . . . . . . . . . . . . . . . . .
61
Hình 5.8
Quản lý thiết bịđăng ký tựđộng (Auto-provision) . . . . . . . . . . . . . . . . . . .
61
Hình 5.9
Quản lý hồsơ bệnh nhân . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
62
Hình 5.10 Lịch sửcảnh báo toàn hệthống . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
62
v


---

## Trang 10

Hình 5.11 Thu thập dữliệu IMU thời gian thực . . . . . . . . . . . . . . . . . . . . . . . . . .
63
Hình 5.12 Tiến trình tối ưu hóa hiệu năng các phiên bản mô hình trên tập kiểm tra độc lập . . .
64
Hình 5.13 Ma trận nhầm lẫn (Confusion Matrix) của mô hình v30_optimize trên tập kiểm tra
độc lập . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
65
Hình 5.14 Sơ đồđánh đổi hiệu năng, tốc độsuy luận và kích thước giữa các kiến trúc trên vi điều
khiển ESP32-S3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
66
vi


---

## Trang 11

DANH MỤC BẢNG BIỂU
Bảng 1.1
Tổng hợp các nghiên cứu vềthuật toán nhận diện té ngã . . . . . . . . . . . . . . . .
6
Bảng 1.2
Tổng hợp các nghiên cứu đã triển khai trên Vi điều khiển (MCU) . . . . . . . . . . .
7
Bảng 2.1
Các toán tửmạng nơ-ron được ESP-NN tăng tốc trên ESP32-S3 (INT8) . . . . . . .
19
Bảng 3.1
Ánh xạnhãn phân loại và mã hoạt động SisFall . . . . . . . . . . . . . . . . . . . .
26
Bảng 3.2
Hệsốtăng tốc của các toán tửESP-NN trong kiến trúc CNN tách kênh . . . . . . . .
30
Bảng 3.3
Kết quảkiểm định chéo dân số(KFold v6) của v30_optimize trên tập SisFall
. . . .
31
Bảng 3.4
Đối chiếu hai tuyến truyền cho bài toán thu luồng dữliệu IMU 100 Hz liên tục. . . .
34
Bảng 4.1
Đặc tảUse case: Giám sát thời gian thực . . . . . . . . . . . . . . . . . . . . . . . .
43
Bảng 4.2
Đặc tảUse case: Xửlý cảnh báo té ngã (Resolve Alert) . . . . . . . . . . . . . . . .
43
Bảng 4.3
Đặc tảUse case: Gán thiết bịcho bệnh nhân (Assign Device) . . . . . . . . . . . . .
43
Bảng 4.4
Đặc tảUse case: Xem thống kê vận động
. . . . . . . . . . . . . . . . . . . . . . .
44
Bảng 4.5
Đặc tảUse case: Tựđộng đăng ký thiết bị(Auto-provisioning) . . . . . . . . . . . .
44
Bảng 4.6
Cấu trúc Measurement của cơ sởdữliệu chuỗi thời gian InfluxDB . . . . . . . . . .
48
Bảng 5.1
Các cột mốc tiến hóa kiến trúc mô hình phát hiện té ngã trên ESP32-S3 . . . . . . .
56
Bảng 5.2
So sánh hiệu năng các phiên bản mô hình trên tập kiểm tra độc lập (LSO) . . . . . .
64
Bảng 5.3
So sánh hiệu năng suy luận các họkiến trúc trên ESP32-S3 (INT8, CPU 240 MHz,
bật tối ưu ESP-NN) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
66
Bảng 5.4
Đối chiếu tài nguyên phần cứng: phiên bản v25 cũ và phương án đềxuất v30_optimize
(cảhai đều bật ESP-NN) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
67
Bảng 5.5
Ma trận kịch bản kiểm thửcơ chếxác nhận ngã hai pha . . . . . . . . . . . . . . . .
68
vii


---

## Trang 12

DANH MỤC THUẬT NGỮVÀ TỪVIẾT TẮT
Thuật ngữ
Ý nghĩa
ADC
Bộchuyển đổi tương tự–số(Analog-to-Digital
Converter)
ADL
Hoạt động sinh hoạt hàng ngày (Activities of Daily
Living)
AI
Trí tuệnhân tạo (Artificial Intelligence)
ANN
Mạng nơ-ron nhân tạo (Artificial Neural Network)
API
Giao diện lập trình ứng dụng (Application
Programming Interface)
BN
Chuẩn hóa theo lô (Batch Normalization)
CNN
Mạng nơ-ron tích chập (Convolutional Neural
Network)
CRUD
Bốn thao tác dữliệu Tạo–Đọc–Sửa–Xóa (Create,
Read, Update, Delete)
ECG
Điện tâm đồ(Electrocardiogram)
ERD
Sơ đồthực thể–liên kết (Entity-Relationship
Diagram)
ESP-IDF
Bộcông cụphát triển IoT của Espressif (Espressif
IoT Development Framework)
ESP-NN
Thư viện hàm mạng nơ-ron tăng tốc của Espressif
(Espressif Neural Network)
FIFO
Cơ chếhàng đợi vào trước ra trước (First In, First
Out)
FSM
Máy trạng thái hữu hạn (Finite State Machine)
GAP
Gộp trung bình toàn cục (Global Average Pooling)
GMP
Gộp cực đại toàn cục (Global Max Pooling)
GPIO
Chân vào/ra đa dụng (General-Purpose
Input/Output)
GPS
Hệthống định vịtoàn cầu (Global Positioning
System)
HAR
Nhận dạng hoạt động người (Human Activity
Recognition)
HDLC
Điều khiển liên kết dữliệu mức cao (High-Level
Data Link Control)
HTTP
Giao thức truyền siêu văn bản (HyperText Transfer
Protocol)
I2C
Chuẩn giao tiếp liên mạch tích hợp
(Inter-Integrated Circuit)
IMU
Đơn vịđo lường quán tính (Inertial Measurement
Unit)
INT8
Sốnguyên 8-bit (8-bit Integer)
IoMT
Internet vạn vật trong y tế(Internet of Medical
Things)
IoT
Internet vạn vật (Internet of Things)
viii


---

## Trang 13

Thuật ngữ
Ý nghĩa
ISR
Trình phục vụngắt (Interrupt Service Routine)
JWT
Mã thông báo web dạng JSON (JSON Web Token)
KD
Chưng cất tri thức (Knowledge Distillation)
LSO
Phương pháp đánh giá tách đối tượng
(Leave-Subjects-Out)
LSTM
Mạng bộnhớdài–ngắn hạn (Long Short-Term
Memory)
LTE
Công nghệdi động tiến hóa dài hạn (Long-Term
Evolution)
LTE-M
Chuẩn LTE công suất thấp cho thiết bịmáy móc
(LTE-Machine / Cat-M1)
MCU
Vi điều khiển (Microcontroller Unit)
ML
Học máy (Machine Learning)
MQTT
Giao thức truyền tin theo hàng đợi (Message
Queuing Telemetry Transport)
NB-IoT
IoT băng hẹp (Narrowband IoT)
ORM
Ánh xạđối tượng–quan hệ(Object-Relational
Mapping)
PCB
Bảng mạch in (Printed Circuit Board)
PCNT
Ngoại vi bộđếm xung (Pulse Counter)
PPG
Phép đo thểtích mạch bằng quang học
(Photoplethysmography)
PPPoS
Giao thức điểm–điểm trên cổng nối tiếp
(Point-to-Point Protocol over Serial)
PSRAM
Bộnhớgiảtĩnh (Pseudo-Static Random-Access
Memory)
PTQ
Lượng tửhóa sau huấn luyện (Post-Training
Quantization)
QoS
Chất lượng dịch vụ(Quality of Service)
RAI
Chỉthịhỗtrợgiải phóng kết nối (Release
Assistance Indication)
ReLU
Đơn vịtuyến tính chỉnh lưu (Rectified Linear Unit)
ResNet
Mạng nơ-ron thặng dư (Residual Network)
REST
Kiến trúc chuyển trạng thái biểu diễn
(Representational State Transfer)
RMS
Căn quân phương (Root Mean Square)
RNN
Mạng nơ-ron hồi quy (Recurrent Neural Network)
RRC
Điều khiển tài nguyên vô tuyến (Radio Resource
Control)
RSSI
Chỉsốcường độtín hiệu thu (Received Signal
Strength Indicator)
RTOS
Hệđiều hành thời gian thực (Real-Time Operating
System)
ix


---

## Trang 14

Thuật ngữ
Ý nghĩa
SE
Khối nén–kích thích (Squeeze-and-Excitation)
SIMD
Một lệnh xửlý nhiều dữliệu (Single Instruction,
Multiple Data)
SPI
Giao tiếp ngoại vi nối tiếp (Serial Peripheral
Interface)
SRAM
Bộnhớtruy cập ngẫu nhiên tĩnh (Static
Random-Access Memory)
SVM
Độlớn véc-tơ tín hiệu gia tốc (Signal Vector
Magnitude)
TCN
Mạng tích chập theo thời gian (Temporal
Convolutional Network)
TFLite
Bộsuy luận học máy gọn nhẹTensorFlow Lite
TFLM
TensorFlow Lite cho vi điều khiển (TensorFlow
Lite for Microcontrollers)
TinyML
Học máy thu nhỏtrên vi điều khiển (Tiny Machine
Learning)
TLS
Giao thức bảo mật tầng truyền tải (Transport Layer
Security)
UART
Bộthu–phát không đồng bộ(Universal
Asynchronous Receiver-Transmitter)
UI
Giao diện người dùng (User Interface)
UML
Ngôn ngữmô hình hóa thống nhất (Unified
Modeling Language)
UUID
Định danh duy nhất toàn cục (Universally Unique
Identifier)
UX
Trải nghiệm người dùng (User Experience)
x


---

## Trang 15

CHƯƠNG 1. GIỚI THIỆU ĐỀTÀI
1.1
Đặt vấn đề
Sựphát triển mạnh mẽcủa Internet vạn vật trong y tế(IoMT) đang tạo ra những bước tiến mang tính
cách mạng trong công tác chăm sóc sức khỏe và theo dõi bệnh nhân. Tại các môi trường yêu cầu sựgiám sát
liên tục như viện dưỡng lão và bệnh viện, việc đảm bảo an toàn cho người cao tuổi và bệnh nhân gặp khó
khăn vềvận động luôn là một thách thức lớn đối với đội ngũ y tế. Đặc biệt, các sựcốté ngã xảy ra ngoài
tầm quan sát của nhân viên nếu không được phát hiện và xửlý kịp thời có thểdẫn đến những hậu quảy
khoa nghiêm trọng, thậm chí đe dọa đến tính mạng. Tuy nhiên, việc bốtrí nhân sựtúc trực 24/7 đểtheo dõi
từng bệnh nhân là điều không khảthi do áp lực vềnguồn nhân lực y tếngày càng gia tăng. Thực trạng này
đòi hỏi một giải pháp công nghệtựđộng hóa có khảnăng giám sát liên tục, phản hồi tức thời và quản lý tập
trung, nhằm giảm thiểu tối đa rủi ro từcác tai nạn không mong muốn.
1.2
Các giải pháp hiện tại và hạn chế
Bài toán phát hiện té ngã tựđộng bằng thiết bịđeo wearable đã được nghiên cứu rộng rãi trong
hơn hai thập kỷqua do tầm quan trọng y tếcấp thiết của nó. Tổchức Y tếThếgiới (WHO) ước tính
khoảng 684.000 ca tửvong mỗi năm liên quan đến té ngã, trong đó người cao tuổi chiếm tỷlệcao nhất
mekruksavanich2024resnet. Điều đặc biệt nghiêm trọng là khoảng 50% người cao tuổi nằm bất động dưới
sàn sau khi ngã quá một giờsẽtửvong trong vòng sáu tháng, bất kểchấn thương trực tiếp có nghiêm trọng
hay không mekruksavanich2024resnet. Điều này đặt ra yêu cầu bắt buộc vềviệc rút ngắn thời gian phát
hiện và can thiệp y tế.
Vềmặt kỹthuật, bài toán phát hiện té ngã được phân chia thành hai pha xửlý chính. Phát hiện trước
va chạm (Pre-Impact Fall Detection — PIFD) nhận diện chuyển động ngã trong khoảng thời gian từkhi bắt
đầu mất thăng bằng đến khi cơ thểchạm đất, thường chỉkéo dài từ100 đến 500 mili giây. Pha này đòi hỏi
suy luận hoàn toàn trên thiết bị(on-device inference) với độtrễcực thấp, không thểdựa vào kết nối đám
mây. Phát hiện sau va chạm (Post-Impact Fall Detection) xác nhận cú ngã đã xảy ra sau khi cơ thểtiếp đất,
thường kết hợp với cơ chếchờphản hồi của người dùng trước khi phát cảnh báo. Pha này có độtrễcho phép
lớn hơn song yêu cầu kết nối mạng đểthông báo đến người giám sát. Đồán này tập trung vào pha thứhai:
phát hiện sau va chạm kết hợp với truyền thông cảnh báo qua 4G LTE đến dashboard y tế.
1.2.1
Hiện trạng các sản phẩm thương mại
Sựcấp thiết của bài toán đã thúc đẩy sựra đời của nhiều sản phẩm thương mại, tập trung vào hai hướng
tiếp cận tương ứng với hai pha phát hiện trên.
Nhóm thiết bịtúi khí bảo vệchủđộng (PIFD). Hướng tiếp cận này tích hợp IMU on-device với cơ
chếbơm túi khí khí nén đểbảo vệcác vùng xương dễgãy trong khoảng thời gian trước khi cơ thểchạm
đất. H¨ovding1 (H¨ovding Sverige AB, Thụy Điển) là vòng đeo cổdành cho người đi xe đạp, tích hợp túi khí
bao phủtoàn bộđầu và cổ; hệthống xửlý dữliệu IMU ởtần số200 Hz ngay trên vi điều khiển nhúng và
kích hoạt túi khí trong vòng 0,1 giây — nhanh hơn phản xạbảo vệtựnhiên của con người. Trong lĩnh vực
thểthao mô-tô, Alpinestars Tech-Air2 (Alpinestars, Ý) là hệthống áo giáp túi khí tích hợp cho người lái xe
máy, phát hiện va chạm và bơm phồng toàn bộvùng vai, ngực và lưng trong khoảng 25 mili giây, sửdụng
thuật toán phân tích IMU nhiều trục chạy hoàn toàn độc lập với điện thoại. Chuyển sang lĩnh vực chăm sóc
người cao tuổi, Helite3 (Pháp) cung cấp hai sản phẩm có định vịkhác nhau: Hip’Air là đai hông túi khí
điện tử, bơm phồng hai túi khí bảo vệkhớp hông trong khoảng 80 mili giây sau khi phát hiện ngã; HipSafe
là phiên bản thụđộng hơn, sửdụng tấm đệm hấp thụlực cơ học tích hợp sẵn trong đai, không cần nguồn
1https://hovding.com
2https://www.alpinestars.com/pages/tech-air
3https://www.helite.com
1


---

## Trang 16

CHƯƠNG 1. GIỚI THIỆU ĐỀTÀI
điện hay thuật toán, phù hợp với người cao tuổi không quen dùng thiết bịđiện tử. TangoBelt4 là đai bụng
chuyên dụng cho người cao tuổi, kết hợp cảhai cơ chếtrong cùng một nền tảng phần cứng: phiên bản túi
khí bơm phồng bảo vệhông khi phát hiện ngã (tương tựHip’Air), trong khi phiên bản kết nối gửi cảnh báo
tức thì đến người thân hoặc nhân viên chăm sóc qua Bluetooth Low Energy (BLE) và ứng dụng di động đi
kèm. Điểm nổi bật là khảnăng tích hợp cảbảo vệvật lý lẫn luồng thông báo xã hội (social alerting) trên
cùng một thiết bị. Hạn chếcủa phiên bản kết nối là phụthuộc vào điện thoại trung gian và vùng phủBLE
(khoảng 10 mét), chưa đáp ứng được môi trường cơ sởđiều dưỡng quy mô lớn với nhiều bệnh nhân phân
tán trên nhiều phòng.
Nhóm đồng hồthông minh (Post-Impact FD). Apple Watch Series 4 trởlên5 tích hợp tính năng Fall
Detection sửdụng gia tốc kếvà con quay hồi chuyển kết hợp với mô hình phân loại học máy chạy hoàn
toàn trên thiết bị(on-device). Khi phát hiện cú ngã mạnh, đồng hồhiển thịthông báo yêu cầu xác nhận; nếu
người dùng không phản hồi trong vòng 60 giây, hệthống tựđộng gọi cấp cứu và gửi vịtrí GPS đến danh
sách liên lạc khẩn cấp. Samsung Galaxy Watch cung cấp tính năng tương đương. Nhóm sản phẩm này phù
hợp cho người dùng cá nhân di động nhưng không đáp ứng nhu cầu của cơ sởy tếvì thiếu dashboard giám
sát tập trung đa bệnh nhân, không lưu trữlịch sửvận động có cấu trúc và không tích hợp quy trình xác nhận
xửlý sựcốtheo chuẩn nghiệp vụy tế.
4https://www.tangobelt.com
5https://support.apple.com/en-us/111839
2


---

## Trang 17

CHƯƠNG 1. GIỚI THIỆU ĐỀTÀI
(a) H¨ovding 3 — vòng cổtúi khí cho người đi xe đạp (Nguồn:
hovding.com)
(b) Alpinestars Tech-Air — áo giáp túi khí dành cho người lái
mô-tô (Nguồn: alpinestars.com)
(c) Hip’Air (Helite) — đai hông túi khí bảo vệkhớp hông
người cao tuổi (Nguồn: helite.com)
(d) TangoBelt — đai bụng IoT kết nối BLE cảnh báo té ngã
cho người cao tuổi (Nguồn: tangobelt.com)
Hình 1.1: Các sản phẩm thiết bịđeo phát hiện té ngã thương mại tiêu biểu, phân loại theo đối tượng sửdụng và cơ chế
bảo vệ.
Khoảng trống rõ ràng từphân tích trên là chưa có giải pháp nào kết hợp đồng thời: suy luận TinyML
on-device, truyền thông 4G LTE độc lập Wi-Fi, dashboard y tếthời gian thực đa bệnh nhân và lưu trữlịch
sửvận động chuỗi thời gian — đây chính là mục tiêu mà đồán này hướng đến.
1.2.2
Các phương pháp nghiên cứu giải quyết bài toán
Song song với sựphát triển của các sản phẩm thương mại, cộng đồng học thuật đã đềxuất nhiều hướng
tiếp cận khác nhau đểgiải quyết bài toán phát hiện té ngã bằng cảm biến IMU. Hệthống trong đồán này kế
thừa và vận dụng tri thức từba dòng nghiên cứu chính được khảo sát dưới đây.
a, Phương pháp dựa trên ngưỡng
Hướng tiếp cận dựa trên ngưỡng (threshold-based) là nhóm phương pháp lâu đời nhất và có chi phí tính
toán thấp nhất, phù hợp với vi điều khiển năng lượng thấp. Nguyên lý chung là so sánh các đặc trưng tín
hiệu IMU (biên độgia tốc, căn bậc hai trung bình — RMS, góc nghiêng) với một tập ngưỡng được định
nghĩa trước; khi tín hiệu vượt ngưỡng, hệthống kết luận có sựkiện té ngã.
1) Alsaadi và cộng sựalsaadi2024logical đềxuất hệthống nhận diện hoạt động con người kết hợp suy
luận logic dựa trên đặc trưng vật lý của chuyển động với cơ chếhiệu chỉnh ngưỡng thích ứng bằng
3


---

## Trang 18

CHƯƠNG 1. GIỚI THIỆU ĐỀTÀI
hồi quy véc-tơ hỗtrợ(Support Vector Regression — SVR). Dữliệu được thu thập từmạng lưới bốn
cảm biến IMU 9 trục đặt tại đầu, cổtay, thắt lưng và bàn chân của 20 tình nguyện viên, đồng bộhóa
ởtần số50 Hz. Thay vì dùng mô hình hộp đen, hệthống phân loại 12 hoạt động hằng ngày thông
qua một ma trận quan hệhành động và cây logic dựa trên giá trịRMS, biên độ, và chu kỳtín hiệu.
Điểm sáng tạo nổi bật là cơ chếthích ứng cá nhân hóa: chỉcần người dùng mới đi bộthửhai bước,
thuật toán SVR sẽnội suy toàn bộtập ngưỡng cho 11 hành vi còn lại, giải quyết trực tiếp bài toán
khái quát hóa chéo người dùng (cross-person generalization) mà không cần thu thập dữliệu té ngã từ
đối tượng mới. Hệthống đạt độchính xác trung bình 90,8–92,1% trong kịch bản chéo người dùng,
vượt trội SVM (84,7%) và DT (80,2%). Đối với đồán, pipeline tiền xửlý "bộlọc bù bậc nhất + RMS
triggering" là công thức có thểtriển khai trực tiếp trên vi điều khiển ESP32; hạn chếchính là yêu cầu
đồng thời bốn thiết bịđeo, không phù hợp với kịch bản một cảm biến duy nhất.
2) Tseng và cộng sựtseng2025wearable phát triển thiết bịđeo tích hợp vi điều khiển, cảm biến IMU,
GPS và NB-IoT (Narrowband Internet of Things) nhằm khắc phục giới hạn nhận thức vịtrí của các
hệthống phát hiện té ngã trong nhà. Thuật toán được thiết kếtheo mô hình máy trạng thái hữu hạn
(Finite-State Machine — FSM), có khảnăng lọc tám loại hoạt động hằng ngày và phân biệt bốn
hướng ngã (trước, sau, trái, phải). Khi phát hiện té ngã, thiết bịlập tức gửi cảnh báo kèm tọa độGPS
qua NB-IoT đến máy chủ, giải quyết bài toán cứu hộtrong môi trường ngoài trời. Thửnghiệm thu
thập 6.750 mẫu từ15 người tham gia, hệthống đạt độnhạy 97,9%, độđặc hiệu 99,9% và độchính
xác tổng thể99,7%. Nghiên cứu khẳng định tính khảthi của FSM trên phần cứng nhúng năng lượng
thấp và kiến trúc truyền thông hướng sựkiện (event-driven) — hướng tiếp cận này được đồán vận
dụng làm cơ sởthiết kếFSM phát hiện ngã trên firmware ESP32-S3.
3) Booranawong và cộng sựbooranawong2025stairs giới thiệu hệthống giám sát và phân loại hoạt
động trên cầu thang theo thời gian thực, sửdụng module không dây XBee3 chuẩn IEEE 802.15.4 ở
băng tần 2,4 GHz kết hợp gia tốc kếba trục GY-521 đeo tại thắt lưng. Pipeline xửlý gồm tính véc-tơ
độlớn tín hiệu (SVM), lọc nhiễu bằng bộlọc EWMA (α = 0,3), trích xuất đặc trưng trong cửa sổ
15 mẫu (1,5 giây ở10 Hz), và phân loại bằng K lân cận gần nhất (KNN). Kết quảđáng chú ý là hệ
thống nhận diện cú ngã với độchính xác 100%, đồng thời đạt tỷlệgói tin thành công (PDR) 100%
cảtrong điều kiện có và không có tầm nhìn thẳng. Nghiên cứu chứng minh rằng chỉmột đặc trưng
phương sai (variance) tính trên cửa sổtrượt cực nhỏlà đủđểphân biệt cú ngã, mởra hướng tối giản
hóa thuật toán cho hệthống nhúng. Điểm hạn chếlà dataset chỉcó một tình nguyện viên nam trẻtuổi,
chưa phản ánh được động lực học té ngã của người cao tuổi.
b, Phương pháp học máy
Các phương pháp học máy (machine learning) cải thiện độchính xác phát hiện bằng cách học các mẫu
đặc trưng phức tạp từdữliệu huấn luyện thay vì dựa trên ngưỡng cứng. Pipeline điển hình gồm tiền xửlý tín
hiệu, trích xuất đặc trưng thủcông và huấn luyện một mô hình phân loại. Tuy độchính xác cao hơn nhóm
threshold-based, chi phí tính toán trong pha suy luận vẫn đủnhỏđểchạy trên thiết bịnhúng.
1) Nazar và Jalal nazar2025csohm đềxuất hệthống phát hiện té ngã kết hợp thuật toán tối ưu bầy đàn
Cuckoo (Cuckoo Search Optimization — CSO) đểlựa chọn đặc trưng với mô hình Markov ẩn dạng
Gaussian (Hidden Markov Model — HMM) đểphân loại chuỗi thời gian. Dữliệu IMU được khử
nhiễu bằng bộlọc Kalman trước khi phân đoạn qua cửa sổtrượt 200 mẫu; các đặc trưng entropy
Shannon, độlệch chuẩn, năng lượng phổ, chiều dài tích lũy và biên độtín hiệu được tối ưu bằng CSO
đểloại bỏdư thừa. Mỗi hoạt động được đại diện bởi một HMM ba trạng thái ẩn, giúp nắm bắt tốt sự
phụthuộc tuần tựcủa tín hiệu chuyển động và phân biệt các kiểu ngã có động lực học gần giống nhau
(trượt chân, vấp ngã, ngất xỉu). Kiểm thửtrên tập KFall đạt độchính xác 93,7% cho 15 lớp hoạt động,
vượt trội SVM (84,89%) và Random Forest (89,37%). Hạn chếlà pha tối ưu hóa CSO và huấn luyện
HMM bằng thuật toán Baum-Welch yêu cầu tài nguyên tính toán rất lớn, bắt buộc phải chạy offline,
không phù hợp triển khai trực tiếp trên vi điều khiển cạnh.
4


---

## Trang 19

CHƯƠNG 1. GIỚI THIỆU ĐỀTÀI
2) Aqillah và cộng sựaqillah2024comparative thực hiện nghiên cứu so sánh bốn mô hình học máy trên
cùng một hệthống phát hiện té ngã thời gian thực dùng cảm biến IMU: Máy véc-tơ hỗtrợ(SVM),
Rừng ngẫu nhiên (RF), Mạng nơ-ron tích chập (CNN) và Mạng nơ-ron nhân tạo (ANN). Dữliệu gia
tốc, vận tốc góc và góc định hướng được thu thập ở100 Hz từcác hoạt động giảlập gồm đi bộ, đứng
yên và ngã theo nhiều hướng. ANN đạt hiệu quảtốt nhất với độchính xác 98% và độtrễsuy luận
chỉ0,1 giây, tiếp theo là CNN (97%), RF (96%) và SVM (90%). Hệthống được thiết kếđểkích hoạt
phản ứng bảo vệtức thì (bung túi khí vest) khi phát hiện ngã, nhấn mạnh yêu cầu khắt khe vềđộtrễ
thấp trong ứng dụng y tếkhẩn cấp. Nghiên cứu này là một trong những cơ sởđịnh lượng đểđồán lựa
chọn kiến trúc học sâu tích chập (CNN) thay vì SVM/RF; điểm hạn chếlà dataset nhỏvới chỉmột
người thực hiện giảlập, chưa có dữliệu người cao tuổi.
3) Park và cộng sựpark2025fallrisk nghiên cứu chiến lược tối ưu hóa vịtrí đặt cảm biến IMU và thuật
toán phân loại đểtối đa hóa độchính xác đánh giá nguy cơ té ngã thông qua phân tích dáng đi. Nghiên
cứu thu thập dữliệu động học từ93 người cao tuổi sống trong cộng đồng (tuổi trung bình 77,8) sử
dụng 10 cảm biến IMU đặt tại các vịtrí khác nhau trên cơ thểtrong bài kiểm tra đi bộ10 mét, với
đánh giá nguy cơ ngã qua công cụPPA rút gọn. Kết quảcho thấy vịtrí đặt cảm biến có ảnh hưởng có
ý nghĩa thống kê đến độchính xác phân loại (p < 0,001), trong khi sựkhác biệt giữa sáu thuật toán
(SVM, DT, RF, KNN, XGBoost, LightGBM) là không đáng kể. Hiệu quảtốt nhất đạt được bởi SVM
dùng cảm biến chân dưới bên trái với độchính xác 90,1%, độnhạy 95,7% và độđặc hiệu 84,1%. Phát
hiện quan trọng nhất của nghiên cứu — vùng thắt lưng và chân dưới cho tín hiệu dáng đi chất lượng
cao nhất với người cao tuổi — củng cốtrực tiếp quyết định đặt thiết bịđeo tại thắt lưng trong đồán.
c, Phương pháp học sâu
Học sâu (deep learning) cho phép học đặc trưng tựđộng từdữliệu thô mà không cần bước trích xuất
đặc trưng thủcông, đạt độchính xác vượt trội trong các bài toán phân loại tín hiệu chuỗi thời gian phức tạp.
Hạn chếchính là yêu cầu bộnhớvà tính toán lớn, đặt ra thách thức triển khai lên vi điều khiển nhúng.
1) Cai và cộng sựcai2026stanet xây dựng tập dữliệu quy mô lớn FallTL (28,4 giờdữliệu, 45 người
tham gia, 8 vịtrí đặt cảm biến) và phát triển mạng STA-Net (Spatial-Temporal Attention Network)
kiến trúc nhánh kép đểphát hiện té ngã trước thời điểm va chạm (Pre-Impact Fall Detection — PIFD).
Nhánh không gian dùng tích chập 2D đa tỷlệkết hợp khối chú ý SE (Squeeze-and-Excitation) đểhọc
tương quan giữa các trục cảm biến, trong khi nhánh thời gian dùng Bi-GRU kết hợp Criss-Cross
Attention đểnắm bắt phụthuộc dài hạn theo thời gian. Mô hình huấn luyện với hàm mất mát Focal
Loss nhằm xửlý mất cân bằng lớp nghiêm trọng giữa mẫu hoạt động bình thường và mẫu té ngã. Kết
quảđạt khoảng 94% (PIFD trên FallTL) và 96–99% (phát hiện sau va chạm), với thời gian cảnh báo
sớm trung bình 456,69 ms trước khi chạm đất — đủđểkích hoạt thiết bịbảo vệchủđộng. Hạn chế
chính là kích thước mô hình 22,4 MB vượt quá giới hạn Flash/RAM của đa sốvi điều khiển, đòi hỏi
lượng tửhóa INT8 hoặc chạy trên Edge Gateway đểtriển khai thực tế.
2) Mekruksavanich và cộng sựmekruksavanich2024resnet đềxuất kiến trúc mạng phần dư một chiều
ResNeXt tùy chỉnh (1D ResNeXt) đểphân tích tín hiệu IMU từgia tốc kếvà con quay hồi chuyển
ba trục. Kiến trúc phần dư (residual) giải quyết vấn đềtiêu biến gradient trong quá trình huấn luyện
mạng sâu thông qua các kết nối tắt (skip connection), cho phép học các đặc trưng phân cấp từtín hiệu
chuyển động. Hệthống được kiểm thửtrên tập PIF gồm 12 cá thểđa dạng vềđộtuổi và thểtrạng, đạt
độchính xác 91,52% chỉvới gia tốc kế, 83,80% với con quay hồi chuyển, và 92,27% khi kết hợp cả
hai — vượt trội các baseline CNN, LSTM, BiLSTM, GRU và BiGRU. Đây là một cơ sởquan trọng
cho định hướng đưa mạng học sâu tích chập 1D xuống chạy suy luận on-device trên ESP32-S3 trong
đồán (dù đồán lựa chọn một biến thểtích chập tách kênh nhẹhơn ResNeXt đểphù hợp ràng buộc
phần cứng); điểm cần lưu ý là tập PIF còn nhỏ(12 người) và chỉgồm dữliệu ngã giảlập từngười trẻ.
3) Gaud và cộng sựgaud2025fibils đềxuất mô hình FIBiLS kết hợp mạng nơ-ron tích chập 1D (1D-
5


---

## Trang 20

CHƯƠNG 1. GIỚI THIỆU ĐỀTÀI
CNN) và mạng LSTM hai chiều (BiLSTM) đểphát hiện sớm té ngã trong quá trình thực hiện hoạt
động hằng ngày. Hệthống sửdụng hai cảm biến IMU đeo trên người và huấn luyện trên tập dữliệu
công khai SisFall — bộdữliệu gồm 19 loại hoạt động hằng ngày và 15 kiểu té ngã từ23 người trẻ
và 14 người cao tuổi trên 62 tuổi, thu thập bằng thiết bịtựchếvới gia tốc kếvà con quay hồi chuyển
sucerquia2017sisfall. FIBiLS đạt độchính xác 99,68% với thời gian suy luận nhanh và được triển
khai thực tếlên vi điều khiển NodeMCU đểkiểm chứng khảnăng tính toán biên. Sựkết hợp giữa đặc
trưng cục bộ(CNN) và phụthuộc tuần tự(BiLSTM) cho phép mô hình nắm bắt đồng thời hình dạng
tín hiệu và tiến trình chuyển động theo thời gian; hạn chếlà tập SisFall thiên lệch vềdữliệu người trẻ,
ảnh hưởng đến hiệu quảnhận diện với người cao tuổi thực sự.
d, Nhận xét tổng hợp
Việc khảo sát các nghiên cứu hiện tại cho thấy rõ hai trường phái tối ưu hóa trái ngược nhau: (1) Cải tiến
độchính xác của thuật toán học máy/học sâu trên nền tảng điện toán mạnh mẽvà (2) Lược giản mô hình
đểtriển khai trực tiếp trên vi điều khiển nhúng (Edge Computing / TinyML). Bảng 1.1 và Bảng 1.2 lần lượt
tổng hợp các công trình tiêu biểu theo hai hướng tiếp cận này.
Trường phái 1: Tối ưu hóa độchính xác thuật toán
Các nghiên cứu thuộc nhóm này thường ứng dụng các kiến trúc học sâu phức tạp nhằm đạt độchính xác
tối đa trên các bộdữliệu công khai lớn. Mặc dù có hiệu suất nhận diện cực cao, nhưng rào cản lớn nhất là
khối lượng tính toán khổng lồ, khiến chúng khó chạy trực tiếp trên các thiết bịđeo nhỏgọn.
Bảng 1.1: Tổng hợp các nghiên cứu vềthuật toán nhận diện té ngã
Tác giả& Năm
Bộdữliệu
Thuật toán / Mô hình
Độ
chính
xác
Nhược điểm chính đối với
thiết bịđeo
Cai
et
al.
(2026)
cai2026stanet
FallTL,
Fal-
lAllD
Mạng nơ-ron nhánh kép
(STA-Net)
∼99%
Kích thước mô hình lớn (22,4
MB), độtrễsuy luận cao.
Mekruksavanich
(2025)
mekruksavanich2024resnet
PIF Dataset
1D-ResNeXt
92,27%
Phụthuộc thư viện tính toán
lớn, chưa thửnghiệm nhúng.
Gaud et al. (2025)
gaud2025fibils
SisFall
BiLSTM
99,68%
Mạng chuỗi thời gian tiêu tốn
quá nhiều bộnhớđộng RAM.
Aqillah et al. (2025)
aqillah2024comparative
Tựthu thập
Mạng
nơ-ron
nhân
tạo
(ANN)
98,00%
Chỉđánh giá offline trên PC,
chưa đánh giá mức tiêu thụpin.
Nazar et al. (2025)
nazar2025csohm
KFall
CSO + HMM
93,70%
Thuật toán tối ưu hóa bầy đàn
cần tính toán lặp cực kỳtốn
CPU.
Lee
et
al.
(2021)
lee2021deep
IMU + RGB
DNN Double-Check
Rất cao
Phụthuộc vào camera và dữ
liệu hình ảnh, xâm phạm quyền
riêng tư.
Trường phái 2: Nhúng trí tuệnhân tạo lên thiết bịbiên (Edge AI & TinyML)
Một thách thức cốt lõi trong các hệthống giám sát sức khỏe đeo trên người là vịtrí thực thi suy luận
(Inference Location). Rất nhiều hệthống hiện nay chỉdùng vi điều khiển (MCU) như một cảm biến thụ
động (dumb sensor), làm nhiệm vụthu thập dữliệu IMU thô và truyền liên tục qua Bluetooth/Wi-Fi lên
điện thoại hoặc Đám mây (Cloud) đểtính toán. Dù tận dụng được sức mạnh của các mô hình học sâu ở
Bảng 1.1, phương pháp này lại làm cạn kiệt pin nhanh chóng do băng thông truyền dẫn liên tục và gây ra
rủi ro tính mạng nếu đường truyền mạng bịgián đoạn.
Đểgiải quyết triệt để, nhóm nghiên cứu thứhai đã chuyển dịch sang On-device Inference: bắt vi điều
khiển phải tựthân tính toán kết quả(Edge AI) và chỉphát sóng khi thực sựxảy ra sựcốngã. Bảng 1.2 tổng
hợp các công trình tiên phong theo hướng đi này. Tuy nhiên, giới hạn khắt khe vềRAM và Flash khiến họ
thường phải đánh đổi bằng cách sửdụng các thuật toán quá đơn giản, làm giảm độtin cậy trong môi trường
thực tế.
6


---

## Trang 21

CHƯƠNG 1. GIỚI THIỆU ĐỀTÀI
Bảng 1.2: Tổng hợp các nghiên cứu đã triển khai trên Vi điều khiển (MCU)
Tác giả(Năm)
Bộdữliệu
Thiết bị
Thuật toán
Flash
RAM
Chính
xác
Edge
AI/
Tiny-
ML
Hạn chế
Luong-
Cong
(2026)
LuongCong2026Energy
KFall, Sis-
Fall
Edge
Devices
(Cortex-M)
Spatial-
Temporal
TinyML
∼250
KB
∼80
KB
Khá cao
✓
Kiến
trúc
không
gian-thời
gian
nặng, đòi hỏi CPU
ARM mạnh.
Tseng
et
al.
(2025)
tseng2025wearable
Tựthu thập
(15 người)
MCU năng
lượng thấp
Máy
trạng
thái (FSM)
<
20
KB
<
10
KB
99,70%
✓
Phụthuộc ngưỡng
tĩnh (cứng) gây kém
khái quát hóa, dễ
báo giả, nhạy cảm
với góc đeo.
Booranawong
(2025)
booranawong2025stairs
Tựthu thập
(1 người)
XBee3 Mi-
cro
KNN
&
EWMA
Filter
∼50
KB
∼30
KB
100%
(ngã cầu
thang)
× (PC)
Truyền dữliệu thô
liên tục (Streaming)
gây hao pin, phụ
thuộc mạng.
Zhang
et
al.
(2024)
zhang2024gait
Tựthu thập
(Quy
mô
rất nhỏ)
32-bit
MCU
TinyML
Gait
Recog-
nition
∼120
KB
∼45
KB
Tốt
✓
Chỉphân tích dáng
đi (Gait), thời gian
phản hồi trễ.
Paramasivam
et
al.
(2024)
Paramasivam2024Heliyon
Tựthu thập
(120 người)
MPU (Jet-
son
Nano,
RPi)
CNN-
LSTM
+
Attention
>
16
GB
∼4 GB
97,00%
Edge
AI
(Không
Tiny-
ML)
Dùng
vi
xử
lý
(MPU)
gây
tốn
pin, tỏa nhiệt, cồng
kềnh, khó ứng dụng
thiết
bị
đeo
nhỏ
gọn.
Lựa chọn giải pháp cho đồán
Từkết quảkhảo sát ởhai bảng trên, có thểnhận thấy một khoảng trống công nghệrõ rệt: Các mô hình
học sâu hiện đại có khảnăng trích xuất đặc trưng tốt nhưng bắt buộc phải chạy trên Cloud/PC; trong khi
các thiết bịđeo có khảnăng tựtính toán (On-device) thì lại bịkẹt ởcác thuật toán cơ sở(FSM, KNN,
Thresholding) dẫn đến dễbáo động giả.
Nhận thấy khoảng trống đó, đồán này đềxuất một giải pháp "lai" (hybrid) đột phá: Mang sức mạnh
của học sâu xuống vi mạch (On-device Deep Learning). Vềphần cứng, vịtrí đặt cảm biến tại thắt lưng
được ưu tiên theo kết quảtừbooranawong2025stairs, cai2026stanet, park2025fallrisk. Tổhợp gia tốc kế
và con quay hồi chuyển (6 trục) là đủđểnhận diện ngã mà không cần từkế. Vềthuật toán, đồán sửdụng
nền tảng TinyML (TensorFlow Lite for Microcontrollers) đểlượng tửhóa (Quantization) một mạng học
sâu tích chập 1D tách kênh (depthwise-separable CNN) được thiết kếriêng cho vi điều khiển. Quá trình
lượng tửhóa giúp ép kích thước mạng nơ-ron từhàng Megabyte xuống chỉcòn vài chục KB Flash và tốn
chưa tới 30 KB RAM. Điều này trao quyền cho lõi vi xửlý ESP32-S3 tựthực thi suy luận tại biên (On-
device Inference) trong tích tắc. Vi điều khiển không cần truyền dữliệu thô đi đâu cả, nó tựtính toán và
chỉkích hoạt module 4G đểgửi đúng một thông báo Alert khi có ngã xảy ra. Giải pháp này vừa không phụ
thuộc vào điện thoại thông minh, vừa tiết kiệm pin tối đa, đáp ứng trọn vẹn cảđộchính xác học sâu (Bảng
1.1) và tính khảthi phần cứng (Bảng 1.2).
1.3
Mục tiêu và định hướng giải pháp
Hiện nay, trên thịtrường đã xuất hiện một sốgiải pháp phát hiện té ngã, từcác hệthống camera giám sát
(Computer Vision) đến các thiết bịđeo tay thông minh (Smartwatch). Tuy nhiên, hệthống camera thường
xâm phạm quyền riêng tư nghiêm trọng và bịgiới hạn bởi các điểm mù trong không gian, trong khi các thiết
bịđeo cá nhân hiện hành phần lớn phụthuộc vào điện thoại thông minh qua sóng Bluetooth, khiến chúng
thiếu tính đồng bộvà khó quản lý tập trung trong môi trường viện dưỡng lão.
Dựa trên những hạn chếđó, đềtài hướng tới mục tiêu thiết kếvà xây dựng một hệthống cảnh báo khép
7


---

## Trang 22

CHƯƠNG 1. GIỚI THIỆU ĐỀTÀI
kín chuyên dụng cho các cơ sởy tếtập trung. Cụthể, hệthống bao gồm thiết bịđeo thu thập dữliệu trực
tiếp từngười dùng và một nền tảng Web quản trị. Phạm vi của đồán tập trung vào việc nghiên cứu và ứng
dụng trí tuệnhân tạo đểphân tích trực tiếp hành vi trên thiết bịnhằm phát hiện các biến cốté ngã, đồng thời
đảm bảo khảnăng truyền nhận dữliệu độc lập và liên tục mà không cần thông qua điện thoại thông minh
của bệnh nhân.
Đểgiải quyết bài toán trên, đồán đềxuất giải pháp "Nghiên cứu và xây dựng hệthống giám sát hành
vi người già và phát hiện té ngã ứng dụng IoT và TinyML". Vềmặt phần cứng thiết bịđeo, đồán sửdụng
kiến trúc học máy tại biên (Edge AI) thông qua nền tảng TinyML trên vi điều khiển ESP32-S3, cho phép
phân tích dữliệu cảm biến gia tốc và nhận diện hành vi ngay tại thiết bịvới độtrễsiêu thấp. Vềmặt truyền
thông mạng, thiết bịsửdụng mạng di động 4G LTE kết hợp giao thức MQTT đểđẩy dữliệu trực tiếp lên
máy chủ, loại bỏsựphụthuộc vào hạtầng mạng Wi-Fi hay thiết bịtrung gian. Cuối cùng, một hạtầng Web
Dashboard thời gian thực được xây dựng đểcung cấp giao diện quản lý tập trung danh sách thiết bịvà tự
động phát âm thanh cảnh báo tức thời cho nhân viên chăm sóc.
1.4
Đóng góp của đồán
Đóng góp chính của đồán là việc hoàn thiện một hệthống giám sát toàn diện từphần cứng nhúng đến
ứng dụng Web, giúp giảm tải áp lực cho nhân viên y tế, nâng cao hiệu quảphản hồi khẩn cấp và bảo vệan
toàn cho người cao tuổi.
Bên cạnh giá trịvềmặt hệthống, đồán còn mang tính nghiên cứu với mục tiêu trọng tâm là trảlời câu
hỏi: liệu một mạng học sâu có thểđạt độnhạy phát hiện té ngã (Fall-recall) tương đương các mô hình chạy
trên máy chủ, nhưng vẫn suy luận trọn vẹn trong một chu kỳcửa sổtrượt trên vi điều khiển ESP32-S3 dưới
ràng buộc chỉvài chục KB Flash và RAM hay không? Đểtrảlời câu hỏi này, đồán thực hiện các đóng góp
nghiên cứu chính sau:
• Đồng thiết kếkiến trúc mô hình theo ràng buộc phần cứng: thiết kếmột mạng tích chập tách kênh
1 chiều (Depthwise Separable 1D CNN) bám sát tập lệnh tăng tốc ESP-NN của ESP32-S3, qua đó
đạt độnhạy phát hiện té ngã cao trong khi vẫn suy luận thấp hơn chu kỳcửa sổtrượt và vừa với ngân
sách Flash/RAM của vi điều khiển.
• Chiến lược thiết kếnhãn và gán nhãn theo sựkiện: đềxuất sơ đồphân loại 5 lớp (tách riêng nhãn
chuyển tư thếTrans) cùng cơ chếcắt cửa sổcăn theo sựkiện dựa trên độlớn gia tốc và vận tốc xoay,
nhằm giảm thiểu đáng kểcảnh báo giảtừcác sinh hoạt thường ngày.
• Quy trình lượng tửhóa và đánh giá trên phần cứng thật: xây dựng quy trình lượng tửhóa INT8
và sinh mã nguồn nhúng có kiểm soát tập toán tử(ops), kết hợp phương pháp đánh giá độc lập theo
đối tượng (subject-independent) ưu tiên chỉsốFall-recall và Trans-F1, đồng thời đo trực tiếp độtrễ
suy luận, dung lượng Flash và RAM trên chip.
• Hạtầng thực nghiệm đầu–cuối: hiện thực một hệthống hoàn chỉnh (firmware hướng sựkiện với
lấy mẫu chính xác bằng ngắt phần cứng PCNT, truyền 4G/MQTT, máy chủcơ sởdữliệu kép và giao
diện Web thời gian thực) đóng vai trò bệphóng đểthu thập dữliệu và kiểm chứng mô hình trong điều
kiện vận hành thực tế.
1.5
Bốcục đồán
Phần còn lại của báo cáo đồán tốt nghiệp này được tổchức như sau.
Chương 2 đi sâu vào việc giới thiệu các nền tảng lý thuyết và công nghệđược áp dụng trong đồán, bao
gồm kiến trúc truyền thông IoT (MQTT qua 4G LTE), nền tảng học máy TinyML, thuật toán mạng nơ-ron
tích chập tách kênh 1 chiều (Depthwise Separable 1D CNN) và các công nghệphát triển ứng dụng Web.
Chương 3 trình bày chi tiết ba đóng góp kỹthuật nổi bật của đồán: (i) chiến lược thiết kếnhãn phân loại
5 lớp nhằm giảm thiểu cảnh báo sai từcác hành vi chuyển tư thếthường ngày; (ii) tiến trình tối ưu hóa kiến
8


---

## Trang 23

CHƯƠNG 1. GIỚI THIỆU ĐỀTÀI
trúc mô hình học sâu từCNN-LSTM, qua TCN, đến mạng tích chập tách kênh (CNN) tương thích TinyML
với các kỹthuật tối ưu phần cứng ESP-NN; và (iii) phương pháp lấy mẫu IMU chính xác sửdụng ngắt phần
cứng PCNT thay thếcơ chếtrễphần mềm FreeRTOS.
Chương 4 trình bày quá trình phân tích, thiết kếvà xây dựng hệthống, bao gồm kiến trúc phần mềm
firmware theo mô hình Hướng sựkiện và Máy trạng thái, thiết kếcơ sởdữliệu kép, giao thức truyền thông,
cùng quá trình triển khai các thành phần cốt lõi như bộlọc Kalman, pipeline TinyML, Backend và Frontend.
Chương 5 trình bày kết quảkiểm thửtích hợp hệthống đầu cuối, đánh giá kết quảtrên vi điều khiển và
đánh giá các chỉsốcủa mô hình máy học.
Cuối cùng, Chương 6 tổng kết lại các kết quảchính đã đạt được, đồng thời đềxuất những hướng phát
triển và mởrộng ứng dụng trong tương lai.
9


---

## Trang 24

CHƯƠNG 2. CƠ SỞLÝ THUYẾT VÀ CÔNG NGHỆSỬDỤNG
Chương này sẽgiới thiệu chi tiết vềcác nền tảng lý thuyết và công nghệcốt lõi được ứng dụng đểxây
dựng hệthống giám sát người cao tuổi. Nhằm đảm bảo tính rõ ràng, nội dung được chia thành hai nhóm
chính: nhóm công nghệphần cứng và thuật toán nhận diện (phía thiết bịbiên), và nhóm công nghệphần
mềm (phía máy chủvà ứng dụng quản lý).
2.1
Cơ sởlý thuyết vềNhận diện hành vi và Phát hiện té ngã dựa trên cảm biến quán tính (IMU)
2.1.1
Cơ chếnhận diện hành vi con người (HAR)
Nhận diện hành vi con người (Human Activity Recognition - HAR) thông qua cảm biến quán tính (IMU)
hoạt động dựa trên nguyên lý thu thập và phân tích các mẫu động học của cơ thể. Mỗi hành động như đi bộ
(Walk), chạy (Run), hay đứng yên (Idle) đều tạo ra một mẫu tín hiệu (pattern) gia tốc và vận tốc góc đặc
trưng, mang tính tuần hoàn và lặp lại trên không gian 3 chiều.
• Đứng yên (Idle): Trục gia tốc dọc theo chiều trọng lực của Trái Đất (thường là trục Z hoặc Y tùy vị
trí đeo) sẽđo được giá trịxấp xỉ1g (9.8m/s2), trong khi các trục còn lại xấp xỉ0g. Vận tốc góc từ
con quay hồi chuyển gần như bằng 0.
• Đi bộ(Walk) và Chạy (Run): Bước chân tạo ra các xung gia tốc có tính chu kỳhình sin. Đi bộcó
biên độdao động và tần sốthấp, trong khi chạy tạo ra các đỉnh gia tốc (peaks) sắc nhọn với biên độ
lớn và tần sốcao hơn. Con quay hồi chuyển cũng ghi nhận sựvung tay hoặc chuyển động xoay của
cơ thểtương ứng với từng bước đi.
Bằng cách cắt tín hiệu liên tục thành các cửa sổtrượt (sliding windows) với kích thước cốđịnh (ví dụ: 2
giây tương đương 200 mẫu ởtần số100 Hz), chúng ta thu được các ma trận dữliệu hai chiều chứa toàn bộ
thông tin không gian và thời gian của hành động. Hình 2.1 minh họa một sốmẫu tín hiệu gia tốc đặc trưng
của các hành vi thường gặp. Các mô hình học máy và học sâu sẽtựđộng trích xuất các đặc trưng tiềm ẩn từ
ma trận này đểphân loại chính xác hành vi nazar2025csohm, booranawong2025stairs.
10


---

## Trang 25

CHƯƠNG 2. CƠ SỞLÝ THUYẾT VÀ CÔNG NGHỆSỬDỤNG
Hình 2.1: Tín hiệu gia tốc đặc trưng của các hành vi Đứng yên (Idle), Đi bộ(Walk) và Chạy (Run) trong cửa sổ2 giây.
2.1.2
Cơ chếphát hiện té ngã (Fall Detection)
Khác với các hành vi mang tính chu kỳ, té ngã là một chuỗi sựkiện bất thường, diễn ra cực kỳnhanh và
có đặc điểm động lực học chia làm 4 giai đoạn rõ rệt:
1. Giai đoạn trước khi ngã (Pre-fall): Người bệnh đang thực hiện các hoạt động bình thường.
2. Giai đoạn rơi tựdo (Free-fall): Cơ thểbắt đầu mất thăng bằng và rơi xuống. Trong khoảnh khắc
này, gia tốc tổng hợp (Sum Vector Magnitude - SVM) của cả3 trục tiến dần vềmức 0g do trạng thái
không trọng lượng tạm thời.
3. Giai đoạn va chạm (Impact): Đây là đặc trưng quan trọng nhất. Cơ thểđập vào mặt đất sinh ra một
lực phản hồi cực lớn. Gia tốc kếsẽghi nhận một đỉnh (peak) đột biến vọt lên rất cao, thường vượt qua
mức 2.5g đến 3g. Cùng lúc đó, con quay hồi chuyển ghi nhận một sựthay đổi góc nghiêng cực gắt.
4. Giai đoạn sau khi ngã (Post-fall): Sau cú va chạm, cơ thểnằm bất động trên mặt sàn. Dữliệu gia
tốc kếsẽtrởlại trạng thái tĩnh, nhưng lúc này sựphân bốtrọng trường trên các trục không gian đã
thay đổi hoàn toàn so với tư thếđứng (do cơ thểnằm ngang).
Nhờsựkết hợp của cảđỉnh gia tốc đột biến và sựthay đổi tư thếtĩnh (orientation change) — được
minh họa rõ nét qua các giai đoạn trong Hình 2.2 — hệthống có thểdễdàng phân biệt được một cú té ngã
nguy hiểm so với các hành động mạnh khác như nhảy lên, hoặc việc bệnh nhân chủđộng nằm xuống giường
tseng2025wearable, lee2021deep.
11


---

## Trang 26

CHƯƠNG 2. CƠ SỞLÝ THUYẾT VÀ CÔNG NGHỆSỬDỤNG
Hình 2.2: Bốn giai đoạn động học của một sựkiện té ngã (Fall) điển hình trên tín hiệu gia tốc: Pre-fall (Trước khi ngã),
Free-fall (Rơi tựdo), Impact (Va chạm) và Post-fall (Sau khi ngã).
2.1.3
Bộdữliệu thực nghiệm SisFall
Đểhuấn luyện và đánh giá các mô hình nhận diện, đồán sửdụng SisFall — một bộdữliệu công khai
vềvận động và té ngã được công bốnăm 2017 sucerquia2017sisfall. Đây là một trong sốít các bộdữliệu
vừa có quy mô lớn, vừa bao gồm dữliệu thu thập trực tiếp từngười cao tuổi — đúng đối tượng đích của hệ
thống — thay vì chỉmô phỏng bằng người trẻ.
Dữliệu được thu bằng một thiết bịđeo tựchếđặt ởthắt lưng (trùng với vịtrí đeo của thiết bịtrong đồ
án), tích hợp gia tốc kếvà con quay hồi chuyển, lấy mẫu ởtần số200 Hz. Mỗi bản ghi gồm sáu kênh tín
hiệu: ba trục gia tốc (ax, ay, az) trong dải ±8g và ba trục vận tốc góc (gx, gy, gz) trong dải ±2000 ◦/s —
cũng chính là dải đo của cảm biến MPU6050 dùng ởthiết bịthật, bảo đảm tính tương thích giữa dữliệu
huấn luyện và dữliệu suy luận thực tế. Cụthể, bộdữliệu bao gồm:
• 38 đối tượng: 23 người trẻ(mã SA01–SA23, độtuổi 19–30) và 15 người cao tuổi (mã SE01–SE15,
độtuổi 60–75).
• 19 loại hoạt động sinh hoạt hằng ngày (ADL, mã D01–D19): đi bộ, chạy bộ, lên/xuống cầu thang,
ngồi xuống, đứng dậy, nằm, cúi người...
• 15 kiểu té ngã (mã F01–F15) theo nhiều hướng và bối cảnh khác nhau: ngã trước/sau/ngang khi
đang đi, ngã khi đang ngồi, ngất xỉu...
Mỗi hoạt động được lặp lại nhiều lần trên nhiều đối tượng, tạo nên khoảng 4.500 bản ghi tín hiệu. Cần lưu ý
rằng vì lý do an toàn, phần lớn các kịch bản té ngã được thực hiện bởi nhóm người trẻ, khiến bộdữliệu thiên
lệch vềđặc trưng của người trẻ— một hạn chếquan trọng cần cân nhắc khi đánh giá khảnăng tổng quát hóa.
Trong đồán, dữliệu thô được giảm tần sốxuống 100 Hz, ánh xạmột tập con các mã hoạt động sang sơ đồ
5 nhãn (chi tiết ánh xạtại Bảng 3.1 của Chương 5) và được phân chia theo đối tượng (subject-independent)
nhằm phản ánh trung thực khảnăng vận hành trên người dùng mới (chi tiết tại Chương 4).
2.2
Nhóm Công nghệPhần cứng và Giao thức mạng
2.2.1
Vi điều khiển ESP32-S3 (Module Seeed Studio XIAO)
ESP32-S3 là một hệthống trên chip (SoC) mạnh mẽdo Espressif Systems phát triển espressif2023esp32s3,
được tích hợp vi xửlý lõi kép Xtensa 32-bit LX7 hoạt động ởxung nhịp lên đến 240 MHz. Điểm nổi bật
nhất của ESP32-S3 so với các phiên bản tiền nhiệm là việc được bổsung bộtập lệnh mởrộng SIMD (Single
Instruction, Multiple Data). Nhờđó, chip có khảnăng tính toán song song các mảng dữliệu lớn, giúp gia
12


---

## Trang 27

CHƯƠNG 2. CƠ SỞLÝ THUYẾT VÀ CÔNG NGHỆSỬDỤNG
tăng đáng kểtốc độxửlý mạng nơ-ron thông qua thư viện ESP-NN espressif2023espnn.
Trong đồán này, đểtối ưu hóa kích thước cho thiết bịđeo (wearable), hệthống sửdụng module Seeed
Studio XIAO ESP32S3 seeed2023xiao. Đây là một bo mạch phát triển có kích thước siêu nhỏ(chỉcỡngón
tay cái) nhưng vẫn mang đầy đủsức mạnh của chip ESP32-S3, với 512 KB SRAM tích hợp và 8MB bộnhớ
PSRAM (phù hợp cho các tác vụcần bộnhớđệm lớn mà cần tốc độxửlý cao như stream video MJEPG,
tensor arena cho tinyML warden2019tinyml). Vi điều khiển này đóng vai trò là "bộnão" trung tâm, không
chỉlàm nhiệm vụthu thập tín hiệu từcác cảm biến ngoại vi qua giao thức I2C, mà còn trực tiếp thực thi mô
hình học máy (TinyML) ngay tại thiết bịbiên (Edge Computing).
Một ưu điểm vượt trội khác của module XIAO ESP32S3 là thiết kếphần cứng thân thiện với thiết bịđeo
di động. Ởmặt sau của bo mạch được tích hợp sẵn 2 pad hàn (chân BAT+ và BAT-) dành riêng cho việc kết
nối trực tiếp với pin Lithium 3.7V. Tính năng này kết hợp với mạch quản lý sạc pin đã được tích hợp sẵn
trên bo mạch giúp thiết bịcó thểhoạt động hoàn toàn độc lập, dễdàng được cung cấp nguồn điện trực tiếp
từpin mà không cần phải thiết kếthêm mạch nguồn cồng kềnh.
Hình 2.3: Mặt trước và mặt sau của module Seeed Studio XIAO ESP32S3 (chú ý 2 chân BAT cấp nguồn pin ởmặt sau)
13


---

## Trang 28

CHƯƠNG 2. CƠ SỞLÝ THUYẾT VÀ CÔNG NGHỆSỬDỤNG
2.2.2
Cảm biến quán tính MPU6050
MPU6050 là một cảm biến vi cơ điện tử(MEMS) 6 bậc tựdo (6-DOF) bao gồm một gia tốc kế(Ac-
celerometer) 3 trục và một con quay hồi chuyển (Gyroscope) 3 trục invensense2013mpu6050.
• Gia tốc kế: Đo lường lực gia tốc tuyến tính (bao gồm cảgia tốc trọng trường), giúp xác định sựthay
đổi vận tốc và hướng của thiết bị. Trong bài toán phát hiện té ngã, gia tốc kếchịu trách nhiệm phát
hiện các xung lực va chạm cực đại khi người bệnh tiếp đất.
• Con quay hồi chuyển: Đo lường vận tốc góc của thiết bịtheo 3 trục không gian. Thông sốnày cực kỳ
hữu ích trong việc tính toán góc nghiêng của cơ thể, hỗtrợphân biệt các tư thếsinh hoạt bình thường
và trạng thái mất thăng bằng.
Dữliệu thô từMPU6050 được lấy mẫu liên tục thông qua giao tiếp I2C với tốc độcao, tạo thành các chuỗi
dữliệu đầu vào cho mạng nơ-ron Paramasivam2024Heliyon.
Hình 2.4: Cảm biến quán tính MPU6050 đo gia tốc và vận tốc góc
2.2.3
Module truyền thông 4G LTE A7680C
Nhằm khắc phục những hạn chếcủa kết nối Wi-Fi (phụthuộc vào cơ sởhạtầng mạng cục bộ) và
Bluetooth (yêu cầu phải ghép nối với điện thoại thông minh), đồán sửdụng module SIM 4G LTE A7680C
simcom2021a7680c. Đây là một module viễn thông siêu nhỏgọn, hỗtrợbăng tần LTE Cat-1, tối ưu hóa
cho các ứng dụng IoT (Internet of Things) đòi hỏi độtrễthấp và băng thông vừa phải. Nhờtích hợp module
A7680C, thiết bịđeo có thểhoạt động hoàn toàn độc lập, liên tục truyền tải dữliệu cảnh báo và viễn trắc
trực tiếp lên máy chủđám mây từbất kỳvịtrí nào có phủsóng di động tseng2025wearable.
14


---

## Trang 29

CHƯƠNG 2. CƠ SỞLÝ THUYẾT VÀ CÔNG NGHỆSỬDỤNG
Hình 2.5: Module truyền thông mạng di động 4G LTE A7680C (Mặt trước và mặt sau)
2.2.4
Giao thức truyền thông PPPoS
Đểkết nối module 4G A7680C với vi điều khiển ESP32-S3 một cách tối ưu, đồán không sửdụng tập
lệnh AT truyền thống đểgửi dữliệu từng bước, mà ứng dụng giao thức PPPoS (Point-to-Point Protocol over
Serial) lwip2023pppos. PPPoS cho phép thiết lập một kết nối mạng trực tiếp qua cổng nối tiếp (UART).
Sau khi kết nối thành công, hệđiều hành FreeRTOS trên ESP32 sẽnhận diện kết nối 4G như một giao diện
mạng (Network Interface) thực thụ, có địa chỉIP riêng. Việc này giúp các ứng dụng tầng trên (như MQTT
client hay HTTP client) có thểtương tác với mạng di động bằng các socket tiêu chuẩn một cách mượt mà
và ổn định.
Hình 2.6: Kiến trúc giao thức PPPoS ánh xạmạng 4G thành giao diện mạng trên ESP32S3
2.2.5
Giao thức truyền tải MQTT
MQTT (Message Queuing Telemetry Transport) là một giao thức nhắn tin theo mô hình Xuất bản/Đăng
ký (Publish/Subscribe), được thiết kếđặc biệt cho các thiết bịIoT hoạt động trong điều kiện băng thông thấp
và mạng không ổn định oasis2019mqtt. Khác với kiến trúc Request/Response nặng nềcủa HTTP, MQTT
15


---

## Trang 30

CHƯƠNG 2. CƠ SỞLÝ THUYẾT VÀ CÔNG NGHỆSỬDỤNG
sửdụng một máy chủtrung gian (Broker) đểđiều phối thông điệp.
• Cơ chếQoS (Quality of Service): MQTT hỗtrợ3 mức QoS (0, 1, 2). Trong đồán, các thông điệp
cảnh báo té ngã khẩn cấp được đặt mức QoS 1 (At least once) đểđảm bảo gói tin chắc chắn được máy
chủtiếp nhận, trong khi dữliệu viễn trắc thông thường dùng QoS 0 đểtối ưu băng thông.
• Keep-Alive: MQTT duy trì một kết nối TCP liên tục nhưng tiêu tốn cực ít năng lượng thông qua cơ
chếgửi gói tin Ping định kỳ, giúp máy chủlập tức nhận biết khi thiết bịmất tín hiệu hoặc cạn pin.
Hình 2.7: Mô hình giao tiếp Publish/Subscribe của MQTT trong hệthống giám sát
2.3
Công nghệNhận diện hành vi (TinyML)
2.3.1
Mạng nơ-ron tích chập tách kênh 1 chiều (Depthwise Separable 1D CNN)
Trong lĩnh vực xửlý chuỗi thời gian (time-series) như tín hiệu IMU, mạng nơ-ron tích chập 1 chiều (1D
CNN) tỏra vượt trội so với các mạng nơ-ron hồi quy (RNN/LSTM) vềtốc độsuy luận (inference speed) và
khảnăng trích xuất đặc trưng cục bộcủa chuyển động. Tuy nhiên, phép tích chập tiêu chuẩn vẫn khá tốn
kém vềsốphép tính và sốtham sốkhi triển khai trên vi điều khiển có tài nguyên eo hẹp.
Đểgiảm mạnh chi phí tính toán mà vẫn giữđược năng lực biểu diễn, đồán sửdụng kỹthuật tích chập
tách kênh theo chiều sâu (Depthwise Separable Convolution) howard2017mobilenets. Thay vì một phép
tích chập đầy đủtrộn đồng thời cảtheo trục thời gian lẫn giữa các kênh, phép toán này được phân rã thành
hai bước nhẹhơn: (i) tích chập theo chiều sâu (depthwise) lọc riêng từng kênh dọc trục thời gian, và (ii)
tích chập điểm 1 × 1 (pointwise) trộn thông tin giữa các kênh. Cách phân rã này giảm sốtham sốvà số
phép nhân–cộng đi nhiều lần so với tích chập tiêu chuẩn. Quan trọng hơn, chính hai toán tửdepthwise và
pointwise 1 × 1 lại nằm trong nhóm được thư viện ESP-NN tăng tốc mạnh nhất trên ESP32-S3 (xem Mục
4.2.2), khiến mạng CNN tách kênh trởthành lựa chọn vừa nhẹvừa nhanh, lý tưởng cho suy luận tại biên.
Chi tiết quá trình lựa chọn và tinh chỉnh kiến trúc cụthể— bao gồm việc thửnghiệm rồi loại bỏcác biến
thểnặng hơn như mạng thặng dư (ResNet) hay mạng tích chập giãn nởtheo thời gian (TCN) vì không phù
hợp ràng buộc phần cứng — được trình bày ởChương 4.
2.3.2
Kỹthuật lượng tửhóa (Quantization) cho TinyML
TinyML (Tiny Machine Learning — Học máy thu nhỏ) là khái niệm chỉviệc triển khai các mô hình học
máy lên các vi điều khiển có tài nguyên phần cứng cực kỳeo hẹp (vài chục KB RAM) warden2019tinyml.
Một mô hình tích chập 1D được huấn luyện bằng TensorFlow/Keras thường biểu diễn trọng sốdưới dạng số
thực dấu phẩy động 32-bit (Float32). Dạng dữliệu này có kích thước rất lớn và yêu cầu vi xửlý tính toán số
thực mạnh mẽ, gây tốn pin và vượt quá giới hạn SRAM của ESP32.
Đểgiải quyết rào cản này, kỹthuật lượng tửhóa sau huấn luyện (Post-Training Quantization - PTQ)
được áp dụng. Toàn bộtrọng sốvà tham sốkích hoạt của mạng nơ-ron được ánh xạtừkhông gian Float32
xuống sốnguyên 8-bit (INT8). Nhờđó, kích thước mô hình (ROM) giảm đi 4 lần (từvài MB xuống chỉcòn
16


---

## Trang 31

CHƯƠNG 2. CƠ SỞLÝ THUYẾT VÀ CÔNG NGHỆSỬDỤNG
dưới 100 KB), đồng thời vi điều khiển ESP32-S3 có thểtận dụng tập lệnh SIMD đểthực hiện phép nhân
ma trận sốnguyên siêu tốc. Lượng tửhóa tuy có làm giảm một phần nhỏđộchính xác của mô hình, nhưng
hoàn toàn nằm trong mức độchấp nhận được đểđổi lấy khảnăng chạy trực tiếp trên thiết bịbiên.
2.4
Nền tảng Phần mềm và Hệthống
2.4.1
Bộlọc Kalman 1D cho Dung hợp Cảm biến (Sensor Fusion)
Trong bài toán ước lượng góc nghiêng (Roll, Pitch) của thiết bịđeo từtín hiệu IMU, mỗi loại cảm biến
đều mang một điểm mạnh và điểm yếu đối nghịch nhau. Gia tốc kếcho phép tính toán góc tĩnh rất chính
xác dựa trên hướng của véc-tơ trọng lực, nhưng lại cực kỳnhạy cảm với nhiễu tần sốcao (high-frequency
noise) khi thiết bịva đập mạnh hoặc chuyển động đột ngột — đúng là đặc trưng của cú ngã. Ngược lại, con
quay hồi chuyển (gyroscope) phản ứng tức thời và mượt mà với mọi chuyển động, nhưng khi ước lượng góc
bằng cách tích phân vận tốc góc theo thời gian, sai sốnhỏcủa mỗi chu kỳlấy mẫu sẽtích lũy thành sai số
trôi (drift) không thểtựhiệu chỉnh được.
Bộlọc Kalman 1 chiều (1D Kalman Filter) giải quyết mâu thuẫn này bằng cách kết hợp linh hoạt đầu
ra của cảhai cảm biến theo một trọng sốtối ưu được cập nhật động theo từng chu kỳkalman1960new.
Thuật toán hoạt động qua hai bước tuần hoàn: bước Dựbáo (Predict) sửdụng vận tốc góc từgyroscope để
ước lượng góc nghiêng tại thời điểm hiện tại và tính toán sai sốdựbáo tích lũy; bước Cập nhật (Update) sử
dụng góc tĩnh tính từgia tốc kếnhư một phép đo tham chiếu đểhiệu chỉnh lại kết quảdựbáo thông qua hệ
sốKalman Gain. Tham sốphương sai nhiễu đo lường của gia tốc kế(R_measure) đóng vai trò điều chỉnh
mức độtin tưởng vào phép đo gia tốc: giá trịcao hơn sẽlàm bộlọc ít bịdao động khi gia tốc nhiễu (như lúc
va chạm), trong khi giá trịthấp hơn giúp hội tụnhanh hơn khi cơ thểởtrạng thái tĩnh.
Trong hệthống này, thư viện lib_kalman được gọi trực tiếp trong svc_imu tại mỗi chu kỳlấy mẫu
100 Hz. Góc Roll và Pitch đã được làm mượt bởi bộlọc được đưa vào cùng với dữliệu gia tốc thô và vận
tốc góc thô đểtạo thành véc-tơ đặc trưng 6 chiều đầu vào cho mô hình TinyML. Điều này giúp loại bỏphần
lớn nhiễu ngắn hạn không mang thông tin hành vi, đồng thời cung cấp cho mô hình một biểu diễn tư thếổn
định hơn, từđó giảm thiểu đáng kểtỷlệcảnh báo sai trong sinh hoạt hàng ngày.
2.4.2
Nền tảng phát triển Nhúng ESP-IDF và FreeRTOS
ESP-IDF (Espressif IoT Development Framework) là bộcông cụphát triển phần mềm chính thức cho
dòng chip ESP32 espressif2023espidf. Khác với môi trường Arduino IDE vốn chỉphù hợp cho các dựán
nhỏvới cấu trúc lập trình tuần tự(Super Loop), ESP-IDF cung cấp khảnăng can thiệp sâu vào phần cứng
và hỗtrợđa luồng thông qua hệđiều hành thời gian thực FreeRTOS freertos2023manual.
FreeRTOS đóng vai trò là "nhạc trưởng" điều phối toàn bộhoạt động của thiết bịbiên. Thay vì bắt bộ
vi xửlý thực hiện các công việc nối tiếp nhau và phải chờđợi (blocking), FreeRTOS cho phép chia nhỏ
chương trình thành các tác vụ(Tasks) độc lập. Trong đồán này, các tác vụnhư lấy mẫu cảm biến IMU, nội
suy AI, và truyền thông MQTT được cấp phát các mức độưu tiên (priority) khác nhau. Hệthống sửdụng
cơ chếhàng đợi (Queue) và cờhiệu (Semaphore) đểđồng bộhóa dữliệu giữa các tác vụ, đảm bảo rằng cảm
biến không bao giờbịbỏlỡmẫu dữliệu nào ngay cảkhi mô hình AI đang chiếm dụng CPU đểtính toán.
2.4.3
Nền tảng triển khai mô hình học máy (TinyML Pipeline)
Đồán xây dựng một quy trình (pipeline) khép kín đểphát triển và triển khai mô hình học máy lên thiết
bịnhúng với các công cụchuyên dụng:
• Huấn luyện mô hình (Training): Quá trình xây dựng và huấn luyện mạng tích chập 1D (CNN)
được thực hiện trên máy tính bằng thư viện mã nguồn mởTensorFlow và Keras (phiên bản 2.21)
abadi2016tensorflow. Đây là framework mạnh mẽgiúp định nghĩa các lớp tích chập, hàm mất mát
và tối ưu hóa trọng sốmô hình với độchính xác cao.
• Nén và Lượng tửhóa (Quantization): Sau khi huấn luyện, mô hình được chuyển đổi thông qua
TensorFlow Lite (TFLite). Công cụnày thực hiện lượng tửhóa sau huấn luyện (Post-Training Quan-
17


---

## Trang 32

CHƯƠNG 2. CƠ SỞLÝ THUYẾT VÀ CÔNG NGHỆSỬDỤNG
tization), ép kiểu trọng sốtừFloat32 xuống INT8, giúp giảm dung lượng mô hình tới 4 lần mà gần
như không làm suy giảm độchính xác.
• Suy luận tại biên (Inference): Mô hình đã lượng tửhóa được nạp vào ESP32-S3 và thực thi bằng
thư viện TensorFlow Lite for Microcontrollers david2021tensorflowlite. Đây là một phiên bản rút
gọn của TFLite, được thiết kếđặc biệt đểchạy trên vi điều khiển mà không cần hệđiều hành nền tảng
máy chủ, tiêu tốn chỉvài chục kilobyte bộnhớ.
• Tối ưu hóa phần cứng (Hardware Acceleration): Đểtối đa hóa tốc độsuy luận, đồán tích hợp thư
viện ESP-NN espressif2023espnn do Espressif cung cấp. Thư viện này chứa các hàm toán học (như
Convolution, Fully Connected) được viết bằng hợp ngữ(Assembly) và tối ưu hóa chuyên biệt cho tập
lệnh SIMD của lõi Xtensa trên ESP32-S3, giúp quá trình nhận diện diễn ra gần như tức thời.
2.4.4
Thư viện suy luận nhúng: TensorFlow Lite Micro và ESP-NN
Khâu suy luận tại biên trong đồán được xây dựng trên một chồng phần mềm (software stack) ba lớp, từ
định dạng mô hình chung cho tới thư viện kernel tăng tốc riêng cho ESP32-S3.
Ởlớp định dạng, mô hình sau huấn luyện được chuyển sang LiteRT — tên gọi mới của TensorFlow
Lite do Google đặt lại từnăm 2024 google2024litert. Đây là runtime suy luận gọn nhẹdành cho thiết bị
biên, lưu mô hình dưới dạng FlatBuffer (.tflite) đã được tối ưu và lượng tửhóa, cho phép nạp và thực
thi mà không cần toàn bộđồthịtính toán nặng nềcủa TensorFlow gốc.
Ởlớp thực thi trên vi điều khiển, đồán sửdụng TensorFlow Lite for Microcontrollers (TFLM)
david2021tensorflowlite. Khác với LiteRT bản đầy đủvốn vẫn cần hệđiều hành và cấp phát bộnhớđộng,
TFLM được viết bằng C++ tối giản, không phụthuộc thư viện chuẩn nặng và không dùng cấp phát động:
toàn bộtensor trung gian được đặt trong một vùng nhớtĩnh do lập trình viên cấp phát trước gọi là tensor
arena. TFLM cũng cho phép đăng ký chọn lọc tập toán tửqua cơ chếMicroMutableOpResolver —
chỉnạp đúng những toán tử(op) mà mô hình sửdụng — nhằm tiết kiệm tối đa Flash và RAM. Espres-
sif đóng gói TFLM thành component esp-tflite-micro tích hợp sẵn trong hệsinh thái ESP-IDF
espressif2024esptflitemicro, giúp việc biên dịch và nạp mô hình lên chip trởnên liền mạch.
Ởlớp tăng tốc phần cứng, TFLM mặc định thực thi các toán tửbằng kernel tham chiếu (reference
kernel) viết bằng C thuần, vốn chạy chậm. Đểkhai thác sức mạnh của ESP32-S3, Espressif cung cấp thư
viện ESP-NN espressif2023espnn chứa các kernel toán học (tích chập, tích chập tách kênh, kết nối đầy
đủ, gộp...) được viết tay bằng hợp ngữvà tối ưu cho tập lệnh SIMD véc-tơ của lõi Xtensa LX7. Khi esp-
tflite-micro được biên dịch cùng ESP-NN, các toán tửtương ứng tựđộng được thay bằng kernel tăng
tốc, mang lại tốc độcao gấp nhiều lần so với kernel tham chiếu. Điểm mấu chốt — và cũng là ràng buộc
định hình toàn bộthiết kếkiến trúc mô hình ởChương 4 và Chương 5 — là chỉnhững toán tửnằm trong
danh sách được ESP-NN hỗtrợmới được tăng tốc, do đó mô hình phải được xây dựng hoàn toàn từcác toán
tửthân thiện phần cứng này.
Bảng 2.1 liệt kê các toán tửmạng nơ-ron tiêu biểu được ESP-NN tăng tốc trên ESP32-S3, kèm hệsố
tăng tốc so với kernel tham chiếu C thuần (ANSI C).
18


---

## Trang 33

CHƯƠNG 2. CƠ SỞLÝ THUYẾT VÀ CÔNG NGHỆSỬDỤNG
Bảng 2.1: Các toán tửmạng nơ-ron được ESP-NN tăng tốc trên ESP32-S3 (INT8)
Toán tử(Operator)
Vai trò trong mạng
Hệsốtăng tốc
Tích chập điểm 1 × 1 (Pointwise)
Trộn thông tin giữa các kênh
8,0–14,2×
Hàm kích hoạt ReLU6
Phi tuyến, chặn biên [0, 6]
11,5×
Max Pooling
Hạmẫu, bắt đỉnh tín hiệu
7,8×
Fully Connected (Dense)
Lớp phân loại đầu ra
7,8×
Tích chập tách kênh (Depthwise)
Lọc đặc trưng theo từng kênh
4,5–6,3×
Tích chập chuẩn 3 × 3
Trích đặc trưng theo thời gian
5,5×
Average Pooling / GAP
Gộp trung bình toàn cục
3,6×
Cộng / Nhân phần tử(Add/Mul)
Kết nối tắt, hiệu chỉnh kênh
3,5–3,8×
Softmax
Chuẩn hóa xác suất lớp
1,4×
Các sốliệu trên được trích từtài liệu chính thức của ESP-NN espressif2023espnn (đo trên ESP32-S3 ở
240 MHz, bộnhớđệm dữliệu 64 KB). Ởcấp độtoàn mô hình, mức tăng tốc còn ấn tượng hơn nhờtác động
cộng dồn: ví dụmô hình Person Detection (INT8) giảm thời gian suy luận từ2300 ms xuống chỉcòn 54 ms
khi bật ESP-NN espressif2024esptflitemicro. Ngược lại, các toán tửnằm ngoài danh sách này — điển hình
là LSTM/GRU, tích chập giãn nở(dilated convolution) và các hàm sigmoid/tanh — không có kernel tối ưu
nên phải chạy bằng kernel tham chiếu chậm; đây chính là lý do chúng bịloại khỏi thiết kếmô hình của đồ
án (xem Chương 4).
2.4.5
Các thông sốđặc trưng khi triển khai mô hình TinyML lên vi điều khiển
Sau khi lượng tửhóa xong, mô hình TinyML phải vượt qua một khâu đóng gói và triển khai đặc thù để
hoạt động được trong môi trường vi điều khiển không có hệđiều hành nặng. Có ba thông sốkỹthuật quan
trọng nhất phản ánh trực tiếp chi phí tài nguyên và hiệu năng của mô hình trên chip: mảng trọng số(bộnhớ
Flash), tensor arena (bộnhớRAM) và thời gian suy luận.
Mảng trọng sốmô hình trong Flash (model_data.cc/.h)
Khác với môi trường máy tính nơi tệp .tflite được đọc từđĩa qua hệthống tập tin, vi điều khiển
chạy TFLM không có filesystem thông thường trong quá trình suy luận. Đểđưa mô hình lên chip, tệp nhị
phân .tflite — vốn là một FlatBuffer chứa toàn bộcấu trúc đồthị, trọng sốINT8 và tham sốlượng tử
hóa — được chuyển đổi thành một mảng hằng sốkiểu byte trong C bằng lệnh xxd -i. Mảng này, thường
đặt trong cặp tệp model_data.cc/.h, được biên dịch thẳng vào firmware và nằm trong vùng nhớFlash
(ROM) của chip. Tại thời điểm khởi động, TFLM nhận một con trỏtới mảng này và dựng lại đồthịtính
toán mà không cần đọc/ghi bộnhớđộng, bảo đảm tính xác định (determinism) tuyệt đối.
Một yêu cầu quan trọng khi sinh tệp này là phải xác định đầy đủdanh sách toán tử(ops) mà mô hình sử
dụng đểcấu hình MicroMutableOpResolver trong C++. Việc thiếu sót dù chỉmột toán tửẩn (ví dụ:
MAX_POOL_2D được ánh xạngầm từMaxPooling1D, hay STRIDED_SLICE xuất hiện do cắt tensor)
sẽkhiến thiết bịcrash ngay khi khởi động với lỗi “Didn’t find op for builtin opcode”. Trong đồán, công
cụexport_tflite_with_ops.py xửlý vấn đềnày bằng cách phân tích trực tiếp cấu trúc FlatBuffer
thay vì dùng API cấp cao của TFLite vốn hay bỏsót op ẩn, rồi nhúng sẵn gợi ý resolver vào phần comment
của tệp .cc sinh ra.
Tensor Arena (Vùng nhớtĩnh cho tensor trung gian)
TFLM không sửdụng cấp phát bộnhớđộng (malloc/new) trong quá trình suy luận. Thay vào đó, mọi
tensor kích hoạt trung gian (intermediate activation tensor), vùng đệm tính toán của kernel (scratch buffer),
và siêu dữliệu của interpreter đều được đặt vào một vùng nhớliên tục duy nhất do lập trình viên khai báo
trước, gọi là tensor arena. Đây là một mảng uint8_t có kích thước cốđịnh, thường được khai báo dưới
dạng biến tĩnh toàn cục đểnằm trong vùng SRAM của chip:
constexpr int TENSOR_ARENA_SIZE = 32 * 1024;
// ví dụ: 32 KB
alignas(16) static uint8_t tensor_arena[TENSOR_ARENA_SIZE];
19


---

## Trang 34

CHƯƠNG 2. CƠ SỞLÝ THUYẾT VÀ CÔNG NGHỆSỬDỤNG
Kích thước tensor arena cần thiết phụthuộc vào: (i) kích thước của tensor kích hoạt lớn nhất trong đồthị,
(ii) dung lượng vùng đệm tạm thời mà các kernel ESP-NN yêu cầu, và (iii) overhead của interpreter. Đáng
chú ý, khi bật cờtối ưu ESP-NN, kích thước Tensor Arena thường tăng thêm từ3 KB đến 10 KB so với khi
chạy bằng kernel tham chiếu ANSI-C thuần. Nguyên nhân là do các kernel tối ưu hóa (như kỹthuật Im2Col
cho tích chập, hay các bộđệm trung gian cho SIMD véc-tơ) yêu cầu cấp phát thêm vùng nhớđệm tạm thời
(scratch buffers) và thực hiện căn lềbộnhớ(memory alignment) đểCPU có thểnạp dữliệu hàng loạt. Sự
đánh đổi một lượng nhỏSRAM này là hoàn toàn xứng đáng đểđổi lấy tốc độsuy luận nhanh gấp nhiều
lần (từ4-6 lần). Trên thực tế, tensor arena được khai báo là một mảng tĩnh kiểu uint8_t với kích thước
định sẵn, ví dụalignas(16) static uint8_t tensor_arena[N], và truyền cho interpreter khi
khởi tạo. Nếu kích thước N nhỏhơn mức cần thiết, hàm interpreter.AllocateTensors() trảvề
lỗi và firmware không thểkhởi động. Đểxác định kích thước tối thiểu chính xác, TFLM cung cấp hàm
interpreter.arena_used_bytes() trảvềlượng bộnhớthực sựđã dùng sau khi cấp phát thành
công — đây là giá trịđược ghi nhận và báo cáo trong tệp report_*_firmware.txt của từng thí
nghiệm dưới trường “Tensor Arena (RAM) sửdụng”. Tensor arena là một trong hai tài nguyên khan hiếm
nhất của vi điều khiển cần kiểm soát chặt, tài nguyên còn lại là dung lượng Flash đểchứa trọng sốmô hình.
Thời gian suy luận (Inference Latency)
Thời gian suy luận là khoảng thời gian tính từkhi gọi interpreter.Invoke() đến khi hàm này trả
về, bao gồm toàn bộquá trình tính toán của mọi toán tửtrong đồthịtheo đúng thứtựtopology. Đây là chỉ
sốphản ánh trực tiếp khảnăng đáp ứng thời gian thực của hệthống và được đo bằng bộđếm thời gian độ
phân giải cao (esp_timer_get_time() trảvềmicro-giây) ngay trước và sau lời gọi.
Thời gian suy luận bịchi phối bởi ba yếu tốchính. Thứnhất, kiến trúc mô hình: sốlượng toán tử, kích
thước bản đồđặc trưng (feature map) và sốkênh trong mỗi lớp quyết định tổng sốphép tính nhân–cộng cần
thực hiện. Thứhai, mức độtăng tốc ESP-NN: như đã đềcập ởBảng 2.1, các toán tửđược ESP-NN hỗtrợ
(tích chập tiêu chuẩn, tích chập tách kênh, dense, max pooling...) chạy nhanh hơn nhiều lần so với kernel
tham chiếu; do đó, cùng một sốphép tính nhưng mô hình dùng toán tửnằm ngoài danh sách (như tích chập
giãn nởhay sigmoid) sẽchậm hơn đáng kể. Thứba, tốc độxung nhịp và bộnhớđệm: ESP32-S3 chạy
ở240 MHz với bộđệm dữliệu 64 KB; nếu tensor arena vượt quá sức chứa SRAM tích hợp và tràn sang
PSRAM, băng thông truy cập chậm hơn sẽlàm tăng latency.
Trong ngữcảnh của bài toán nhận diện hành vi với cửa sổdữliệu 2 giây (200 mẫu ở100 Hz), thời gian
suy luận cần thỏa mãn ràng buộc: nếu hệthống xửlý cửa sổtrượt liên tục (sliding window), inference phải
hoàn thành trong thời gian nhỏhơn chu kỳlấy mẫu cửa sổđểkhông gây trễtích lũy. Kết quảđo thực tếtrên
phần cứng thật của từng mô hình trong đồán được trình bày chi tiết tại Chương 4.
2.5
Hệquản trịCơ sởdữliệu
Hệthống ứng dụng kiến trúc cơ sởdữliệu kép (Dual-Database) đểxửlý hiệu quảhai loại dữliệu có
tính chất hoàn toàn khác biệt.
2.5.1
Cơ sởdữliệu chuỗi thời gian InfluxDB
Dữliệu thu thập từcác cảm biến IoT (gia tốc, sốbước chân, mức pin) mang tính chất chuỗi thời gian
(time-series), tức là được sinh ra liên tục, sốlượng cực lớn và chỉđược ghi nối tiếp chứhiếm khi bịsửa đổi.
Đối với loại dữliệu này, các cơ sởdữliệu quan hệtruyền thống sẽnhanh chóng bịquá tải.
Do đó, đồán sửdụng InfluxDB, một hệquản trịcơ sởdữliệu chuỗi thời gian chuyên biệt. InfluxDB lưu
trữdữliệu theo cấu trúc Measurement (bảng), Tags (thẻphân loại có đánh chỉmục, ví dụ: device_id),
và Fields (giá trịthực tế, ví dụ: accX, accY). Với cơ chếnén dữliệu cực tốt và ngôn ngữtruy vấn Flux
mạnh mẽ, InfluxDB có thểđáp ứng hàng chục nghìn luồng ghi (write) mỗi giây và truy xuất dữliệu lịch sử
cực nhanh đểvẽbiểu đồgiám sát.
20


---

## Trang 35

CHƯƠNG 2. CƠ SỞLÝ THUYẾT VÀ CÔNG NGHỆSỬDỤNG
2.5.2
Cơ sởdữliệu quan hệPostgreSQL
Ngược lại với dữliệu cảm biến, các thông tin vềhồsơ bệnh nhân, danh sách thiết bị, phân quyền y tá và
lịch sửcảnh báo lại có tính quan hệchặt chẽvà yêu cầu tính toàn vẹn dữliệu (ACID) tuyệt đối. Đểgiải quyết
bài toán này, đồán sửdụng PostgreSQL - hệquản trịcơ sởdữliệu quan hệmã nguồn mởmạnh mẽnhất
hiện nay. PostgreSQL xửlý việc liên kết (JOIN) các bảng dữliệu phức tạp, đảm bảo rằng một thiết bịtại một
thời điểm chỉđược gán cho một bệnh nhân duy nhất (Unique Constraint), và duy trì tính nhất quán cho toàn
bộhệthống quản trị. Đặc biệt, PostgreSQL được thiết kếtheo kiến trúc Đa khách thuê (Multi-tenancy),
bổsung trường org_id vào các bảng nhằm cách ly dữliệu an toàn giữa các viện dưỡng lão khác nhau.
2.6
Nền tảng Web và Dịch vụBackend
2.6.1
Framework phát triển Backend FastAPI
Trái tim của máy chủhệthống được xây dựng bằng FastAPI, một web framework hiện đại và hiệu năng
cao dành cho Python ramirez2023fastapi.
• Hiệu năng cao và Bất đồng bộ(Async): FastAPI hỗtrợxửlý bất đồng bộ(Asynchronous) gốc thông
qua ASGI. Điều này cực kỳquan trọng khi Backend phải đồng thời lắng nghe hàng trăm thông điệp
từMQTT Broker, ghi vào InfluxDB và phục vụcác HTTP Request từFrontend mà không bịchặn
luồng (blocking).
• Xác thực dữliệu tựđộng: Nhờtích hợp chặt chẽvới thư viện Pydantic, FastAPI tựđộng kiểm tra
tính hợp lệcủa các gói tin JSON gửi lên, giảm thiểu đáng kểlỗi do dữliệu không đúng định dạng.
• Tài liệu API tựsinh: FastAPI tựđộng tạo ra tài liệu API tương tác trực quan (Swagger UI), giúp quá
trình kiểm thửvà tích hợp với Frontend diễn ra trơn tru, nhanh chóng.
Hình 2.8: Giao diện tài liệu API Swagger tựsinh từFastAPI
2.6.2
Framework Frontend Next.js và Tailwind CSS
Giao diện quản lý dành cho nhân viên y tế(Dashboard) được xây dựng bằng Next.js (phiên bản App
Router) kết hợp cùng công cụđóng gói Turbopack, một framework phát triển dựa trên thư viện ReactJS.
• Next.js: Khác với ReactJS thuần túy (chỉrender ởphía client), Next.js cung cấp khảnăng kết hợp
giữa Server-Side Rendering (SSR) và Client-Side Rendering (CSR) vercel2023nextjs. Nhờđó, ứng
dụng tải trang cực nhanh, tối ưu trải nghiệm người dùng và giúp bảo mật các khóa truy cập API quan
trọng ởphía máy chủ.
• Quản lý trạng thái (State Management): Hệthống ứng dụng TanStack Query đểtối ưu hóa việc
21


---

## Trang 36

CHƯƠNG 2. CƠ SỞLÝ THUYẾT VÀ CÔNG NGHỆSỬDỤNG
gọi API, quản lý bộnhớđệm (caching) và đồng bộdữliệu với máy chủ, kết hợp với Zustand đểquản
lý các trạng thái giao diện cục bộmột cách nhẹnhàng.
• Tailwind CSS và Shadcn UI: Đây là một framework CSS theo phong cách Utility-first kết hợp cùng
thư viện UI components hiện đại tailwind2023css. Thay vì phải viết các file CSS độc lập, lập trình
viên áp dụng trực tiếp các class định dạng ngay trong JSX. Công cụnày giúp tạo ra một giao diện
Web trực quan, độtùy biến cao, hỗtrợthiết kếđáp ứng (Responsive Design) mượt mà.
22


---

## Trang 37

CHƯƠNG 3. PHƯƠNG PHÁP VÀ GIẢI PHÁP ĐỀXUẤT
3.1
Quy Trình Tiền XửLý và Phân Tích Phân BốDữLiệu
Quá trình xây dựng một hệthống học sâu hiệu quảtrên thiết bịbiên đòi hỏi dữliệu huấn luyện phải
được tinh chỉnh kỹlưỡng đểtận dụng tối đa cấu trúc phần cứng. Tất cảcác mô hình trong đồán đều được
huấn luyện trên cơ sởdữliệu SisFall với một quy trình tiền xửlý được thiết kếđặc thù nhằm giảm thiểu
khối lượng tính toán mà vẫn bảo toàn các đặc trưng động học quan trọng.
3.1.1
Tiền xửlý và chuẩn hóa đầu vào
Tần sốlấy mẫu gốc của cảm biến trong SisFall là 200 Hz. Đểtối ưu hóa cho cấu hình phần cứng nhúng,
đồán tiến hành giảm tần sốlấy mẫu (downsampling) bằng cách lấy mẫu xen kẽ, đưa tần sốvề100 Hz. Việc
giảm một nửa sốlượng điểm dữliệu giúp tiết kiệm đáng kểbộnhớvà giảm tải khối lượng phép tính tích
chập, trong khi tần số100 Hz vẫn hoàn toàn đáp ứng định lý Nyquist đểbắt được mọi dao động của hành vi
con người.
Sau khi hạlấy mẫu, dữliệu được chuẩn hóa vềmiền giá trị[−1, 1] trước khi đưa vào mạng nơ-ron nhằm
cải thiện khảnăng hội tụvà phục vụcho quá trình lượng tửhóa (quantization INT8). Dải đo tối đa của gia
tốc được cấu hình là ±8g (với giới hạn là 8 đểchia tỷlệ), và vận tốc góc là ±500 dps (chia cho 500). Việc
lựa chọn ngưỡng vận tốc góc 500 dps thay vì 2000 dps là một thiết kếquan trọng dựa trên phân tích phân
bốthống kê. Quá trình phát triển các phiên bản đầu tiên từng xuất hiện lỗi trong đơn vịcủa dữliệu vận tốc
góc (sửdụng rad/s thay vì dps), vô tình làm tín hiệu gyro khi lượng tửhóa vềchuẩn INT8 trởnên cực kỳbé.
Hậu quảlà các mô hình thời kỳđầu (như v25) mất đi sựnhạy bén không gian do "mù" con quay hồi chuyển,
dù quá trình huấn luyện diễn ra rất dễdàng do nhiễu đã bịloại bỏ. Khắc phục lỗi này, đồán đã tiến hành
khảo sát toàn diện phân bốgiá trịcủa tập dữliệu đểchọn ra ngưỡng tối ưu nhất.
3.1.2
Phân tích phân bốdữliệu và lựa chọn ngưỡng cắt
Đểtìm ra giới hạn tối ưu cho thang đo phần cứng mà không làm xén mất (clipping) dữliệu của các sự
kiện khốc liệt, toàn bộtập dữliệu SisFall đã được phân tích bách phân vị(percentiles).
Hình 3.1 minh họa biểu đồphân bố(theo thang logarit cơ số10) của ba trục gia tốc và tổng hợp véc-tơ
gia tốc (SVM). Ởbách phân vị99,9%, mức gia tốc lớn nhất (của trục Y và SVM) chỉxoay quanh mốc 4,5 g
đến 5,2 g. Việc đồán chọn cấu hình thang đo phần cứng ±8 g đã bao phủhoàn toàn mọi dao động mạnh
nhất của các cú ngã, giữlại trọn vẹn thông tin xung lực mà không bịcắt xén hay bão hòa cảm biến.
23


---

## Trang 38

CHƯƠNG 3. PHƯƠNG PHÁP VÀ GIẢI PHÁP ĐỀXUẤT
Hình 3.1: Phân bốcác trục gia tốc của bộdữliệu SisFall và ngưỡng cắt tối ưu.
Tương tự, Hình 3.2 biểu diễn phân bốcủa vận tốc góc. Thống kê bách phân vịcho thấy trong gần 95%
thời gian hoạt động, tốc độxoay người (RMS) chỉnằm dưới 111 dps. Ngay cảởmức 99,9% đại diện cho
các pha lộn vòng hoặc vấp ngã mạnh nhất, tốc độxoay cực đại cũng chỉchạm mức 463,57 dps. Phân tích
này là minh chứng rõ ràng đểthiết lập thang đo ±500 dps cho cảm biến con quay hồi chuyển. Nếu chọn
thang đo phổbiến 2000 dps, một lượng lớn độphân giải sẽbịlãng phí trong dải từ500–2000 dps, dẫn đến
khi nén tín hiệu xuống mức 8-bit (INT8), các chấn động tinh vi của những hành vi tĩnh sẽbịlàm tròn về
không, khiến mô hình bịmất thông tin.
24


---

## Trang 39

CHƯƠNG 3. PHƯƠNG PHÁP VÀ GIẢI PHÁP ĐỀXUẤT
Hình 3.2: Phân bốcác trục vận tốc góc của bộdữliệu SisFall và ngưỡng cắt tối ưu.
3.1.3
Kỹthuật trích xuất cửa sổvà tăng cường dữliệu
Dữliệu chuỗi thời gian liên tục được phân chia thành các đoạn ngắn (windowing) có độdài 200 mẫu
(tương đương 2 giây ởtần số100 Hz). Thay vì kỹthuật trượt cửa sổ(sliding window) truyền thống, hệthống
áp dụng kỹthuật cắt theo sựkiện (event-based windowing) nhằm giải quyết nhiễu nhãn. Kỹthuật trượt cửa
sổchỉáp dụng cho các hành động mang tính chu kỳliên tục như Đi bộ(Walk) và Chạy bộ(Run). Đối với
các chuỗi hành động chứa nhiều thao tác chuyển đổi hay nhiễu (vấp, nhảy), thuật toán tính giá trịRMS của
vận tốc góc. Mỗi vùng liên tục có RMS vượt ngưỡng 20 dps được gom thành một sựkiện và hệthống chỉ
trích xuất duy nhất một cửa sổ2 giây căn đúng vào đỉnh của sựkiện đó. Kỹthuật này giúp mô hình chống
nhiễu cực tốt khi đối mặt với các hành động có nhiều đỉnh phụ. Những đoạn dữliệu nằm tĩnh lặng (dưới
ngưỡng) sẽđược tựđộng tách ra và gán nhãn Idle.
Ngoài ra, nhằm gia tăng tính tổng quát cho mô hình khi dựđoán hành vi của các đối tượng có vóc dáng
và sức mạnh cơ bắp khác biệt, đồán áp dụng kỹthuật tăng cường dữliệu (Data Augmentation) chuyên biệt
cho lớp chuyển tiếp (Trans). Thay vì dịch chuyển không gian (sliding shift) dễgây sai lệch nhãn đỉnh, tín
hiệu của lớp này được nhân với các hệsốbiên độtỷlệngẫu nhiên là 0,9 và 1,1. Quá trình này mô phỏng
sựbiến thiên cường độlực thực tếkhi thay đổi từngười cao tuổi sang người trẻtuổi, góp phần lớn vào khả
năng chịu lỗi (robustness) của mô hình đềxuất.
3.2
Chiến Lược Thiết KếNhãn Phân Loại Nhằm Giảm Thiểu Cảnh Báo Sai
3.2.1
Bài toán
Trong giai đoạn phát triển đầu tiên (v1–v12), hệthống sửdụng sơ đồphân loại bốn nhãn gồm Walk,
Run, Static/ADL và Fall. Nhãn Static/ADL được thiết kếđểgộp tất cảcác hoạt động còn lại không thuộc di
chuyển hay té ngã, bao gồm đứng yên, ngồi, nằm, cúi người và chuyển đổi tư thế. Tuy nhiên, trong quá trình
kiểm thửthực tế, hệthống liên tục phát sinh cảnh báo sai (False Positive) khi người dùng thực hiện các thao
tác chuyển tư thếthông thường như ngồi xuống, đứng dậy hay nằm xuống từtư thếngồi.
Phân tích tín hiệu cho thấy nguyên nhân cốt lõi: các hành động chuyển tư thếnày tạo ra xung gia tốc tức
thời có biên độvà hình thái (morphology) rất tương đồng với xung gia tốc của cú ngã thực sự. Khi bịgộp
25


---

## Trang 40

CHƯƠNG 3. PHƯƠNG PHÁP VÀ GIẢI PHÁP ĐỀXUẤT
vào nhãn Static/ADL — vốn được mô hình kỳvọng là trạng thái yên tĩnh — mô hình không có cơ sởđểhọc
ranh giới phân biệt rõ ràng giữa chuyển động đột ngột có chủý và té ngã ngoài ý muốn, dẫn đến xác suất
dựđoán nhãn Fall cao một cách bất thường khi gặp các mẫu chuyển tư thế.
3.2.2
Giải pháp
Giải pháp được đềxuất là bổsung một nhãn chuyên biệt Trans (Transition — Chuyển tiếp) đểtách biệt
hoàn toàn các hành vi chuyển đổi tư thếra khỏi cảnhóm trạng thái tĩnh lẫn nhóm té ngã. Trước khi chốt
phương án năm nhãn, đồán cũng đã thửcấu hình sáu nhãn bằng cách tách thêm hai trạng thái tĩnh Nằm
(Lie) và Đứng/Ngồi (StandSit); tuy nhiên cảhai trạng thái này đều có véc-tơ gia tốc trỏgần như cùng hướng
trọng lực với biên độdao động rất thấp, gần như không thểphân biệt qua tín hiệu IMU, và cũng không mang
ý nghĩa lâm sàng khác biệt đủđểphân loại riêng — do đó chúng được gộp lại thành siêu nhãn Idle. Với sơ
đồnăm nhãn chốt gồm Walk, Run, Idle, Trans và Fall, mô hình được cung cấp đủbối cảnh ngữnghĩa đểhọc
được ranh giới quyết định riêng biệt cho mỗi loại động học. Cụthể, nhãn Idle chỉchứa các trạng thái thực
sựtĩnh (đứng yên, ngồi, nằm), trong khi nhãn Trans gộp tất cảcác thao tác chuyển đổi tư thếtừbộdữliệu
SisFall. Bảng 3.1 trình bày chi tiết ánh xạnhãn, trong đó đáng chú ý là nhãn Idle và Trans cùng được trích
xuất từnhóm mã hoạt động D07–D16: ban đầu phương pháp phát hiện đỉnh SVM được áp dụng nhưng đỉnh
SVM dễbịnhiễu bởi bước chân mạnh; tiêu chí gán nhãn sau đó được cải tiến sang dùng giá trịRMS của
con quay hồi chuyển với ngưỡng kích hoạt > 20 dps — mỗi vùng vượt ngưỡng xác định một sựkiện chuyển
tiếp và được cắt một cửa sổ2 giây căn vào đỉnh sựkiện đểgán nhãn Trans; các đoạn không vượt ngưỡng
(xác định theo hướng véc-tơ trọng lực) được gán nhãn Idle.
Bảng 3.1: Ánh xạnhãn phân loại và mã hoạt động SisFall
Nhãn
Mã SisFall
Phương pháp xác định
Walk
D01, D02, D05, D06
Đi bộchậm/nhanh, leo/xuống cầu thang
Run
D03, D04
Chạy bộchậm/nhanh
Idle
D07–D16 (đoạn không vượt
ngưỡng)
Gyro RMS ≤20 dps — vùng tĩnh theo hướng trọng
lực
Trans
D07–D16 (vùng vượt ngưỡng)
Gyro RMS > 20 dps — 1 cửa sổcăn vào đỉnh sựkiện
Fall
F01–F15
Toàn bộsựkiện ngã
Song song với việc bổsung nhãn, một chiến lược đa lớp đểxửlý mất cân bằng dữliệu cũng được áp
dụng. Trọng sốlớp được tính toán tựđộng bằng phương pháp class_weight=‘balanced’ của scikit-
learn và được nhân thêm hệsố3,0 cho nhãn Fall đểbù đắp tỷlệmẫu thấp. Hàm mất mát sửdụng kỹthuật
làm mờnhãn (Label Smoothing với ε = 0,1) nhằm giảm sựquá tựtin của mô hình vào một nhãn duy nhất,
từđó cải thiện khảnăng hiệu chỉnh xác suất (calibration). Cuối cùng, ngưỡng quyết định cho nhãn Fall được
hạxuống θ = 0,25 thay vì ngưỡng mặc định 0,5, phản ánh ưu tiên tối đa hóa Recall trong bối cảnh y tế
khẩn cấp, nơi hậu quảcủa việc bỏsót một cú ngã nghiêm trọng hơn nhiều so với một cảnh báo nhầm.
3.2.3
Kết quả
Việc chuyển từsơ đồbốn nhãn sang năm nhãn chứng minh hiệu quảrõ rệt trong việc giảm thiểu cảnh
báo sai từcác hoạt động sinh hoạt hàng ngày, đặc biệt trong bài kiểm thửvới kịch bản chuyển tư thếnhanh.
Ngoài ra, sơ đồphân loại năm lớp còn mang lại giá trịứng dụng bổsung: Backend có thểtổng hợp sốliệu
vận động hàng ngày từcác nhãn Walk, Run và Idle đểxây dựng báo cáo mức độhoạt động thểchất (activity
level) của người cao tuổi, mởrộng khảnăng theo dõi sức khỏe của hệthống vượt ra ngoài chức năng phát
hiện té ngã đơn thuần.
3.3
Chiến Lược Kiểm Soát ĐộTin Cậy và Tần Suất Cảnh Báo Ngã
3.3.1
Cơ chếxác nhận ngã hai pha (Post-Impact Confirmation)
Mặc dù chiến lược năm nhãn phân loại đã cải thiện đáng kểđộchính xác, ngưỡng θ = 0,25 dành cho
nhãn Fall (nhằm ưu tiên Fall Recall, xem Mục 3.2) khiến hệthống trởnên rất nhạy. Điều này dẫn đến một
26


---

## Trang 41

CHƯƠNG 3. PHƯƠNG PHÁP VÀ GIẢI PHÁP ĐỀXUẤT
sốcảnh báo dương tính giả(false positive) lẻtẻtừcác động tác sinh hoạt có độxóc nảy giống va đập như
ngồi phịch xuống ghế, nhảy, hoặc đặt mạnh thiết bị. Cơ chếthời gian chờ(cooldown) chỉchống lặp lại cảnh
báo liên tiếp, không giải quyết được việc báo sai.
Đểkhắc phục, đồán đềxuất bổsung cơ chếxác nhận ngã hai pha (Post-Impact Confirmation). Ý tưởng
chủđạo là giữnguyên mô hình học máy đóng vai trò bộkích hoạt nhạy (trigger) đểbảo toàn Recall, nhưng
không phát cảnh báo ngay. Thay vào đó, hệthống chuyển sang pha xác nhận hậu va chạm, tiến hành quan
sát tư thếcủa đối tượng trong một khoảng thời gian chờgọi là fall_confirm_window (tính bằng giây).
Tín hiệu xác nhận được kích hoạt khi đa sốcác cửa sổsuy luận trong thời gian quan sát trảvềlớp Idle
và góc nghiêng Roll của thiết bịrơi vào vùng tư thếnằm (nằm ngoài khoảng [60◦, 90◦] ∪[−90◦, −60◦]).
Khi đó, trạng thái ngã được xác nhận (CONFIRMED) và hệthống phát cảnh báo. Ngược lại, nếu đối tượng
hồi phục lại tư thếbình thường (mô hình dựđoán lớp Walk/Run kết hợp với tư thếđứng), hệthống sẽhủy
báo động (ABORT), loại bỏcác báo giả. Cơ sởcủa cơ chếnày dựa trên nguyên lý đồng pha hậu va chạm
(post-impact) giữa Recall và Precision: người ngã thật sựthường nằm lại trên sàn, trong khi người thực hiện
thao tác sinh hoạt (như ngồi phịch) sẽđứng dậy ngay sau đó.
Vềmặt hiện thực, cơ chếtrên được biểu diễn bằng một Máy trạng thái hữu hạn (FSM) phụvới hai trạng
thái ổn định FALL_FSM_NORMAL và CONFIRMING nằm hoàn toàn bên trong svc_ai, tách biệt với FSM
hệthống cấp cao. Thiết kếchi tiết của FSM này — bao gồm điều kiện chuyển trạng thái, thời gian quan sát
fall_confirm_window cấu hình được từxa, và tích hợp với cờcomms-critical — được trình bày tại
Mục 4.4.5 (Hình 4.12).
Bên cạnh đó, cơ chếxác nhận được củng cốbằng một bằng chứng vật lý độc lập: bộphát hiện theo từng
mẫu trên biên độvector gia tốc thô (SVM).
SV M =
q
a2x + a2y + a2z
(3.1)
Thiết kếcốý sửdụng gia tốc thô thay vì dữliệu đã qua bộlọc Kalman nhằm không làm cùn mất các
đỉnh xung lực. Trạng thái rơi tựdo (free-fall) được nhận diện khi SVM giảm xuống dưới 0,6g, và va chạm
(impact) xảy ra khi SVM vượt ngưỡng 2,5g. Các chỉsốnày hoạt động như một bộtăng cường độtin cậy
(boost), chứkhông phải là điều kiện bắt buộc, đảm bảo không làm cắt giảm Recall của mô hình.
Hai cơ chếtrên bổtrợnhau thành một mạch bảo đảm độtin cậy cảnh báo khép kín: xác nhận hậu va
chạm lọc báo giảởtầng quyết định thuật toán, còn cờcomms-critical được duy trì bởi sys_manager
trong kiến trúc firmware (Mục 4.2) ngăn svc_network ngắt kết nối mạng trong đúng pha xác nhận và
phát báo động, đảm bảo cảnh báo đã xác nhận chắc chắn được gửi đến máy chủ.
3.3.2
Điều Chỉnh Ngưỡng Kích Hoạt và Kiểm Soát Tần Suất Cảnh Báo
Cơ chếxác nhận hậu va chạm (Mục 3.3.1) hoạt động phối hợp với hai tham sốcấu hình bổtrợđểtạo
thành chiến lược chống báo động giảba tầng.
Ngưỡng kích hoạt phát hiện ngã (fall_threshold). Đây là ngưỡng xác suất θ mà bộphân loại
HAR phải vượt qua đểchuyển FSM sang trạng thái CONFIRMING: P(Fall) ≥θ. Giá trịmặc định trên
firmware được thiết lập ởmức nhạy 0,25 (khớp với ngưỡng θ lựa chọn khi huấn luyện mô hình), với dải
cấu hình hợp lệ[0,15; 0,95]. Việc sửdụng ngưỡng thấp như vậy nhằm tối đa hóa độnhạy (ưu tiên Fall
Recall), chấp nhận việc hệthống có thểchuyển sang pha CONFIRMING nhiều lần. Điểm then chốt là
fall_threshold chỉkiểm soát việc vào pha xác nhận, không trực tiếp quyết định có phát cảnh báo hay
không — vai trò đó thuộc vềFSM CONFIRMING. Nhờsựtách biệt này, hệthống đạt được độnhạy (Recall)
cao ởtầng kích hoạt, trong khi pha CONFIRMING đóng vai trò bù đắp lại độchính xác (Precision), đảm
bảo không đểbáo động giảđến được người dùng cuối.
Thời gian hồi cảnh báo (fall_cooldown). Sau khi một cảnh báo ngã đã được xác nhận và gửi lên
Backend, thành phần svc_cloud áp dụng một khoảng im lặng bắt buộc (mặc định 15 giây, cấu hình được
27


---

## Trang 42

CHƯƠNG 3. PHƯƠNG PHÁP VÀ GIẢI PHÁP ĐỀXUẤT
trong dải 5–300 giây) trước khi cho phép phát cảnh báo tiếp theo. Cooldown ngắn hơn phù hợp với kịch
bản kiểm thửnhiều lần liên tiếp; cooldown dài hơn phù hợp với môi trường vận hành thực tếđểtránh nhiễu
thông báo. Thiết kếđặt cooldown tại svc_cloud thay vì svc_ai nhằm tách biệt trách nhiệm: svc_ai
luôn phát sựkiện mỗi khi phát hiện ngã, còn chính sách giới hạn tần suất cảnh báo thuộc tầng giao tiếp đám
mây (D-006).
Bốn cơ chếtạo thành một chiến lược phân tầng: (1) Chốt chặn tiền va chạm (Pre-Impact Posture Gating)
lọc bỏnhiễu do thiết bịkhông được đeo trên người (ví dụ: đặt trên mặt bàn); (2) fall_threshold kiểm
soát độnhạy ởtầng kích hoạt mô hình; (3) FSM xác nhận hậu va chạm (Mục 3.3.1) lọc báo giảởtầng quyết
định dựa trên tư thếhậu va chạm; (4) fall_cooldown giới hạn tần suất phát cảnh báo ởtầng giao tiếp.
Cảba tham số— fall_threshold, fall_cooldown và fall_confirm_window (cửa sổquan
sát FSM) — đều cấu hình được từxa qua Dashboard mà không cần nạp lại firmware, cho phép tinh chỉnh
theo đặc điểm vận động của từng bệnh nhân cụthể.
3.4
Tiến Trình Tối Ưu Hóa Kiến Trúc Mô Hình Học Sâu Tương Thích TinyML
3.4.1
Bài toán
Việc triển khai mạng nơ-ron học sâu trên vi điều khiển (TinyML) đặt ra hai ràng buộc đối nghịch nhau.
Một mặt, kiến trúc mô hình phải đủbiểu đạt đểnắm bắt được các mẫu động học phức tạp trong chuỗi tín
hiệu IMU sáu chiều với độdài 200 mẫu. Mặt khác, mô hình phải vừa với tài nguyên cực kỳhạn chếcủa
ESP32-S3 và phải có thểlượng tửhóa (quantize) sang định dạng sốnguyên 8-bit (INT8) hoặc dấu phẩy
động 32-bit (Float32) đểthực thi hiệu quảqua thư viện TensorFlow Lite Micro.
Kiến trúc CNN-LSTM ban đầu (v1–v4) gặp vấn đềnghiêm trọng ởbước lượng tửhóa: các lớp LSTM
chứa các phép tính phụthuộc tuần tự(sequential recurrent computation) không được thư viện TensorFlow
Lite Micro tối ưu tốt, dẫn đến thời gian suy luận cao và độsai sốlượng tửhóa đáng kể. Trong khi đó, tích
chập 1D (Conv1D) được cảTFLite Micro và ESP-NN (thư viện tăng tốc phần cứng tích hợp trong ESP-IDF)
hỗtrợvà tối ưu đặc biệt tốt cho kiến trúc ESP32.
3.4.2
Giải pháp
Quá trình tối ưu hóa kiến trúc diễn ra qua ba thếhệchính, mỗi thếhệtháo gỡmột nút thắt còn tồn đọng
từthếhệtrước.
Thếhệthứnhất là mô hình TCN (Temporal Convolutional Network — phiên bản v8 đến v22), thay toàn
bộkhối LSTM bằng chồng tích chập giãn nhân quả(dilated causal convolution) với hệsốgiãn tăng dần
d ∈{1, 2, 4, 8}. Việc này giải quyết hoàn toàn vấn đềlượng tửhóa và cho độchính xác cao nhất, đặc biệt
ởnhãn chuyển tiếp Trans nhờtrường tiếp nhận dài bao trọn pha động học của cú ngã. Tuy nhiên, tích chập
giãn nởkhi xuất sang TFLite lại sinh ra các toán tửxáo trộn bộnhớkhông được ESP-NN tăng tốc, khiến
thời gian suy luận lên tới hơn 2 giây trên ESP32-S3 — bất khảthi cho ứng dụng thời gian thực (chi tiết tại
Mục 4.3.2).
Thếhệthứhai là dòng CNN thuần tối ưu phần cứng (phiên bản v23 đến v30). Toàn bộtích chập giãn nở
được thay bằng tích chập tách kênh (SeparableConv1D), tích chập điểm 1 × 1, hàm kích hoạt relu6
và hạmẫu bằng strided conv kết hợp MaxPool — tất cảđều là toán tửđược ESP-NN tăng tốc — kéo thời
gian suy luận xuống dưới 20 ms. Một biến thểtrong giai đoạn này (v25) từng thửbổsung khối thặng dư
(Residual) và Squeeze-and-Excitation (SE); tuy nhiên hàm sigmoid trong SE không được tăng tốc và làm
phình siêu dữliệu của tệp INT8, nên cuối cùng kiến trúc được tinh giản thành CNN thuần. Hạn chếcòn lại
của thếhệnày là khối gộp đặc trưng GAP+GMP nén phẳng trục thời gian, khiến mô hình yếu ởhai nhãn
Idle và Trans.
28


---

## Trang 43

CHƯƠNG 3. PHƯƠNG PHÁP VÀ GIẢI PHÁP ĐỀXUẤT
Tích chập tiêu chuẩn
(Standard Conv1D)
Input
(Cin × L)
Conv1D
Nhân: K × Cin × Cout
Output
(Cout × L′)
Độphức tạp tính toán:
O(K · Cin · Cout · L)
Tích chập tách kênh
(Depthwise Separable Conv1D)
Input
(Cin × L)
Depthwise Conv1D
Nhân: K × Cin
Pointwise Conv1D (1 × 1)
Nhân: Cin × Cout
Output
(Cout × L′)
Lọc không gian
Trộn kênh
Độphức tạp tính toán:
O(K · Cin · L) + O(Cin · Cout · L)
Hình 3.3: Minh họa sựphân rã tích chập tách kênh (Depthwise Separable 1D CNN)
Kỹthuật tích chập tách kênh (Depthwise Separable Convolution) chia tách một phép tích chập tiêu chuẩn
thành hai bước độc lập: (1) Depthwise Conv: áp dụng một bộlọc không gian duy nhất (kích thước K) cho
từng kênh đầu vào riêng biệt đểtrích xuất đặc trưng cục bộ; và (2) Pointwise Conv: sửdụng nhân chập
1 × 1 đểtrộn và tổhợp tuyến tính các đặc trưng xuyên suốt các kênh.
Như được minh họa trong Hình 3.3, phép phân rã này giúp giảm đáng kểkhối lượng tính toán. Tỉlệsố
lượng phép tính giữa tích chập tách kênh và tiêu chuẩn xấp xỉbằng
1
Cout + 1
K . Nhờviệc chuyển từtích chập
giãn nởsang CNN tách kênh thuần túy, mô hình loại bỏđược hàng triệu phép tính dư thừa mà vẫn đảm bảo
độsâu biểu đạt, kéo thời gian suy luận trên vi điều khiển từhơn 2 giây xuống vỏn vẹn dưới 20 mili-giây.
Thếhệthứba — đóng góp kiến trúc trọng tâm — là mô hình v30_optimize. Sau khi một hướng
chưng cất tri thức (Knowledge Distillation) từTCN sang CNN được thửnghiệm nhưng thất bại (không thể
khắc phục giới hạn của head pooling), giải pháp là cải tiến trực tiếp kiến trúc: bổsung nhánh Flatten vào
khối gộp (head GAP+GMP+Flatten) đểgiữlại layout thời gian của bản đồđặc trưng, kết hợp tăng độsâu
và độrộng mạng. Nhờđó, v30_optimize chắt lọc được nguyên lý mô hình hóa thời gian của TCN trong
một CNN vẫn thuần toán tửESP-NN, nâng F1-Trans từ0,799 lên 0,907 (xấp xỉTCN) mà thời gian suy luận
chớp nhoáng chỉtốn 11,20 ms. Đáng chú ý, một thí nghiệm cắt bỏ(ablation) cho thấy chính khâu chưng cất
tri thức là không cần thiết: bản tắt hoàn toàn KD đạt kết quảngang bằng hoặc nhỉnh hơn mọi bản có KD,
khẳng định toàn bộthắng lợi đến từkiến trúc head chứkhông phải từnhãn mềm. Cuối cùng, việc đổi tiêu
chí chọn mô hình tốt nhất từval_loss sang val_accuracy (do val_loss không trọng sốthiên về
lớp đa số) còn nâng thêm điểm F1-Trans và đưa Fall recall lên 97,73%.
3.4.3
Kết quả
Hình 3.4 mô tảkiến trúc khối chức năng của mô hình v30_optimize với 26.629 tham số. So với biến
thểv25 trước đó, kiến trúc này loại bỏhoàn toàn khối SE và kết nối thặng dư (vốn chứa toán tửkhông được
tăng tốc), bù lại bổsung nhánh Flatten trong khối gộp đểbảo toàn thông tin theo trục thời gian — chính cải
tiến giúp vượt nút thắt nhãn Idle/Trans.
29


---

## Trang 44

CHƯƠNG 3. PHƯƠNG PHÁP VÀ GIẢI PHÁP ĐỀXUẤT
Đầu vào
(200 timesteps × 6 kênh)
Stem
Conv1D(32, k=3, s=2) + BN + ReLU6
(100, 32)
Block 1
SepConv1D(48, k=3) ×2 + ReLU6 + MaxPool(2)
(50, 48)
Block 2
SepConv1D(64, k=3) ×2 + ReLU6 + MaxPool(2)
(25, 64)
Block 3
SepConv1D(96, k=3) + ReLU6 + MaxPool(2)
(12, 96)
GMP
GAP
Flatten
Concat (1.344 đặc trưng)
Dense(5) & Softmax
Đầu ra (5 lớp hành vi)
Dropout
Hình 3.4: Sơ đồkhối kiến trúc mạng nơ-ron v30_optimize (tổng tham số: 26.629)
Bảng 3.2 tổng hợp hệsốtăng tốc của các toán tửthân thiện ESP-NN tạo nên kiến trúc này khi chạy trên
ESP32-S3.
Bảng 3.2: Hệsốtăng tốc của các toán tửESP-NN trong kiến trúc CNN tách kênh
Kỹthuật tối ưu hóa
Tăng tốc (ESP-NN)
SeparableConv1D (depthwise)
6,3×
Pointwise Conv 1 × 1
14,2×
Hàm kích hoạt relu6
11,5×
Lượng tửhóa INT8 (toàn bộ)
∼4× (bộnhớ), ∼2× (tốc độ)
Kết quảthực đo trên phần cứng cho thấy v30_optimize đạt thời gian suy luận trung bình 11,20 ms cho
một cửa sổđầu vào 200 × 6 (chưa tới 3% chu kỳcập nhật 500 ms của cơ chếcửa sổtrượt), bảo đảm dư dả
thời gian thực. Mô hình đạt độchính xác firmware 95,40% và Fall Recall 97,50%, với điểm F1 nhãn Trans
đạt 0,907 — vượt xa các biến thểCNN baseline (v30: F1-Trans 0,799) và mô hình v25 cũ (độchính xác
83,50% khi đo tham chiếu C). Như vậy, cải tiến head giữtrục thời gian kết hợp khai thác tối đa ESP-NN đã
nâng đáng kểchất lượng phân loại ởcác nhãn khó đồng thời gia tốc suy luận lên gấp nhiều lần. Kết quảso
sánh đầy đủgiữa các kiến trúc được trình bày trong các Bảng 5.2 và 5.3 tại Mục 4.3.
Đánh giá khái quát hóa qua kiểm định chéo dân số(KFold v6).
Nhận thấy ưu điểm của v30_tcn ởkhả
năng mô hình hóa ngữcảnh thời gian dài — đặc biệt trong các kịch bản kiểm tra chéo giữa người trẻvà
người già — đồán tiến hành kiểm định chéo 5 kịch bản Leave-Subjects-Out trên v30_optimize đểxác nhận
khảnăng khái quát hóa, không chỉtrên phân chia chuẩn.
30


---

## Trang 45

CHƯƠNG 3. PHƯƠNG PHÁP VÀ GIẢI PHÁP ĐỀXUẤT
Bảng 3.3: Kết quảkiểm định chéo dân số(KFold v6) của v30_optimize trên tập SisFall
Kịch bản
Mô tả
Acc.
Trans F1
Fall Recall
S1 Elderly-only
Train+Test = SE (người
già)
89,1%
0,83
†
S2 Young-only
Train+Test = SA (người
trẻ)
96,8%
0,91
99,6%
S3 TrainSE→TestSA
Già →Trẻ(cross-pop)
94,6%
0,83
95,3%
S4 TrainSA→TestSE
Trẻ→Già (cross-pop)
92,8%
0,87
98,7%‡
S5 Both
Train+Test
=
SA+SE
(hỗn hợp)
96,3%
0,92
99,5%
† S1: chỉ1/5 fold có mẫu Fall trong tập kiểm tra (375 mẫu, 0/375 phát hiện) — giới hạn dữliệu Fall của SE.
‡ S4: Fall Recall 98,7% nhưng Precision chỉ74,6% — người già chuyển tư thếsinh nhiều cảnh báo sai hơn.
Kết quảS5 (hỗn hợp cảhai nhóm) xác nhận v30_optimize đạt khảnăng khái quát hóa tốt: accuracy
trung bình 96,3%, Trans F1 ≈0,92 và Fall Recall 99,5% trên tập chưa gặp, tiệm cận kết quảphân chia
chuẩn. Kịch bản S1 bộc lộgiới hạn của tập SisFall: dữliệu Fall của người già (SE) quá ít; khi phân chia
chéo, hầu hết fold kiểm tra không có mẫu Fall đểđánh giá — đây là giới hạn dữliệu, không phải giới hạn
mô hình. Kết quảS4 cho thấy mô hình huấn luyện trên người trẻcó độnhạy Fall cao với người già (Recall
98,7%) nhưng sinh nhiều cảnh báo sai hơn (Precision 74,6%), phản ánh sựkhác biệt vềkiểu chuyển tư thế
giữa hai nhóm tuổi.
Thửnghiệm Chưng cất tri thức (KD) nhằm đóng thêm khoảng cách với TCN.
Sau khi xác nhận
v30_optimize qua KFold, đồán thực hiện thêm một thửnghiệm Chưng cất tri thức (Knowledge Distillation)
từv30_tcn sang v30_optimize, mang tên v30_kd2 (hệsốalpha = 0,5), nhằm hấp thụphân phối xác suất
mềm của TCN đểcải thiện thêm Trans F1. Kết quảđo trực tiếp trên phần cứng cho thấy v30_kd2 đạt độ
chính xác firmware 95,30%, Trans F1 = 0,945 (tăng từ0,907) và Fall Recall 97,5%, với thời gian suy luận
11,20 ms và tensor arena 28,3 KB — tài nguyên gần như không đổi so với bản không có KD. Tuy nhiên,
thí nghiệm cắt bỏ(ablation) cho thấy chính phiên bản tắt hoàn toàn KD (KD_weight=0) đạt kết quảF1
tương đương hoặc nhỉnh hơn mọi bản có KD, khẳng định phần lớn thắng lợi đến từkiến trúc head giữtrục
thời gian chứkhông phải từnhãn mềm. KD là hướng tiếp cận có giá trịđểnghiên cứu thêm, nhưng không
phải đóng góp kiến trúc trọng tâm của đồán.
3.5
Phương Pháp Lấy Mẫu IMU Chính Xác SửDụng Ngắt Phần Cứng PCNT
3.5.1
Bài toán
Độchính xác của cơ chếcửa sổtrượt 200 mẫu tại tần số100 Hz phụthuộc trực tiếp vào tính đều đặn
của khoảng cách giữa các lần lấy mẫu. Nếu tần sốlấy mẫu thực tếdao động, phổtần sốcủa tín hiệu IMU sẽ
bịdịch chuyển, gây ra sai lệch giữa phân bốđặc trưng của dữliệu trong môi trường suy luận thực tếso với
dữliệu đã dùng đểhuấn luyện mô hình.
Trong giai đoạn đầu, svc_imu sửdụng hàm vTaskDelay của FreeRTOS đểtạo chu kỳlấy mẫu
10 ms. Tuy nhiên, trình lập lịch tác vụ(scheduler) của FreeRTOS hoạt động dựa trên tick timer phần mềm
với độphân giải mặc định 1 ms (1000 tick/giây). Khi hệthống đang xửlý ngắt từmodule 4G LTE (A7680C)
hoặc thực hiện suy luận AI trong svc_ai, tick timer bịtrì hoãn, gây ra jitter tích lũy trong chuỗi lấy mẫu
và làm lệch tần sốlấy mẫu thực tếkhỏi mục tiêu 100 Hz.
3.5.2
Giải pháp
Giải pháp được triển khai là sửdụng ngoại vi PCNT (Pulse Counter — Bộđếm xung) của ESP32-S3
như một nguồn ngắt phần cứng hoàn toàn độc lập với CPU và FreeRTOS scheduler. Một bộđịnh thời phần
cứng (hardware timer) được cấu hình phát ra xung vuông tần số100 Hz vào chân GPIO được kết nối với
kênh PCNT. Mỗi khi PCNT đếm đủmột xung, Interrupt Service Routine (ISR) được kích hoạt trực tiếp
từphần cứng, không phụthuộc vào trạng thái của hệđiều hành. ISR này ghi nhận thời điểm lấy mẫu và
đưa dữliệu IMU vào hàng đợi vòng (ring buffer) của svc_imu thông qua cơ chếthông báo tác vụ(task
31


---

## Trang 46

CHƯƠNG 3. PHƯƠNG PHÁP VÀ GIẢI PHÁP ĐỀXUẤT
notification) từISR.
Kiến trúc PCNT-driven sẽloại bỏhoàn toàn sựphụthuộc của tần sốlấy mẫu vào mức tải CPU, đảm
bảo jitter dưới 1 µs so với jitter có thểlên tới vài mili giây khi sửdụng vTaskDelay. Ngoài ra, kiến trúc
ngắt phần cứng này còn tạo ra tiền đềquan trọng cho một cải tiến hiệu suất năng lượng: trong khoảng 10 ms
giữa hai ngắt PCNT liên tiếp, CPU có thểđược đặt vào trạng thái Automatic Light Sleep của FreeRTOS
(Tickless Idle). Khi ởtrạng thái này, xung nhịp CPU giảm từ240 MHz xuống còn xung nhịp tinh thểXTAL
40 MHz, ước tính tiết kiệm 30–50% điện năng so với chếđộchạy liên tục. Điều kiện tiên quyết đểkích hoạt
tính năng này là cấu hình lại nguồn xung nhịp của ngoại vi I2C và PCNT sang nguồn RTC clock đểcác
ngoại vi này duy trì hoạt động trong khi CPU ởtrạng thái ngủ.
3.5.3
Kết quảvà Định hướng phát triển
Kiến trúc PCNT-driven đã được thiết kếvà đặc tảđầy đủtrong svc_imu như bước tối ưu phần cứng
tiếp theo của dựán. Ởgiai đoạn đánh giá hiện tại, quá trình kiểm thửfirmware sửdụng một bản firmware
thửnghiệm riêng: máy tính gửi từng cửa sổdữliệu IMU (200×6) đã được tiền xửlý qua UART, MCU thực
hiện suy luận và trảnhãn kết quả— do đó kết quảinference không phụthuộc vào độchính xác tần sốlấy
mẫu trong vòng đo này.
Tính năng Automatic Light Sleep đang trong giai đoạn phát triển tiếp theo. Sau khi hoàn tất tích hợp,
hệthống dựkiến đạt mức tiêu thụđiện trung bình thấp hơn đáng kể, kéo dài thời gian sửdụng pin và nâng
cao tính khảdụng của thiết bịđeo trong môi trường viện dưỡng lão, nơi việc sạc pin thường xuyên gây bất
tiện cho cảngười cao tuổi lẫn nhân viên y tế.
3.6
Đếm Bước Chân Thông Minh Gating Theo Nhận Dạng Hoạt Động
3.6.1
Bài toán
Máy đếm bước truyền thống hoạt động theo nguyên lý phát hiện đỉnh trên tín hiệu gia tốc tổng hợp mà
không có ngữcảnh hành vi. Điểm yếu cốhữu của phương pháp này là rung lắc ngẫu nhiên, thao tác chuyển
tư thế, va chạm với vật thểhay di chuyển bằng phương tiện (xe lăn, ô tô) đều sinh ra các đỉnh gia tốc có
hình thái tương tựđỉnh bước chân, dẫn đến một lượng lớn dương tính giả(false positive). Vấn đềnày đặc
biệt nghiêm trọng với người cao tuổi — đối tượng sửdụng của hệthống — do dáng đi thường không đều và
sải chân kém ổn định, khiến biên độtín hiệu mỗi bước biến động rộng và ngưỡng phân biệt cốđịnh trởnên
thiếu đáng tin cậy.
Trong khi đó, hệthống cần sốliệu bước chân đủtin cậy đểtính quãng đường di chuyển phục vụtính
năng theo dõi mức độvận động thểchất (use case Xem thống kê vận động). Đây là chức năng theo dõi sức
khỏe chủđộng bổsung, mởrộng giá trịcủa thiết bịvượt ra ngoài đơn thuần phát hiện té ngã.
3.6.2
Giải pháp
Đồán triển khai thư viện lib_pedometer tích hợp trong tác vụsvc_imu, hoạt động per-sample
trực tiếp trên gia tốc thô (không qua bộlọc Kalman). Quyết định xửlý gia tốc thô thay vì tín hiệu đã làm
mượt xuất phát từthực tếrằng bộlọc Kalman làm giảm biên độđỉnh tức thời, vô hình trung làm cùn chính
tín hiệu đặc trưng mà thuật toán phát hiện đỉnh cần khai thác.
Pipeline đếm bước gồm ba tầng lọc tuần tự: (i) bộlọc thông dải (band-pass) dải tần [0,5; 3,5] Hz tương
ứng với nhịp bước sinh lý của con người, loại bỏrung động tần sốcao và trôi tần sốthấp không liên quan
đến bước chân; (ii) phát hiện đỉnh ngưỡng động (adaptive peak-detect) tựđiều chỉnh ngưỡng so sánh theo
mức nền tín hiệu cục bộgần đây, thích nghi với cường độbước khác nhau của từng người; (iii) thời gian trơ
(refractory period) khoảng 300 ms cho bước đi bộvà 200 ms cho bước chạy bộ, ngăn đếm đúp trên vùng
đỉnh rộng của cùng một bước chân.
Điểm cốt lõi của giải pháp là cơ chếgating theo nhận dạng hoạt động: bộđếm chỉtích lũy khi nhãn
hành vi mới nhất từbộphân loại HAR — đọc qua svc_ai_get_latest_prediction() — là Walk
hoặc Run. Khi mô hình dựđoán nhãn khác (Idle, Trans, Fall), bộđếm tạm dừng, giữnguyên giá trịtích lũy.
32


---

## Trang 47

CHƯƠNG 3. PHƯƠNG PHÁP VÀ GIẢI PHÁP ĐỀXUẤT
Độtrễnhãn HAR tối đa 0,5 giây (chu kỳcập nhật của cửa sổtrượt) là chấp nhận được, do hành vi đi bộ
hay chạy bộthay đổi chậm hơn nhiều so với chu kỳcập nhật của bộphân loại. Hình 3.5 minh họa toàn bộ
pipeline từtín hiệu thô đến hai bộđếm riêng.
Bộđếm bước được chia thành hai bộđếm độc lập walk_steps và run_steps, tương ứng với nhãn
Walk và Run; cảhai được lưu định kỳvào bộnhớflash NVS đểbảo toàn qua các lần khởi động lại. Backend
nhận hai giá trịnày qua bản tin trạng thái định kỳ, rồi áp dụng công thức sinh trắc học với hệsốsải chân
khác nhau giữa đi bộvà chạy bộđểước lượng quãng đường di chuyển theo chiều cao của bệnh nhân (chi
tiết tại Chương 5).
Gia tốc thô (ax, ay, az)
(svc_imu, per-sample)
Band-pass [ 0,5; 3,5 ] Hz
Peak-detect ngưỡng động
Trơ ≈300 ms / 200 ms
Cổng HAR
nhãn là Walk hay Run?
walk_steps++
run_steps++
Bỏqua
(Idle/Trans/Fall)
Lưu NVS định kỳ
walk_steps, run_steps
d = (walk×0,415 + run×0,5)×h
Backend: ước tính quãng đường
svc_ai_get_
latest_prediction()
Walk
Run
ngược lại
nhãn
Hình 3.5: Pipeline đếm bước chân gating theo nhận dạng hoạt động HAR (lib_pedometer trong svc_imu) —
D-010
3.6.3
Lý do và Kết quả
Ba lý do kỹthuật chính lý giải thiết kếnày. Thứnhất, việc tái sửdụng bộphân loại HAR — đã chạy liên
tục phục vụphát hiện té ngã — làm cổng lọc hành vi là một sáng kiến chi phí gần bằng không: toàn bộ
công việc phân loại hành vi đã được thực hiện cho mục đích chính, nên việc gate bộđếm bước theo nhãn
đầu ra của bộphân loại chỉtốn một phép đọc biến nguyên tửmỗi mẫu. Tuy nhiên, đổi lại cơ chếnày loại bỏ
được hầu hết nguồn dương tính giảmà pedometer truyền thống không thểxửlý bằng ngưỡng tĩnh. Đây là
ví dụđiển hình của việc biến điểm yếu kinh điển của pedometer — thiếu ngữcảnh hành vi — thành điểm
mạnh nhờkhai thác bộphân loại HAR vốn đã có sẵn trong hệthống.
Thứhai, xửlý gia tốc thô (không qua Kalman) giữnguyên biên độđỉnh tức thời, tạo điều kiện đểngưỡng
động hoạt động ổn định trên đặc trưng gốc của tín hiệu. Thứba, tách riêng walk_steps/run_steps
thay vì gộp chung thành một biến tổng là điều kiện cần thiết đểBackend áp đúng hệsốsải chân theo từng
loại vận động — dáng chạy bộcó sải chân dài hơn đáng kểso với đi bộ— mang lại ước lượng quãng đường
33


---

## Trang 48

CHƯƠNG 3. PHƯƠNG PHÁP VÀ GIẢI PHÁP ĐỀXUẤT
thực tếmà không cần phụthuộc vào module GPS.
Nhờthiết kếnày, hệthống có khảnăng cung cấp sốliệu vận động đủtin cậy đểxây dựng báo cáo
mức độhoạt động thểchất (activity level) trong dashboard, mởrộng phạm vi ứng dụng của thiết bịtừmột
thiết bịan toàn đơn thuần thành một nền tảng theo dõi sức khỏe chủđộng toàn diện hơn. Mô tảtích hợp
lib_pedometer trong svc_imu được trình bày chi tiết tại Mục 4.2 (Kiến trúc phần mềm Firmware).
3.7
Giải Pháp Đảm Bảo Toàn Vẹn DữLiệu Thu Thập Qua Lựa Chọn Đường Truyền
3.7.1
Bài toán
Chiến lược dữliệu của đồán phân tách rõ hai nguồn: bộdữliệu công khai SisFall dùng đểhuấn luyện
mô hình, còn một bộdữliệu cá nhân thu trực tiếp từthiết bịđeo thật dùng đểkiểm thửvà đánh giá. Việc
đánh giá trên dữliệu thu bằng chính phần cứng và quy trình tiền xửlý của hệthống là cần thiết, bởi SisFall
được thu trong điều kiện cảm biến và bốtrí khác, không phản ánh đầy đủđặc trưng tín hiệu mà mô hình
gặp khi vận hành thực tế.
Đểxây dựng bộdữliệu cá nhân, thiết bịphải truyền luồng dữliệu IMU thô tần số100 Hz một cách liên
tục vềmáy chủ(chếđộSTATE_STREAMING). Yêu cầu cốt lõi của dữliệu huấn luyện và đánh giá là tính
liên tục theo thời gian: mỗi cửa sổtrượt 200 × 6 phải gồm các mẫu kềnhau đúng theo trục thời gian. Khi
một gói dữliệu (batch) bịmất giữa luồng, chuỗi mẫu bịđứt quãng — hai đoạn tín hiệu không liền mạch bị
ghép thành một cửa sổ, tạo ra bản ghi sai lệch vềmặt vật lý và làm nhiễu nhãn của bộdữliệu.
Tuyến truyền 4G LTE qua module A7680C (giao thức PPPoS) không đáp ứng được yêu cầu luồng
liên tục tốc độcao này do các hạn chếphần cứng cốhữu. Thứnhất, đường UART nối giữa vi điều khiển và
module hoạt động ởtốc độ115200 baud nhưng không có điều khiển luồng phần cứng (hai chân RTS/CTS
không được nối). Khi lưu lượng tăng đột biến, bộđệm UART bịtràn, gây mất byte và làm hỏng khung dữ
liệu của giao thức PPP/HDLC. Thứhai, đường dữliệu đi vòng qua nhiều tầng (ESP32 →UART →PPP
→modem →trạm phát) khiến độtrễdao động lớn và băng thông thực tếthấp. Hệquảlà dữliệu thu
qua 4G rụng mẫu rải rác và mất giá trịcho huấn luyện hay đánh giá.
3.7.2
Giải pháp
Đồán giải quyết bằng cách tách đôi đường truyền theo ngữcảnh sửdụng, thay vì ép một tuyến duy
nhất phục vụhai nhu cầu trái ngược. Pha thu thập dữliệu sửdụng WiFi: vi điều khiển ESP32-S3 giao tiếp
trực tiếp qua ngăn xếp TCP/IP gắn liền địa chỉMAC nội bộ, kiểm soát luồng chặt ởtầng vật lý nên không
mất byte, với băng thông và độtrễdư thừa so với mức 100 Hz của luồng IMU. Pha vận hành thực địa giữ
nguyên 4G LTE, nơi tải truyền thông rất nhẹ— gói viễn trắc định kỳvà cảnh báo té ngã tức thời — hoàn
toàn phù hợp với năng lực của PPPoS. Bảng 3.4 đối chiếu hai tuyến theo các tiêu chí quyết định cho bài
toán streaming.
Bảng 3.4: Đối chiếu hai tuyến truyền cho bài toán thu luồng dữliệu IMU 100 Hz liên tục.
Tiêu chí
WiFi (STA)
4G LTE (PPPoS, A7680C)
Điều khiển luồng phần cứng
Có (tầng MAC nội bộ)
Không (thiếu RTS/CTS)
Mất byte/khung khi tải cao
Không
Có (tràn UART, hỏng khung PPP)
Băng thông khảdụng
Cao, dư thừa
Thấp
Độtrễ
Thấp, ổn định
Dao động lớn
Phù hợp streaming 100 Hz liên tục
Phù hợp
Không phù hợp
Đểmột bản firmware duy nhất phục vụcảhai ngữcảnh mà không cần biên dịch lại, hệthống tựđộng
nhận diện đường truyền ngay khi khởi động. Cơ chếnhận diện dựa trên hoạt động sớm của bus UART,
thay vì chờphản hồi lệnh AT — vốn đến muộn do module 4G cần hàng chục giây đểkhởi động xong.
Firmware lắng nghe các sựkiện báo hiệu trên bus (UART_BREAK, UART_DATA): nếu phát hiện hoạt động
bền vững, hệthống xác nhận có module và đi tuyến PPPoS; nếu bus im lặng tuyệt đối trong cửa sổquan sát,
hệthống kết luận không có module và tựchuyển sang khởi tạo WiFi. Hình 3.6 mô tảluồng quyết định này.
34


---

## Trang 49

CHƯƠNG 3. PHƯƠNG PHÁP VÀ GIẢI PHÁP ĐỀXUẤT
Khởi động dịch vụmạng
(svc_network)
Lắng nghe bus UART
trong cửa sổquan sát
(UART_BREAK / UART_DATA)
Bus có hoạt động?
Tuyến 4G LTE (PPPoS)
vận hành thực địa
Tuyến WiFi
thu thập dữliệu
Có (module 4G)
Không (bus im)
Hình 3.6: Luồng tựnhận diện đường truyền theo hoạt động bus UART — D-026.
Bên cạnh đó, ởphía thu (máy chủvà giao diện web), hệthống tựkiểm chứng tính liên tục của dữ
liệu bằng cách đối sánh nhãn thời gian và sốlượng mẫu đính kèm mỗi gói: nếu phát hiện khoảng trống bất
thường giữa hai gói liên tiếp, phiên thu tương ứng bịđánh dấu lỗi và loại bỏthay vì âm thầm sinh ra một tệp
dữliệu hỏng. Cơ chếnày bảo đảm bộdữliệu xuất ra luôn liên tục, không phụthuộc vào đường truyền.
3.7.3
Kết quảvà Định hướng phát triển
Cơ chếtựnhận diện đường truyền đã được hiện thực và kiểm chứng trên phần cứng thực tế. Trong trường
hợp thiết bịkhông gắn module 4G, firmware nhận ra bus UART im lặng và chuyển sang WiFi trong khoảng
11 giây, so với khoảng 40 giây của cơ chếdò bằng lệnh AT trước đó. Phần lớn thời gian tiết kiệm đến từ
việc loại bỏthao tác thoát chếđộdữliệu (+++) vốn chờphản hồi vô ích khi không có module.
Vềchiến lược dữliệu, đồán sửdụng SisFall làm nguồn huấn luyện chính (trình bày tại Chương 5) và
thiết lập sẵn quy trình thu bộdữliệu cá nhân qua WiFi đểphục vụđánh giá mô hình trong điều kiện vận
hành thực. Bộdữliệu cá nhân được thu và gán nhãn theo đúng định dạng SisFall nhằm tái sửdụng trực tiếp
quy trình tiền xửlý và đánh giá đã xây dựng. Việc thu thập đầy đủbộdữliệu cá nhân trên nhiều đối tượng
là bước triển khai tiếp theo của đồán.
Vềđịnh hướng phát triển, việc bổsung điều khiển luồng phần cứng — nối hai chân RTS/CTS giữa vi
điều khiển và module — sẽnâng độtin cậy của tuyến 4G đủđểkham cảluồng streaming, từđó hợp nhất
hai tuyến truyền và cho phép thu thập dữliệu thực địa từxa mà không cần WiFi cục bộ.
35


---

## Trang 50

CHƯƠNG 4. PHÂN TÍCH VÀ THIẾT KẾHỆTHỐNG
4.1
Tổng quan chức năng
Phần này mô tảtổng quan các chức năng cốt lõi của hệthống, dựa trên định hướng gồm một vai trò
người dùng (Nhân viên y tế) và một tác nhân hệthống (Thiết bịgiám sát).
4.1.1
Biểu đồuse case tổng quát
Biểu đồuse case tổng quát mô tảcác tương tác chính giữa con người và hệthống. Các tác nhân (Actors)
tham gia bao gồm:
• Nhân viên y tế(Medical Staff): Người sửdụng hệthống qua giao diện Dashboard đểgiám sát thời
gian thực, theo dõi hồsơ bệnh nhân, thiết lập/quản lý thiết bịvà xửlý các sựcốté ngã khẩn cấp.
• Thiết bịgiám sát (ESP32 Node): Tác nhân hệthống (System Actor), liên tục thu thập và gửi dữliệu
viễn trắc (telemetry) thông qua giao thức PPPoS trên mạng 4G LTE và kích hoạt các cảnh báo (alerts)
khẩn cấp.
Các ca sửdụng (Use case) cốt lõi bao gồm: Đăng nhập & Xác thực, Quản lý thiết bị, Quản lý bệnh nhân
(Wearer), Gán/Thu hồi thiết bị, Giám sát thời gian thực, Xửlý cảnh báo té ngã, và Xem thống kê vận động.
Đặc biệt, Thiết bịgiám sát còn đóng vai trò tác nhân tựđăng ký vào use case Quản lý thiết bịthông qua cơ
chếauto-provisioning dựa trên địa chỉMAC phần cứng, không cần nhân viên nhập thủcông. Biểu đồuse
case tổng quát được thểhiện ởHình 4.1.
Hệthống giám sát người cao tuổi
Đăng nhập &
Xác thực
Quản lý thiết bị
Quản lý bệnh nhân
Gán / Thu hồi thiết bị
Giám sát thời gian thực
Xửlý cảnh báo té ngã
Xem thống kê vận động
Nhân viên
y tế
Thiết bị
giám sát
Hình 4.1: Biểu đồuse case tổng quát của hệthống
36


---

## Trang 51

CHƯƠNG 4. PHÂN TÍCH VÀ THIẾT KẾHỆTHỐNG
4.1.2
Biểu đồuse case phân rã Giám sát thời gian thực
Use case "Giám sát thời gian thực" yêu cầu hệthống cung cấp cho nhân viên y tếmột giao diện Dash-
board tổng quan. Thông qua giao diện này, nhân viên y tếcó thểtheo dõi danh sách toàn bộcác thiết bịđang
hoạt động, xem trạng thái kết nối mạng, mức pin hiện tại của từng thiết bị. Đặc biệt, chức năng này ứng
dụng cơ chếĐồng bộcảnh báo lai (Hybrid Alert Sync), liên tục lắng nghe các gói tin từMQTT Broker
qua WebSocket đểngay lập tức hiển thịcảnh báo (kèm âm thanh và viền đỏnhấp nháy) khi có sựcốté ngã
xảy ra với độtrễchưa tới 1 giây, đồng thời tựđộng cập nhật dữliệu từAPI. Biểu đồphân rã cho nhóm chức
năng này tập trung vào luồng hiển thịdữliệu và cơ chếcảnh báo.
Giám sát thời gian thực
Xem danh sách
thiết bịhoạt động
Xem trạng thái
kết nối & pin
Nhận cảnh báo realtime
(Hybrid Alert Sync)
Tựđộng cập nhật
dữliệu từAPI
Phát âm thanh
& viền đỏ
Nhân viên
y tế
Thiết bị
giám sát
MQTT
«include»
Hình 4.2: Biểu đồuse case phân rã "Giám sát thời gian thực"
4.1.3
Biểu đồuse case phân rã Xửlý cảnh báo té ngã
Use case "Xửlý cảnh báo té ngã" mô tảquy trình tiếp nhận và xửlý sựcố. Khi màn hình Dashboard
hiển thịcảnh báo té ngã, nhân viên y tếsẽkiểm tra và đến hiện trường đểhỗtrợngười bệnh. Sau khi hoàn
thành sơ cứu hoặc xác minh tình trạng an toàn, nhân viên y tếsẽtương tác với hệthống bằng cách nhấn nút
"Đã xửlý" (Resolve). Chức năng này cập nhật trạng thái của cảnh báo trong cơ sởdữliệu đểđảm bảo không
có sựcốnào bịbỏsót, đồng thời lưu trữlịch sửđểphục vụbáo cáo sau này.
37


---

## Trang 52

CHƯƠNG 4. PHÂN TÍCH VÀ THIẾT KẾHỆTHỐNG
Xửlý cảnh báo té ngã
Xem cảnh báo
trên Dashboard
Đến hiện trường
hỗtrợbệnh nhân
Nhấn "Đã xửlý"
(Resolve)
Cập nhật trạng thái
is_resolved
Lưu lịch sử
cảnh báo
Nhân viên
y tế
«include»
«include»
Hình 4.3: Biểu đồuse case phân rã "Xửlý cảnh báo té ngã"
4.1.4
Biểu đồuse case phân rã Gán thiết bịcho bệnh nhân
Use case "Gán thiết bịcho bệnh nhân" phục vụmục đích thiết lập liên kết vật lý giữa một thiết bịESP32
và một hồsơ bệnh nhân. Nhân viên y tếsẽchọn một thiết bịđã được tựđộng đăng ký trên hệthống và chọn
một bệnh nhân từdanh sách. Hệthống lấy chiều cao từhồsơ bệnh nhân đã chọn đểtính toán ước tính sải
bước và quãng đường di chuyển — chiều cao thuộc hồsơ bệnh nhân (wearer profile) và được nhập riêng
khi tạo hồsơ, không nhập lại tại bước gán. Việc gán thiết bịcũng tựđộng kích hoạt quá trình thu thập và
lưu trữviễn trắc cho bệnh nhân đó.
Gán thiết bịcho bệnh nhân
Chọn thiết bị
đã đăng ký
Chọn bệnh nhân
từdanh sách
Lấy chiều cao
từhồsơ wearer
Kiểm tra ràng buộc
1-1 (unique)
Kích hoạt
thu thập viễn trắc
Nhân viên
y tế
«include»
«include»
«include»
Hình 4.4: Biểu đồuse case phân rã "Gán thiết bịcho bệnh nhân"
38


---

## Trang 53

CHƯƠNG 4. PHÂN TÍCH VÀ THIẾT KẾHỆTHỐNG
4.1.5
Biểu đồuse case phân rã Xem thống kê vận động
Use case "Xem thống kê vận động" giúp nhân viên y tế(đồng thời đảm nhiệm vai trò quản trịviên) tra
cứu các sốliệu lịch sử. Người dùng có thểchọn một hồsơ bệnh nhân cụthểvà thiết lập mốc thời gian cần
tra cứu (ví dụ: trong tuần qua). Hệthống sẽtruy xuất dữliệu chuỗi thời gian (time-series) từInfluxDB và
vẽcác biểu đồtrực quan như: biểu đồsốbước chân đi bộ, biểu đồsốbước chạy, và biểu đồkhoảng cách di
chuyển. Các biểu đồnày cung cấp thông tin y khoa quan trọng đểđánh giá mức độphục hồi hoặc suy giảm
chức năng vận động của người bệnh.
Xem thống kê vận động
Chọn hồsơ
bệnh nhân
Chọn mốc thời gian
(tuần / tháng)
Truy xuất time-series
từInfluxDB
Vẽbiểu đồbước chân
& quãng đường
Nhân viên
y tế
«include»
«include»
Hình 4.5: Biểu đồuse case phân rã "Xem thống kê vận động"
4.1.6
Quy trình nghiệp vụ(Activity Diagram)
Quy trình nghiệp vụquan trọng nhất của hệthống là Luồng xửlý sựcốté ngã khẩn cấp. Quy trình
diễn ra như sau (minh họa bằng biểu đồhoạt động ởHình 4.6):
1. Thiết bịđeo (ESP32-S3) phát hiện té ngã thông qua mô hình học sâu tích chập 1D dạng tách kênh
theo chiều sâu (Depthwise CNN 1D).
2. Thiết bịngay lập tức gửi gói tin cảnh báo qua giao thức MQTT (kết nối 4G LTE bằng PPPoS) đến
MQTT Broker.
3. Giao diện Web (Dashboard) đang đăng ký (subscribe) luồng MQTT sẽlập tức hiển thịcảnh báo đỏ
toàn màn hình kèm theo âm thanh báo động.
4. Nhân viên y tếxác nhận cảnh báo trên màn hình và di chuyển đến vịtrí bệnh nhân đểsơ cứu.
5. Sau khi xửlý xong sựcố, nhân viên y tếthao tác chọn "Đã xửlý" (Resolve) trên hệthống.
6. Hệthống gọi API cập nhật trạng thái cảnh báo vào cơ sởdữliệu PostgreSQL, kết thúc quy trình.
39


---

## Trang 54

CHƯƠNG 4. PHÂN TÍCH VÀ THIẾT KẾHỆTHỐNG
Thiết bịđeo
(ESP32-S3)
Web Dashboard
Nhân viên y tế
Backend
/ PostgreSQL
Phát hiện té ngã
(mô hình Depth-
wise CNN 1D)
Gửi cảnh báo
qua MQTT
(4G LTE / PPPoS)
Hiển thịcảnh báo đỏ
toàn màn hình
+ âm thanh
Xác nhận cảnh báo
& đến hỗtrợbệnh nhân
Nhấn "Đã xử
lý" (Resolve)
Cập nhật trạng thái cảnh
báo (is_resolved)
qua MQTT Broker (QoS 1)
REST API (PATCH)
Hình 4.6: Biểu đồhoạt động (Activity Diagram) luồng xửlý sựcốté ngã khẩn cấp
4.1.7
Tựđộng đăng ký thiết bị(Auto-provisioning)
Cơ chếtựđộng đăng ký thiết bị(auto-provisioning) là điểm nổi bật của kiến trúc hệthống theo quyết
định D-020, cho phép thiết bịESP32-S3 xuất hiện trên Dashboard ngay sau khi cắm nguồn mà không yêu
cầu bất kỳthao tác nhập thủcông nào. Cụthể, mỗi thiết bịđọc địa chỉMAC 12 chữsốhex từbộnhớeFuse
không thểthay đổi (thông qua esp_read_mac) — giá trịnày đóng vai trò vân tay phần cứng, ổn định qua
toàn bộvòng đời thiết bịkểcảkhi xóa flash hay cập nhật firmware OTA, và là khóa định danh topic MQTT
theo cấu trúc eldercare/<mac>/.... Khi thiết bịthiết lập kết nối MQTT (qua 4G LTE/PPPoS),
nó ngay lập tức publish một gói tin config/status chứa trường mac và fw_version. Phía back-
end, dịch vụmqtt_service nhận gói tin này và gọi hàm _get_or_create_device_by_mac:
nếu MAC chưa tồn tại trong cơ sởdữliệu, hệthống tựđộng sinh một device_id ngữnghĩa có dạng
esp32_eldercare_NN (tuần tựtrong tổchức) rồi lưu MAC vào cột devices.mac; nếu MAC đã tồn
tại, hệthống chỉcập nhật trường firmware_version từfw_version nhận được. Phương án này loại
bỏhoàn toàn rủi ro nhập device_id thủcông (dễgây trùng lặp hoặc nhầm lẫn), đồng thời giữtên hiển
thịngắn gọn và có ý nghĩa cho nhân viên. Sau khi thiết bịxuất hiện tựđộng trên Dashboard, nhân viên y tế
chỉcần thực hiện một thao tác duy nhất là gán wearer (bệnh nhân) đểbắt đầu thu thập dữliệu viễn trắc có
ý nghĩa lâm sàng. Biểu đồuse case phân rã và biểu đồhoạt động swimlane của luồng này được trình bày
lần lượt tại Hình 4.7 và Hình 4.8.
40


---

## Trang 55

CHƯƠNG 4. PHÂN TÍCH VÀ THIẾT KẾHỆTHỐNG
Tựđộng đăng ký thiết bị
Đọc MAC
từeFuse
Kết nối MQTT
& publish config/status
Sinh device_id
esp32_eldercare_NN
Lưu MAC +
cập nhật firmware_version
Hiển thịtrên
Dashboard
Gán wearer
cho thiết bị
Thiết bị
giám sát
Nhân viên
y tế
«include»
«include»
«include»
«include»
Hình 4.7: Biểu đồuse case phân rã "Tựđộng đăng ký thiết bị"
41


---

## Trang 56

CHƯƠNG 4. PHÂN TÍCH VÀ THIẾT KẾHỆTHỐNG
Thiết bị
(ESP32-S3)
MQTT Broker
Backend
(mqtt_service)
Nhân viên
y tế
Boot và đọc
MAC từeFuse
Kết nối 4G/WiFi
+ MQTT
Publish con-
fig/status
{mac, fw_version}
Tra cứu thiết bịtheo
MAC trong DB
MAC đã
tồn tại?
Sinh device_id
esp32_eldercare_NN
+ lưu MAC
Chỉcập nhật
firmware_version
Thiết bịxuất hiện
trên Dashboard
Gán wearer
cho thiết bị
qua MQTT Broker (QoS 1)
Chưa
Rồi
Hình 4.8: Biểu đồhoạt động luồng tựđộng đăng ký thiết bị(Auto-provisioning)
4.2
Đặc tảchức năng
Dưới đây là đặc tảchi tiết của 5 Use Case quan trọng nhất, phản ánh nghiệp vụcốt lõi của hệthống
giám sát.
42


---

## Trang 57

CHƯƠNG 4. PHÂN TÍCH VÀ THIẾT KẾHỆTHỐNG
4.2.1
Đặc tảUse case: Giám sát thời gian thực
Bảng 4.1: Đặc tảUse case: Giám sát thời gian thực
Tên Use case
Giám sát thời gian thực
Tác nhân
Nhân viên y tế
Mô tả
Cung cấp giao diện lưới (grid) hiển thịtrạng thái của toàn bộthiết bịđang
hoạt động (Pin, kết nối mạng) và tiếp nhận cảnh báo khẩn cấp.
Tiền điều kiện
Nhân viên đã đăng nhập và có thiết bịđang online.
Luồng sựkiện chính
1. Nhân viên y tếtruy cập vào trang chủ(Dashboard).
2. Hệthống (Frontend) thiết lập kết nối WebSocket tới MQTT Broker.
3. Hệthống hiển thịdanh sách thiết bịkèm trạng thái kết nối.
4. Khi có gói tin cảnh báo té ngã từBroker, Frontend lập tức bung màn hình
cảnh báo (Overlay) và phát âm thanh.
Hậu điều kiện
Cảnh báo được hiển thịthành công cho đến khi nhân viên xác nhận.
4.2.2
Đặc tảUse case: Xửlý cảnh báo té ngã
Bảng 4.2: Đặc tảUse case: Xửlý cảnh báo té ngã (Resolve Alert)
Tên Use case
Xửlý cảnh báo té ngã
Tác nhân
Nhân viên y tế
Mô tả
Nhân viên đánh dấu một cảnh báo té ngã là "Đã xửlý" sau khi đã hỗtrợ
bệnh nhân.
Tiền điều kiện
Tồn tại ít nhất một cảnh báo té ngã chưa được xửlý.
Luồng sựkiện chính
1. Nhân viên y tếbấm vào nút "Xác nhận đã xửlý" trên cảnh báo tương
ứng.
2. Frontend gửi yêu cầu PATCH kèm Access Token tới Backend FastAPI.
3. Backend cập nhật trạng thái is_resolved = True trong cơ sởdữ
liệu PostgreSQL.
4. Backend trảvềphản hồi thành công, Frontend ẩn cảnh báo khỏi danh
sách chờ.
Hậu điều kiện
Cảnh báo được lưu trữvào lịch sửvới trạng thái đã xửlý.
4.2.3
Đặc tảUse case: Gán thiết bịcho bệnh nhân
Bảng 4.3: Đặc tảUse case: Gán thiết bịcho bệnh nhân (Assign Device)
Tên Use case
Gán thiết bịcho bệnh nhân
Tác nhân
Nhân viên y tế
Mô tả
Liên kết một thiết bịgiám sát vật lý với hồsơ của một bệnh nhân cụthể.
Tiền điều kiện
Thiết bịđang ởtrạng thái trống (chưa gán) và hồsơ bệnh nhân đã được tạo.
Luồng sựkiện chính
1. Nhân viên y tếchọn thiết bịtừdanh sách và nhấn "Gán bệnh nhân".
2. Hệthống hiển thịdanh sách bệnh nhân chưa có thiết bị.
3. Nhân viên chọn bệnh nhân tương ứng và bấm lưu.
4. Hệthống Backend kiểm tra ràng buộc 1-1 (unique constraint) và cập nhật
wearer_id cho thiết bị.
Hậu điều kiện
Dữliệu viễn trắc của thiết bịtừthời điểm này sẽđược tính toán dựa trên
chiều cao của bệnh nhân được gán.
43


---

## Trang 58

CHƯƠNG 4. PHÂN TÍCH VÀ THIẾT KẾHỆTHỐNG
4.2.4
Đặc tảUse case: Xem thống kê vận động
Bảng 4.4: Đặc tảUse case: Xem thống kê vận động
Tên Use case
Xem thống kê vận động
Tác nhân
Nhân viên y tế
Mô tả
Tra cứu và xem biểu đồthống kê mức độvận động (sốbước chân, quãng
đường) theo tuần/tháng.
Tiền điều kiện
Bệnh nhân đã đeo thiết bịvà sinh ra dữliệu viễn trắc.
Luồng sựkiện chính
1. Người dùng chọn khoảng thời gian cần tra cứu trong tab Thống kê.
2. Backend tiến hành truy vấn (Query) dữliệu tổng hợp từInfluxDB.
3. Dữliệu được trảvềvà Frontend sửdụng thư viện Recharts đểvẽbiểu đồ
trực quan.
Hậu điều kiện
Biểu đồđược hiển thịchính xác.
4.2.5
Đặc tảUse case: Tựđộng đăng ký thiết bị(Auto-provisioning)
Bảng 4.5: Đặc tảUse case: Tựđộng đăng ký thiết bị(Auto-provisioning)
Tên Use case
Tựđộng đăng ký thiết bị(Auto-provisioning)
Tác nhân
Thiết bịgiám sát (ESP32) — tác nhân chính; Nhân viên y tế— tác nhân
phụ(gán wearer)
Mô tả
Thiết bịtựđăng ký vào hệthống bằng địa chỉMAC eFuse ngay khi lần đầu
kết nối MQTT; backend sinh device_id ngữnghĩa tuần tựmà không cần
nhân viên nhập thủcông.
Tiền điều kiện
Tổchức (Organization) và MQTT Broker của deployment đã tồn tại; thiết
bịcó kết nối SIM 4G hoặc WiFi.
Luồng sựkiện chính
1. Thiết bịkhởi động, đọc địa chỉMAC 12 hex từeFuse (esp_read_mac).
2. Thiết bịthiết lập kết nối MQTT và publish gói tin config/status
{mac, fw_version}.
3. Backend (mqtt_service) nhận gói tin, gặp MAC chưa có trong DB
 gọi _get_or_create_device_by_mac.
4. Backend sinh device_id ngữnghĩa dạng esp32_eldercare_NN
(tuần tựtrong tổchức) và lưu MAC vào cột devices.mac.
5. Backend cập nhật firmware_version từtrường fw_version nhận
được.
6. Thiết bịxuất hiện tựđộng trên Dashboard; nhân viên y tếthực hiện gán
wearer đểbắt đầu thu thập dữliệu viễn trắc.
Hậu điều kiện
Thiết bịcó device_id ngữnghĩa duy nhất trong tổchức, sẵn sàng để
nhân viên gán wearer và bắt đầu giám sát.
4.3
Yêu cầu phi chức năng
Hệthống giám sát khẩn cấp đòi hỏi các tiêu chuẩn khắt khe vềkỹthuật và độtin cậy:
• Độtrễthấp (Low Latency): Thời gian từlúc thiết bịphát hiện té ngã đến khi chuông báo động vang
lên trên màn hình Web của y tá phải dưới 1 giây.
• Độtin cậy truyền thông: Sửdụng ngăn xếp giao thức mạng qua giao tiếp PPPoS (Point-to-Point
Protocol over Serial) trên module SIM 4G kết hợp cơ chếQoS của MQTT đểđảm bảo gói tin cảnh
báo luôn được gửi đi ngay cảtrong điều kiện sóng yếu.
• Khảnăng mởrộng (Scalability): Kiến trúc Dual-Database giúp hệthống xửlý đồng thời hàng nghìn
luồng dữliệu viễn trắc (InfluxDB) mà không gây tắc nghẽn cho các truy vấn quản lý (PostgreSQL).
Hỗtrợkiến trúc đa khách thuê (Multi-tenancy) cho phép quản lý đồng thời nhiều viện dưỡng lão trên
cùng một máy chủvật lý.
• Tính bảo mật (Security): Mọi API giao tiếp từFrontend đều phải được xác thực thông qua JSON
44


---

## Trang 59

CHƯƠNG 4. PHÂN TÍCH VÀ THIẾT KẾHỆTHỐNG
Web Token (JWT), kết hợp phân quyền quản trịđa tổchức, chống rò rỉthông tin cá nhân của bệnh
nhân.
• Độtin cậy cảnh báo (Alert Reliability): Hệthống phải giảm tỉlệbáo động giảtrong các sinh hoạt
thường ngày (ADL) trong khi vẫn giữFall Recall lớn hơn hoặc bằng ngưỡng KPI. Việc đánh đổi một
khoảng thời gian trễxác nhận xấp xỉfall_confirm_window giây được chấp nhận như một giải
pháp cân bằng giữa độđặc hiệu (Precision) và độtrễ(Latency).
• Khảnăng cấu hình từxa (Remote Configurability): Hệthống cho phép cấu hình thiết bịtừxa các
tham sốvận hành (như chu kỳtelemetry, ngưỡng ngã, cooldown, cửa sổxác nhận, và chu kỳđo RSSI)
trực tiếp thông qua dashboard mà không cần thiết phải nạp lại phần sụn (firmware).
4.4
Phân tích và thiết kếhệthống
4.4.1
Kiến trúc tổng thểhệthống
Hệthống giám sát người cao tuổi 24/7 được cấu thành từba thành phần chính, giao tiếp mật thiết với
nhau thông qua mạng di động 4G LTE và mạng Internet (như minh họa trong Hình 4.9):
• Thiết bịbiên (ESP32): Chịu trách nhiệm lấy mẫu cảm biến IMU, nội suy mô hình học máy nhúng
(TinyML) và truyền tải gói tin cảnh báo qua giao thức bảo mật MQTT TLS.
• Đám mây - Server: Sửdụng FastAPI Backend đểxửlý lô-gic, định tuyến dữliệu vào cơ sởdữliệu
quan hệ(PostgreSQL) hoặc chuỗi thời gian (InfluxDB).
• Giao diện Web (Next.js): Phục vụcho các y bác sĩ tại trạm điều khiển, có khảnăng nhận cảnh báo
theo thời gian thực (Real-time) qua WebSockets đồng thời truy xuất dữliệu bệnh án qua REST API.
Hình 4.9: Sơ đồKiến trúc Tổng thểHệthống IoT Eldercare
4.4.2
Kiến trúc phần mềm Firmware
Phần sụn (firmware) trên vi điều khiển ESP32-S3 được thiết kếtheo mô hình Hướng sựkiện (Event-
Driven) và Máy trạng thái hữu hạn (FSM). Kiến trúc này giúp hệthống hoạt động ổn định, phân tách rõ
ràng các luồng xửlý và tối ưu hóa tài nguyên khi tích hợp mô hình học máy nhúng (TinyML). Hệthống
được chia thành ba lớp chính:
• Lớp Ứng dụng (Application Layer): Bao gồm hàm khởi tạo app_main và máy trạng thái sys_manager
đóng vai trò là trung tâm điều phối các sựkiện của toàn hệthống, bao gồm cảviệc duy trì cờcomms-
critical đểngăn svc_network ngắt kết nối mạng khi đang trong pha xác nhận hoặc phát cảnh báo
khẩn cấp.
• Lớp Dịch vụ(Middleware/Service Layer): Các tác vụ(task) chạy độc lập trên hệđiều hành thời
45


---

## Trang 60

CHƯƠNG 4. PHÂN TÍCH VÀ THIẾT KẾHỆTHỐNG
gian thực FreeRTOS, bao gồm: svc_imu (đọc dữliệu từFIFO của cảm biến, áp dụng bộlọc
Kalman, gom lô mẫu 100Hz và quản lý bộđệm cửa sổtrượt; đồng thời tích hợp thư viện đếm bước
lib_pedometer đểtách riêng sốbước đi bộvà chạy theo nhãn hành vi, cùng với bộphát hiện va
chạm/rơi tựdo trên từng mẫu hỗtrợlấy trạng thái qua imu_service_get_last_impact()),
svc_ai (chạy nội suy mô hình AI và duy trì một FSM phụNORMAL/CONFIRMING cho quá trình
xác nhận ngã hậu va chạm, xem chi tiết Mục 3.3.1), svc_network (quản lý kết nối mạng — WiFi
ởmôi trường phát triển hoặc 4G LTE qua giao thức PPPoS ởmôi trường vận hành), và svc_cloud
(quản lý vòng đời MQTT Client và xửlý lệnh điều khiển từxa).
• Lớp Trình điều khiển (Driver Layer): Cung cấp giao tiếp trực tiếp với phần cứng, bao gồm drv_mpu6050
(giao tiếp I2C với cảm biến quán tính), drv_battery (đọc mức pin qua bộchuyển đổi ADC kết
hợp cầu phân áp), và drv_a7680c (điều khiển nguồn module 4G LTE qua chân PWRKEY). Phần
giao tiếp lệnh AT và thiết lập kênh PPPoS của module 4G được giao cho thành phần esp_modem
trong svc_network đảm nhiệm, với đường truyền khóa cứng ởchếđộchỉ-LTE (AT+CNMP=38)
nhằm tránh việc dò mạng 2G gây sụt dòng tiêu thụ.
Việc trao đổi thông tin giữa các thành phần tuân theo hai cơ chếtách biệt: các tín hiệu điều khiển và
chuyển trạng thái FSM được truyền qua vòng lặp sựkiện hệthống (esp_event), trong khi các mảng dữ
liệu lớn (lô mẫu và cửa sổtrượt) được chuyển qua hàng đợi của FreeRTOS (xQueue) nhằm tiết kiệm bộ
nhớvà chu kỳCPU. Hoạt động thu thập dữliệu và nội suy AI được thiết kếtheo cơ chếcửa sổtrượt (Sliding
Window) đểkhông làm gián đoạn quá trình lấy mẫu tần sốcao (100Hz) của cảm biến, đảm bảo tính liên
tục của dữliệu thời gian thực.
Vòng đời hoạt động của phần sụn được quản lý bởi Máy trạng thái hữu hạn (FSM) đóng vai trò là hạt
nhân điều phối trung tâm thông qua Default Event Loop. Hệthống chuyển đổi tuần tựtừkhởi tạo phần cứng
(STATE_INIT), thiết lập mạng 4G/WiFi và MQTT (STATE_CONNECTING), cho đến chếđộvận hành
tiêu chuẩn (STATE_NORMAL). Tại chếđộbình thường, các thuật toán AI và đếm bước chân được chạy cục
bộ. Ngoài ra, thiết bịcó thểchuyển sang chếđộtruyền dữliệu thô (STATE_STREAMING) khi nhận lệnh
điều khiển từđám mây, hoặc rơi vào trạng thái báo lỗi và tựđộng phục hồi (STATE_ERROR) khi gặp sựcố
ngắt kết nối vật lý (chi tiết tại Hình 4.10).
46


---

## Trang 61

CHƯƠNG 4. PHÂN TÍCH VÀ THIẾT KẾHỆTHỐNG
Hình 4.10: Sơ đồChuyển trạng thái (FSM) của Firmware trên thiết bịESP32 (FSM phụxác nhận ngã của svc_ai
được trình bày riêng tại Hình 4.12)
4.4.3
Thiết kếcơ sởdữliệu
Hệthống sửdụng mô hình cơ sởdữliệu kép (Dual-Database) đểđáp ứng đồng thời yêu cầu quản lý
thông tin phức tạp có tính liên kết và khảnăng lưu trữdữliệu thời gian thực với tần suất lớn.
• Cơ sởdữliệu quan hệ(PostgreSQL): Được sửdụng đểquản lý thông tin siêu dữliệu (metadata).
Các thực thểchính bao gồm tổchức (organizations), người dùng (users), người bệnh đeo thiết
bị(wearers), danh mục thiết bị(devices), lịch sửcảnh báo té ngã (alerts) và nhật ký sựkiện
thiết bị(device_events, ghi nhận các biến cốnhư mất kết nối hay pin yếu). Bảng devices
không chỉlưu trạng thái vận hành (mức pin, cường độsóng di động RSSI, thời điểm online gần
nhất) mà còn lưu các tham sốcấu hình điều khiển từxa của từng thiết bị: chu kỳgửi viễn trắc
(telemetry_interval), ngưỡng phát hiện ngã (fall_threshold), thời gian hồi cảnh báo
(fall_cooldown), cửa sổxác nhận hậu va chạm (fall_confirm_window — mặc định 4
giây) và chu kỳđo RSSI 4G (rssi_interval — mặc định 300 giây, 0 là tắt). Mô hình này cho
phép gán/hủy linh hoạt một thiết bịcho một người đeo cụthể(ràng buộc duy nhất một-một) và bảo
đảm cách ly dữliệu giữa các tổchức qua trường org_id.
• Cơ sởdữliệu chuỗi thời gian (InfluxDB): Chuyên dụng đểlưu trữdữliệu có tính liên tục và số
lượng lớn. Measurement telemetry lưu các chỉsốđo đếm bước chân (tách riêng đi bộvà chạy),
quãng đường di chuyển và mức pin đểứng dụng web vẽbiểu đồtheo dõi sức khỏe một cách trực quan.
Sơ đồThực thể- Mối quan hệ(Entity-Relationship Diagram - ERD) của cơ sởdữliệu quan hệ(Post-
greSQL) được thểhiện như trong Hình 4.11. Sơ đồnày mô tảchi tiết các bảng siêu dữliệu và mối liên kết
khóa ngoại (Foreign Key) giữa chúng, với trọng tâm là kiến trúc Đa khách thuê (Multi-tenancy) thông qua
trường org_id. Các sựkiện từthiết bịvà cảnh báo té ngã đều được ánh xạchặt chẽvới bệnh nhân và thiết
bịphát sinh nhằm đảm bảo tính toàn vẹn dữliệu.
47


---

## Trang 62

CHƯƠNG 4. PHÂN TÍCH VÀ THIẾT KẾHỆTHỐNG
Hình 4.11: Sơ đồThực thể- Mối quan hệ(ERD) của cơ sởdữliệu PostgreSQL
Cấu trúc lưu trữcủa cơ sởdữliệu chuỗi thời gian (InfluxDB) được mô tảchi tiết trong Bảng 4.6.
Bảng 4.6: Cấu trúc Measurement của cơ sởdữliệu chuỗi thời gian InfluxDB
Measurement
Tags (chỉmục, chuỗi)
Fields (giá trịsố)
telemetry
device_id, wearer_id,state, ai_pred
battery_pct
(int),
steps
(int),
walk_steps
(int),
run_steps
(int),
ai_conf
(float), distance_m (float)
48


---

## Trang 63

CHƯƠNG 4. PHÂN TÍCH VÀ THIẾT KẾHỆTHỐNG
4.4.4
Thiết kếgiao thức truyền thông
Hệthống phân tách luồng dữliệu thành hai lớp giao thức riêng biệt đểđảm bảo hiệu năng và tính bảo
mật:
• Lớp Thời gian thực (MQTT): Đảm nhiệm việc truyền tải dữliệu tức thời giữa thiết bịIoT và máy
chủ. Broker MQTT sửdụng cấu trúc topic thống nhất, được phân luồng và định danh duy nhất theo
địa chỉMAC phần cứng của từng thiết bị(cấu trúc gốc: eldercare/{mac}/...). Cụthể, thiết bị
gửi các gói tin viễn trắc định kỳqua topic eldercare/{mac}/status hoặc phát sựkiện khẩn
cấp qua topic eldercare/{mac}/alert/fall khi phát hiện té ngã. Việc phân chia topic rõ
ràng kết hợp với giao thức MQTT giúp tối thiểu hóa băng thông, chống nhiễu loạn dữliệu giữa các
thiết bịvà đảm bảo duy trì kết nối ổn định trong môi trường mạng di động 4G.
• Lớp Quản lý (HTTP REST API): Cung cấp các điểm cuối (endpoints) đểứng dụng web (Frontend)
giao tiếp với máy chủ(Backend). Các chức năng chính bao gồm xác thực (Authentication), quản lý
thông tin người bệnh, quản lý trạng thái thiết bị, truy xuất lịch sửcảnh báo và tổng hợp sốliệu thống
kê. Mọi giao dịch qua REST API đều yêu cầu đính kèm mã thông báo bảo mật (Access Token). Điểm
đặc biệt của kiến trúc này là cơ chế"Đồng bộcảnh báo lai" (Hybrid Alert Sync), cho phép Frontend
hiển thịcảnh báo té ngã tức thời qua MQTT với một UUID tạm thời, và sau đó được Backend xửlý
và liên kết đồng bộvới cơ sởdữliệu một cách liền mạch.
• Lớp Cấu hình từxa (Remote Configuration): Mô tảluồng cấu hình bền vững cho thiết bị. Nhằm
tối ưu băng thông, Backend đóng gói toàn bộcác tham sốvào một payload JSON duy nhất gửi
xuống thiết bịthông qua topic eldercare/{mac}/config/set. Các tham sốnày bao gồm:
chu kỳgửi viễn trắc (telemetry_interval), ngưỡng ngã (fall_threshold), thời gian hồi
(fall_cooldown), cửa sổxác nhận ngã (fall_confirm_window), chu kỳđo RSSI (rssi_interval),
và chu kỳtimeout cho luồng stream (stream_timeout). Thiết bịnhận payload, áp dụng cấu hình,
lưu bền vững vào bộnhớNVS (Non-Volatile Storage) và dội lại thông báo phản hồi qua topic el-
dercare/{mac}/config/status đểBackend đồng bộngược vềcơ sởdữliệu.
• Lớp đường truyền vật lý kép (Dual-transport): Thiết bịhỗtrợhai tuyến truyền theo ngữcảnh sử
dụng — WiFi cho pha thu thập dữliệu cần luồng IMU liên tục, và 4G LTE (PPPoS) cho vận hành
thực địa — và tựđộng nhận diện tuyến phù hợp ngay khi khởi động. Cơ sởlý thuyết và cơ chếnhận
diện được trình bày tại Mục 3.7.
4.4.5
Thiết kếFSM phụxác nhận ngã trong svc_ai
Như đã trình bày tại Mục 3.3.1, cơ chếxác nhận ngã hai pha được hiện thực hóa bằng một Máy trạng
thái hữu hạn (FSM) phụnằm bên trong thành phần svc_ai, tách biệt hoàn toàn với FSM trung tâm của
sys_manager (vốn chỉquản lý các trạng thái hệthống cấp cao như STATE_NORMAL, STATE_STREAMING).
FSM phụnày có hai trạng thái ổn định và một trạng thái kết thúc tạm thời, như được mô tảtrong Hình 4.12.
FALL_FSM_NORMAL
(Bình thường)
CONFIRMING
(Đang quan sát)
CONFIRMED
(Phát cảnh báo)
ML trigger:
P(Fall) ≥θ
≥60% window:
Idle + ROLL nằm
trong N giây
Sau khi post AI_EVT_FALL_DETECTED
→reset vềNORMAL + cooldown
ABORT: Walk/Run
+ tư thếđứng
Khi vào CONFIRMING:
sys_manager_bump_comms_critical()
(ngăn svc_network đứt link 4G)
Hình 4.12: Sơ đồFSM phụxác nhận ngã hậu va chạm trong svc_ai (D-021)
49


---

## Trang 64

CHƯƠNG 4. PHÂN TÍCH VÀ THIẾT KẾHỆTHỐNG
Luồng hoạt động cụthểcủa FSM phụnày như sau. Ởtrạng thái FALL_FSM_NORMAL, svc_ai liên
tục chạy suy luận mô hình TinyML trên cửa sổtrượt 200 mẫu (trượt 50 mẫu mỗi 0,5 giây). Ngay khi xác
suất đầu ra vượt ngưỡng θ (tham sốfall_threshold cấu hình được), hệthống sẽđi qua lớp lọc nhiễu
tiền va chạm (Pre-Impact Posture Gating): nếu thiết bịđã nằm hoàn toàn ngang (góc Roll nằm trong khoảng
[−45◦, 45◦]) trong suốt 3 giây trước đó, hệthống sẽkết luận đây là thiết bịđang không được đeo trên người
(ví dụ: đặt trên bàn và bịva đập) và lập tức từchối cảnh báo. Ngược lại, nếu vượt qua lớp lọc, FSM chuyển
sang trạng thái CONFIRMING. Đồng thời, svc_ai gọi sys_manager_bump_comms_critical()
đểđặt cờcomms-critical trong sys_manager, ngăn thành phần svc_network thực hiện lệnh AT+CSQ
(đo RSSI 4G) vốn sẽlàm gián đoạn kết nối MQTT trong 15–20 giây.
Tại CONFIRMING, FSM quan sát pha hậu va chạm trong khoảng thời gian fall_confirm_window
giây (mặc định 4 giây, cấu hình được từxa qua config/set). Nếu tỉlệsốcửa sổsuy luận trảvềnhãn Idle
kết hợp với góc Roll nằm trong vùng tư thếnằm đạt từ60% trởlên, FSM chuyển sang CONFIRMED và
post sựkiện AI_EVT_FALL_DETECTED. Ngược lại, nếu phát hiện đối tượng phục hồi tư thế(nhãn Walk
hoặc Run kèm góc Roll tư thếđứng), FSM hủy báo động (ABORT) và trởvềFALL_FSM_NORMAL. Sau
khi phát cảnh báo, FSM tựreset vềtrạng thái bình thường và thành phần svc_cloud chịu trách nhiệm áp
dụng thời gian hồi (fall_cooldown) nhằm tránh lặp cảnh báo.
4.4.6
Tối ưu hóa Firmware và Độổn định mạng
Nhằm đảm bảo thiết bịhoạt động ổn định liên tục trong thời gian dài (24/7) và tiết kiệm năng lượng,
một sốcơ chếtối ưu đã được thiết kếvà tích hợp vào Firmware:
• Cổng logic trạng thái (FSM Gating): Mô hình học máy nhúng (TinyML) chỉđược kích hoạt suy
luận khi thiết bịởtrạng thái giám sát thông thường (STATE_NORMAL). Khi thiết bịchuyển sang chế
độtruyền phát dữliệu thô phục vụthu thập dataset (STATE_STREAMING), luồng suy luận AI sẽbị
ngắt bỏqua nhằm giải phóng tài nguyên CPU và tiết kiệm điện năng.
• Cơ chếWatchdog chống kẹt mạng tĩnh: Mạng 4G LTE thường gặp hiện tượng kết nối vật lý vẫn
duy trì nhưng luồng dữliệu TCP bịnghẽn (kẹt tĩnh) do hiện tượng tràn bộđệm (UART overrun) khi
module thiếu luồng điều khiển phần cứng (Hardware Flow Control). Hệthống sửdụng một cơ chế
Watchdog 2 bậc: Nếu mất kết nối MQTT quá 60 giây, firmware sẽép buộc khởi động lại tiến trình
mạng; nếu vượt quá 150 giây, toàn bộvi điều khiển sẽđược khởi động lại đểlàm sạch cache và khôi
phục kết nối.
• Khởi động nhanh (Boot Fast-path): Thiết bịghi nhớtrạng thái khóa mạng 4G (lte_lock) vào bộ
nhớkhông bay hơi (NVS). Ởcác lần khởi động tiếp theo, firmware sẽbỏqua các bước khởi tạo dò
mạng rườm rà (thường mất hơn 30 giây) và tiến hành gắn kết IP ngay lập tức, giúp thiết bịonline trở
lại trong thời gian ngắn nhất sau khi reboot.
4.4.7
Tựđộng xửlý cảnh báo tồn đọng (Auto-resolve)
Trong thực tếvận hành, có những cảnh báo té ngã bịbỏsót không được nhân viên y tếxác nhận xửlý,
làm rác cơ sởdữliệu và hiển thịtrên giao diện. Đểgiải quyết vấn đềnày, Backend được thiết kếmột tiến
trình chạy ngầm (background task) dựa trên vòng lặp bất đồng bộasyncio.
Tiến trình này được gắn trực tiếp vào vòng đời khởi động (lifespan) của ứng dụng FastAPI. Mỗi
giờ, tiến trình sẽtựđộng quét cơ sởdữliệu và thực hiện cập nhật đồng loạt (bulk update) chuyển trạng thái
is_resolved = True cho tất cảcác cảnh báo đã tồn tại quá 24 giờ. Phương pháp này tận dụng triệt để
kiến trúc bất đồng bộcủa Python, giúp hệthống tựđộng làm sạch dữliệu một cách gọn nhẹmà không cần
phụthuộc vào các thư viện lập lịch bên thứba cồng kềnh (như Celery hay APScheduler).
4.4.8
Tối ưu hóa Thiết kếPhần cứng và Giao tiếp Ngoại vi
Quá trình thiết kếmạch nguyên lý và giao tiếp ngoại vi cho ESP32-S3 gặp phải một sốthách thức đặc
thù liên quan đến vi kiến trúc phần cứng, đòi hỏi phải có những điều chỉnh so với lý thuyết ban đầu:
50


---

## Trang 65

CHƯƠNG 4. PHÂN TÍCH VÀ THIẾT KẾHỆTHỐNG
• Xung đột IO MUX trên UART0: Ban đầu, giao tiếp UART với module 4G A7680C được gán vào
chân GPIO 43 và 44. Tuy nhiên, trên vi kiến trúc ESP32-S3, hai chân này được ưu tiên mức cao nhất
(Priority 3) cho Console/Bootloader. Việc cốép sửdụng chúng dẫn đến luồng dữliệu mạng 4G bị
các đoạn log hệthống chèn ngang làm hỏng gói tin. Thiết kếsau đó đã được điều chỉnh lại đểđịnh
tuyến UART 4G sang GPIO 4 và 5, giải quyết triệt đểvấn đềrớt gói tin.
• Khởi động module 4G (PWRKEY và RST): Thông thường, vi điều khiển sửdụng chân RST để
khởi động lại module mạng khi cần. Tuy nhiên, mạch breakout A7680C sửdụng trong dựán không
hỗtrợchân cấp nguồn PWRKEY. Do đó, nếu ESP32-S3 kéo chân RST xuống mức thấp, module sẽbị
tắt hoàn toàn mà không thểtựbật lại. Firmware được thiết kếđể"thảnổi" chân RST, phó thác hoàn
toàn việc khởi động module mạng cho mạch Auto-Power-On bằng tụđiện tích hợp sẵn trên mạch.
51


---

## Trang 66

CHƯƠNG 5. TRIỂN KHAI VÀ ĐÁNH GIÁ THỰC NGHIỆM
Chương này trình bày toàn bộquá trình phân tích yêu cầu, thiết kếkiến trúc và hiện thực hóa hệthống
IoT giám sát người cao tuổi. Dựa trên nền tảng lý thuyết đã được khảo sát ởcác chương trước, nhóm tác giả
đềxuất kiến trúc ba lớp tích hợp thiết bịbiên (ESP32-S3), nền tảng đám mây (FastAPI) và giao diện người
dùng web (Next.js), vận hành thông qua giao thức MQTT trên mạng di động 4G LTE. Tiếp theo, chương
tổng hợp và phân tích các kết quảthực nghiệm nhằm đánh giá hiệu năng tổng thểcủa hệthống trong điều
kiện thực tế.
5.1
Triển khai và Xây dựng ứng dụng
Hình 5.1: Mạch phần cứng sau khi lắp ráp hoàn thiện
Hình 5.2: Thiết bịgiám sát đeo trên người thực tế
Dựa trên thiết kếkiến trúc tổng thể, hệthống được lắp ráp và triển khai thực tếnhư trong Hình 5.1 và
Hình 5.2. Thiết bịđeo được tối ưu hóa kích thước nhằm đảm bảo sựthoải mái cho người sửdụng trong sinh
hoạt hàng ngày, đồng thời đảm bảo độchính xác của cảm biến gia tốc.
5.1.1
Triển khai thuật toán xửlý tín hiệu IMU (Bộlọc Kalman)
Khi tính toán góc nghiêng (Roll và Pitch) từcảm biến quán tính 6 bậc tựdo (IMU), gia tốc kếthường
tính toán góc tĩnh rất chính xác nhưng lại chịu nhiễu mạnh (high-frequency noise) khi thiết bịva đập hoặc
có chuyển động đột ngột. Ngược lại, cảm biến góc quay (Gyroscope) phản ứng rất nhanh với chuyển động
nhưng lại sinh ra sai sốtrôi tích lũy (drift) khi thực hiện tích phân vận tốc góc theo thời gian.
Đểkhắc phục nhược điểm này, hệthống triển khai một thư viện bộlọc số(lib_kalman) ứng dụng
Bộlọc Kalman 1 chiều. Thuật toán tiến hành dung hợp dữliệu (sensor fusion) từcảhai loại cảm biến thông
qua hai bước chính:
1. Bước Dựbáo (Predict): Sửdụng vận tốc góc từGyroscope đểcập nhật giá trịdựbáo cho góc nghiêng
ởchu kỳhiện tại và tính toán sai sốtrôi.
2. Bước Cập nhật (Update): Sửdụng góc thực tếtính toán từGia tốc kếđểhiệu chỉnh lại kết quảdự
báo, qua đó triệt tiêu sai sốtrôi tích lũy.
52


---

## Trang 67

CHƯƠNG 5. TRIỂN KHAI VÀ ĐÁNH GIÁ THỰC NGHIỆM
Trong quá trình tinh chỉnh (tuning) thực tế, tham sốphương sai nhiễu đo lường của gia tốc kế(R_measure)
được thiết lập ởmức độphù hợp ( 0.03). Cấu hình này giúp bộlọc giảm bớt sựtin tưởng vào gia tốc kế
trong các pha va chạm mạnh (đặc trưng của hành vi té ngã), từđó giữcho góc ước lượng đầu ra luôn trơn
tru, mượt mà và giảm thiểu đáng kểcác trường hợp báo động giả(False Positive) cho hệthống nhận diện.
5.1.2
Phân tích kiến trúc phần cứng ESP32-S3 định hướng thiết kếmô hình
Khác với bài toán học sâu trên máy chủvốn có tài nguyên gần như vô hạn, việc triển khai mô hình học
máy lên vi điều khiển là một bài toán đồng thiết kếphần cứng — phần mềm (hardware–software co-design):
kiến trúc mạng nơ-ron phải được định hình ngay từđầu theo các ràng buộc vật lý của chip đích. Vì vậy,
trước khi xây dựng mô hình, đồán tiến hành khảo sát kỹkiến trúc xửlý và phân cấp bộnhớcủa ESP32-S3
espressif2023esp32s3, espressif2023esp32s3trm đểrút ra các nguyên tắc thiết kếbắt buộc.
a, Khối tính toán: lõi vô hướng và khối tăng tốc véc-tơ
ESP32-S3 sửdụng vi xửlý lõi kép Xtensa LX7 hoạt động ở240 MHz. Điểm cốt lõi cho tác vụAI là
bộtập lệnh mởrộng SIMD (Single Instruction, Multiple Data) đi kèm tập thanh ghi véc-tơ rộng 128-bit,
cho phép một lệnh duy nhất thực hiện song song nhiều phép nhân–cộng tích lũy (MAC) trên các phần tử
sốnguyên 8-bit hoặc 16-bit trong cùng một chu kỳmáy. Trong quá trình suy luận, các phép toán vô hướng
thông thường chạy trên đường ống (pipeline) lõi LX7, còn các phép tích chập và nhân ma trận khối lượng
lớn được điều phối (dispatch) sang khối tăng tốc véc-tơ thông qua các lệnh chuyên dụng được đóng gói sẵn
trong thư viện ESP-NN espressif2023espnn. Cơ chếchuyển đổi này chỉphát huy tác dụng đối với những
toán tửcó thểánh xạsang lệnh véc-tơ; mọi toán tửkhông được hỗtrợsẽbuộc phải thực thi bằng nhân vô
hướng tham chiếu (reference kernel) thuần phần mềm, làm tốc độsuy luận sụt giảm nhiều lần. Đây chính
là ràng buộc nền tảng đầu tiên: mô hình phải được cấu thành từcác toán tửnằm trong danh sách tăng tốc
của ESP-NN (tích chập điểm 1 × 1, tích chập tách kênh, ReLU6, MaxPool, trung bình toàn cục), đồng thời
tránh các toán tửngoại lai (LSTM/GRU, tích chập giãn nở, sigmoid/tanh).
b, Phân cấp bộnhớ: MMU, bộnhớđệm và bộnhớngoài
Trọng sốmô hình sau khi lượng tửhóa được nhúng trong bộnhớFlash, trong khi vùng làm việc động
(tensor arena) nằm trên RAM. ESP32-S3 quản lý bộnhớngoài (PSRAM/PSROM) thông qua đơn vịquản
lý bộnhớ(MMU) ánh xạkhông gian địa chỉtheo từng khối (block) kích thước 64 KB, với tổng dung lượng
ánh xạtối đa lên tới 32 MB. CPU truy xuất các vùng nhớngoài này qua bus SPI, và băng thông của bus
quyết định trực tiếp tốc độnạp trọng số: thực nghiệm cho thấy cùng một mô hình, khi đọc qua Quad SPI
ở40 MHz mất tới 70,23 ms cho mỗi lần suy luận, nhưng khi nâng lên Octal SPI ở80 MHz thời gian rút
xuống còn khoảng 32 ms (chi tiết tại Mục 4.3.2).
Đểbù đắp độtrễtruy cập bộnhớngoài, ESP32-S3 trang bịbộnhớđệm dữliệu (L1 data cache) dung
lượng 64 KB nhận dữliệu ánh xạtừMMU. Khi suy luận, nếu toàn bộtrọng sốmô hình cùng vùng làm
việc thường trú được trong bộnhớđệm thì tốc độtruy cập tiệm cận với SRAM nội chip; ngược lại, mỗi lần
thiếu trang (cache-miss) sẽbuộc CPU dừng chờđểnạp lại dữliệu từFlash/PSRAM qua SPI, phá vỡtính
liên tục của khối tăng tốc véc-tơ. Từđó suy ra ràng buộc thiết kếthen chốt thứhai: tổng kích thước (trọng
sốmô hình + tensor arena) cần tiệm cận hoặc nhỏhơn 64 KB, càng nhỏcàng tốt, nhằm giảm thiểu tỷlệ
cache-miss và giữcho dữliệu thường trú trong bộnhớđệm.
Hai ràng buộc trên — toán tửthân thiện ESP-NN và kích thước lọt bộnhớđệm — chính là kim chỉnam
định hướng toàn bộquá trình phát triển mô hình được trình bày ởcác mục tiếp theo, lý giải vì sao đồán
phải liên tục thửnghiệm và loại bỏnhiều kiến trúc cho tới khi đạt được phiên bản tối ưu cuối cùng.
5.1.3
Huấn luyện và triển khai mô hình học máy (TinyML)
Trong giai đoạn phát triển mô hình nhận diện hành vi và phát hiện té ngã, hệthống sửdụng bộdữliệu
công khai SisFall làm nguồn dữliệu cốt lõi. Bộdữliệu này chứa các bản ghi hoạt động thường ngày (ADL)
và các kịch bản té ngã được thu thập từnhiều đối tượng khác nhau, đảm bảo tính đa dạng và độtin cậy cao.
53


---

## Trang 68

CHƯƠNG 5. TRIỂN KHAI VÀ ĐÁNH GIÁ THỰC NGHIỆM
Bên cạnh nguồn huấn luyện công khai này, đồán thiết lập một bộdữliệu cá nhân thu trực tiếp từthiết bị
đeo thật đểkiểm thửvà đánh giá mô hình trong điều kiện vận hành thực; quá trình thu được thực hiện qua
WiFi nhằm bảo toàn tính liên tục của tín hiệu (xem Mục 3.7).
Quá trình tiền xửlý dữliệu (Preprocessing) đóng vai trò then chốt đểchuẩn hóa dữliệu trước khi nạp
(feed) vào mạng nơ-ron:
• Giảm tần sốlấy mẫu (Downsampling): Dữliệu gốc của bộSisFall có tần sốlấy mẫu là 200Hz.
Nhằm tối ưu hóa tài nguyên tính toán trên vi điều khiển mà vẫn giữđược các đặc trưng tần sốquan
trọng của chuyển động, hệthống tiến hành giảm tần sốlấy mẫu (downsample) xuống còn 100Hz.
• Phân mảnh cửa sổtrượt (Windowing): Chuỗi dữliệu thời gian thực sau đó được băm (split) thành
các cửa sổtrượt (sliding window) có kích thước cốđịnh kèm theo độtrễgối nhau (overlap). Quá trình
này giúp mô hình nắm bắt được toàn vẹn thông tin động học diễn ra trong một chu kỳthời gian liên
tục (từlúc bắt đầu mất thăng bằng cho đến khi va chạm mặt đất).
Việc chuẩn hóa dải tín hiệu cũng là một quyết định thiết kếđáng lưu ý chứkhông hiển nhiên. Gia tốc
được kẹp trong dải [−8, 8] g rồi chia cho 8 đểđưa về[−1, 1]; riêng vận tốc góc, các nghiên cứu kinh điển
thường lấy mốc bão hòa của cảm biến là ±2000 dps. Tuy nhiên, phân tích phân vịthực nghiệm trên bộ
SisFall cho thấy ngay cảởbách phân vị99,9% (các pha lộn vòng hoặc vấp ngã mạnh nhất), tốc độxoay tổng
hợp cực đại cũng chỉchạm khoảng 463 dps. Do đó, đồán chọn thang đo ±500 dps thay vì ±2000 dps: việc
thu hẹp dải này tránh lãng phí độphân giải khi lượng tửhóa INT8 (nếu dùng ±2000 dps, phần lớn các vi
chấn động của trạng thái tĩnh sẽbịlàm tròn về0), qua đó giúp mô hình phân biệt tốt hơn các hành vi cường
độthấp.
Hệthống sửdụng sơ đồphân loại 5 nhãn gồm Walk, Run, Idle, Trans và Fall — đây là kết quảcủa quá
trình thửnghiệm từsơ đồbốn nhãn lên sáu nhãn rồi chốt lại năm nhãn; phân tích đầy đủlý do lựa chọn và
đánh giá tác động định lượng của từng thay đổi được trình bày trong Mục 5.1.
Tương ứng với từng nhóm nhãn, thuật toán cắt cửa sổvà gán nhãn cũng được tinh chỉnh qua nhiều lần
thửđểbám đúng bản chất vật lý của tín hiệu, thay cho cách cắt cửa sổtrượt mù quáng ban đầu:
• Nhãn Fall và Walk/Run: Đối với té ngã, hệthống căn cửa sổvào đỉnh va chạm xác định bằng độlớn
véc-tơ gia tốc tổng hợp (SVM — Signal Vector Magnitude, SVM =
q
a2x + a2y + a2z), vốn tăng vọt
tại khoảnh khắc tiếp đất. Các hành vi mang tính chu kỳliên tục như Đi bộvà Chạy được cắt bằng cửa
sổtrượt truyền thống.
• Nhãn Trans — bài học từviệc đổi tiêu chí gán nhãn: Ban đầu, đồán dùng chính đỉnh SVM gia
tốc đểdò và gán nhãn các pha chuyển tiếp. Tuy nhiên, xung gia tốc của hành vi chuyển tiếp (đứng
lên, ngồi xuống) rất dễtrùng lặp với xung của bước chân mạnh và với chính cú ngã, khiến việc phân
đoạn bịnhiễu và làm "bẩn" nhãn. Quan sát cho thấy đặc trưng phân biệt thật sựcủa chuyển trạng thái
nằm ởvận tốc xoay của thân người chứkhông phải ởbiên độgia tốc. Do đó, tiêu chí gán nhãn được
chuyển sang dựa trên giá trịtrung bình bình phương (RMS) của con quay hồi chuyển với ngưỡng kích
hoạt > 20 dps: mỗi vùng vượt ngưỡng được gom thành một sựkiện và cắt đúng một cửa sổ2 giây căn
vào đỉnh sựkiện. Cách tiếp cận theo sựkiện dựa trên RMS gyro này giúp tách bạch rõ ràng giữa tĩnh
(Idle) và chuyển tiếp (Trans), tăng tính bền vững (robustness) ngay cảkhi tín hiệu có nhiều đỉnh phụ.
• Tăng cường dữliệu (Augmentation): Lớp Trans — vốn ít mẫu và ranh giới mờ— được làm phong
phú trong huấn luyện bằng cách nhân biên độtín hiệu theo các tỷlệ×0,9 và ×1,1, mô phỏng sựkhác
biệt vềlực tác động giữa người cao tuổi và người trẻcó vóc dáng khác nhau.
Khi hoàn tất huấn luyện, mô hình được biên dịch thành dạng mảng mã nguồn C/C++ (model_data.cc)
đểnạp thẳng vào vi điều khiển ESP32-S3.
54


---

## Trang 69

CHƯƠNG 5. TRIỂN KHAI VÀ ĐÁNH GIÁ THỰC NGHIỆM
5.1.4
Quá trình phát triển lặp và tối ưu kiến trúc hướng phần cứng
Mô hình triển khai cuối cùng không đạt được trong một lần, mà là kết quảcủa hàng chục phiên bản thử
nghiệm, trong đó mỗi phiên bản tháo gỡmột nút thắt cụthểbộc lộtừhai ràng buộc phần cứng đã phân tích
ởmục trên (toán tửthân thiện ESP-NN và kích thước lọt bộnhớđệm 64 KB). Bảng 5.1 tóm tắt các cột mốc
tiến hóa chính cùng lý do mỗi hướng đi bịloại bỏhoặc được giữlại.
Điểm ngoặt quan trọng nhất của quá trình là việc loại bỏdòng mạng Tích chập theo thời gian (TCN). Về
mặt độchính xác thuần túy, TCN với tích chập giãn nở(dilated convolution) cho kết quảvượt trội, đặc biệt ở
nhãn Trans khó nhằn và trong các kịch bản đánh giá chéo miền dữliệu giữa người trẻvà người già. Tuy nhiên,
tích chập giãn nởkhi chuyển sang TFLite lại sinh ra các toán tửxáo trộn bộnhớ(SPACE_TO_BATCH_ND)
hoàn toàn không nằm trong danh sách tăng tốc của ESP-NN, buộc vi điều khiển phải chạy bằng nhân tham
chiếu phần mềm. Hệquảlà thời gian suy luận của TCN cổđiển trên ESP32-S3 lên tới hơn 2 giây cho mỗi
cửa sổ— một con sốbất khảthi cho ứng dụng thời gian thực; dù có thiết kếlại đểbỏgiãn nởthì độtrễvẫn
còn ởmức 180–220 ms. Tương tự, các kiến trúc lai có lớp hồi quy LSTM (không được tăng tốc, ∼210 ms)
cũng bịloại khỏi nhánh tối ưu tốc độ. Đây là minh chứng định lượng cho nguyên tắc thiết kếmạng thuận
theo phần cứng (hardware-aware design): một mô hình chính xác hơn trên máy chủchưa chắc khảdụng trên
thiết bịbiên.
Sau khi chuyển hẳn sang kiến trúc tích chập thuần (CNN) với các khối tích chập tách kênh (Separa-
bleConv) và hàm kích hoạt ReLU6, hai vấn đềtinh vi còn lại tiếp tục được xửlý. Thứnhất, phiên bản
ResNet-1D v25 mắc lỗi nhầm đơn vịvận tốc góc (xửlý nhầm rad/s thành dps), khiến biên độgyro bị
thu nhỏkhoảng 57 lần và gần như triệt tiêu sau lượng tửhóa INT8 — mô hình vô tình trởnên "mù" với
thông tin xoay; lỗi này được khắc phục ởv30 với thang đo gyro ±500 dps đã nêu. Thứhai, khối Squeeze-
and-Excitation (SE) trong v25 tuy nhẹvềsốtham sốnhưng chứa hàm sigmoid (không được tăng tốc) và
làm phân mảnh mô hình thành nhiều tensor nhỏ, khiến phần siêu dữliệu (metadata) của tệp TFLite phình
to. Việc loại bỏhoàn toàn SE block và sigmoid ởv30/v31, kết hợp rút gọn đầu vào của v31 xuống còn bốn
kênh (ax, ay, az và Gyro RMS tính trực tiếp trên thiết bị), đã đưa kích thước mô hình vềmức ∼25 KB —
đủnhỏđểcùng với vùng làm việc thường trú trọn vẹn trong bộnhớđệm 64 KB, mởkhóa tốc độsuy luận
tối ưu.
55


---

## Trang 70

CHƯƠNG 5. TRIỂN KHAI VÀ ĐÁNH GIÁ THỰC NGHIỆM
Bảng 5.1: Các cột mốc tiến hóa kiến trúc mô hình phát hiện té ngã trên ESP32-S3
Phiên bản Kiến trúc
#Nhãn Thay đổi chính & lý do loại bỏ/ giữlại
v1–v7
CNN-LSTM,
Two-
Stream
4
Mô hình nền. 4 nhãn quá thô, nhầm lẫn nặng giữa Trans và Fall;
bổsung kênh Jerk làm đầu vào phình lên 9 kênh, tốn tài nguyên
→loại.
v8–v17
TCN giãn nở(dilation 1–
8)
4→6
Trường nhìn tốt nhưng v12/v14 chứa lớp Lambda/float16 không
tương thích TFLM. v16–v17 chuẩn hóa 6 kênh thô, bỏLambda;
mởrộng lên 6 nhãn.
v18–v19
TCN giãn nở
6→5
Gộp hai trạng thái tĩnh Lie + StandSit thành Idle (không thểtách,
không thiết yếu) →chốt 5 nhãn.
v20–v22
TCN + GAP/GMP + SE +
Label Smoothing
5
Tăng kernel 5 →7 (trường nhìn 121 →181 mẫu), thêm SE
block, phạt nặng lớp Fall. TCN tốt nhất (Acc 91,56%) nhưng giãn
nởsinh SPACE_TO_BATCH_ND →∼286 ms, không khảthi.
v23–v24
TCN bỏgiãn nở(strided
conv)
5
Thay giãn nởbằng strided conv + MaxPool, padding same →xóa
toán tửxáo trộn; gắn cứng tiền xửlý + ReLU6. Vẫn còn ∼180–
220 ms.
v25
ResNet-1D + Separable-
Conv + SE
5
CNN dạng ResNet, nhanh hơn (∼32–70 ms) nhưng SE/sigmoid
chưa tăng tốc, lỗi scaling gyro (mù xoay), tệp INT8 lớn do meta-
data phình.
v30
CNN
thuần
Separable-
Conv (6 trục)
5
Sửa scaling gyro (±500 dps), bỏhẳn SE & sigmoid →100% toán
tửthân thiện ESP-NN. ∼25 KB, 19,78 ms. Nhanh nhất nhưng yếu
ởIdle/Trans (head pooling xóa trục thời gian).
v31
CNN thuần (4 trục: Accel
+ Gyro RMS)
5
Rút đầu vào còn 4 kênh, tựtính Gyro RMS trên thiết bị→nhẹ
nhất, arena ∼16,5 KB, 19,25 ms. Nhanh hơn v30 không đáng kể
(∼0,5 ms) nhưng kém chính xác hơn do mất 3 trục gyro gốc →
không ưu tiên.
v32
CNN thuần, thửcửa sổ
128/256
5
Khảo sát kích thước cửa sổ; bản 256 mẫu (2,56 s) cho độchính xác
tương đương v30 (firmware 92,70%, 25,07 ms). Cửa sổlũy thừa
của 2 không giúp tăng tốc — độtrễtỷlệtuyến tính với độdài cửa
sổ.
v30_opt
CNN
head
GAP+GMP+Flatten
(6 trục)
5
Cải tiến head giữlayout thời gian (chắt lọc nguyên lý của TCN),
sâu/rộng hơn (26.629 params). Trans F1 0,80 →0,91 (≈TCN),
11,20 ms, arena 28,3 KB. Bản deploy đềxuất cuối.
5.1.5
Mô hình triển khai đềxuất cuối cùng (v30_optimize)
Trong nhóm CNN thuần, các phiên bản baseline (v30, v31) tuy đạt tốc độlý tưởng (từ5–19 ms) nhưng
luôn yếu nhất ởhai nhãn khó là Idle và Trans (F1-Trans chỉ0,799 so với 0,927 của TCN), do khối gộp
đặc trưng GAP+GMP nén phẳng trục thời gian của cửa sổ. Mô hình triển khai đềxuất cuối cùng —
v30_optimize (26.629 tham số) — khắc phục hạn chếnày bằng khối gộp GAP+GMP+Flatten giữlại bố
cục thời gian của bản đồđặc trưng, kết hợp mởrộng trường nhìn bằng tích chập có bước nhảy (strided conv)
và MaxPool — đều là toán tửđược ESP-NN tăng tốc — thay cho tích chập giãn nở. Nhờđó, mô hình nâng
điểm F1 nhãn Trans từ0,799 lên 0,907 (tiệm cận TCN) và Idle từ0,910 lên 0,942, trong khi vẫn chạy thuần
trên ESP-NN và chỉtốn 11,20 ms mỗi lượt suy luận — nhanh gấp ∼180 lần so với TCN giãn nở(2014 ms).
Quá trình đi tới cải tiến này không hiển nhiên: nó bao gồm cảmột thửnghiệm Chưng cất tri thức
(Knowledge Distillation) từTCN sang CNN thất bại nhưng có giá trị, giúp nhận ra điểm yếu Idle/Trans là
một giới hạn kiến trúc (do head pooling xóa trục thời gian) chứkhông phải giới hạn huấn luyện có thểvá
bằng nhãn mềm. Vì đây là lập luận thiết kếcốt lõi — đóng góp nghiên cứu trọng tâm của đồán — toàn bộ
phân tích chi tiết (thất bại của KD, thí nghiệm cắt bỏchứng minh thắng lợi đến từkiến trúc, và việc đổi tiêu
chí chọn mô hình sang val_accuracy) được trình bày ởMục 5.2. Sốliệu so sánh định lượng đầy đủgiữa
các họkiến trúc được trình bày ngay ởMục 4.3 tiếp theo.
5.1.6
Triển khai hạtầng giao tiếp MQTT
Trong quá trình triển khai thực tế, hệthống không sửdụng các dịch vụMQTT Broker công cộng (Public
Broker) nhằm tránh rủi ro rò rỉdữliệu y tế, mà tận dụng hệthống MQTT Broker nội bộ(Private Broker)
do giáo viên hướng dẫn cung cấp. Máy chủBroker được đặt tại tên miền mqtt.toolhub.app, mang lại
nhiều lợi thếkỹthuật quan trọng cho hệthống:
• Đảm bảo tính bảo mật và quyền riêng tư: Dữliệu sinh hiệu (vitals) và tín hiệu IMU mang tính cá
nhân cao. Private Broker bảo mật kết nối thông qua tài khoản đăng nhập (Authentication) và phân
56


---

## Trang 71

CHƯƠNG 5. TRIỂN KHAI VÀ ĐÁNH GIÁ THỰC NGHIỆM
quyền chặt chẽ. Đặc biệt, hệthống hỗtrợkết nối mã hóa qua cổng 8883 (MQTTS) và 8084 (WSS),
giúp mã hóa toàn bộluồng dữliệu trên đường truyền (data in transit), ngăn chặn các nguy cơ nghe
lén (Man-in-the-Middle).
• Tối ưu hóa độtrễvà băng thông: Với yêu cầu stream dữliệu IMU liên tục ởtần sốcao (100 Hz),
hệthống đòi hỏi mạng phải có độtrễcực thấp. Hạtầng Private Broker giúp giảm thiểu tối đa hiện
tượng nghẽn mạng do chia sẻtài nguyên (như trên Public Broker) và rớt gói tin (packet loss), đảm
bảo backend và giao diện giám sát luôn nhận được dòng dữliệu trơn tru.
• Hỗtrợgiao tiếp đa giao thức linh hoạt: Broker được cấu hình mở4 cổng giao tiếp riêng biệt:
1883 (MQTT) dành cho kết nối từthiết bịESP32 (tiết kiệm tài nguyên xửlý SSL/TLS trên chip); và
8083/8084 (WebSockets/Secure WebSockets) phục vụriêng cho Frontend Next.js. Sựphân tách và
hỗtrợđa giao thức này giúp Web Dashboard có thểsubscribe trực tiếp vào luồng dữliệu thô (raw
data) đểvẽbiểu đồvà hiện cảnh báo ngay tức khắc mà không phải tạo thêm gánh nặng cho Backend.
Hệthống đã kết nối và vận hành rất ổn định trên Private Broker này xuyên suốt quá trình kiểm thửphần
cứng bằng các công cụbên thứba (MQTT Explorer, MQTTX), thu thập bộdữliệu, cũng như trong các kịch
bản đánh giá nhận diện cảnh báo ngã.
5.1.7
Triển khai phần mềm máy chủ(Backend)
Phần mềm máy chủ(Backend) được phát triển dựa trên framework FastAPI của ngôn ngữPython, tận
dụng triệt đểtính năng xửlý bất đồng bộ(Asynchronous) đểđạt hiệu suất cao. Hệthống Backend đóng vai
trò là cầu nối cốt lõi giữa thiết bịphần cứng, cơ sởdữliệu và ứng dụng người dùng, với các nhiệm vụchính:
• Cung cấp giao diện lập trình ứng dụng (RESTful API): Xây dựng các điểm cuối (endpoints)
chuẩn hóa theo phiên bản (VD: /api/v1/devices, /api/v1/wearers) phục vụviệc quản trị
dữliệu, phân quyền JWT và truy vấn lịch sửcảnh báo. Hệthống đảm bảo tính toàn vẹn dữliệu bằng
Unique Device Assignment (Một bệnh nhân chỉgắn với một thiết bị). Ngoài ra, Backend còn tổng
hợp dòng thời gian hoạt động (timeline) của mỗi thiết bịbằng cách hợp nhất (UNION) lịch sửcảnh
báo té ngã và nhật ký sựkiện thiết bị.
• Cầu nối bản tin MQTT (MQTT Bridge): Backend duy trì một MQTT Client bất đồng bộthường
trực, lắng nghe đồng thời ba luồng chủđềtheo ký tựđại diện: bản tin trạng thái (status) đểcập
nhật mức pin, thời điểm online và sốliệu viễn trắc; bản tin cảnh báo (alert/fall) đểtạo bản ghi
cảnh báo; và bản tin sựkiện (event) đểghi nhật ký thiết bị. Cơ chếtựkết nối lại (auto-reconnect)
bảo đảm cầu nối không gián đoạn trong môi trường mạng di động.
• Điều khiển và cấu hình thiết bịtừxa: Thông qua endpoint command, Backend chuyển tiếp các lệnh
thời gian thực (bật/tắt chếđộtruyền dữliệu thô) từgiao diện web xuống thiết bịqua MQTT. Vềcác
tham sốhệthống, người dùng thao tác qua form (có hỗtrợdropdown, trong đó rssi_interval
có lựa chọn "Tắt"). Form sẽgửi yêu cầu PUT /devices/{id} lên Backend. Sau đó, máy chủ
publish các thông sốthay đổi vào topic eldercare/{mac}/config/set. Thiết bịnhận được
sẽáp dụng, lưu xuống NVS, và dội lại thông điệp eldercare/{mac}/config/status đểmáy
chủđồng bộvới cơ sởdữliệu. Nhằm đảm bảo luồng khẩn cấp không bịđứt đoạn, thiết bịáp dụng cơ
chếbảo vệtrạng thái giao tiếp cốt lõi (comms-critical guard): bỏqua việc đo RSSI 4G khi đang xác
nhận hoặc phát tín hiệu cảnh báo.
• Thuật toán nội suy quãng đường: Khi nhận bản tin trạng thái chứa sốbước đi bộvà sốbước chạy
được tách riêng từthiết bị, Backend truy vấn chiều cao của bệnh nhân từPostgreSQL rồi áp dụng
công thức sinh trắc học (sải chân đi bộvà chạy có hệsốkhác nhau) đểước lượng quãng đường di
chuyển thực tếvà ghi vào InfluxDB mà không cần module GPS.
• Phân luồng cơ sởdữliệu kép đa khách thuê: Đóng vai trò định tuyến dữliệu thông minh. Các thông
tin cấu trúc (thiết bị, bệnh nhân) được lưu vào PostgreSQL thông qua ORM với trường org_id để
57


---

## Trang 72

CHƯƠNG 5. TRIỂN KHAI VÀ ĐÁNH GIÁ THỰC NGHIỆM
cách ly dữliệu giữa các viện dưỡng lão (Multi-tenancy), trong khi dữliệu chuỗi thời gian được ghi
vào InfluxDB. Riêng trong giai đoạn thu thập dữliệu huấn luyện, endpoint data-collection
tiếp nhận các phiên ghi IMU thô, thực hiện tiền xửlý và cắt cửa sổ(sửdụng thư viện SciPy) trước khi
lưu vào measurement imu_windowed.
5.1.8
Triển khai giao diện giám sát (Frontend)
Giao diện người dùng (Frontend) được thiết kếchuyên biệt đểhỗtrợnhân viên y tếgiám sát đồng thời
sốlượng lớn thiết bịtrong viện dưỡng lão. Ứng dụng được xây dựng trên nền tảng Next.js 16 (kiến trúc App
Router) kết hợp cùng Turbopack, với các đặc điểm kỹthuật nổi bật:
• Quản lý trạng thái và Dữliệu: Sửdụng thư viện TanStack Query đểtựđộng đồng bộvà lưu bộ
nhớđệm (cache) dữliệu từBackend, kết hợp cùng Zustand đểquản lý các trạng thái cục bộ.
• Cơ chếĐồng bộcảnh báo lai (Hybrid Alert Sync): Giao diện tích hợp MQTT.js kết nối trực tiếp
với Broker qua WebSockets. Khi có sựkiện té ngã, cảnh báo khẩn cấp (âm thanh và banner) xuất hiện
ngay lập tức (trễ< 1s). Song song đó, Frontend chủđộng gửi tín hiệu "invalidate cache" đểTanStack
Query kéo danh sách lịch sửcảnh báo mới nhất từBackend vềđồng bộ, kết hợp hoàn hảo giữa tốc độ
của MQTT và tính nhất quán của REST API (Hình 5.3).
• Giám sát thời gian thực và Lớp phủcảnh báo: Giao diện đăng ký các chủđềtrạng thái và cảnh báo
qua MQTT, lưu dữliệu viễn trắc tức thời (mức pin, sốbước đi bộ/chạy) vào kho trạng thái cục bộđể
cập nhật trực tiếp lên thẻthiết bịmà không cần tải lại trang. Khi phát hiện té ngã, một lớp phủtoàn
màn hình màu đỏ(FallDetectionOverlay) hiện ra kèm thông tin thiết bị, thời điểm, độtin cậy
của mô hình, nút xác nhận đã xửlý và âm thanh báo động, bảo đảm nhân viên y tếkhông bỏsót sự
kiện khẩn cấp (xem Hình 5.4 và 5.5).
• Bộmàn hình quản lý và cấu hình thiết bị: Ngoài bảng điều khiển chính, ứng dụng cung cấp
các trang chuyên biệt cho từng thiết bị: trang cấu hình (điều chỉnh chu kỳgửi viễn trắc, tinh chỉnh
ngưỡng phát hiện ngã bằng thanh trượt 15–95%, thời gian hồi cảnh báo, cửa sổxác nhận hậu va chạm
fall_confirm_window, chu kỳđo RSSI rssi_interval qua dropdown với tùy chọn "Tắt",
và bật/tắt theo dõi), trang chỉsốsinh tồn (Hình 5.7), trang lịch sửhoạt động (Hình 5.6) và trang thu
thập dữliệu IMU (Hình 5.11). Các trang thu thập dữliệu nhận luồng cảm biến 100Hz dưới dạng nhị
phân (mã hóa Base64 sốnguyên 16-bit nhằm giảm khoảng một nửa băng thông so với JSON), vẽbiểu
đồgia tốc/vận tốc góc theo thời gian thực và cho phép xuất tệp CSV phục vụgán nhãn huấn luyện.
Các bảng danh sách tổng hợp (Hình 5.8 và 5.9) giúp quản lý thiết bịvà hồsơ bệnh nhân hiệu quả.
• Thẩm mỹvà trải nghiệm người dùng (UI/UX): Thiết kếsửdụng Tailwind CSS và thư viện
Shadcn UI, mang lại một giao diện hiện đại, trực quan, hỗtrợthiết kếđáp ứng (Responsive) xuất
sắc trên cảmàn hình máy tính bảng và màn hình giám sát trung tâm.
58


---

## Trang 73

CHƯƠNG 5. TRIỂN KHAI VÀ ĐÁNH GIÁ THỰC NGHIỆM
Hình 5.3: Sơ đồTuần tựcủa Cơ chếĐồng bộcảnh báo lai (Hybrid Alert Sync) trên Frontend
Hình 5.4: Giao diện bảng điều khiển trung tâm (Dashboard) giám sát đa thiết bị
Giao diện bảng điều khiển trung tâm (Hình 5.4) là nơi nhân viên y tếtheo dõi tổng quan toàn bộthiết
bịđang hoạt động. Mỗi thiết bịđược hiển thịdưới dạng một thẻ(card) cung cấp các thông tin thiết yếu như
mức pin hiện tại, cường độsóng 4G, trạng thái kết nối trực tuyến (online/offline) và sốbước chân được cập
nhật theo thời gian thực.
59


---

## Trang 74

CHƯƠNG 5. TRIỂN KHAI VÀ ĐÁNH GIÁ THỰC NGHIỆM
Hình 5.5: Lớp phủcảnh báo ngã khẩn cấp toàn màn hình với độtin cậy của AI
Khi một sựkiện té ngã được thiết bịphát hiện và gửi vềmáy chủ, một lớp phủmàu đỏ(Hình 5.5) sẽ
ngay lập tức xuất hiện toàn màn hình kèm theo âm thanh báo động. Giao diện này cung cấp đầy đủthông
tin vềthiết bị, thời gian xảy ra sựkiện và mức độtin cậy của dựđoán AI, đòi hỏi nhân viên y tếphải bấm
xác nhận "Đã xửlý" đểghi nhận và tắt báo động.
Hình 5.6: Lịch sửtrạng thái và nhật ký hoạt động
Trang lịch sử(Hình 5.6) cung cấp biểu đồthểhiện các trạng thái hoạt động của người đeo (Đi bộ, Chạy,
Nằm, Đứng/Ngồi) theo thời gian. Các sựkiện ngã được đánh dấu bằng các mốc màu đỏnổi bật, đi kèm bên
dưới là danh sách chi tiết các bản ghi nhật ký hoạt động của thiết bị.
60


---

## Trang 75

CHƯƠNG 5. TRIỂN KHAI VÀ ĐÁNH GIÁ THỰC NGHIỆM
Hình 5.7: Biểu đồsinh hiệu (Pin và sóng 4G)
Đểđảm bảo thiết bịluôn trong trạng thái sẵn sàng, trang sinh hiệu (Hình 5.7) vẽbiểu đồlịch sửmức pin
và cường độtín hiệu mạng di động. Việc theo dõi xu hướng này giúp nhân viên y tếchủđộng nhắc nhởsạc
pin hoặc phát hiện các vùng không có sóng 4G trong viện dưỡng lão.
Hình 5.8: Quản lý thiết bịđăng ký tựđộng (Auto-provision)
Hình 5.8 minh họa màn hình quản lý thiết bị, nơi liệt kê toàn bộcác phần cứng đã được kích hoạt. Nhờ
cơ chếtựđộng đăng ký (Auto-provision) qua MQTT, thiết bịmới hoặc sau khi xuất xưởng chỉcần kết nối
mạng là sẽtựđộng xuất hiện trên hệthống mà không cần các thao tác thêm mới thủcông từquản trịviên.
61


---

## Trang 76

CHƯƠNG 5. TRIỂN KHAI VÀ ĐÁNH GIÁ THỰC NGHIỆM
Hình 5.9: Quản lý hồsơ bệnh nhân
Hệthống quản lý thông tin bệnh nhân (Hình 5.9) lưu trữcác thông tin sinh trắc học cơ bản như chiều
cao, cân nặng, độtuổi. Đặc biệt, thông sốchiều cao được thuật toán phía Backend sửdụng đểnội suy chính
xác sải chân và quãng đường di chuyển dựa trên sốbước chân đếm được.
Hình 5.10: Lịch sửcảnh báo toàn hệthống
Trang lịch sửcảnh báo (Hình 5.10) tổng hợp toàn bộcác sựkiện té ngã hoặc mức pin tới hạn của tất cả
các thiết bị. Quản trịviên có thểdễdàng lọc theo thời gian, thiết bịhoặc bệnh nhân đểtrích xuất báo cáo
định kỳphục vụphân tích điều dưỡng.
62


---

## Trang 77

CHƯƠNG 5. TRIỂN KHAI VÀ ĐÁNH GIÁ THỰC NGHIỆM
Hình 5.11: Thu thập dữliệu IMU thời gian thực
Phục vụcho mục đích nghiên cứu phát triển mô hình (Data Collection), giao diện ởHình 5.11 cho phép
hiển thịtrực tiếp đồthịtín hiệu gia tốc và vận tốc góc ởtần số100Hz ngay trên trình duyệt. Người dùng có
thểgiám sát dạng sóng theo thời gian thực, gắn nhãn hành vi đang thực hiện (theo mã chuẩn của tập dữliệu
SisFall) và xuất trực tiếp ra tệp CSV đểlàm nguồn dữliệu tái huấn luyện (Retraining).
5.2
Kết quảđạt được và Kiểm thử
5.2.1
Đánh giá hiệu năng mô hình phân loại
Nhằm đảm bảo kết quảđánh giá phản ánh trung thực khảnăng tổng quát hóa của mô hình trên dữliệu
chưa gặp trong quá trình huấn luyện, toàn bộquy trình thực nghiệm áp dụng phương pháp phân chia theo
đối tượng (Leave-Subjects-Out — LSO). Toàn bộ38 đối tượng của bộdữliệu SisFall được phân chia cố
định thành ba tập không giao nhau: tập huấn luyện gồm SA01–SA18 và SE01–SE08, tập kiểm định gồm
SA19–SA21 và SE09–SE11, và tập kiểm tra độc lập gồm SA22–SA23 và SE12–SE15. Cách phân chia này
loại trừkhảnăng mô hình ghi nhớđặc điểm sinh lý riêng của từng cá nhân thay vì học được biểu diễn đặc
trưng hành vi tổng quát, từđó phản ánh đúng khảnăng vận hành thực tếtrên những người dùng mới.
Các chỉsốđánh giá bao gồm độchính xác tổng thể(Accuracy), điểm F1 trên nhãn Fall (F1-Fall) và
điểm F1 trung bình không trọng sốtrên cảnăm nhãn (Macro-F1). Trong bối cảnh ứng dụng y tếkhẩn cấp,
độnhạy (Recall) của nhãn Fall được ưu tiên cao hơn độđặc hiệu (Precision), vì một cú ngã bịbỏsót gây
hậu quảnghiêm trọng hơn so với một cảnh báo sai. Bảng 5.2 tổng hợp kết quảso sánh giữa các phiên bản
kiến trúc chính trên tập kiểm tra độc lập.
63


---

## Trang 78

CHƯƠNG 5. TRIỂN KHAI VÀ ĐÁNH GIÁ THỰC NGHIỆM
Bảng 5.2: So sánh hiệu năng các phiên bản mô hình trên tập kiểm tra độc lập (LSO)
Ver.
Kiến trúc
#Nhãn
Acc. (%) F1-Fall
F1-Trans Macro-F1
Thếhệ1 — pipeline windowing ban đầu (9.135 mẫu)
v1
CNN-LSTM baseline
4
91,57
0,9755
—
0,9294
v4
TCN (tốt nhất 4 nhãn)
4
92,41
0,9774
—
0,9353
v8
TCN dilated causal
4
91,34
0,9667
—
0,9303
v18
TCN chuyển sang 5 nhãn
5
89,89
0,9759
0,7820
0,9092
v22
TCN + SE + Dual Pooling
5
91,56
0,9786
0,8554
0,9267
v23
TCN + ngưỡng Fall tối ưu
5
91,33
0,9832
0,8444
0,9273
v25
ResNet-1D + SeparableConv
5
91,01
0,9784
0,8365
0,9238
v26_v3
ResNet-1D + Focal Loss
5
88,54
0,9514
0,8041
0,8964
Thếhệ2 — pipeline tinh chỉnh (6.106 mẫu)
v30
CNN thuần (6 trục)
5
93,43
0,9859
0,7993
0,9259
v31
CNN thuần (4 trục)
5
92,37
0,9779
0,7878
0,9154
v30_optimize
CNN head Flatten (6 trục)
5
95,33
0,9826
0,9071
0,9524
v30_lstm32
CNN + LSTM
5
92,74
0,9782
0,8322
0,9235
v30_resnet1d
ResNet-1D + SE block
5
94,15
0,9831
0,8484
0,9367
v30_tcn_opt
TCN bỏgiãn nở
5
93,81
0,9797
0,8315
0,9310
v30_tcn
TCN giãn nở(cổđiển)
5
96,02
0,9785
0,9266
0,9596
Hình 5.12: Tiến trình tối ưu hóa hiệu năng các phiên bản mô hình trên tập kiểm tra độc lập
Đểminh họa chi tiết hơn cho phiên bản v30_optimize được chọn, Hình 5.13 trình bày đối chiếu ma
trận nhầm lẫn (Confusion Matrix) giữa hai môi trường: mô hình nguyên bản Float32 đánh giá trên máy tính
bằng Python (trái) và mô hình đã qua lượng tửhóa INT8 chạy thực tếtrên vi điều khiển ESP32-S3 với bộ
tăng tốc ESP-NN (phải).
64


---

## Trang 79

CHƯƠNG 5. TRIỂN KHAI VÀ ĐÁNH GIÁ THỰC NGHIỆM
Mô hình gốc (Float32 / Python)
Mô hình INT8 (ESP-NN / ESP32-S3)
Hình 5.13: Ma trận nhầm lẫn (Confusion Matrix) của mô hình v30_optimize trên tập kiểm tra độc lập
Việc đối chiếu này khẳng định quá trình lượng tửhóa xuống sốnguyên 8-bit không làm suy giảm hiệu
năng của mô hình. Các nhãn quan trọng như Fall và các hoạt động động (Walk, Run) vẫn duy trì khảnăng
phân loại xuất sắc. Lỗi nhầm lẫn duy nhất tập trung ởnhãn Idle và Trans, phản ánh bản chất của việc gộp
trục thời gian bằng Flatten trong kiến trúc CNN. Tuy nhiên, sựphân bốnày là hoàn toàn chấp nhận được
trong bối cảnh ứng dụng thực tế. Bảng 5.2 được chia thành hai nhóm tương ứng hai thếhệpipeline tiền xử
lý. Nhóm trên (v1–v26) phản ánh giai đoạn thăm dò kiến trúc trên pipeline ban đầu. Nhóm dưới gồm nhiều
kiến trúc khác nhau (CNN thuần, CNN+LSTM, ResNet-1D, TCN) cùng được huấn luyện và đánh giá trên
pipeline tinh chỉnh (thang đo gyro ±500 dps và tăng cường biên độcho lớp Trans), cho phép so sánh công
bằng giữa các họmô hình trên cùng một tập dữliệu.
Trong nhóm dưới, có thểthấy rõ v30_tcn (TCN giãn nở) đạt độchính xác cao nhất (Accuracy 96,02%,
Macro-F1 0,9596) và đặc biệt vượt trội ởnhãn khó Trans (F1-Trans 0,9266 so với chỉ≈0,80 của các kiến
trúc CNN thuần) — nhờtích chập giãn nởmởrộng trường nhìn, nắm bắt tốt ngữcảnh chuỗi thời gian dài
của hành vi chuyển tiếp. Tuy nhiên, như sẽphân tích ởMục 4.3.2, chính kiến trúc giãn nởnày lại bất khảthi
vềtốc độtrên vi điều khiển. Điểm mấu chốt là phiên bản v30_optimize đã thu hẹp gần như toàn bộkhoảng
cách đó: nhờhead Flatten giữlại trục thời gian (Mục 4.2.5), nó đạt F1-Trans 0,9071 và Accuracy 95,33%
— tiệm cận TCN nhưng vẫn thuần toán tửESP-NN nên triển khai được. Vì vậy v30_optimize được chọn
làm mô hình triển khai đềxuất, thay cho các bản CNN baseline (v30, v31) vốn yếu hơn rõ rệt ởIdle/Trans.
Vì hai nhóm dùng tập kiểm tra có sốmẫu khác nhau (9.135 so với 6.106 mẫu), các chỉsốchỉnên so sánh
trực tiếp trong cùng một nhóm.
5.2.2
Đánh giá hiệu năng suy luận trên vi điều khiển
Đểkiểm chứng định lượng các nguyên tắc thiết kếhướng phần cứng đã nêu ởMục 4.2, mỗi họkiến trúc
tiêu biểu đều được xuất INT8 và đo trực tiếp thời gian suy luận trên Seeed Studio XIAO ESP32S3 (Xtensa
LX7 ở240 MHz) thông qua công cụkiểm thửfirmware — nạp lần lượt từng mô hình lên chip và chạy lại
toàn bộtập kiểm tra ngay trên thiết bị. Trước hết, ảnh hưởng của băng thông bus bộnhớthểhiện rất rõ ở
phiên bản ResNet-1D (v25) hiện đang vận hành trên thiết bịtích hợp (cấu hình arena trên PSRAM, CPU
160 MHz): cùng một mô hình, khi đọc trọng sốqua Quad SPI ở40 MHz mất trung bình 70,23 ms mỗi lần
suy luận (min 70,07 / max 70,32 ms), nhưng khi chuyển sang Octal SPI ở80 MHz thời gian rút còn khoảng
32 ms. Điều này khẳng định lập luận vềphân cấp bộnhớ: khi trọng sốchưa lọt trọn bộnhớđệm, tốc độnạp
từFlash trởthành nút cổchai.
Bảng 5.3 so sánh trực tiếp các họkiến trúc khi cùng được huấn luyện trên pipeline tinh chỉnh và đo trên
cùng phần cứng với cờtối ưu ESP-NN được kích hoạt. Kết quảcho thấy khoảng cách hiệu năng khổng lồ
giữa các kiến trúc: nhóm CNN thuần (v30, v31) đạt độtrễcực thấp dưới 12 ms, trong khi TCN giãn nởcổ
65


---

## Trang 80

CHƯƠNG 5. TRIỂN KHAI VÀ ĐÁNH GIÁ THỰC NGHIỆM
điển mất tới hơn 2 giây — chậm gấp hơn 180 lần — do tích chập giãn nởvà các toán tửxáo trộn bộnhớ
không được ESP-NN tăng tốc. Ngay cảcác biến thể"lai" như CNN+LSTM cũng bịkéo lùi vì khối lượng
tính toán nội tại lớn không thểsong song hóa hoàn toàn.
Bảng 5.3: So sánh hiệu năng suy luận các họkiến trúc trên ESP32-S3 (INT8, CPU 240 MHz, bật tối ưu ESP-NN)
Mô hình
Họkiến trúc
Kích thước
Arena
Trễ
Acc.
Fall
INT8 (kB)
(kB)
(ms)
(%)
Recall
v32_w128
CNN thuần (cửa sổ128)
24,5
12,5
3,72
92,20
98,00%
v31
CNN thuần (4 trục)
24,9
16,5
5,13
92,60
97,50%
v30
CNN thuần (6 trục)
25,0
16,5
5,14
93,00
97,50%
v32_w256
CNN thuần (cửa sổ256)
24,5
19,6
6,04
92,80
99,00%
v30_optimize
CNN head Flatten (6 trục)
55,8
28,3
11,20
95,40
97,50%
v30_resnet1d
ResNet-1D + SE block
83,3
25,1
20,16
95,00
96,50%
v25
ResNet-1D (cũ)
80,0
28,9
22,27
90,60
94,00%
v30_lstm32
CNN + LSTM
39,2
80,4
94,46
94,50
95,50%
v30_tcn_opt
TCN bỏgiãn nở
65,6
49,6
137,57
95,60
97,00%
v30_tcn
TCN giãn nở(cổđiển)
105,0
50,1
2014,30
95,80
98,50%
Ghi chú: Tất cảmô hình đều được đo ởCPU 240 MHz và bật tối ưu ESP-NN.
Hình 5.14: Sơ đồđánh đổi hiệu năng, tốc độsuy luận và kích thước giữa các kiến trúc trên vi điều khiển ESP32-S3
Cột độchính xác tổng thểlàm rõ cảbức tranh đánh đổi lẫn lời giải cho nó. Trước khi có v30_optimize
tồn tại một mâu thuẫn: TCN cho độchính xác cao nhất nhưng độtrễhơn 2000 ms khiến nó bất khảthi,
trong khi các CNN thuần nhanh (v30, v31; chỉtốn ∼5 ms) lại yếu ởIdle/Trans. Phiên bản v30_optimize
hóa giải mâu thuẫn này: nó đạt độchính xác firmware cao nhất bảng (95,40%, ngang TCN) nhưng chỉtốn
11,20 ms — nhanh gấp ∼180 lần TCN và vẫn thừa sức xửlý thời gian thực. Đây là minh chứng định lượng
cho luận điểm ởMục 4.2.5: việc chuyển nguyên lý giữ-cấu-trúc-thời-gian của TCN sang một CNN thân
thiện ESP-NN cho phép đạt độchính xác của TCN mà gần như không phải trảgiá vềtốc độ. Đó là lý do
v30_optimize được chọn làm mô hình triển khai đềxuất.
Một quan sát đáng chú ý khác đến từthí nghiệm khảo sát kích thước cửa sổ(v32), giữnguyên kiến
trúc CNN thuần 6 trục như v30 và chỉđổi độdài cửa sổ. Cảba mốc cho thấy độtrễtỷlệgần như tuyến
tính với sốmẫu thời gian: cửa sổ128 mẫu chạy 3,72 ms, 200 mẫu (v30) 5,14 ms, và 256 mẫu 6,04 ms
— các tỷlệ3,72/5,14 ≈0,72 và 6,04/5,14 ≈1,18 gần sát với tỷlệđộdài cửa sổ(128/200 = 0,64 và
256/200 = 1,28), trong khi độchính xác giữa các mốc gần như tương đương. Tuy nhiên cấu hình w256 lại
66


---

## Trang 81

CHƯƠNG 5. TRIỂN KHAI VÀ ĐÁNH GIÁ THỰC NGHIỆM
đạt Fall Recall xuất sắc tuyệt đối lên tới 99,00%. Nói cách khác, việc chọn kích thước cửa sổlà lũy thừa của
2 (128 hay 256) không mang lại sựđột biến vềtăng tốc nào, thời gian chủyếu phụthuộc vào tổng sốphép
tính. Đây là một lưu ý thực nghiệm hữu ích khi tinh chỉnh siêu tham số.
Xét riêng nhóm CNN thuần baseline, v30 (6 trục) và v31 (4 trục) đều đạt độtrễsiêu thấp ∼5 ms. Việc
v31 rút đầu vào còn bốn kênh làm mất thông tin chuyển động xoay, kéo độchính xác xuống thấp hơn v30;
do đó v30 là baseline tốt hơn. Tuy nhiên cảhai baseline này đều bịgiới hạn ởIdle/Trans bởi head pooling.
Phiên bản v30_optimize — với head Flatten giữtrục thời gian — vượt trội cảhai vềđộchính xác (Bảng
5.2 và 5.3), trong khi độtrễ11,20 ms vẫn cực kỳnhỏso với chu kỳcập nhật cửa sổ500 ms. Vì vậy, đồán
chọn v30_optimize làm mô hình triển khai đềxuất cuối cùng.
Bảng 5.4 đối chiếu trực tiếp v30_optimize với phiên bản v25 cũ. Nhờkiến trúc head giữtrục thời gian,
v30_optimize có trọng sốnhỏhơn hẳn (55,8 KB so với 80,0 KB), độchính xác cao hơn (95,40% so với
90,60%), và tốc độnhanh gấp đôi (11,20 ms so với 22,27 ms). Yếu tốcốt lõi vềtốc độbên cạnh tập lệnh
véc-tơ SIMD còn là việc trọng sốcó lọt bộnhớđệm 64 KB hay không: cảv30_optimize (55,8 KB) lẫn các
CNN baseline đều nằm gọn trong cache nên không bịnghẽn nạp trọng số, trong khi v25 (80,0 KB) vượt quá
dung lượng cache và phải liên tục nạp lại qua bus SPI. Cần nhấn mạnh rằng một khi trọng sốđã đủnhẹđể
thường trú trong bộnhớđệm, việc đặt vùng làm việc ởSRAM nội hay PSRAM ngoài gần như không tạo ra
khác biệt vềtốc độ— yếu tốquyết định là kích thước trọng sốso với dung lượng bộnhớđệm, chứkhông
phải nơi cấp phát arena. Thực nghiệm đo trực tiếp trên v30 và v31 (tensor arena xấp xỉ16 KB, lọt trọn bộ
nhớđệm 64 KB) xác nhận thời gian suy luận khi đặt arena ởSRAM nội và PSRAM ngoài chênh lệch dưới
0,5 ms, trong khi v25 (vượt cache) bịphụthuộc rõ vào băng thông bus.
Bảng 5.4: Đối chiếu tài nguyên phần cứng: phiên bản v25 cũ và phương án đềxuất v30_optimize (cảhai đều bật ESP-
NN)
Chỉsố
v25 (ResNet-1D cũ)
v30_optimize (đềxuất)
Thời gian suy luận (ms)
22,27
11,20
Kích thước mô hình INT8
≈80,0 kB
≈55,8 kB
Tensor arena thực dùng
28,9 kB (SRAM)
28,3 kB (SRAM)
Độchính xác trên firmware
90,60%
95,40%
Fall Recall trên firmware
94,00%
97,50%
Với độtrễchớp nhoáng chỉ11,20 ms đo được trên chip — chỉbằng một nửa của một khung mẫu 10 ms
(100Hz) và chưa tới 3% chu kỳcập nhật cửa sổtrượt 500 ms — v30_optimize thừa thời gian hoàn tất mỗi
lượt suy luận mà gần như không chiếm dụng CPU, không gây trệhàng đợi (queue backpressure) và nhường
toàn bộtài nguyên còn lại cho các tác vụtruyền thông. So với v25 cũ, v30_optimize nhanh gấp 2 lần, đồng
thời nhẹhơn vềdung lượng Flash và chính xác hơn hoàn toàn vềtổng thể(Acc từ90,60% lên 95,40%,
Fall Recall từ94,00% lên 97,50%). Sựkhác biệt vềTensor Arena là không đáng kể. Do đó, thay thếbằng
v30_optimize làm firmware sản phẩm là bước tiến nhảy vọt của hệthống.
a, Triển khai cơ chếxác nhận ngã hậu va chạm
Cơ chếxác nhận ngã hai pha được triển khai bằng một máy trạng thái phụtrong tác vụsvc_ai. Trên
mỗi cửa sổsuy luận, nếu FSM đang ởNORMAL và dựđoán lớp Fall vượt ngưỡng, hệthống sẽchuyển sang
nhánh CONFIRMING. Tại đây, một mốc thời gian được lưu lại và thiết bịlập tức đọc trạng thái va chạm gần
nhất thông qua hàm imu_service_get_last_impact(). Trong quá trình CONFIRMING, hệthống
liên tục tính tỉlệsốcửa sổtrảvềIdle hoặc tư thếnằm trên tổng sốmẫu. Nếu phát hiện người dùng có vận
động (lớp Walk/Run kèm tư thếđứng), FSM sẽthoát vềNORMAL (hủy cảnh báo - ABORT). Nếu kết thúc
fall_confirm_window giây mà tỉlệnằm tĩnh ≥0,6, sựkiện AI_EVT_FALL_DETECTED sẽđược
phát ra. Đồng thời, bộphát hiện theo mẫu độc lập trong svc_imu dựa trên giá trịSVM sẽtăng cường tính
chính xác và tránh các nhiễu đo lường do bộlọc Kalman làm trơn.
67


---

## Trang 82

CHƯƠNG 5. TRIỂN KHAI VÀ ĐÁNH GIÁ THỰC NGHIỆM
5.2.3
Kiểm thửtích hợp hệthống đầu cuối
Kiểm thửtích hợp được thực hiện theo hai nhóm kịch bản đối lập nhau. Nhóm thứnhất bao gồm các
kịch bản hoạt động sinh hoạt bình thường như đi bộ, ngồi và đứng dậy, nhằm xác nhận hệthống không phát
sinh cảnh báo sai trong điều kiện sửdụng hàng ngày. Nhóm thứhai bao gồm các kịch bản té ngã giảlập,
nhằm xác minh toàn bộchuỗi sựkiện từcảm biến đến giao diện người dùng được kích hoạt chính xác và
kịp thời.
Trong một kịch bản té ngã điển hình, chuỗi sựkiện lần lượt diễn ra như sau: (i) cảm biến MPU6050 thu
nhận xung gia tốc đặc trưng của cú ngã; (ii) svc_ai xác nhận nhãn Fall khi xác suất đầu ra vượt ngưỡng
P(Fall) ≥0,25; (iii) sys_manager kích hoạt svc_cloud thông qua esp_event; (iv) gói tin cảnh báo
được gửi lên MQTT Broker với mức đảm bảo QoS 1; (v) Backend lưu sựkiện vào PostgreSQL và phát tín
hiệu làm mới bộnhớđệm; (vi) giao diện Dashboard hiển thịcảnh báo khẩn cấp kèm âm thanh. Tổng độtrễ
đầu cuối (end-to-end latency) từthời điểm ngã đến khi cảnh báo xuất hiện trên Dashboard dưới điều kiện
mạng 4G ổn định nhỏhơn 1 giây.
Cơ chếlàm lạnh (cooldown) 15 giây sau mỗi cảnh báo được xác nhận hoạt động đúng, ngăn chặn hiện
tượng gửi cảnh báo lặp lại do cùng một sựkiện ngã kích hoạt nhiều cửa sổphân loại liên tiếp.
Bảng 5.5: Ma trận kịch bản kiểm thửcơ chếxác nhận ngã hai pha
Kịch bản thực tế
Kỳvọng trạng thái FSM
Cảnh báo?
Ngã thật sựvà nằm lại sàn
Vào CONFIRMING →CONFIRMED
Có (sốliệu chờđo
thực địa)
Ngồi phịch mạnh xuống ghế
Vào CONFIRMING →ABORT (phục hồi)
Không
Nhảy và đứng vững
Vào CONFIRMING →ABORT
Không
Đo RSSI trong lúc xác nhận
Hoãn (guard comms-critical) →Giữlink
—
68


---

## Trang 83

CHƯƠNG 6. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN
6.1
Kết luận
Đồán đã hoàn thành mục tiêu đềra ởChương 1: thiết kếvà xây dựng thành công một hệthống giám sát
hành vi và phát hiện té ngã khép kín cho người cao tuổi, vận hành xuyên suốt từthiết bịđeo nhúng đến ứng
dụng web quản trịtập trung. Vềphần cứng, thiết bịtrên nền vi điều khiển ESP32-S3 thực hiện lấy mẫu cảm
biến quán tính ổn định, nội suy mô hình học sâu ngay tại biên và truyền cảnh báo qua mạng 4G LTE bằng
giao thức MQTT mà không phụthuộc vào điện thoại trung gian. Vềphần mềm, hệthống máy chủFastAPI
với kiến trúc cơ sởdữliệu kép (PostgreSQL cho siêu dữliệu và InfluxDB cho dữliệu chuỗi thời gian) cùng
giao diện web thời gian thực cho phép nhân viên y tếgiám sát đồng thời nhiều thiết bịvà tiếp nhận cảnh
báo té ngã với độtrễđầu–cuối dưới một giây.
Quan trọng hơn, đồán đã trảlời được câu hỏi nghiên cứu đặt ra ởChương 1: một mạng học sâu hoàn
toàn có thểđạt độnhạy phát hiện té ngã cao mà vẫn suy luận trọn vẹn trên vi điều khiển tài nguyên hạn
chế. Mô hình đềxuất cuối cùng — v30_optimize, một mạng tích chập tách kênh 1 chiều (Depthwise
Separable 1D CNN) được đồng thiết kếtheo tập lệnh tăng tốc ESP-NN — đạt độchính xác 95,40% và
Fall recall 97,50% đo trực tiếp trên chip, với thời gian suy luận chớp nhoáng chỉ11,20 ms (khoảng 2% chu
kỳcửa sổtrượt 500 ms) và dung lượng xấp xỉ55,8 KB. Bốn đóng góp kỹthuật nổi bật được trình bày ở
Chương 5 gồm: (i) chiến lược thiết kếnhãn 5 lớp kết hợp gán nhãn theo sựkiện nhằm giảm thiểu cảnh báo
giả; (ii) quá trình đồng thiết kếkiến trúc hướng phần cứng, chắt lọc nguyên lý mô hình hóa thời gian của
mạng TCN vào một CNN thân thiện ESP-NN; (iii) cơ chếlấy mẫu IMU chính xác bằng ngắt phần cứng
PCNT; và (iv) cơ chếphát hiện ngã hai pha (kết hợp bộkích hoạt học máy và xác nhận hậu va chạm) giúp
giảm báo động giảmà không hi sinh độnhạy (Fall Recall).
So với các hướng tiếp cận hiện có đã khảo sát ởChương 2, đồán lấp được khoảng trống công nghệgiữa
hai thái cực: các mô hình học sâu chính xác cao nhưng buộc phải chạy trên Cloud/PC, và các thiết bịđeo tự
tính toán nhưng bịgiới hạn ởcác thuật toán ngưỡng hoặc máy học cơ sởdễphát sinh báo động giả. Bằng
việc đưa độchính xác của học sâu xuống chạy trực tiếp trên vi điều khiển giá thành thấp, hệthống vừa bảo
toàn quyền riêng tư (không sửdụng camera, không truyền dữliệu thô lên máy chủ), vừa hoạt động độc lập
và liên tục trên mạng di động.
Bên cạnh các kết quảđạt được, đồán vẫn còn một sốhạn chế. Mô hình được đánh giá chủyếu trên bộdữ
liệu công khai SisFall kết hợp một tập dữliệu tựthu quy mô nhỏ, chưa được kiểm chứng trên sốlượng lớn
người cao tuổi trong điều kiện thực tế. Phiên bản v30_optimize hiện là phương án đềxuất; việc thay thế
hẳn mô hình v25 đang vận hành trong firmware sản phẩm và hoàn thiện cơ chếngủtiết kiệm điện vẫn là
bước triển khai kếtiếp. Bài học lớn nhất rút ra là nguyên tắc thiết kếthuận theo phần cứng (hardware-aware
design): một mô hình chính xác hơn trên máy chủchưa chắc đã khảdụng trên thiết bịbiên — ràng buộc
của tập lệnh tăng tốc phải được đưa vào ngay từkhâu thiết kếkiến trúc, thay vì tối ưu hóa sau khi đã huấn
luyện.
6.2
Hướng phát triển
Đểhoàn thiện hệthống thành một sản phẩm hoàn chỉnh, trước mắt cần tích hợp chính thức mô hình
v30_optimize vào firmware sản phẩm, hoàn thiện cơ chếlấy mẫu PCNT kèm chếđộngủtiết kiệm điện
(Automatic Light Sleep) đã đặc tảởMục 5.3, đồng thời mởrộng tập dữliệu huấn luyện bằng dữliệu vận
động thực tếcủa người cao tuổi thu thập qua chính pipeline thu thập dữliệu của hệthống. Bên cạnh các
công việc hoàn thiện này, đồán xác định một sốhướng nâng cấp giàu tiềm năng sau đây.
Tối ưu năng lượng ởkhâu cảm biến bằng IMU có FIFO và ngắt thông minh. Cơ chếlấy mẫu PCNT
hiện tại tuy bảo đảm tần sốchính xác nhưng phụthuộc vào hoạt động liên tục của ngoại vi, gây khó khăn khi
đưa CPU vào chếđộLight Sleep — rào cản trực tiếp cho việc tiết kiệm điện sâu. Hướng khắc phục là chuyển
69


---

## Trang 84

CHƯƠNG 6. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN
sang các IMU thếhệmới (như Bosch BMI270, STMicroelectronics LSM6DSO hay TDK InvenSense ICM-
42688) tích hợp sẵn bộđệm FIFO phần cứng cùng ngắt theo ngưỡng đầy (FIFO watermark interrupt): cảm
biến tựtích lũy mẫu trong FIFO và chỉđánh thức vi điều khiển khi bộđệm đầy tới mức định trước, cho phép
CPU ngủgiữa các đợt thay vì phải thức liên tục ởtần số100 Hz. Sâu hơn nữa, các IMU này còn hỗtrợngắt
phát hiện chuyển động ởmức phần cứng (wake-on-motion, any-motion, significant-motion): thiết bịcó thể
chuyển vào chếđộDeep Sleep khi người dùng nằm hoặc ngồi yên trong thời gian dài và chỉ“bừng tỉnh” khi
phát sinh chuyển động đáng kể. Đặc thù người cao tuổi phần lớn thời gian ởtrạng thái tĩnh khiến cơ chếnày
có tiềm năng kéo dài tuổi thọpin lên nhiều lần.
Tối ưu năng lượng ởkhâu truyền thông di động. Module A7680C hiện sửdụng chuẩn LTE Cat-1 duy
trì kết nối vô tuyến (trạng thái RRC Connected) trong khoảng 10 giây sau mỗi lần publish bản tin — đây
là thành phần tiêu thụdòng điện chủyếu đối với một thiết bịchỉgửi tin thưa thớt. Hướng tối ưu là chuyển
sang các module LTE-M (Cat-M1) hoặc NB-IoT vốn được thiết kếchuyên cho IoT công suất thấp và hỗtrợ
tín hiệu RAI (Release Assistance Indication): ngay sau khi gửi xong gói tin cảnh báo, thiết bịbáo cho mạng
biết không còn dữliệu đểgiải phóng kết nối tức thì, loại bỏhoàn toàn khoảng “treo” 10 giây tốn điện của
chuẩn Cat-1.
Đa dạng hóa giao thức cho môi trường viện dưỡng lão cốđịnh. Trong môi trường triển khai cốđịnh
như viện dưỡng lão, có thểbổsung các chuẩn truyền thông mạng lưới (mesh) công suất thấp như Zigbee
hoặc Thread/Matter, kết hợp cùng một cổng kết nối (gateway) trung tâm. So với phương án mỗi thiết bị
mang một module di động riêng, giải pháp mesh cục bộgiảm đáng kểchi phí và điện năng tiêu thụtrên mỗi
nút mạng, đồng thời chuẩn Matter/Thread mởra khảnăng tương tác liền mạch với hạtầng nhà thông minh
và các thiết bịy tếkhác trong cùng cơ sở.
Nâng cấp truyền thông và bảo mật thiết bị. Đểkhắc phục rớt liên kết khi đo RSSI mạng 4G, tích hợp
giao thức CMUX (Multiplexer) đểtạo đa luồng trên một cổng UART là hướng đi cần thiết (dù thửnghiệm
ban đầu chưa khảthi). Vềbảo mật, hệthống cần áp dụng bảo mật MQTT cấp thiết bị(per-device) qua chứng
chỉmTLS hoặc ACL riêng biệt thay vì dùng chung thông tin xác thực. Cuối cùng, việc hoàn thiện cơ chếtự
phục hồi (STATE_ERROR recovery) khi gặp sựcốngắt mạng sâu sẽđảm bảo độsẵn sàng 24/7 của thiết bị.
Tích hợp cảm biến sinh hiệu và thiết kếPCB hướng sản phẩm. Đểtiến gần tới một sản phẩm thương
mại hoàn chỉnh, một hướng phát triển quan trọng là thiết kếbo mạch in (PCB) tối ưu, tích hợp thêm module
đo điện tâm đồ(ECG) hoặc nhịp tim quang học (PPG). Điều này cho phép hệthống phát hiện sớm các biến
cốtim mạch như nhồi máu cơ tim hay đột quỵ— vốn thường chính là nguyên nhân gốc rễdẫn tới té ngã ở
người cao tuổi. Khi nắm bắt được cảnguyên nhân (sựcốtim mạch) lẫn hậu quả(cú ngã), hệthống không
những cảnh báo kịp thời hơn mà còn cung cấp một bức tranh sức khỏe toàn diện, nâng tầm thiết bịtừmột
cảm biến phát hiện ngã đơn thuần thành một thiết bịđeo theo dõi sức khỏe đa năng.
70
