#!/usr/bin/env python3
"""Build the Mutex Studio blog.

Sources: tools/blog/posts/<slug>.html. Each file starts with an HTML comment
holding a JSON object (front matter), followed by the article body HTML.

Front matter keys:
  title        Post title (also <title> and og:title)
  description  Meta description, 140-160 characters
  date         Publication date, YYYY-MM-DD
  updated      Optional last-modified date, YYYY-MM-DD
  product      autoscaler | storage-observer | traefork | consulting
  eyebrow      Short topic label shown above the title
  lead         One or two sentence standfirst shown under the title
  cta          One or two sentences for the closing product box

Outputs: blog/<slug>/index.html, blog/index.html, blog/feed.xml and the blog
entries of sitemap.xml. Run from anywhere: python3 tools/blog/build.py
"""
import html, json, math, os, re, sys
from datetime import datetime, timezone
from email.utils import format_datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SRC = os.path.join(ROOT, "tools", "blog", "posts")
SITE = "https://www.mutexstudio.com"
AUTHOR = "David García García"

PRODUCTS = {
    "autoscaler": {"name": "Azure Autoscaler", "url": "/azure-autoscaler/", "accent": "accent-blue", "button": "See Azure Autoscaler"},
    "storage-observer": {"name": "Storage Observer", "url": "/storage-observer/", "accent": "accent-violet", "button": "See Storage Observer"},
    "traefork": {"name": "Traefork", "url": "/traefik-precompiled/", "accent": "accent-emerald", "button": "See Traefork"},
    "consulting": {"name": "Consulting", "url": "/consulting/", "accent": "accent-blue", "button": "Talk to us"},
}

ARROW = '<svg fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>'
BACK = '<svg fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M10 19l-7-7m0 0l7-7m-7 7h18"/></svg>'


def esc(s):
    return html.escape(s, quote=True)


def chrome():
    """Take nav and footer verbatim from the support page so every page matches."""
    s = open(os.path.join(ROOT, "support", "index.html"), encoding="utf-8").read()
    nav = re.search(r'(?s)  <nav class="site-nav">.*?</nav>\n', s).group(0)
    footer = re.search(r'(?s)  <footer class="site-footer">.*?</footer>\n', s).group(0)
    head_assets = re.search(r'(?s)(  <link rel="icon".*?<link rel="stylesheet"[^>]*>)', s).group(1)
    script = re.search(r'  <script src="/assets/js/site\.js[^"]*"></script>', s).group(0)
    return nav, footer, head_assets, script


def load_posts():
    posts = []
    for fn in sorted(os.listdir(SRC)):
        if not fn.endswith(".html"):
            continue
        raw = open(os.path.join(SRC, fn), encoding="utf-8").read()
        m = re.match(r"\s*<!--(.*?)-->\s*(.*)$", raw, re.S)
        if not m:
            sys.exit(f"{fn}: missing front matter comment")
        meta = json.loads(m.group(1))
        for k in ("title", "description", "date", "product", "eyebrow", "lead", "cta"):
            if not meta.get(k):
                sys.exit(f"{fn}: missing '{k}'")
        if meta["product"] not in PRODUCTS:
            sys.exit(f"{fn}: unknown product {meta['product']}")
        meta["slug"] = fn[:-5]
        meta["body"] = m.group(2).strip()
        meta.setdefault("updated", meta["date"])
        text = re.sub(r"(?s)<pre.*?</pre>", " ", meta["body"])
        words = len(re.sub(r"<[^>]+>", " ", text).split())
        meta["words"] = words
        meta["minutes"] = max(1, math.ceil(words / 220))
        meta["url"] = f"{SITE}/blog/{meta['slug']}/"
        posts.append(meta)
    posts.sort(key=lambda p: (p["date"], p["slug"]), reverse=True)
    return posts


def human_date(d):
    return datetime.strptime(d, "%Y-%m-%d").strftime("%-d %B %Y")


def head(title, description, canonical, head_assets, og_type, extra=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(description)}">
  <title>{esc(title)}</title>

{head_assets}
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" type="application/rss+xml" title="Mutex Studio blog" href="{SITE}/blog/feed.xml">
  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="Mutex Studio">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE}/assets/img/favicons/android-chrome-512x512.png">
  <meta property="og:locale" content="en_US">
  <meta name="twitter:card" content="summary">
{extra}</head>
"""


def render_post(p, nav, footer, head_assets, script):
    prod = PRODUCTS[p["product"]]
    ld = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": p["title"],
        "description": p["description"],
        "datePublished": p["date"],
        "dateModified": p["updated"],
        "inLanguage": "en",
        "wordCount": p["words"],
        "url": p["url"],
        "mainEntityOfPage": {"@type": "WebPage", "@id": p["url"]},
        "image": f"{SITE}/assets/img/favicons/android-chrome-512x512.png",
        "author": {"@type": "Person", "name": AUTHOR, "url": "https://medium.com/@deividb"},
        "publisher": {
            "@type": "Organization",
            "name": "Mutex Studio",
            "url": f"{SITE}/",
            "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/img/favicons/android-chrome-512x512.png"},
        },
    }
    extra = (
        f'  <meta property="article:published_time" content="{p["date"]}">\n'
        f'  <meta property="article:modified_time" content="{p["updated"]}">\n'
        f'  <meta property="article:author" content="{esc(AUTHOR)}">\n'
        f'  <script type="application/ld+json">\n{json.dumps(ld, ensure_ascii=False, indent=2)}\n  </script>\n'
    )
    title = f'{p["title"]} — Mutex Studio'
    return head(title, p["description"], p["url"], head_assets, "article", extra) + f"""
