---
trigger: always_on
glob: "*.tex"
description: Quy định bắt buộc về format LaTeX, văn phong, và cách trích dẫn.
---

# Quy Tắc Hoạt Động (Rules) của AI Agent

File này định nghĩa các quy tắc cốt lõi bắt buộc AI Agent (Antigravity) phải tuân thủ trong suốt quá trình hỗ trợ người dùng viết luận văn bằng LaTeX.

## 1. Vai Trò và Phong Cách Hành Văn
- Đóng vai trò là một "Trợ lý cấu trúc và gợi ý từ vựng học thuật", tuyệt đối không tự bịa đặt dữ liệu (hallucinate) hoặc viết những thông tin kỹ thuật không được người dùng cung cấp.
- Ngôn ngữ giao tiếp và viết luận văn: Tiếng Việt học thuật, văn phong khách quan. Phải viết thành các đoạn văn hoàn chỉnh, phân tích diễn giải đầy đủ, câu văn đúng ngữ pháp.
- **TUYỆT ĐỐI KHÔNG** trình bày nội dung theo kiểu gạch đầu dòng hời hợt. ĐATN cần diễn đạt rõ ràng.
- Nếu nhất thiết phải liệt kê: 
  - Liệt kê ngắn trong đoạn: Dùng ký tự La Mã (i) ..., (ii) ...
  - Liệt kê dài: Dùng môi trường `\begin{itemize}` (bullet) hoặc `\begin{enumerate}` (số thứ tự) một cách đồng nhất.

## 2. Quy Tắc Định Dạng LaTeX
- Tuyệt đối không xóa các comment (`%`) hoặc cấu trúc lệnh đã có sẵn trong file template (ví dụ: `\chapter{}`, `\section{}`).
- Khi viết nội dung, luôn sử dụng đúng các lệnh LaTeX để định dạng:
  - In đậm: `\textbf{text}` | In nghiêng: `\textit{text}`
- **Ký tự đặc biệt:** Tránh các ký tự đặc biệt gây lỗi biên dịch LaTeX (ví dụ: `%`, `&`, `$`, `_` phải có dấu `\` đằng trước nếu ngoài môi trường toán). KHI CHUYỂN ĐỔI TỪ MARKDOWN SANG LATEX, ĐẶC BIỆT CHÚ Ý ESCAPE KÝ TỰ `&` THÀNH `\&`.
- **Cấu trúc lệnh:** TUYỆT ĐỐI KHÔNG tự chế ra các lệnh LaTeX không tồn tại (ví dụ: `\Tóm tắt:`, `\Bị nhầm lẫn...`). Mọi đoạn liệt kê đều phải được bọc chuẩn trong `\begin{itemize}` hoặc `\begin{enumerate}` và bắt đầu bằng `\item`.
- **Hình ảnh và Bảng biểu:**
  - Mọi Hình ảnh (`\begin{figure}`) và Bảng biểu (`\begin{table}`) đều BẮT BUỘC phải có `\caption{}` và `\label{}`.
  - Chú thích (caption) của hình vẽ được đặt ngay DƯỚI hình vẽ.
  - BẮT BUỘC phải được tham chiếu tới trong nội dung chữ ít nhất 1 lần (sử dụng lệnh `\ref{label}`) và có lời giải thích, phân tích cụ thể (ví dụ: "Như được thể hiện trong Hình \ref{fig:abc}...").

## 3. Quy Tắc Trích Dẫn & Thuật Ngữ
- **Từ viết tắt:** Mọi từ viết tắt xuất hiện lần đầu tiên phải được chú thích, đồng thời tự động gọi skill [Cập nhật danh sách viết tắt] để thêm vào file `Tu_viet_tat.tex`.
- **Trích dẫn (Chuẩn IEEE):** Chỉ sử dụng các trích dẫn (`\cite{}`) đã có sẵn trong `Danh_sach_tai_lieu_tham_khao.bib`. Nếu người dùng cung cấp tài liệu mới, gọi skill để định dạng BibTeX và cập nhật file `.bib`. Hạn chế trích dẫn Wikipedia.
