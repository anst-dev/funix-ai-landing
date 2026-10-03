# -*- coding: utf-8 -*-
"""Chuyển thiết kế Stitch (stitch-export/code.html) thành index.html sản xuất:
- Tải ảnh ngoài về assets/ (CDN Google có thể hết hạn)
- Thay 6 khóa mẫu bằng 22 khóa thật (render từ COURSES trong bản cũ)
- Nối lại: bộ lọc, link Zalo (CONFIG), mã giới thiệu (refParams), meta SEO/OG
Chạy: python transform.py  (chạy lại được, idempotent với assets đã tải)
"""
import re, urllib.request, os

stitch = open('stitch-export/code.html', encoding='utf-8').read()
old = open('index.html', encoding='utf-8').read()

# 1) Lấy CONFIG + COURSES từ bản cũ
zalo_phone = re.search(r'zaloPhone:\s*"([^"]+)"', old).group(1)
ref_params = re.search(r'refParams:\s*"([^"]+)"', old).group(1)
courses_js = re.search(r'const COURSES = \[.*?\n\];', old, re.S).group(0)

# 2) Tải ảnh ngoài về assets/
os.makedirs('assets', exist_ok=True)
prefixes = {
    'https://lh3.googleusercontent.com/aida-public/AB6AXuAwFqIkh7ZwVIwXwmgIWuMZd-': 'hero.png',
    'https://lh3.googleusercontent.com/aida-public/AB6AXuBF0-hrnqkR1DVaYnwzYCF4Vz': 'qr-zalo.png',
    'https://lh3.googleusercontent.com/aida-public/AB6AXuBO3BfpT38OF4ocYU4lxvOuy1': 'mentor.png',
    'https://lh3.googleusercontent.com/aida/AEtjO1UjmfYRF_tlP7Y8WWSjsUKz0jyoOWeqNu2Du': 'logo.png',
}
for prefix, name in prefixes.items():
    m = re.search(re.escape(prefix) + r'[A-Za-z0-9_\-]+', stitch)
    assert m, 'không tìm thấy URL ' + prefix
    url = m.group(0)
    dest = 'assets/' + name
    if not os.path.exists(dest):
        urllib.request.urlretrieve(url, dest)
    stitch = stitch.replace(url, 'assets/' + name)
    print('da local hoa:', name, os.path.getsize(dest), 'bytes')

def replace_div_block(html, start_marker, replacement):
    i = html.find(start_marker)
    assert i >= 0, start_marker[:60]
    j = html.find('<div', i)
    depth = 0
    token = re.compile(r'<div\b|</div>')
    for m in token.finditer(html, j):
        depth += 1 if m.group(0).startswith('<div') else -1
        if depth == 0:
            return html[:j] + replacement + html[m.end():]
    raise RuntimeError('không cân bằng thẻ div: ' + start_marker[:60])

# 3) Thay chips và lưới khóa bằng container do JS render
stitch = replace_div_block(
    stitch,
    '<div class="flex items-center gap-2 overflow-x-auto pb-4 mb-8 custom-scrollbar">',
    '<div id="courseFilters" class="flex items-center gap-2 overflow-x-auto pb-4 mb-8 custom-scrollbar"></div>')

grid_new = ('<div id="courseGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"></div>\n'
            '<p id="emptyMsg" class="hidden text-center text-on-surface-variant py-10">Khong co khoa nao trong nhom nay.</p>')
stitch = replace_div_block(
    stitch,
    '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">',
    grid_new)

# 4) Meta SEO/OG + favicon sau <title>
title_end = stitch.find('</title>') + len('</title>')
meta = ('\n<meta name="description" content="Hơn 20 khoá AI thực chiến FUNiX cho sinh viên, dân văn phòng, sales, marketing, giáo viên, IT. Nhắn Zalo nhận tư vấn lộ trình miễn phí."/>'
        '\n<meta property="og:title" content="Khoá AI thực chiến FUNiX — Học cùng Mentor"/>'
        '\n<meta property="og:description" content="Chọn khoá theo nghề của bạn, nhắn Zalo nhận lộ trình + lịch khai giảng + học phí ưu đãi."/>'
        '\n<meta property="og:type" content="website"/>'
        '\n<meta property="og:locale" content="vi_VN"/>'
        '\n<link rel="icon" href="assets/logo.png"/>')
stitch = stitch[:title_end] + meta + stitch[title_end:]

