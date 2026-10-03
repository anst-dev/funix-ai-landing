# Nghiên cứu thiết kế + Prompt cho Stitch

> Mục tiêu: nâng cấp `funix-landing/index.html` lên mức **chuyên nghiệp hơn đối thủ** đang bán khóa AI trên mạng, giữ nguyên cơ chế phễu (mọi CTA → Zalo).

---

## 1. Đối thủ học được gì (RedPola + chuẩn ngành)

Cấu trúc trang đối thủ bán khóa AI trực tiếp (RedPola) và best practice 2025 (Unbounce, Framer, Ladipage):

| Yếu tố | Đối thủ làm | Trang mình hiện tại | Gap |
|---|---|---|---|
| Hero "5 giây" | Lời hứa rõ + hình minh họa | Có headline + stats, **chưa có hình** | ⚠️ Thiếu visual |
| Ảnh thẻ khóa học | Mỗi khóa 1 ảnh banner | Chỉ text | ❌ Thiếu |
| Logo "đơn vị đã đào tạo" | Wall logo BIDV, Viettel, FPT... | Không có | ❌ Thiếu |
| Credentials giảng viên | Ảnh + chức danh, bằng cấp | Không có | ❌ Thiếu |
| Testimonial học viên | Có | Không có | ❌ Thiếu |
| CTA từng khóa | "Đăng ký & Lịch học" mỗi card | Có "Hỏi về khóa này" | ✅ Đủ |
| Bộ lọc/phân khúc | Không có | Lọc theo 7 nhóm nghề | ✅ Mình mạnh hơn |
| Quy trình bắt đầu | Có | Có (3 bước) | ✅ Đủ |
| FAQ | Có | Có | ✅ Đủ |
| Urgency (lịch khai giảng, ưu đãi) | Có | Không | ⚠️ Thiếu |

**Kết luận:** nội dung + phân loại nghề của mình đã tốt hơn đối thủ; cần bổ sung **lớp niềm tin và hình ảnh** (visual, social proof, mentor, urgency) và làm hero "đắt" hơn.

## 2. Hướng nâng cấp (đưa vào prompt Stitch)

1. Hero thêm **hình minh họa/mockup** + giữ headline hiện có (đã pass 5-second test).
2. Thêm **trust bar**: số liệu + logo (FUNiX, đối tác) ngay dưới hero.
3. Thêm **3 testimonial học viên** (kèm ghi chú cho user thay bằng feedback thật).
4. Thêm **section Mentor** (ảnh + chức danh + thành tích) — khớp phễu vì khách đến từ trang cá nhân.
5. Card khóa có **ảnh thumbnail minh họa theo chủ đề**.
6. Thêm **urgency**: dòng "Lịch khai giảng gần nhất · Ưu đãi nhóm" ở CTA band.
7. CTA band có **ô QR Zalo** (chụp bằng điện thoại là nhắn được ngay).
8. Hệ màu giữ navy gradient + Zalo blue #0068FF làm màu hành động duy nhất.

---

## 3. PROMPT CHÍNH cho Stitch (copy nguyên khối vào Stitch)

Stitch: https://stitch.withgoogle.com (hoặc qua MCP sau khi restart session). Chọn mode **Desktop** trước, dán prompt dưới đây:

