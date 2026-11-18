#!/usr/bin/env python3
"""Validación mínima de Pucón Creativo para GitHub Pages."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import json
import re

ROOT=Path(__file__).resolve().parents[1]
required=[
  "index.html","noticia.html",
  "assets/logo-pucon-creativo.png","assets/banner-pucon-creativo.jpg",
  "assets/logo-reino-fungi.png","assets/experiencia-v2.css",
  "content/sitio.json","content/agenda.json","content/noticias.json",
  ".pages.yml","robots.txt","sitemap.xml"
]
for filename in required:
    path=ROOT/filename
    assert path.is_file(),f"Falta {filename}"
    if path.suffix in {'.png','.jpg'}:
        assert path.stat().st_size>1000,f"Imagen vacía: {filename}"

if (ROOT/'CNAME').exists():
    assert (ROOT/'CNAME').read_text(encoding='utf8').strip()=='puconcreativo.cl'

for name in ("sitio.json","agenda.json","noticias.json"):
    with (ROOT/"content"/name).open(encoding="utf8") as handle:
        data=json.load(handle)
    if name!="sitio.json":
        assert isinstance(data,list),f"{name} debe ser una lista"

html=(ROOT/"index.html").read_text(encoding="utf8")
for section in ("inicio","mapeo","red","agenda","actualidad"):
    assert f'id="{section}"' in html,f"Falta sección {section}"
assert '352 respuestas' in html,f"Revisar denominador del mapeo"
assert 'data-report-link' in html,"Falta acceso al informe fuente"
assert 'assets/experiencia-v2.css' in html,"Falta hoja de estilo principal"

class AuditHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids=[]
        self.fragments=[]
        self.local_resources=[]
    def handle_starttag(self,tag,attrs):
        for key,value in attrs:
            if key=="id" and value:self.ids.append(value)
            if key=="href" and value and value.startswith("#"):
                self.fragments.append(value[1:])
            if key in ("src","href") and value and value.startswith("assets/"):
                self.local_resources.append(value)
p=AuditHTML()
p.feed(html)
assert len(p.ids)==len(set(p.ids)),"IDs HTML repetidos"
assert set(p.fragments)<=set(p.ids),f"Anclas no encontradas: {set(p.fragments)-set(p.ids)}"
for path in p.local_resources:
    assert (ROOT/path).exists(),f"Recurso local inexistente: {path}"
for section in ('id="agenda"','id="actualidad"'):
    assert section in html
assert 'hidden' in html,"Secciones editoriales vacías deben iniciar ocultas"

site=json.loads((ROOT/"content"/"sitio.json").read_text(encoding="utf8"))
assert site.get("informe","").startswith("https://"),"Enlace fuente inválido"
assert (ROOT/"robots.txt").read_text(encoding="utf8").find("sitemap.xml")!=-1
print("✓ Estructura editorial, anclas, recursos, contenidos y dominio verificados.")
