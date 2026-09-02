#!/usr/bin/env python3
"""Сборка сайта Lizhong Steel Structure (версия для Узбекистана).

Статические страницы собираются из общих шапки/подвала и словаря PAGES.
CSS дизайн-системы копируется из design-system/ в docs/assets/css/ —
design-system остаётся единственным источником правды по токенам.

Запуск:  python3 build.py   →  результат в docs/ (папка для GitHub Pages)
"""
import shutil
import time
from pathlib import Path

V = str(int(time.time()))

ROOT = Path(__file__).parent
DS = ROOT / "design-system"
SITE = ROOT / "docs"

# Контакты клиента. Пока пустые: компания подключает корпоративный номер.
# Когда контакты появятся — вписать сюда и пересобрать, все блоки включатся сами.
EMAIL = ""
PHONE = ""
WA = ""  # например https://api.whatsapp.com/send?phone=...

# Купленный домен. DNS настроен в Billur 2 сентября 2026 (4 A-записи апекса
# на IP GitHub Pages + CNAME www). CNAME-файл в docs/ задаёт custom domain
# в GitHub Pages автоматически.
DOMAIN = "l-steel.uz"

CHEVRON = ('<svg class="chevron" width="20" height="12" viewBox="0 0 20 12" fill="none" '
           'stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M2 2l8 8 8-8"/></svg>')


def heading(label: str) -> str:
    return f'<div class="section-heading"><h2 class="label">{label}</h2>{CHEVRON}</div>'


def card(img: str, title: str, body: str, square: bool = True) -> str:
    sq = " square" if square else ""
    return (f'<article class="card"><div class="card-media{sq}">'
            f'<img src="assets/img/{img}" alt="{title}" loading="lazy"></div>'
            f'<h3 class="card-title">{title}</h3><p class="card-body">{body}</p></article>')


NAV_ITEMS = [("index.html", "Главная"), ("about.html", "О компании"),
             ("products.html", "Продукция"), ("contact.html", "Контакты")]

# --- условные блоки, зависящие от наличия контактов -----------------------

HERO_WA = (f'<a class="btn btn-secondary" style="border-color:#fff;color:#fff" '
           f'href="{WA}" rel="noopener">WhatsApp</a>') if WA else ""

if EMAIL:
    BAND_BUTTONS = (f'<a class="btn btn-accent" href="mailto:{EMAIL}">{EMAIL}</a>'
                    f'<a class="btn btn-secondary" href="{WA}" rel="noopener">WhatsApp: {PHONE}</a>')
else:
    BAND_BUTTONS = '<a class="btn btn-accent" href="contact.html">Получить расчёт</a>'

if EMAIL:
    FOOTER_CONTACTS = f"""<div class="contact-lines">
          <a href="mailto:{EMAIL}">{EMAIL}</a>
          <a href="{WA}" rel="noopener">WhatsApp: {PHONE}</a>
          <a href="tel:{PHONE}">Тел.: {PHONE}</a>
        </div>"""
else:
    FOOTER_CONTACTS = ('<p style="color:var(--color-neutral-500)">Телефон и email '
                       'появятся здесь после подключения корпоративного номера.</p>')

TOOLBAR_WA = (f"""<a class="toolbar-item" href="{WA}" rel="noopener">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2 4.1 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.7c.1 1 .4 2 .7 2.9a2 2 0 0 1-.4 2.1L8 10a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.9.6 2.9.7A2 2 0 0 1 22 16.9Z"/></svg>
    WhatsApp</a>""") if WA else ""

TOOLBAR_EMAIL = (f"""<a class="toolbar-item" href="mailto:{EMAIL}">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>
    Email</a>""") if EMAIL else ""

if EMAIL:
    CONTACT_LINES = f"""<div class="contact-lines">
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <a href="{WA}" rel="noopener">WhatsApp: {PHONE}</a>
        <a href="tel:{PHONE}">Тел.: {PHONE}</a>
      </div>"""
    FORM_TAIL = f"""<button class="btn btn-accent btn-block" type="submit">Отправить запрос</button>
        <p style="font:var(--text-caption);color:var(--color-text-muted)">Кнопка откроет письмо в вашей почтовой программе — данные попадают напрямую на {EMAIL}.</p>
      </form>
      <script>
      function sendInquiry(f) {{
        var body = 'Компания: ' + f.company.value + '\\nКонтакт: ' + f.contact.value + '\\n\\n' + f.message.value;
        location.href = 'mailto:{EMAIL}?subject=' + encodeURIComponent('Запрос с сайта Lizhong') + '&body=' + encodeURIComponent(body);
        return false;
      }}
      </script>"""
