#!/usr/bin/env python3
"""Genera el sitio estatico en site/ a partir de proyectos.py.

Uso: python3 build.py
"""
from html import escape
from pathlib import Path
from urllib.parse import quote

from PIL import Image

import json

from proyectos import NECESIDADES, PERFIL, PREGUNTAS, PROCESO, PROYECTOS, RUBROS, SERVICIOS

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"
IMG = SITE / "img"
SITE_URL = "https://dglab-ar.com"
FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com" />'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />'
    '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />'
)
# Un color por proyecto, en orden.
# Estadisticas de visitas sin cookies (cuenta en umami.is).
UMAMI_ID = "85720f9e-abdc-4577-87f2-56e73641223c"
ACENTOS = ["#7c3aed", "#0284c7", "#059669", "#4f46e5", "#0e7490"]
# Frases que rotan en el titulo de la portada; la ultima es la que queda sin JS.
ROTATIVAS = ["vender más", "ordenar su stock", "cobrar sin errores", "atender mejor", "más eficiencia", "trabajar mejor"]
MARQUESINA = [
    "Sistemas de gestión", "Turnos online", "Pedidos por WhatsApp", "Liquidaciones automáticas",
    "Apps de campo", "Reportes", "IA aplicada", "Portales para clientes", "Stock y presupuestos",
]
ICONOS_SERVICIO = [
    '<path d="M4 6h16M4 12h16M4 18h10" />',
    '<path d="M13 3 5 14h6l-1 7 8-11h-6z" />',
    '<path d="M4 19V9m6 10V5m6 14v-7m4 7H2" />',
    '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z" /><circle cx="12" cy="10" r="2.5" />',
]


def size(name):
    with Image.open(IMG / name) as im:
        return im.size


def is_tall(name):
    w, h = size(name)
    return h > w * 1.2


def acento(i):
    return ACENTOS[i % len(ACENTOS)]


def img(name, alt, css="", prefix="", lazy=True):
    w, h = size(name)
    loading = ' loading="lazy"' if lazy else ""
    clase = f' class="{css}"' if css else ""
    return f'<img src="{prefix}img/{name}" alt="{escape(alt)}" width="{w}" height="{h}"{loading}{clase} />'


def url_canonica(path):
    """Direccion unica de cada pagina (sin .html), para que Google no la cuente dos veces."""
    return f"{SITE_URL}/{path.removesuffix('.html')}"


def head(title, description, path, depth=0):
    prefix = "../" * depth
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}" />
<meta name="theme-color" content="#fdfbf6" />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="{PERFIL['marca']}" />
<meta property="og:title" content="{escape(title)}" />
<meta property="og:description" content="{escape(description)}" />
<meta property="og:image" content="{SITE_URL}/img/og-dglab.jpg" />
<meta property="og:url" content="{url_canonica(path)}" />
<link rel="canonical" href="{url_canonica(path)}" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="icon" href="{prefix}favicon.ico?v=2" sizes="any" />
<link rel="icon" href="{prefix}favicon.png?v=2" type="image/png" />
<link rel="apple-touch-icon" href="{prefix}img/dglab-icono.png" />
{FONTS}
<link rel="stylesheet" href="{prefix}styles.css" />
<script>document.documentElement.classList.add("js");</script>
{datos_google() if depth == 0 else ""}
<script src="{prefix}app.js" defer></script>
<script defer src="https://cloud.umami.is/script.js" data-website-id="{UMAMI_ID}"></script>
</head>
<body>
<div class="blobs" aria-hidden="true"><span></span><span></span><span></span></div>"""


def datos_google():
    # Ficha para buscadores: atiende negocios de todo el pais.
    data = {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": PERFIL["marca"],
        "description": PERFIL["bajada"],
        "url": SITE_URL,
        "image": f"{SITE_URL}/img/og-dglab.jpg",
        "email": PERFIL["email"],
        "telephone": "+" + PERFIL["whatsapp"],
        "founder": {"@type": "Person", "name": PERFIL["nombre"]},
        "areaServed": {"@type": "Country", "name": "Argentina"},
    }
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def nav(depth=0):
    prefix = "../" * depth
    return f"""
