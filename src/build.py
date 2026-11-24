#!/usr/bin/env python3
"""Erzeugt die statische Website in drei Sprachen. Aufruf: python3 src/build.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content_de import C as DE  # noqa: E402
from content_es import C as ES  # noqa: E402
from content_en import C as EN  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = [DE, ES, EN]
PAGES = ['home', 'care', 'clean', 'arrival', 'property', 'process', 'about', 'region', 'faq',
         'contact', 'imprint', 'privacy']
SERVICES = ['care', 'clean', 'arrival', 'property']
IMG = {'care': 'pool.jpg', 'clean': 'wohnraum.jpg', 'arrival': 'eingang.jpg', 'property': 'schluessel.jpg'}

PHONE_SHOW = '+34 643 202 485'
PHONE = '+34643202485'
WA = '34643202485'
MAIL = 'pfadt-propertycaremallorca@outlook.de'
HAS_PORTRAIT = os.path.exists(os.path.join(ROOT, 'assets', 'img', 'leoni.jpg'))

WA_ICON = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
           'stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.5 8.5 0 0 1-12.6 7.400L3 20.500l1.700-5.100'
           'A8.5 8.5 0 1 1 21 11.500Z"/><path d="M8.500 10.500h7M8.500 13.500h4.500"/></svg>')


def url(c, key):
    return c['slugs'][key] + '.html'


def wa_link(c):
    from urllib.parse import quote
    return 'https://wa.me/%s?text=%s' % (WA, quote(c['ui']['wa_text']))


def head(c, key):
    m = c['meta'][key]
    alts = ''.join('<link rel="alternate" hreflang="%s" href="../%s/%s">\n' % (l['code'], l['code'], url(l, key))
                   for l in LANGS)
    return '''<!doctype html>
<html lang="%s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
%s<link rel="icon" href="../assets/favicon.png" type="image/png">
<link rel="preload" href="../assets/fonts/cormorant-500.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<a class="skip" href="#inhalt">%s</a>
''' % (c['code'], m[0], m[1], alts, c['ui']['skip'])


def brand(c):
    return ('<a class="brand" href="index.html"><img src="../assets/img/pfadt-logo.webp" '
            'width="876" height="716" alt="PFADT Property Care Mallorca"></a>')


def header(c, key):
    n = c['nav']

    def item(k, label):
        cur = ' aria-current="page"' if k == key else ''
        return '<li><a href="%s"%s>%s</a></li>' % (url(c, k), cur, label)

    subs = ''.join(item(s, c['services'][s]['title']) for s in SERVICES)
    langs = ''.join('<a href="../%s/%s" lang="%s" hreflang="%s"%s title="%s">%s</a>' % (
        l['code'], url(l, key), l['code'], l['code'], ' aria-current="true"' if l is c else '', l['name'],
        l['code'].upper()) for l in LANGS)
    return '''<header class="site-header"><div class="wrap">
<svg width="0" height="0" aria-hidden="true" focusable="false" style="position:absolute"><defs>
<filter id="pfadt-ink" color-interpolation-filters="sRGB">
<feColorMatrix type="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 -4 3.84 0"/>
</filter></defs></svg>
%s
<nav aria-label="%s"><ul class="nav" id="nav">
<li class="has-sub"><button class="sub-toggle" type="button" aria-haspopup="true">%s</button><ul class="sub">%s</ul></li>
%s%s%s%s%s
</ul></nav>
<div class="head-right">
<div class="langs" aria-label="%s">%s</div>
<a class="btn btn-gold head-cta" href="%s">%s</a>
<button class="menu-btn" type="button" aria-controls="nav" aria-expanded="false" aria-label="%s"><span></span></button>
</div>
</div></header>
<main id="inhalt">
''' % (brand(c), n['main'], n['services'], subs, item('process', n['process']), item('about', n['about']),
       item('region', n['region']), item('faq', n['faq']), item('contact', n['contact']), n['lang'], langs,
       url(c, 'contact'), n['cta'], n['menu'])


def footer(c):
    u, n = c['ui'], c['nav']
    svc = ''.join('<li><a href="%s">%s</a></li>' % (url(c, s), c['services'][s]['title']) for s in SERVICES)
    more = ''.join('<li><a href="%s">%s</a></li>' % (url(c, k), n[k]) for k in ['process', 'about', 'region', 'faq'])
    return '''</main>
<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div>%s<p>%s</p></div>
<div><h4>%s</h4><ul>%s</ul></div>
<div><h4>%s</h4><ul>%s</ul></div>
<div><h4>%s</h4><ul>
<li><a href="tel:%s">%s</a></li>
<li><a href="%s" rel="noopener">WhatsApp</a></li>
<li><a href="mailto:%s">%s</a></li>
<li>Santanyí, Mallorca</li></ul></div>
</div>
<div class="foot-bottom"><span>© 2026 PFADT Property Care Mallorca · <a href="%s">%s</a> · <a href="%s">%s</a></span>
</div>
</div></footer>
<a class="wa-float" href="%s" rel="noopener" aria-label="%s">%s</a>
<script src="../assets/site.js" defer></script>
</body>
</html>
''' % (brand(c), u['foot_text'], n['services'], svc, u['foot_more'], more, n['contact'], PHONE, PHONE_SHOW,
       wa_link(c), MAIL, u['mail_short'], url(c, 'imprint'), u['imprint'], url(c, 'privacy'), u['privacy'],
       wa_link(c), u['wa'], WA_ICON)


def buttons(c, light=False, center=False):
    u = c['ui']
    second = 'btn-light' if light else 'btn-wa'
    return ('<div class="btns"><a class="btn btn-gold" href="%s">%s</a>'
            '<a class="btn %s" href="%s" rel="noopener">%s%s</a></div>') % (
        url(c, 'contact'), u['offer'], second, wa_link(c), WA_ICON, u['wa'])


def cta(c):
    x = c['cta']
    return ('<section class="cta"><div class="wrap"><h2>%s</h2><p>%s</p>'
            '<div class="center">%s</div></div></section>') % (x['h'], x['p'], buttons(c, light=True))


def cards(c, keys, cls=''):
    out = ''
    for s in keys:
        v = c['services'][s]
        out += ('<a class="card" href="%s"><img src="../assets/img/%s" alt="" loading="lazy" width="800" height="600">'
                '<div><h3>%s</h3><p>%s</p><span class="more">%s</span></div></a>') % (
            url(c, s), IMG[s], v['title'], v['short'], c['ui']['more'])
    return '<div class="cards %s">%s</div>' % (cls, out)


def steps(c, light=False):
    return '<ol class="steps%s">%s</ol>' % (' light' if light else '', ''.join(
        '<li><h3>%s</h3><p>%s</p></li>' % (t, p) for t, p in c['process']['steps']))


def portrait(c):
    if HAS_PORTRAIT:
        return '<img src="../assets/img/leoni.jpg" alt="Leoni Pfadt" loading="lazy">'
    return '<div class="portrait"><b>LP</b><small>%s</small></div>' % c['ui']['portrait']


def faq_block(c, items):
    return '<div class="faq">%s</div>' % ''.join(
        '<details><summary>%s</summary><p>%s</p></details>' % (q, a) for q, a in items)


def paras(ps):
    return ''.join('<p>%s</p>' % p for p in ps)


def page_hero(c, eyebrow, h1, lead, img=None, crumb=None):
    crumb_html = ''
    if crumb:
        crumb_html = '<p class="crumb"><a href="index.html">%s</a> / %s</p>' % (c['ui']['home'], crumb)
    media = '<img src="../assets/img/%s" alt="" width="900" height="675">' % img if img else ''
    return ('<div class="page-hero%s"><div class="wrap"><div>%s<span class="eyebrow">%s</span><h1>%s</h1>'
            '<p class="lead">%s</p></div>%s</div></div>') % ('' if img else ' plain', crumb_html, eyebrow, h1, lead, media)


def p_home(c):
    h, u = c['home'], c['ui']
    promises = ''.join('<div class="promise"><span class="num">%s</span><h3>%s</h3><p>%s</p></div>' % (
        '0%d' % (i + 1), t, p) for i, (t, p) in enumerate(h['promises']))
    voices = ''.join('<figure class="voice"><span class="tag">%s</span><p>%s</p><cite>%s</cite></figure>' % (
        h['voice_tag'], q, who) for q, who in h['voices'])
    return '''<div class="hero"><img src="../assets/img/hero.jpg" alt="" width="2000" height="1333" fetchpriority="high">
<div class="wrap"><span class="eyebrow">%s</span><h1>%s</h1><p class="lead">%s</p>%s</div></div>
<div class="facts"><div class="wrap"><ul>%s</ul></div></div>

<section><div class="wrap split">
<div><span class="eyebrow">%s</span><h2>%s</h2>%s</div>
<div class="media"><img src="../assets/img/steinhaus.jpg" alt="" loading="lazy" width="900" height="1125"></div>
</div></section>

<section class="bg-sand"><div class="wrap">
<div class="sec-head center"><span class="eyebrow">%s</span><h2>%s</h2></div>
<div class="promises">%s</div></div></section>

<section><div class="wrap">
<div class="sec-head"><span class="eyebrow">%s</span><h2>%s</h2><p class="lead">%s</p></div>
%s</div></section>

<section class="bg-ink"><div class="wrap">
<div class="sec-head"><span class="eyebrow">%s</span><h2>%s</h2><p class="lead">%s</p></div>
%s
<div class="btns"><a class="btn btn-light" href="%s">%s</a></div></div></section>

<section><div class="wrap split">
<div class="media">%s</div>
<div><span class="eyebrow">%s</span><h2>%s</h2>%s
<div class="btns"><a class="btn btn-line" href="%s">%s</a></div></div>
</div></section>

<section class="bg-sand"><div class="wrap">
<div class="sec-head center"><span class="eyebrow">%s</span><h2>%s</h2><p class="sample-note">%s</p></div>
<div class="voices">%s</div></div></section>

<section><div class="wrap narrow">
<div class="sec-head"><span class="eyebrow">%s</span><h2>%s</h2></div>
%s
<div class="btns"><a class="btn btn-line" href="%s">%s</a></div></div></section>
%s''' % (
        h['eyebrow'], h['h1'], h['sub'], buttons(c, light=True),
        ''.join('<li>%s</li>' % f for f in h['facts']),
        h['worry_eyebrow'], h['worry_h'], paras(h['worry_p']),
        h['promise_eyebrow'], h['promise_h'], promises,
        c['nav']['services'], h['services_h'], h['services_lead'], cards(c, SERVICES),
        c['nav']['process'], c['process']['h'], c['process']['lead'], steps(c), url(c, 'process'), h['process_more'],
        portrait(c), c['nav']['about'], h['about_h'], paras(h['about_p']), url(c, 'about'), h['about_more'],
        h['voices_eyebrow'], h['voices_h'], h['voices_note'], voices,
        c['nav']['faq'], h['faq_h'], faq_block(c, c['faq']['items'][:4]), url(c, 'faq'), h['faq_more'],
        cta(c))


def p_service(c, key):
    v, u = c['services'][key], c['ui']
    others = [s for s in SERVICES if s != key]
    return '''%s
<section><div class="wrap split wide-img">
<div><span class="eyebrow">%s</span><h2>%s</h2><ul class="checks">%s</ul></div>
<div><span class="eyebrow">%s</span><h2>%s</h2><p>%s</p>
<h3>%s</h3><p>%s</p>%s</div>
</div></section>
<section class="bg-sand"><div class="wrap">
<div class="sec-head"><span class="eyebrow">%s</span><h2>%s</h2></div>%s</div></section>
%s''' % (
        page_hero(c, c['nav']['services'], v['title'], v['lead'], IMG[key], v['title']),
        u['inc_eyebrow'], u['inc_h'], ''.join('<li>%s</li>' % i for i in v['includes']),
        u['how_eyebrow'], u['how_h'], v['how'], u['who_h'], v['who'], buttons(c),
        u['other_eyebrow'], u['other_h'], cards(c, others, 'three'), cta(c))


def p_process(c):
    p = c['process']
    return '''%s
<section><div class="wrap">%s</div></section>
<section class="bg-sand"><div class="wrap split wide-img">
<div><span class="eyebrow">%s</span><h2>%s</h2><ul class="checks">%s</ul></div>
<div class="media"><img src="../assets/img/pool.jpg" alt="" loading="lazy" width="900" height="675"></div>
</div></section>
%s''' % (page_hero(c, c['nav']['process'], p['h'], p['lead']), steps(c, light=True),
         p['expect_eyebrow'], p['expect_h'], ''.join('<li>%s</li>' % i for i in p['expect']), cta(c))


def p_about(c):
    a = c['about']
    secs = ''.join('<h2>%s</h2>%s' % (h, paras(ps)) for h, ps in a['sections'])
    return '''%s
<section><div class="wrap split">
<div class="media">%s</div>
<div class="prose">%s%s</div>
</div></section>
<section class="bg-sand"><div class="wrap"><blockquote class="quote">%s<footer>Leoni Pfadt</footer></blockquote></div></section>
%s''' % (page_hero(c, c['nav']['about'], a['h'], a['lead']), portrait(c), secs, buttons(c), a['quote'], cta(c))


def p_region(c):
    r = c['region']
    return '''%s
<section><div class="wrap split wide-img">
<div><span class="eyebrow">%s</span><h2>%s</h2>%s<ul class="places">%s</ul></div>
<div class="media"><img src="../assets/img/bucht.jpg" alt="" loading="lazy" width="900" height="675"></div>
</div></section>
<section class="bg-sand"><div class="wrap narrow"><span class="eyebrow">%s</span><h2>%s</h2>%s%s</div></section>
%s''' % (page_hero(c, c['nav']['region'], r['h'], r['lead'], 'cala.jpg'),
         r['area_eyebrow'], r['area_h'], paras(r['area_p']), ''.join('<li>%s</li>' % p for p in r['places']),
         r['why_eyebrow'], r['why_h'], paras(r['why_p']), buttons(c), cta(c))


def p_faq(c):
    f = c['faq']
    return '''%s
<section><div class="wrap narrow">%s</div></section>
%s''' % (page_hero(c, c['nav']['faq'], f['h'], f['lead']), faq_block(c, f['items']), cta(c))


def p_contact(c):
    k, u = c['contact'], c['ui']
    opts = ''.join('<option>%s</option>' % c['services'][s]['title'] for s in SERVICES)
    return '''%s
<section><div class="wrap contact-grid">
<div><ul class="contact-list">
<li><small>%s</small><a href="tel:%s">%s</a></li>
<li><small>WhatsApp</small><a href="%s" rel="noopener">%s</a></li>
<li><small>%s</small><a href="mailto:%s">%s</a></li>
<li><small>%s</small><a href="%s">Santanyí, Mallorca</a></li>
</ul></div>
<form class="box" data-contact data-wa="%s" data-mail="%s" data-subject="%s" data-intro="%s">
<h2>%s</h2>
<label>%s<input type="text" name="name" data-label="%s" required autocomplete="name"></label>
<label>%s<input type="text" name="reach" data-label="%s" required></label>
<label>%s<input type="text" name="place" data-label="%s"></label>
<label>%s<select name="service" data-label="%s"><option value="">%s</option>%s<option>%s</option></select></label>
<label>%s<textarea name="msg" data-label="%s"></textarea></label>
<div class="btns" style="margin-top:0"><button class="btn btn-wa" type="submit" value="wa">%s%s</button>
<button class="btn btn-line" type="submit" value="mail">%s</button></div>
<p class="form-note">%s <a href="%s">%s</a></p>
</form>
</div></section>''' % (
        page_hero(c, c['nav']['contact'], k['h'], k['lead']),
        k['phone'], PHONE, PHONE_SHOW, wa_link(c), k['wa_line'], k['mail'], MAIL, MAIL, k['area'], url(c, 'region'),
        WA, MAIL, k['subject'], k['intro'], k['form_h'],
        k['f_name'], k['f_name'], k['f_reach'], k['f_reach'], k['f_place'], k['f_place'],
        k['f_service'], k['f_service'], k['f_choose'], opts, k['f_several'], k['f_msg'], k['f_msg'],
        WA_ICON, k['send_wa'], k['send_mail'], k['note'], url(c, 'privacy'), u['privacy'])


def p_legal(c, key):
    title, ps = c['legal'][key]
    extra = ''
    if key == 'imprint':
        extra = (
            '<p><strong>PFADT Property Care Mallorca</strong><br>%s: Leoni Enya Pfadt<br>'
            'Carrer es Morras 1A<br>07659 Cala Figuera<br>Mallorca, Islas Baleares, España<br>'
            'NIF: Z1536656P<br><a href="mailto:%s">%s</a><br><a href="tel:%s">%s</a></p>'
        ) % (
            c['legal']['owner'], MAIL, MAIL, PHONE, PHONE_SHOW)
    content = paras(ps) if key == 'imprint' else ''.join(
        '<h2>%s</h2><p>%s</p>' % (heading, paragraph) for heading, paragraph in ps)
    return '%s<section><div class="wrap narrow">%s%s</div></section>' % (
        page_hero(c, c['ui']['legal'], title, ''), extra, content)


def render(c, key):
    if key == 'home':
        body = p_home(c)
    elif key in SERVICES:
        body = p_service(c, key)
    elif key in ('imprint', 'privacy'):
        body = p_legal(c, key)
    else:
        body = globals()['p_' + key](c)
    return head(c, key) + header(c, key) + body + footer(c)


ROOT_INDEX = '''<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>PFADT Property Care Mallorca</title><link rel="icon" href="assets/favicon.png" type="image/png">
<script>(function(){var l=(navigator.language||'de').slice(0,2).toLowerCase();
location.replace((l==='es'||l==='en'?l:'de')+'/index.html');})();</script>
<noscript><meta http-equiv="refresh" content="0; url=de/index.html"></noscript>
<style>body{font-family:system-ui,sans-serif;background:#fbf8f2;color:#2a2520;display:grid;place-items:center;min-height:100vh;margin:0}
a{color:#876726;margin:0 10px;font-weight:700}</style></head>
<body><p>PFADT Property Care Mallorca<br><br><a href="de/index.html">Deutsch</a><a href="es/index.html">Español</a>
<a href="en/index.html">English</a></p></body></html>
'''

def main():
    count = 0
    for c in LANGS:
        out = os.path.join(ROOT, c['code'])
        os.makedirs(out, exist_ok=True)
        for key in PAGES:
            with open(os.path.join(out, url(c, key)), 'w', encoding='utf-8') as f:
                f.write(render(c, key))
            count += 1
    with open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(ROOT_INDEX)
    print('%d Seiten erzeugt. Porträt vorhanden: %s' % (count, HAS_PORTRAIT))


if __name__ == '__main__':
    main()