else:
    CONTACT_LINES = ('<p style="color:var(--color-text-muted)">Корпоративный телефон и email '
                     'сейчас подключаются — контакты появятся здесь в ближайшее время.</p>')
    FORM_TAIL = """<button class="btn btn-accent btn-block" type="submit" disabled>Отправить запрос</button>
        <p style="font:var(--text-caption);color:var(--color-text-muted)">Отправка заработает после подключения корпоративной почты.</p>
      </form>"""


def page_shell(slug: str, title: str, description: str, body: str, extra_body_class: str = "") -> str:
    active = ' class="active"'
    links = "".join(
        f'<li><a href="{href}"{active if href == slug else ""}>{label}</a></li>'
        for href, label in NAV_ITEMS)
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="stylesheet" href="assets/css/styles.css?v={V}">
<link rel="stylesheet" href="assets/site.css?v={V}">
</head>
<body class="{extra_body_class}">
<header class="site-header">
  <nav class="nav container">
    <a class="nav-logo" href="index.html"><img src="assets/img/logo-alt.png" alt="Lizhong Steel Structure"></a>
    <ul class="nav-links">{links}</ul>
    <a class="btn btn-primary nav-cta" href="contact.html">Получить расчёт</a>
    <button class="nav-toggle" aria-label="Меню" onclick="this.closest('.nav').classList.toggle('menu-open')">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
    </button>
  </nav>
</header>
{body}
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-logo"><img src="assets/img/logo.png" alt="Lizhong Steel Structure"></div>
        <p>Lizhong Steel Structure (Shandong) Co., Ltd. — проектирование, производство и монтаж стальных конструкций. Цзинань, провинция Шаньдун, Китай. Поставки в Узбекистан и страны Центральной Азии.</p>
      </div>
      <div>
        <h3>Контакты</h3>
        {FOOTER_CONTACTS}
      </div>
      <div>
        <h3>Продукция</h3>
        <ul class="footer-list">
          <li>Обычные стальные здания</li>
          <li>Общественные стальные здания</li>
          <li>Стальные компоненты</li>
          <li>Сталь для стеклянных фасадов</li>
          <li>Горячекатаный прокат</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">© Lizhong Steel Structure (Shandong) Co., Ltd.
      <span style="display:block;margin-top:var(--space-2)">Сайт и продвижение — <a href="https://sales-hub.uz/?utm_source={DOMAIN}&utm_medium=referral&utm_campaign=footer" rel="noopener">Sales HUB</a></span>
    </div>
  </div>
</footer>
</body>
</html>
"""


# ---------------------------------------------------------------- index
INDEX_BODY = f"""
<section class="hero">
  <img class="hero-bg" src="assets/img/hero.jpg" alt="">
  <div class="hero-scrim"></div>
  <div class="container"><div class="hero-inner">
    <h1>Стальные конструкции для проектов в Узбекистане</h1>
    <p>Проектирование, производство и монтаж полного цикла. Любые виды, спецификации и материалы, изготовление под заказ, быстрая поставка и сервис.</p>
    <div class="hero-actions">
      <a class="btn btn-accent" href="contact.html">Получить расчёт</a>
      {HERO_WA}
    </div>
  </div></div>
</section>
<div class="category-row">
  <a class="btn btn-primary" href="products.html">Обычные стальные здания</a>
  <a class="btn btn-primary" href="products.html">Общественные стальные здания</a>
  <a class="btn btn-primary" href="products.html#components">Стальные компоненты</a>
  <a class="btn btn-primary" href="products.html#components">Сталь для стеклянных фасадов</a>
  <a class="btn btn-accent" href="products.html#components">Горячекатаный прокат</a>