<header class="nav">
  <div class="nav-inner">
    <a class="brand" href="{prefix}index.html"><img src="{prefix}img/dglab-logo-tinta.png" alt="{PERFIL['marca']}" width="137" height="36" /></a>
    <nav class="nav-links">
      <a href="{prefix}index.html#servicios">Servicios</a>
      <a href="{prefix}index.html#proyectos">Proyectos</a>
      <a href="{prefix}index.html#preguntas">Preguntas</a>
      <a class="button button-small" href="{prefix}index.html#contacto">Hablemos</a>
    </nav>
  </div>
</header>"""


MENSAJE_WHATSAPP = "¡Hola DGLab! Vi tu página y quería consultar por un proyecto."


def whatsapp_url():
    text = quote(MENSAJE_WHATSAPP)
    return f"https://wa.me/{PERFIL['whatsapp']}?text={text}"


def contact_links(whatsapp=True):
    links = []
    if whatsapp and PERFIL.get("whatsapp"):
        links.append(f'<a class="button button-white" href="{whatsapp_url()}" target="_blank" rel="noopener" data-umami-event="WhatsApp contacto">Escribinos por WhatsApp</a>')
    if PERFIL.get("email"):
        links.append(f'<a class="button button-ghost" data-umami-event="Email" href="mailto:{PERFIL["email"]}?subject={quote("Consulta por un proyecto")}">{escape(PERFIL["email"])}</a>')
    if PERFIL.get("linkedin"):
        links.append(f'<a class="button button-ghost" href="{PERFIL["linkedin"]}" target="_blank" rel="noopener">LinkedIn</a>')
    if PERFIL.get("github"):
        links.append(f'<a class="button button-ghost" href="{PERFIL["github"]}" target="_blank" rel="noopener">GitHub</a>')
    return "\n".join(links)


def footer(depth=0):
    prefix = "../" * depth
    return f"""
<footer class="footer">
  <div class="footer-inner">
    <img src="{prefix}img/dglab-logo-tinta.png" alt="{PERFIL['marca']}" width="137" height="36" />
    <p>{escape(PERFIL['fundador'])}</p>
    <p class="footer-zone">📍 {escape(PERFIL['zona'])}</p>
    <p class="footer-note">Las capturas usan datos de ejemplo y los nombres de clientes se omiten por confidencialidad. © 2026 {PERFIL['marca']}.</p>
  </div>