# 5) App script: CONFIG + COURSES + render + bộ lọc (chèn trước </body>)
app_js = """
<script>
/* ============================================================
   ⚙️ CẤU HÌNH — SỬA CÁC DÒNG DƯỚI ĐÂY
   zaloPhone : số Zalo thật của bạn (đang là placeholder!)
   refParams : mã giới thiệu FUNiX gắn vào mọi link khóa học
   LƯU Ý: ảnh mentor và ảnh QR trong trang đang là ảnh AI tạo
   mẫu — thay bằng ảnh thật (assets/mentor.png, assets/qr-zalo.png)
   trước khi chạy quảng cáo.
   ============================================================ */
const CONFIG = {
  zaloPhone: "__ZALO__",
  refParams: "__REF__",
};

const zaloLink = "https://zalo.me/" + CONFIG.zaloPhone;
const refUrl = (u) => u.split("?")[0] + "?" + CONFIG.refParams;

/* Gắn link Zalo cho mọi nút trong thiết kế */
document.querySelectorAll('a[href="https://zalo.me"]').forEach(a => { a.href = zaloLink; });
document.querySelectorAll(".js-phone").forEach(el => { el.textContent = CONFIG.zaloPhone; });

__COURSES__

const TAG_COLORS = {
  "sinhvien":  "bg-emerald-50 text-emerald-700 border-emerald-200",
  "vanphong":  "bg-indigo-50 text-indigo-700 border-indigo-200",
  "sales":     "bg-orange-50 text-orange-700 border-orange-200",
  "marketing": "bg-pink-50 text-pink-700 border-pink-200",
  "giao-vien": "bg-amber-50 text-amber-700 border-amber-200",
  "it":        "bg-violet-50 text-violet-700 border-violet-200",
  "moi-nguoi": "bg-sky-50 text-sky-700 border-sky-200",
};

const FILTERS = [
  {id:"all",       label:"Tất cả khoá"},
  {id:"sinhvien",  label:"🎓 Sinh viên"},
  {id:"vanphong",  label:"💼 Nhân viên VP"},
  {id:"sales",     label:"📈 Sales"},
  {id:"marketing", label:"📣 Marketing"},
  {id:"giao-vien", label:"🏫 Giáo viên"},
  {id:"it",        label:"💻 IT"},
  {id:"moi-nguoi", label:"🙋 Ai cũng học được"},
];

/* Render chips bộ lọc */
const CHIP_ACTIVE   = "bg-[#0B1224] text-white px-5 py-2 rounded-full font-label-md text-label-md font-bold shadow-sm whitespace-nowrap";
const CHIP_INACTIVE = "bg-surface-container-lowest text-on-surface-variant hover:text-primary hover:border-primary/40 border border-outline-variant/40 px-5 py-2 rounded-full font-label-md text-label-md font-semibold whitespace-nowrap transition-colors";
const filtersEl = document.getElementById("courseFilters");
function renderChips(activeId){
  filtersEl.innerHTML = FILTERS.map(f =>
    `<button class="${f.id===activeId?CHIP_ACTIVE:CHIP_INACTIVE}" data-f="${f.id}">${f.label}</button>`).join("");
}
renderChips("all");

/* Render khóa học theo đúng markup thiết kế Stitch */
function cardHTML(c){
  const tag = TAG_COLORS[c.aud] || TAG_COLORS["moi-nguoi"];
  return `<div class="bg-surface-container-lowest border border-outline-variant/40 rounded-2xl p-6 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between" data-aud="${c.aud}">
    <div>
      <div class="flex items-center justify-between gap-2 mb-4">
        <span class="px-3 py-1 rounded-full text-label-caps font-label-caps font-bold border ${tag}">${c.audLabel}</span>
        <span class="text-label-caps font-label-caps text-outline font-mono">Mã: ${c.code}</span>
      </div>
      <h3 class="text-headline-sm font-headline-sm text-on-surface font-bold mb-2 leading-snug">${c.name}</h3>
      <p class="text-body-sm font-body-sm text-on-surface-variant mb-6 leading-relaxed">${c.desc}</p>
    </div>
    <div>
      <div class="flex items-center gap-4 text-label-md font-label-md text-on-surface-variant mb-5 pt-3 border-t border-outline-variant/20">
        <span class="flex items-center gap-1.5"><span class="material-symbols-outlined text-[16px] text-primary">schedule</span> ${c.buoi} buổi × 60'</span>
        <span class="flex items-center gap-1.5"><span class="material-symbols-outlined text-[16px] text-primary">videocam</span> Online</span>
      </div>
      <div class="flex items-center gap-3">
        <a class="flex-1 text-center bg-primary-container hover:bg-[#0055D6] text-white py-2.5 px-4 rounded-xl text-label-md font-label-md font-bold transition-all shadow-sm" href="${zaloLink}" target="_blank" rel="noopener">💬 Hỏi về khoá này</a>
        <a class="px-3 py-2.5 rounded-xl border border-outline-variant/60 text-on-surface hover:text-primary text-label-md font-label-md font-medium transition-colors" href="${refUrl(c.url)}" target="_blank" rel="noopener">Chi tiết →</a>
      </div>
    </div>
  </div>`;
}
const grid = document.getElementById("courseGrid");
grid.innerHTML = COURSES.map(cardHTML).join("");

/* Bộ lọc */
filtersEl.addEventListener("click", e => {
  const btn = e.target.closest("button[data-f]"); if(!btn) return;
  renderChips(btn.dataset.f);
  let shown = 0;
  grid.querySelectorAll("[data-aud]").forEach(card => {
    const show = btn.dataset.f === "all" || card.dataset.aud === btn.dataset.f;
    card.style.display = show ? "" : "none";
    if (show) shown++;
  });
  document.getElementById("emptyMsg").classList.toggle("hidden", shown > 0);
});
</script>"""
app_js = app_js.replace('__ZALO__', zalo_phone).replace('__REF__', ref_params).replace('__COURSES__', courses_js)
stitch = stitch.replace('</body>', app_js + '\n</body>')

open('index.html', 'w', encoding='utf-8').write(stitch)
print('index.html moi:', len(stitch), 'bytes')