</div>
<section class="section"><div class="container">
  {heading("Продукция")}
  <div class="grid-3">
    {card("factory-1.jpg", "Заводские здания", "Быстровозводимые производственные корпуса на лёгком стальном каркасе из H-, Z- и U-образных компонентов.")}
    {card("warehouse.jpg", "Склады", "Складские комплексы с большими пролётами без промежуточных колонн — максимум полезной площади.")}
    {card("stadium.jpg", "Стадионы", "Большепролётные конструкции практически любой геометрии — трибуны от сотен до тысяч мест.")}
    {card("hangar.jpg", "Ангары", "Авиационные и технические ангары с проёмами под ворота больших габаритов.")}
    {card("residential.jpg", "Жилые здания", "Многоэтажные здания на стальном каркасе — короткие сроки и высокая сейсмостойкость.")}
    {card("bridge.jpg", "Мосты", "Мостовые стальные конструкции — пешеходные и автомобильные пролётные строения.")}
  </div>
  <div style="text-align:center;margin-top:var(--space-6)">
    <a class="btn btn-primary" href="products.html">Вся продукция</a>
  </div>
</div></section>
<section class="section section-alt"><div class="container">
  {heading("О компании")}
  <p style="max-width:680px;margin:0 auto;text-align:center;color:var(--color-text-muted)">
    Lizhong Steel Structure (Shandong) Co., Ltd. — интегрированный поставщик услуг в области стальных
    конструкций: проектирование, производство и строительство. Завод расположен в Цзинане (район Лайу),
    провинция Шаньдун. Компания имеет самостоятельные права на экспорт, продукция поставляется по всему миру.
  </p>
  <div class="stats" style="margin-top:var(--space-7)">
    <div><div class="stat-value">40 000 м²</div><div class="stat-label">производственных цехов</div></div>
    <div><div class="stat-value">90+</div><div class="stat-label">производственный персонал</div></div>
    <div><div class="stat-value">ISO</div><div class="stat-label">9001 · 45001 · 14001</div></div>
    <div><div class="stat-value">2</div><div class="stat-label">производственные линии</div></div>
  </div>
  <div style="text-align:center;margin-top:var(--space-6)">
    <a class="btn btn-ghost" href="about.html">Подробнее о компании</a>
  </div>
</div></section>
<section class="section contact-band"><div class="container" style="text-align:center">
  {heading("Свяжитесь с нами")}
  <p style="max-width:560px;margin:0 auto">Пришлите параметры объекта — ответим с расчётом стоимости и сроков поставки в Узбекистан.</p>
  <div class="hero-actions" style="justify-content:center">
    {BAND_BUTTONS}
  </div>
</div></section>
"""

# ---------------------------------------------------------------- about
ABOUT_BODY = f"""
<div class="container"><div class="breadcrumbs"><a href="index.html">Главная</a> › О компании</div></div>
<section class="section" style="padding-top:var(--space-6)"><div class="container">
  {heading("Lizhong Steel Structure (Shandong) Co., Ltd.")}
  <div class="split">
    <div class="prose">
      <p>Компания расположена в районе Лайу города Цзинань (провинция Шаньдун, Китай) и работает как
      интегрированный поставщик услуг в области стальных конструкций: проектирование, производство
      и строительство в одном контуре. Lizhong Steel Structure имеет самостоятельные права на импорт
      и экспорт, продукция поставляется по всему миру.</p>
      <p>Направления производства: обычные и общественные здания из стальных конструкций, стальные
      компоненты (коробчатые и крестовые колонны, подкрановые балки), точные стальные профили для
      стеклянных фасадов и горячекатаный готовый прокат.</p>
      <p>В штате — профессиональная команда: 2 инженера по промышленному и гражданскому строительству,
      6 старших менеджеров, 15 специалистов по международному и внутреннему маркетингу и сервису,
      более 90 человек производственного персонала.</p>
      <div class="tag-row">
        <span class="tag tag-outline">ISO 9001</span>
        <span class="tag tag-outline">ISO 45001</span>
        <span class="tag tag-outline">ISO 14001</span>
      </div>
    </div>
    <div><img src="assets/img/workshop-6.jpg" alt="Производственный цех Lizhong" style="border-radius:var(--radius-md)"></div>
  </div>
