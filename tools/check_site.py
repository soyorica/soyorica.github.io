from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re, json
ROOT=Path('/mnt/data/soyorica_site')
htmls=list(ROOT.rglob('*.html'))
errors=[]; warnings=[]; titles={}; descs={}
for fp in htmls:
    rel='/' + fp.relative_to(ROOT).as_posix()
    s=BeautifulSoup(fp.read_text(encoding='utf-8'),'html.parser')
    title=s.title.get_text(strip=True) if s.title else ''
    desc=(s.find('meta',attrs={'name':'description'}) or {}).get('content','') if s.find('meta',attrs={'name':'description'}) else ''
    if not title: errors.append((rel,'missing title'))
    if not desc: errors.append((rel,'missing description'))
    if len(s.find_all('h1'))!=1: errors.append((rel,f'h1 count {len(s.find_all("h1"))}'))
    can=s.find('link',rel='canonical')
    if not can: errors.append((rel,'missing canonical'))
    alts=s.find_all('link',rel='alternate')
    hrs={x.get('hreflang') for x in alts}
    if not {'ja','en','x-default'}.issubset(hrs): errors.append((rel,'hreflang incomplete'))
    for img in s.find_all('img'):
        if img.get('alt') is None: errors.append((rel,'img missing alt'))
        src=img.get('src','')
        if src.startswith('/'):
            target=ROOT/src.lstrip('/')
            if not target.exists(): errors.append((rel,f'missing image {src}'))
    for a in s.find_all('a',href=True):
        href=a['href']
        if href.startswith(('http://','https://','mailto:','#')): continue
        if href.startswith('/'):
            p=href.split('#')[0].split('?')[0]
            if not p: continue
            target=ROOT/p.lstrip('/')
            if p.endswith('/'):
                target=target/'index.html'
            elif target.is_dir():
                target=target/'index.html'
            if not target.exists(): errors.append((rel,f'broken internal link {href}'))
    titles.setdefault(title,[]).append(rel); descs.setdefault(desc,[]).append(rel)
for v,ls in titles.items():
    if v and len(ls)>1: warnings.append(('duplicate title',v,ls))
for v,ls in descs.items():
    if v and len(ls)>1: warnings.append(('duplicate description',v,ls))
# only production pages, excluding wireframe from SEO checks? Wireframe intentionally lacks metadata.
errors=[e for e in errors if not (e[0]=='/wireframe.html' and e[1] in {'missing description','missing canonical','hreflang incomplete'})]
# Contrast utility

def lum(hexv):
    rgb=[int(hexv[i:i+2],16)/255 for i in (1,3,5)]
    def c(x): return x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4
    r,g,b=map(c,rgb); return .2126*r+.7152*g+.0722*b

def cr(a,b):
    x,y=sorted([lum(a),lum(b)],reverse=True); return (x+.05)/(y+.05)
print('HTML_FILES',len(htmls))
print('ERRORS',len(errors))
for e in errors[:100]: print('ERR',e)
print('WARNINGS',len(warnings))
for w in warnings[:20]: print('WARN',w)
print('CONTRAST ink/white',round(cr('#102733','#FFFFFF'),2))
print('CONTRAST muted/paper',round(cr('#5D6B74','#F7F9FA'),2))
print('CONTRAST navy/white',round(cr('#11364F','#FFFFFF'),2))
