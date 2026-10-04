from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
ROOT=Path(__file__).resolve().parents[1]
errs=[]; warns=[]; docs={}
for fp in ROOT.rglob('*.html'):
    rel='/' + fp.relative_to(ROOT).as_posix()
    s=BeautifulSoup(fp.read_text(encoding='utf-8'),'html.parser'); docs[rel]=(fp,s)
    if rel!='/404.html':
        if len(s.find_all('h1'))!=1: errs.append((rel,'h1_count',len(s.find_all('h1'))))
        if not s.title: errs.append((rel,'missing_title'))
        if not s.find('meta',attrs={'name':'description'}): errs.append((rel,'missing_description'))
        if not s.find('link',rel='canonical'): errs.append((rel,'missing_canonical'))
        hrs={x.get('hreflang') for x in s.find_all('link',rel='alternate')}
        if not {'ja','en','x-default'}<=hrs: errs.append((rel,'hreflang',hrs))
    for img in s.find_all('img'):
        if img.get('alt') is None: errs.append((rel,'image_alt'))
        src=img.get('src','')
        if src.startswith('/') and not (ROOT/src.lstrip('/')).exists(): errs.append((rel,'missing_asset',src))
    for source in s.find_all('source'):
        src=source.get('src','')
        if src.startswith('/') and not (ROOT/src.lstrip('/')).exists(): errs.append((rel,'missing_media',src))
    for a in s.find_all('a',href=True):
        href=a['href']; u=urlsplit(href)
        if u.scheme or href.startswith(('mailto:','tel:')): continue
        if not u.path: continue
        if u.path.startswith('/'):
            t=ROOT/u.path.lstrip('/')
            if u.path.endswith('/'): t=t/'index.html'
            elif t.is_dir(): t=t/'index.html'
            if not t.exists(): errs.append((rel,'broken_link',href)); continue
            if u.fragment and t.suffix=='.html':
                ts=BeautifulSoup(t.read_text(encoding='utf-8'),'html.parser')
                if not ts.find(id=u.fragment): warns.append((rel,'missing_anchor',href))
# Hreflang paired existence
for rel,(fp,s) in docs.items():
    if rel=='/404.html': continue
    for link in s.find_all('link',rel='alternate'):
        href=link.get('href','')
        if href.startswith('https://soyorica.github.io'):
            path=href.removeprefix('https://soyorica.github.io') or '/'
            t=ROOT/path.lstrip('/')
            if path.endswith('/'): t=t/'index.html'
            if not t.exists(): errs.append((rel,'missing_hreflang_target',href))
print(f'HTML={len(docs)} ERRORS={len(errs)} WARNINGS={len(warns)}')
for x in errs: print('ERR',x)
for x in warns: print('WARN',x)
raise SystemExit(1 if errs else 0)