</div></section>
<section class="section section-alt"><div class="container">
  {heading("Производство")}
  <div class="split">
    <div class="prose">
      <p><strong>Цех стальных конструкций</strong> — 40 000 м² производственных площадей. Оборудование:
      лазерный раскроечный комплекс 20 кВт, линии горизонтальной автоматической сборки, двухдуговая
      двухпроволочная сварка под флюсом, горизонтальная автоматическая правка, трёхмерная лазерная резка,
      пресс 500 т, сварочные роботы, дробеструйная установка с рабочим полем 2000×2500 мм,
      камера автоматической окраски.</p>
      <p><strong>Линия точной стали для фасадов</strong> — производство точных стальных профилей
      для стеклянных навесных фасадов: T-образные, Y-образные, крестовые, треугольные и прямоугольные
      трубные сечения, а также профили специальной формы по чертежам заказчика.</p>
      <p>По сравнению с горячекатаными двутавровыми балками H-профили экономят от 15 до 30% стали —
      компания производит и поставляет полный сортамент горячекатаного проката.</p>
    </div>
    <div class="prose">
      <img src="assets/img/curtainwall.jpg" alt="Оборудование завода" style="border-radius:var(--radius-md)">
      <img src="assets/img/workshop-5.jpg" alt="Лазерный раскрой" style="border-radius:var(--radius-md)">
    </div>
  </div>
</div></section>
<section class="section contact-band"><div class="container" style="text-align:center">
  <h2 style="font:var(--text-h2)">Работаем с проектами в Узбекистане</h2>
  <p style="max-width:560px;margin:var(--space-4) auto 0">Пришлите чертежи или параметры здания — подготовим предложение по производству и поставке.</p>
  <div class="hero-actions" style="justify-content:center">
    <a class="btn btn-accent" href="contact.html">Получить расчёт</a>
  </div>
</div></section>
"""

# ---------------------------------------------------------------- products
PRODUCTS_BODY = f"""
<div class="container"><div class="breadcrumbs"><a href="index.html">Главная</a> › Продукция</div></div>
<div class="container">
  <div class="allcat-bar">Все категории</div>
  <div class="cat-chips">
    <span class="tag tag-primary">Обычные стальные здания</span>
    <span class="tag tag-primary">Общественные стальные здания</span>
    <span class="tag tag-primary">Стальные компоненты</span>
    <span class="tag tag-primary">Сталь для стеклянных фасадов</span>
    <span class="tag tag-accent">Горячекатаный прокат</span>
  </div>
</div>
<section class="section"><div class="container">
  {heading("Здания из стальных конструкций")}
  <div class="grid-3">
    {card("factory-1.jpg", "Заводские здания", "Лёгкий стальной каркас из H-, Z- и U-образных компонентов. Компактный вес, короткие сроки монтажа.")}
    {card("warehouse.jpg", "Склады", "Большепролётные складские корпуса без промежуточных опор.")}
    {card("stadium.jpg", "Стадионы", "Сталь высокого качества формуется практически под любой пролёт — трибуны от сотен до тысяч мест.")}
    {card("residential.jpg", "Жилые здания", "Многоэтажное строительство на стальном каркасе.")}
    {card("hangar.jpg", "Ангары", "Конструкции с широкими проёмами под авиационную и специальную технику.")}
    {card("garage.jpg", "Гаражи", "Гаражные комплексы и техцентры из стальных конструкций.")}
    {card("bridge.jpg", "Мосты", "Пролётные строения пешеходных и автомобильных мостов.")}
    {card("breeding.jpg", "Животноводческие комплексы", "Фермы и производственные корпуса для сельского хозяйства.")}
    {card("factory-3.jpg", "Производственные корпуса под заказ", "Изготовление по чертежам заказчика: любые виды, спецификации и материалы.")}
  </div>
</div></section>
<section class="section section-alt" id="components"><div class="container">
  {heading("Компоненты и прокат")}
  <div class="grid-3">
    {card("workshop-4.jpg", "Коробчатые и крестовые колонны", "Сварные коробчатые колонны, крестовые колонны, подкрановые балки для промышленных зданий.")}
    {card("profile-sq.jpg", "Сталь для стеклянных фасадов", "Точные профили: T-, Y-образные, крестовые, треугольные, прямоугольные трубные и специальные сечения по чертежам.")}
    {card("workshop-5.jpg", "Горячекатаный прокат", "H-балки, лист и полный сортамент готового проката. Экономия стали 15–30% по сравнению с двутавровыми балками.")}
  </div>
  <div style="margin-top:var(--space-7);overflow-x:auto">
    <table class="table">
      <thead><tr><th>Параметр</th><th>Значение</th></tr></thead>
      <tbody>
        <tr><td>Производственные площади</td><td>40 000 м²</td></tr>
        <tr><td>Лазерный раскрой</td><td>комплекс 20 кВт, трёхмерная лазерная резка</td></tr>
        <tr><td>Сварка</td><td>двухдуговая двухпроволочная под флюсом, сварочные роботы</td></tr>
        <tr><td>Обработка поверхности</td><td>дробеструйная установка 2000×2500 мм, автоматическая окраска</td></tr>
        <tr><td>Прессовое оборудование</td><td>500 т</td></tr>
        <tr><td>Сертификация</td><td>ISO 9001, ISO 45001, ISO 14001</td></tr>
      </tbody>
    </table>
  </div>