</footer>
</body>
</html>"""


def cover(p, prefix=""):
    if p.get("portada"):
        foco = f' style="object-position: {p["foco"]}"' if p.get("foco") else ""
        w, h = size(p["portada"])
        return f'<img src="{prefix}img/{p["portada"]}" alt="{escape(p["titulo"])}" loading="lazy" width="{w}" height="{h}"{foco} />'
    return f'<div class="cover-icon"><span>{escape(p.get("icono", "·"))}</span></div>'


# Cuantas tarjetas se ven antes de "Ver todos" (sin contar la destacada).
VISIBLES = 3
VISIBLES_CELULAR = 3


def project_card(i, p, featured=False, extra=""):
    css = "card card-featured reveal" if featured else f"card reveal {extra}".strip()
    return f"""
    <a class="{css}" href="proyectos/{p['slug']}.html" style="--accent: {acento(i)}" data-tilt>
      <div class="card-cover">{cover(p)}</div>
      <div class="card-body">
        <div class="card-top"><span class="card-num">{i + 1:02d}</span><span class="tag">{escape(p['rubro'])}</span></div>
        <h3>{escape(p['titulo'])}</h3>
        <p>{escape(p['resumen'])}</p>
        <span class="card-link">Ver proyecto <span aria-hidden="true">→</span></span>
      </div>
    </a>"""


def titulo_portada():
    titulo = escape(PERFIL["titulo"])
    remate = "trabajar mejor."
    if remate not in titulo:
        return titulo
    frases = "|".join(ROTATIVAS)
    return titulo.replace(
        remate,
        f'<span class="rotator" data-words="{escape(frases)}"><span class="rotator-word">{remate[:-1]}</span>.</span>',
    )


def index():
    first, rest = PROYECTOS[0], PROYECTOS[1:]
    rubros = 6
    servicios = "".join(
        f'<div class="service reveal"><span class="service-icon"><svg viewBox="0 0 24 24" aria-hidden="true">{ICONOS_SERVICIO[i % len(ICONOS_SERVICIO)]}</svg></span>'
        f"<h3>{escape(t)}</h3><p>{escape(d)}</p></div>"
        for i, (t, d) in enumerate(SERVICIOS)
    )
    proceso = "".join(
        f'<li class="reveal"><span class="step">{i:02d}</span><h3>{escape(t)}</h3><p>{escape(d)}</p></li>' for i, (t, d) in enumerate(PROCESO, 1)
    )
    marquesina = "".join(f"<span>{escape(m)}</span><i>✦</i>" for m in MARQUESINA)
    opciones_rubro = "".join(f'<button type="button" class="choice" data-value="{escape(r)}">{escape(r)}</button>' for r in RUBROS)
    necesidades = "".join(f'<button type="button" class="choice" data-value="{escape(n)}">{escape(n)}</button>' for n in NECESIDADES)
    preguntas = "".join(
        f'<details class="faq-item"><summary>{escape(q)}<span aria-hidden="true">+</span></summary><p>{escape(a)}</p></details>' for q, a in PREGUNTAS
    )
    html = head(f"{PERFIL['marca']} · {PERFIL['rol']}", f"{PERFIL['bajada']} {PERFIL['zona']}", "")
    html += nav()
    html += f"""
<section class="hero">
  <div class="hero-inner">
    <div class="hero-text">
      <p class="pill"><span class="dot"></span>{escape(PERFIL['rol'])}</p>
      <h1>{titulo_portada()}</h1>
      <p class="lead">{escape(PERFIL['bajada'])}</p>
      <div class="actions">
        <a class="button" href="#proyectos">Ver proyectos</a>
        <a class="button button-ghost" href="{whatsapp_url()}" target="_blank" rel="noopener" data-umami-event="WhatsApp portada">Hablemos por WhatsApp</a>
      </div>
    </div>
    <div class="hero-visual" aria-hidden="true">
      {img("agencia-panel.webp", "", "float float-main", lazy=False)}
      {img("barberia-mobile.webp", "", "float float-phone", lazy=False)}
      {img("agencia-mobile-inversor.webp", "", "float float-phone-2", lazy=False)}
      <div class="float-badge badge-1"><b>+1.300</b> productos con búsqueda al instante</div>
      <div class="float-badge badge-2"><b>Liquidación</b> calculada sola</div>
    </div>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee-track">{marquesina}{marquesina}</div></div>

<main>
<section class="stats">
  <div class="stat reveal"><strong>+<span data-count="{len(PROYECTOS)}">{len(PROYECTOS)}</span></strong><span>proyectos desarrollados</span></div>
  <div class="stat reveal"><strong>+<span data-count="{rubros}">{rubros}</span></strong><span>rubros abordados: automotriz; comercio; gobierno; hospitalidad y turismo; industria; salud, cuidado personal y estética; entre otros</span></div>
  <div class="stat reveal"><strong>1 a 1</strong><span>siempre hablarás con quien diseñó y programó tu solución</span></div>
</section>

<section id="servicios" class="section">
  <div class="section-head reveal">
    <p class="eyebrow">Servicios</p>
    <h2>¿Cómo podemos <span class="grad">ayudarte?</span></h2>
  </div>
  <div class="services">{servicios}</div>
</section>

