#!/usr/bin/env python3
"""Comprobaciones mínimas para el laboratorio web, sin dependencias externas."""
from pathlib import Path
from html.parser import HTMLParser
import json

ROOT=Path(__file__).resolve().parents[1]
required=["index.html", "noticia.html", "assets/logo-pucon-creativo.png", "assets/banner-pucon-creativo.jpg", "assets/logo-reino-fungi.png", "content/sitio.json", "content/agenda.json", "content/noticias.json", ".pages.yml"]
for filename in required:
    p=ROOT/filename
    assert p.is_file(), f"Falta {filename}"
    if p.suffix in {'.png','.jpg'}: assert p.stat().st_size>1000, f"Imagen vacía: {filename}"
if (ROOT/'CNAME').exists():
    domain = (ROOT/'CNAME').read_text(encoding='utf-8').strip()
    assert domain == 'puconcreativo.cl', f'Dominio personalizado inesperado: {domain}'
for filename in ['sitio.json','agenda.json','noticias.json']:
    with (ROOT/'content'/filename).open(encoding='utf8') as f: json.load(f)
assert isinstance(json.loads((ROOT/'content'/'agenda.json').read_text()),list)
assert isinstance(json.loads((ROOT/'content'/'noticias.json').read_text()),list)
html=(ROOT/'index.html').read_text(encoding='utf8')
for section in ['inicio','somos','ecosistema','mapeo','agenda','gobernanza','actualidad','participa']:
    assert f'id="{section}"' in html, f"Falta sección {section}"
assert '352' in html, 'Verificar la base de mapeo publicada'
class Parser(HTMLParser):
    def error(self,message): raise ValueError(message)
Parser().feed(html)
print('✓ Validaciones básicas superadas. Listo para revisar diseño.')