</div></section>
<nav class="toolbar toolbar-sticky" aria-label="Быстрые действия">
  <a class="toolbar-item" href="contact.html">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21 11.5a8.4 8.4 0 0 1-8.5 8.3 8.6 8.6 0 0 1-3.9-.9L3 20l1.2-5.2a8.2 8.2 0 0 1-.7-3.3A8.4 8.4 0 0 1 12 3.2a8.4 8.4 0 0 1 9 8.3Z"/></svg>
    Заявка</a>
  {TOOLBAR_WA}
  {TOOLBAR_EMAIL}
  <a class="toolbar-item" href="#top" onclick="window.scrollTo({{top:0,behavior:'smooth'}});return false">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="m18 15-6-6-6 6"/></svg>
    Наверх</a>
</nav>
"""

# ---------------------------------------------------------------- contact
CONTACT_BODY = f"""
<div class="container"><div class="breadcrumbs"><a href="index.html">Главная</a> › Контакты</div></div>
<section class="section" style="padding-top:var(--space-6)"><div class="container">
  <div class="split">
    <div class="prose">
      <div class="card-eyebrow">Контакты</div>
      <h1 style="font:var(--text-h1)">Получить расчёт</h1>
      <p>Пришлите параметры объекта: назначение здания, габариты, город строительства.
      Ответим с расчётом стоимости производства и поставки в Узбекистан.</p>
      {CONTACT_LINES}
      <p style="font:var(--text-body-sm)">Завод: Цзинань, район Лайу, провинция Шаньдун, Китай.</p>
    </div>
    <div>
      <form class="form" onsubmit="return typeof sendInquiry==='function' ? sendInquiry(this) : false">
        <div class="field"><label for="f-company">Компания</label>
          <input class="input" id="f-company" name="company" placeholder="Название компании"></div>
        <div class="field"><label for="f-contact">Email или телефон</label>
          <input class="input" id="f-contact" name="contact" required placeholder="Как с вами связаться"></div>
        <div class="field"><label for="f-msg">Сообщение</label>
          <textarea class="textarea" id="f-msg" name="message" required placeholder="Опишите объект: назначение, габариты, сроки"></textarea></div>
        {FORM_TAIL}
    </div>
  </div>
</div></section>
"""

PAGES = {
    "index.html": ("Lizhong Steel Structure — стальные конструкции с поставкой в Узбекистан",
                   "Проектирование, производство и монтаж стальных конструкций: заводские здания, склады, ангары, стадионы. Завод в Китае, поставки в Узбекистан.",
                   INDEX_BODY, ""),
    "about.html": ("О компании — Lizhong Steel Structure",
                   "Lizhong Steel Structure (Shandong) Co., Ltd.: 40 000 м² цехов, ISO 9001/45001/14001, полный цикл от проектирования до монтажа.",
                   ABOUT_BODY, ""),
    "products.html": ("Продукция — Lizhong Steel Structure",
                      "Заводские здания, склады, стадионы, ангары, мосты, стальные компоненты, сталь для фасадов и горячекатаный прокат.",
                      PRODUCTS_BODY, "has-toolbar"),
    "contact.html": ("Контакты — Lizhong Steel Structure",
                     "Получите расчёт стоимости стальных конструкций: параметры объекта, форма запроса.",
                     CONTACT_BODY, ""),
}


def main():
    css_dir = SITE / "assets" / "css"
    if css_dir.exists():
        shutil.rmtree(css_dir)
    (css_dir / "tokens").mkdir(parents=True)
    for rel in ["styles.css", "base.css", "components.css",
                "tokens/colors.css", "tokens/typography.css", "tokens/spacing.css"]:
        shutil.copy(DS / rel, css_dir / rel)
    (SITE / ".nojekyll").write_text("")
    if DOMAIN:
        (SITE / "CNAME").write_text(DOMAIN + "\n")
    for slug, (title, desc, body, cls) in PAGES.items():
        (SITE / slug).write_text(page_shell(slug, title, desc, body, cls), encoding="utf-8")
        print("built", slug)


if __name__ == "__main__":
    main()