<section class="section compare-section">
  <div class="section-head reveal">
    <p class="eyebrow">Antes y después</p>
    <h2>Del Excel que nadie entiende <span class="grad">al sistema que usa todo el equipo</span></h2>
    <p class="lead">Arrastrá la barra o tocá “Antes” y “Después”. Los mismos datos, más herramientas para tomar decisiones.</p>
  </div>
  <div class="compare reveal" style="--pos: 50%">
    {img("antes-excel.webp", "Antes: planilla de Excel desordenada", "compare-before")}
    <div class="compare-after">{img("agencia-panel.webp", "Después: panel del sistema de gestión")}</div>
    <span class="compare-handle" aria-hidden="true"><span>⟷</span></span>
    <input class="compare-range" type="range" min="0" max="100" value="50" aria-label="Comparar antes y después" />
    <button class="compare-label label-before" type="button" data-go="100">Antes</button>
    <button class="compare-label label-after" type="button" data-go="0">Después</button>
  </div>
</section>

<section id="proyectos" class="section">
  <div class="section-head reveal">
    <p class="eyebrow">Proyectos</p>
    <h2>Problemas reales, <span class="grad">resueltos a medida</span></h2>
  </div>
  {project_card(0, first, featured=True)}
  <div class="grid" id="grilla-proyectos">
    {''.join(project_card(i, p, extra=("extra" if i > VISIBLES else "extra-m" if i > VISIBLES_CELULAR else "")) for i, p in enumerate(rest, 1))}
  </div>
  <div class="more-wrap"><button class="button button-ghost more" type="button" data-more="grilla-proyectos">Ver todos los proyectos</button></div>
</section>



<section id="preguntas" class="section">
  <div class="section-head reveal">
    <p class="eyebrow">Preguntas frecuentes</p>
    <h2>Lo que todos preguntan <span class="grad">antes de arrancar</span></h2>
  </div>
  <div class="faq">{preguntas}</div>
</section>

<section id="contacto" class="contact reveal">
  <div class="contact-grid">
    <div>
      <p class="eyebrow eyebrow-dark">Contacto</p>
      <h2>Contanos tu caso</h2>
      <p class="lead">Tocá tu rubro y lo que necesitás: el mensaje se arma solo y lo mandás por WhatsApp. Te respondemos nosotros, no un bot.</p>
      <form class="builder" id="consulta" data-whatsapp="{PERFIL['whatsapp']}">
        <p class="builder-label">Mi negocio es…</p>
        <div class="choices" data-group="rubro" data-single>{opciones_rubro}</div>
        <p class="builder-label">Me interesa…</p>
        <div class="choices" data-group="necesidad">{necesidades}</div>
        <label class="builder-label" for="consulta-detalle">Contanos cómo lo hacés hoy (opcional)</label>
        <textarea id="consulta-detalle" rows="2" maxlength="400" placeholder="Ej: llevo el stock en un Excel y los pedidos llegan por WhatsApp"></textarea>
        <label class="builder-label" for="consulta-nombre">Tu nombre (opcional)</label>
        <input id="consulta-nombre" type="text" maxlength="60" autocomplete="name" />
      </form>
      <div class="actions">{contact_links(whatsapp=False)}</div>
    </div>
    <div class="chat" aria-live="polite">
      <div class="chat-head"><span class="chat-avatar">DG</span><div><b>DGLab</b><small>en línea</small></div></div>
      <div class="chat-body">
        <p class="bubble bubble-in">¡Hola! Contanos qué necesitás 👋</p>
        <p class="bubble bubble-out" id="consulta-preview">{MENSAJE_WHATSAPP}</p>
      </div>
      <a class="button chat-send" id="consulta-enviar" href="{whatsapp_url()}" target="_blank" rel="noopener" data-umami-event="WhatsApp armador">Enviar por WhatsApp</a>
    </div>
  </div>
