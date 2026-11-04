# DESIGN.md — HEARTICLES. News & Journal Editorial System
**Class 6 - Group 1 - Term 127 • Trường Đại học Ngoại ngữ - Đại học Quốc gia Hà Nội (ULIS - VNU)**  
*Language: Modern Minimalist Journalism Typography & Báo Nhân Dân (nhandan.vn) Architecture*

---

## 1. Hệ Thống Nghệ Thuật Chữ Tối Giản (Minimalism Typography System)
Nhằm mang lại trải nghiệm đọc hiện đại, tinh gọn và loại bỏ hoàn toàn sự rườm rà của các phông chữ có chân cổ điển (Bodoni, Playfair, Times), tòa soạn áp dụng cặp phông chữ tối giản chuẩn mực quốc tế:

1. **Tiêu đề chính & Tiêu điểm (Display Headlines & Focal Titles):**
   - **Phông chữ:** `Plus Jakarta Sans` (`font-weight: 700 - 900`).
   - **Đặc trưng:** Nét chữ hình học hiện đại (Geometric Sans), không chân, đường nét đanh thép, độ mở (aperture) khoáng đạt.
   - **Khoảng cách chữ (Tracking):** Tinh chỉnh sát nét `-0.025em` đến `-0.035em`, mang lại sự khúc chiết, sang trọng và thu hút thị giác mạnh mẽ theo phong cách tạp chí thiết kế đương đại (*Kinfolk, Monocle, The Verge*).

2. **Nội dung bài viết & Đoạn trích (Body Reading & Excerpts):**
   - **Phông chữ:** `Inter` (`font-weight: 400 - 500`).
   - **Đặc trưng:** Chuẩn mực toàn cầu về độ dễ đọc trên màn hình số (Swiss Neo-Grotesque). Các dấu tiếng Việt hiển thị tròn trịa, tinh tế, khoảng cách dòng `line-height: 1.7 - 1.75` triệt tiêu mỏi mắt khi đọc các bài phóng sự dài (Long-form).

3. **Giao diện điều hướng, Nhãn & Metadata (UI, Nav, Badges & Bylines):**
   - **Phông chữ:** `Inter` (`font-weight: 600 - 700`).
   - **Đặc trưng:** Nhãn in hoa tinh giản với khoảng cách dãn nhẹ `0.04em`, hiển thị rõ ràng ngày giờ, số phút đọc và tên tác giả.

4. **Biểu trưng Tòa soạn (Masthead Logo `HEARTICLES.`):**
   - Định dạng Sans-Serif Minimalist Bold (`font-family: 'Plus Jakarta Sans'`, `font-weight: 900`, `letter-spacing: -0.04em`, `font-style: normal`), kết hợp dấu chấm đỏ rượu vang đặc trưng.

---

## 2. Kiến Trúc Bố Cục Báo Nhân Dân (Chuẩn Mực - Hiện Đại - Phi Đối Xứng)
- **Cụm Tiêu Điểm 3 Cột (50% | 26% | 24%):** Bài đinh Quốc hội (Báo Nhân Dân NDO) kèm 2 tin nóng gạch đầu dòng đỏ cờ + 2 bài tiêu điểm nhánh + Dòng thời sự 24/7 (Timeline Live Feed).
- **Megastory / E-Magazine Toàn Khổ:** Không gian báo chí thị giác đa phương tiện với trích dẫn Didone tối giản và ảnh phóng sự khổ lớn.
- **Khối Xã Hội & Dân Sinh:** 1 Bài lớn ngang + 3 tin vắn xếp lớp (60% : 40%).
- **Báo Ảnh Phóng Sự:** Mosaic ảnh ghép phi đối xứng giàu tính nhân văn.
- **Bình Luận - Xã Luận & Thăm Dò:** Chuyên luận chính luận của Cố vấn ULIS - VNU và khung bình chọn độc giả.
- **Truyền Hình Đa Phương Tiện:** 5 video phóng sự thực tế chuẩn truyền hình.

---

## 3. Bảng Màu Tương Phản Cao Chuẩn WCAG AAA
- **Tiêu đề chính (Headlines):** `#151011` (Mực đen Obsidian sâu thẳm, tương phản 18.7:1).
- **Nội dung bài viết (Body text):** `#221B1C` (Mực sẫm, tương phản 15.6:1).
- **Thông tin phụ (Metadata):** `#4C413E` (Đá than ấm, tương phản 8.4:1).
- **Kicker & Nhãn chuyên mục:** `#7D1728` (Đỏ Carmine đậm in hoa, tương phản 8.1:1).
- **Màu đỏ cờ thương hiệu:** `#54111E` (Đỏ rượu vang quyền quý, tương phản 12.2:1).
- **Nền giấy báo (Canvas Paper):** `#FAF7F4` (Giấy ngà tinh khôi, sáng mịn).

---

## 4. Kiến Trúc 7 Trang Độc Lập
- `index.html` (Home)
- `trending.html` (Trending)
- `society.html` (Society)
- `human-stories.html` (Human Stories)
- `mind-soul.html` (Mind & Soul)
- `in-depth.html` (In-depth)
- `about.html` (About Us)
