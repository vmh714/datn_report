### Tóm tắt:
Các phương pháp phát hiện ngã hiện nay dành cho người cao tuổi thường gặp hạn chế do tỷ lệ báo động giả cao hoặc bỏ sót các tai nạn thực tế. Để giải quyết vấn đề này, nghiên cứu đề xuất giải pháp kiểm tra kép kết hợp cảm biến quán tính tích hợp định vị (IMU-L) đeo trên người và camera RGB gắn trên robot di động. Thuật toán LSTM được dùng để phát hiện nghi ngờ ngã từ dữ liệu chuyển động, sau đó robot di chuyển đến tọa độ định vị và sử dụng mạng DenseNet-121 để xác nhận lại qua hình ảnh. Thử nghiệm thực tế chứng minh phương pháp này đạt độ chính xác tối ưu 100%, loại bỏ hoàn toàn các trường hợp báo động giả.

### BibTeX:
```bibtex
@article{lee2021deep,
  author={Lee, Deok-Won and Jun, Kooksung and Naheem, Khawar and Kim, Mun Sang},
  journal={IEEE Access},
  title={Deep Neural Network-Based Double-Check Method for Fall Detection Using IMU-L Sensor and RGB Camera Data},
  year={2021},
  volume={9},
  pages={48064-48079},
  doi={10.1109/ACCESS.2021.3065105}
}
```