</section>
</main>"""
    html += footer()
    (SITE / "index.html").write_text(html, encoding="utf-8")


PREGUNTA_CTA = "¿Te imaginás algo así en tu negocio?"


def project_page(i, p):
    nxt = PROYECTOS[(i + 1) % len(PROYECTOS)]
    gallery = ""
    for name, caption in p["imagenes"]:
        w, h = size(name)
        css = "shot tall reveal" if is_tall(name) else "shot reveal"
        gallery += f"""
    <figure class="{css}">
      <a href="../img/{name}" target="_blank" rel="noopener"><img src="../img/{name}" alt="{escape(caption)}" loading="lazy" width="{w}" height="{h}" /></a>
      <figcaption>{escape(caption)}</figcaption>
    </figure>"""
    html = head(f"{p['titulo']} · {PERFIL['marca']}", p["resumen"], f"proyectos/{p['slug']}.html", depth=1)
    html += nav(depth=1)
    html += f"""
<main class="project" style="--accent: {acento(i)}">
  <section class="project-hero">
    <a class="back" href="../index.html#proyectos">← Todos los proyectos</a>
    <div class="card-top"><span class="card-num">{i + 1:02d}</span><span class="tag">{escape(p['rubro'])}</span></div>
    <h1>{escape(p['titulo'])}</h1>
    <p class="lead">{escape(p['resumen'])}</p>
    <div class="project-cta">
      <span>{PREGUNTA_CTA}</span>
      <a class="button" href="{whatsapp_url()}" target="_blank" rel="noopener" data-umami-event="WhatsApp proyecto arriba" data-umami-event-proyecto="{p['slug']}">Escribinos por WhatsApp</a>
    </div>
  </section>
  {'' if p.get('portada') else f'<div class="project-icon">{cover(p, "../")}</div>'}
  <div class="project-grid">
    <section class="panel reveal">
      <h2>El problema</h2>
      <p>{escape(p['problema'])}</p>
      <h2>Resultado</h2>
      <p>{escape(p['resultado'])}</p>
    </section>
    <section class="panel reveal">
      <h2>Lo que hicimos</h2>
      <ul class="checks">{''.join(f'<li>{escape(item)}</li>' for item in p['solucion'])}</ul>
    </section>
  </div>
  {f'<div class="gallery">{gallery}</div>' if gallery else ''}
  <div class="next">
    <div class="next-cta reveal">
      <span>{PREGUNTA_CTA}</span>
      <a class="button" href="{whatsapp_url()}" target="_blank" rel="noopener" data-umami-event="WhatsApp proyecto" data-umami-event-proyecto="{p['slug']}">Escribinos por WhatsApp</a>
    </div>
    <a class="next-project reveal" href="{nxt['slug']}.html" style="--accent: {acento(i + 1)}">
      <span>Siguiente proyecto</span>
      <strong>{escape(nxt['titulo'])} →</strong>
    </a>
  </div>
</main>"""
    html += footer(depth=1)
    (SITE / "proyectos" / f"{p['slug']}.html").write_text(html, encoding="utf-8")


def mapa_del_sitio():
    """sitemap.xml y robots.txt: la lista de paginas que se le entrega a Google."""
    paginas = [""] + [f"proyectos/{p['slug']}" for p in PROYECTOS]
    urls = "\n".join(f"  <url><loc>{SITE_URL}/{pagina}</loc></url>" for pagina in paginas)
    (SITE / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n</urlset>\n",
        encoding="utf-8",
    )
    (SITE / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")


def main():
    (SITE / "proyectos").mkdir(parents=True, exist_ok=True)
    for old in (SITE / "proyectos").glob("*.html"):
        old.unlink()
    for p in PROYECTOS:
        for name in [p.get("portada")] + [n for n, _ in p["imagenes"]]:
            if name and not (IMG / name).exists():
                raise SystemExit(f"Falta la imagen img/{name} ({p['slug']})")
    index()
    for i, p in enumerate(PROYECTOS):
        project_page(i, p)
    mapa_del_sitio()
    print(f"Sitio generado en {SITE}: index + {len(PROYECTOS)} proyectos")


if __name__ == "__main__":
    main()