<body class="{prod['accent']} page-blog">

{nav}
  <main class="post">
    <article class="post-inner">
      <a href="/blog/" class="hero-back">
        {BACK}
        All posts
      </a>
      <header class="post-header">
        <p class="eyebrow">{esc(p['eyebrow'])}</p>
        <h1>{esc(p['title'])}</h1>
        <p class="post-lead">{esc(p['lead'])}</p>
        <p class="post-meta"><span>By {esc(AUTHOR)}</span><span><time datetime="{p['date']}">{human_date(p['date'])}</time></span><span>{p['minutes']} min read</span></p>
      </header>

      <div class="prose">
{p['body']}
      </div>

      <aside class="card post-cta" aria-label="{esc(prod['name'])}">
        <p class="eyebrow">{esc(prod['name'])}</p>
        <h2>Where {esc(prod['name'])} fits</h2>
        <p>{esc(p['cta'])}</p>
        <a href="{prod['url']}" class="btn btn-primary">
          {esc(prod['button'])}
          {ARROW}
        </a>
      </aside>

      <p class="post-footer-nav"><a href="/blog/">← Back to all posts</a></p>
    </article>
  </main>

{footer}
{script}
</body>
</html>
"""


def render_index(posts, nav, footer, head_assets, script):
    items = []
    for p in posts:
        items.append(f"""        <a href="/blog/{p['slug']}/" class="card post-card">
          <p class="post-meta"><span><time datetime="{p['date']}">{human_date(p['date'])}</time></span><span>{p['minutes']} min read</span><span>{esc(p['eyebrow'])}</span></p>
          <h2>{esc(p['title'])}</h2>
          <p>{esc(p['description'])}</p>
        </a>""")
    listing = "\n".join(items) if items else '        <p class="text-muted">No posts yet.</p>'
    desc = "Mutex Studio blog: practical articles on Azure cost and autoscaling, Kubernetes ingress with Traefik, and file storage usage, written by the engineers who build our tools."
    return head("Blog — Mutex Studio", desc, f"{SITE}/blog/", head_assets, "website") + f"""
<body class="accent-blue page-blog">

{nav}
  <section class="hero hero-grid">
    <div class="hero-glow hero-glow--center"></div>
    <div class="container hero-content">
      <a href="/" class="hero-back">
        {BACK}
        Back to Mutex Studio
      </a>
      <div class="hero-narrow">
        <p class="eyebrow">Blog</p>
        <h1 class="heading-xl">
          Notes on Azure, Kubernetes<br><span class="gradient-text">and storage</span>
        </h1>
        <p class="lead">
          Practical articles on scaling Azure resources, running Traefik as a Kubernetes ingress and keeping track of file storage. We write about problems we have worked on in production. A new post goes up every week. <a href="/blog/feed.xml" class="text-muted" style="text-decoration:underline">RSS feed</a>
        </p>
      </div>
    </div>
  </section>

  <section class="section section--border">
    <div class="container">
      <div class="post-list">
{listing}
      </div>
    </div>
  </section>

{footer}
{script}
</body>
</html>
"""


def render_feed(posts):
    now = format_datetime(datetime.now(timezone.utc))
    items = []
    for p in posts:
        pub = format_datetime(datetime.strptime(p["date"], "%Y-%m-%d").replace(hour=8, tzinfo=timezone.utc))
        items.append(f"""    <item>
      <title>{esc(p['title'])}</title>
      <link>{p['url']}</link>
      <guid isPermaLink="true">{p['url']}</guid>
      <pubDate>{pub}</pubDate>
      <dc:creator>{esc(AUTHOR)}</dc:creator>
      <description>{esc(p['description'])}</description>
    </item>""")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/">
  <channel>
    <title>Mutex Studio blog</title>
    <link>{SITE}/blog/</link>
    <atom:link href="{SITE}/blog/feed.xml" rel="self" type="application/rss+xml"/>
    <description>Practical articles on Azure cost and autoscaling, Kubernetes ingress with Traefik, and file storage usage.</description>
    <language>en</language>
    <lastBuildDate>{now}</lastBuildDate>
{chr(10).join(items)}
  </channel>
</rss>
"""


def update_sitemap(posts):
    path = os.path.join(ROOT, "sitemap.xml")
    s = open(path, encoding="utf-8").read()
    s = re.sub(r"\n  <url><loc>https://www\.mutexstudio\.com/blog/[^<]*</loc>.*?</url>", "", s)
    latest = posts[0]["updated"] if posts else datetime.now().strftime("%Y-%m-%d")
    lines = [f"  <url><loc>{SITE}/blog/</loc><lastmod>{latest}</lastmod></url>"]
    lines += [f"  <url><loc>{p['url']}</loc><lastmod>{p['updated']}</lastmod></url>" for p in posts]
    s = s.replace("</urlset>", "\n".join(lines) + "\n</urlset>")
    open(path, "w", encoding="utf-8").write(s)


def main():
    nav, footer, head_assets, script = chrome()
    posts = load_posts()
    for p in posts:
        d = os.path.join(ROOT, "blog", p["slug"])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(render_post(p, nav, footer, head_assets, script))
    os.makedirs(os.path.join(ROOT, "blog"), exist_ok=True)
    open(os.path.join(ROOT, "blog", "index.html"), "w", encoding="utf-8").write(render_index(posts, nav, footer, head_assets, script))
    open(os.path.join(ROOT, "blog", "feed.xml"), "w", encoding="utf-8").write(render_feed(posts))
    update_sitemap(posts)
    for p in posts:
        print(f"{p['date']}  {p['slug']}  {p['words']} words, {p['minutes']} min")


if __name__ == "__main__":
    main()
