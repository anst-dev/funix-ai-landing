# Landing page — Bán khoá AI FUNiX (phễu về Zalo)

Một file duy nhất: `index.html` (Tailwind CDN + font Be Vietnam Pro). Thiết kế được sinh bởi **Google Stitch** từ prompt trong `stitch-prompt.md`, sau đó `transform.py` gắn dữ liệu 22 khóa thật + cơ chế phễu vào.

## Trạng thái trước khi đưa lên mạng

- ✅ Số Zalo: đã gắn vào cả 29 nút CTA — số thật nằm trong `CONFIG` của `index.html` (không ghi ở đây vì repo public)
- ✅ Mã QR: **QR thật** trỏ về link Zalo trong `CONFIG` (file `assets/qr-zalo.png`, tạo lại bằng: `python -c "import qrcode; qrcode.make('https://zalo.me/<SO_ZALO>').save('assets/qr-zalo.png')"`)
- ✅ Ảnh mentor: ảnh thật (`assets/mentor.png`)

## ⚙️ Cấu hình trong `index.html`

```js
const CONFIG = {
  zaloPhone: "<SO_ZALO>",   // số Zalo của bạn — số thật nằm ở đây, không commit vào README
  refParams: "utm_source=Gioithieu_NVCTV_FUNiX&mid=anhnst", // mã giới thiệu
};
```

## Cấu trúc

| File | Vai trò |
|---|---|
| `index.html` | Trang web hoàn chỉnh (duy nhất cần deploy) |
| `assets/` | Logo, minh họa hero, ảnh mentor, QR Zalo |
| `stitch-prompt.md` | Nghiên cứu đối thủ + prompt Stitch gốc |
| `stitch-export/` | Bản export gốc từ Stitch (code + DESIGN.md + screenshot) |
| `transform.py` | Script gắn dữ liệu khóa thật vào thiết kế Stitch |
| `README.md` | File này |

## Sửa danh sách khóa

Dữ liệu nằm trong mảng `COURSES` trong `index.html` (mã môn, tên, đối tượng, số buổi, mô tả, link webpage — đã gắn tự động `refParams`). Sheet gốc: https://docs.google.com/spreadsheets/d/1cVWgN99jqqu8wFduaGtegEE9kBg-VbH4cd2keZP2n50/edit?gid=0#gid=0

Hiện gồm 22 khóa **Đã golive**. Khoá mới golive → thêm 1 object vào `COURSES`.

## Xem thử trên máy

```bash
cd funix-landing
python -m http.server 8642
# mở http://127.0.0.1:8642
```

## Đưa lên mạng

- **Netlify Drop** (nhanh nhất): https://app.netlify.com/drop → kéo thả thư mục `funix-landing` (hoặc zip chỉ chứa `index.html` + `assets/`) → nhận link `*.netlify.app`.
- **GitHub Pages / Vercel / Cloudflare Pages**: đẩy repo, bật Pages.

Trang đã có meta OG (tiêu đề + mô tả đẹp khi dán link lên Facebook).

## Dùng trong phễu

Đăng bài/bình luận MXH → bio hoặc comment dẫn về link này → khách lọc khóa theo nghề → bấm CTA mở Zalo chat với bạn → chốt sale.