```text
Design a high-converting marketing landing page (desktop, 1440px wide) for "Học AI cùng Mentor" — a Vietnamese edtech landing page that sells 22 practical AI courses under the FUNiX program. Traffic arrives from Facebook/TikTok posts, so the page must feel credible within 5 seconds. The single conversion goal is to move visitors into a free Zalo chat consultation with a mentor — there is NO checkout and NO prices on the page (pricing is shared in Zalo), so every section should end with or point to a Zalo CTA.

STYLE DIRECTION
- Modern, premium edtech feel: trustworthy but energetic.
- Palette: deep navy gradient hero (#0B1224 → #12224E) with a soft cyan glow, white cards on a very light gray-blue background (#F6F8FC), primary action color Zalo blue (#0068FF) used ONLY for CTA buttons, secondary accents electric blue #2563EB and cyan #06B6D4.
- Typography: Be Vietnam Pro (fallback Inter) — extra-bold headlines, 16px body, generous line height for Vietnamese diacritics.
- Cards with 16px rounded corners, soft diffuse shadows, 1px light borders; generous whitespace; clean visual rhythm; flat vector illustration style for people (no stock photos of random offices).

SECTIONS, TOP TO BOTTOM
1. Sticky translucent header: logo mark (graduation cap in a blue gradient rounded square) + wordmark "Học AI cùng Mentor" with small subtitle "Khoá thực chiến FUNiX"; right side: filled Zalo-blue pill button "💬 Nhận tư vấn Zalo".
2. Hero, two columns: LEFT — a small pill badge "🔥 Chương trình chính quy FUNiX · Học online 60'/buổi"; huge extra-bold H1 "Biến AI thành vũ khí của riêng bạn — chỉ sau vài buổi học" with the words "vũ khí" in a blue→cyan gradient; a one-sentence subheadline naming the audiences (sinh viên, dân văn phòng, sales, marketing, giáo viên, lập trình viên); a stats row of 3 numbers: "20+ khoá AI thực chiến", "7 nhóm nghề phù hợp", "60' mỗi buổi, học tối nay dùng được ngay"; two buttons: filled Zalo blue "💬 Nhắn Zalo — tư vấn miễn phí" + ghost white-outline "Xem danh sách khoá ↓". RIGHT — a flat-vector illustration of a young Vietnamese student/professional at a laptop with floating AI chat bubbles and sparkles, in the navy/blue/cyan palette.
3. Trust bar directly under the hero (white strip): "Đồng hành cùng học viên FUNiX trên toàn quốc" plus 5 grayscale placeholder logos (FUNiX, VNU-HCM, đối tác doanh nghiệp…) and a stat "3.000+ học viên".
4. Course catalog section titled "Chọn khoá theo nghề của bạn" with a subtitle "Nhắn Zalo để nhận lộ trình học gợi ý + lịch khai giảng + học phí ưu đãi." Below: a horizontally scrollable row of pill filter chips: "Tất cả khoá", "🎓 Sinh viên", "💼 Nhân viên VP", "📈 Sales", "📣 Marketing", "🏫 Giáo viên", "💻 IT", "🙋 Ai cũng học được" (active chip = dark navy filled). Then a 3-column grid of 6 course cards, each card: a small gray code badge (e.g. "SAR121x") + a colored audience tag, a bold 2-line title, a 2-line benefit description in muted gray, a meta row "⏱ 4 buổi × 60' · 🖥 Online", and two buttons: filled Zalo blue "💬 Hỏi về khoá này" and outlined ghost "Chi tiết →". Give each card a small flat-illustration thumbnail matching its topic (notes/graduation/resume/design/video/chatbot/automation). Vary the audience tag colors: green for Sinh viên, indigo for Nhân viên VP, orange for Sales, pink for Marketing, yellow for Giáo viên, violet for IT.
5. "Vì sao học ở đây" — 4 benefit cards with rounded icon tiles: 🎯 "Theo đúng nghề của bạn", ⚡ "Thực chiến, không lý thuyết", 👨‍🏫 "Mentor đồng hành", 📜 "Chương trình chuẩn FUNiX", each with one supporting sentence.
6. Testimonials "Học viên nói gì" — 3 white quote cards, each with a 5-star row, a 2-sentence Vietnamese quote, an avatar circle, name and role (e.g. "Minh Anh — Sinh viên UEH", "Tuấn Kiệt — Nhân viên ngân hàng", "Thu Hà — Giáo viên THPT").
7. Mentor section (navy card, two columns): LEFT — portrait placeholder of "Mentor Tuấn" with credential chips "Mentor chính thức FUNiX", "Chuyên GenAI & tự động hoá", "100+ buổi hướng dẫn trực tiếp". RIGHT — a short first-person Vietnamese bio, then a Zalo CTA button "💬 Nhắn trực tiếp cho mentor".
8. "Bắt đầu thế nào — chỉ 3 bước": three numbered cards "01 Nhắn Zalo cho mentor → 02 Nhận lộ trình phù hợp → 03 Học & dùng được ngay", each with one supporting sentence; big ghost step numbers as background decoration.
9. Final CTA band: full-width navy gradient rounded container "Không biết chọn khoá nào? 💬" + subtitle "Nhắn 1 dòng: 'mình là [nghề], muốn [mục tiêu]' — mentor tư vấn miễn phí trong ngày." + big Zalo button, and to its right a small white card containing a QR-code placeholder labeled "Quét QR để nhắn Zalo ngay" with a tiny urgency line "Ưu đãi nhóm & lịch khai giảng gần nhất — hỏi mentor hôm nay".
10. FAQ accordion "Câu hỏi hay gặp" with 4 items (không biết công nghệ có học nổi không, học lúc nào, học phí bao nhiêu, có chứng chỉ không).
11. Footer (navy): brand + one-line description on the left; contact block "Zalo: <số> · Giờ tư vấn 8h–22h mỗi ngày"; small disclaimer "Khoá học thuộc chương trình FUNiX".

All visible copy is in Vietnamese exactly as written above. The Zalo button must be visually the single dominant action on every viewport. Keep the layout airy and scannable — this page is viewed mostly on phones via social media.
```

Sau khi generate xong bản Desktop → đổi thiết bị sang **Phone (390px)** và generate lại với cùng prompt để ra bản mobile.

## 4. Prompt bổ trợ (dùng khi cần tinh chỉnh trong Stitch)

**Làm đậm CTA hơn:**
```text
Make the Zalo CTA more dominant: increase button size, add a subtle glow shadow (#0068FF at 35% opacity), and ensure it appears both in the sticky header and as a floating action on mobile.
```

**Đổi phong cách hình:**
```text
Switch illustrations to a slightly more premium 3D-clay style, keeping the navy/blue/cyan palette and Vietnamese characters.
```

**Thêm section lịch khai giảng (urgency):**
```text
Add a compact "Lịch khai giảng gần nhất" strip above the FAQ: 3 rows, each with course code, start date pill, seats-left badge ("Còn 5 chỗ"), and a small Zalo text-link "Giữ chỗ qua Zalo".
```

## 5. Sau khi chọn được design trên Stitch

Gửi lại cho tôi (screenshot hoặc để MCP Stitch xuất HTML) — tôi sẽ:
1. Đưa thiết kế vào `index.html` thật (giữ nguyên dữ liệu 22 khóa + mã giới thiệu + cơ chế lọc).
2. Thay QR Zalo thật + số Zalo thật.
3. Commit một lần duy nhất.
