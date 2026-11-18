# Pucón Creativo — Sitio web y laboratorio editorial

**Sitio público:** https://puconcreativo.cl/

**Repositorio:** `festreinofungi-cmd/pucon-creativo-lab`

## Alcance
Pucón Creativo es una plataforma territorial de información y articulación para las economías creativas de Pucón. Su infraestructura web está alojada en GitHub Pages con dominio personalizado. La edición de diseño y de contenidos debe pasar por revisión antes de publicarse.

## Publicación y ramas
- `main`: versión pública servida por GitHub Pages desde `/ (root)`.
- `CNAME`: `puconcreativo.cl`, obligatorio para el dominio personalizado.
- `diseno/...`: propuestas de diseño y experiencia revisables por pull request, sin efecto público hasta integrar a `main`.
- DNS: administrado en Cloudflare; el dominio permanece registrado en NIC Chile. No se deben alterar los registros DNS desde este repositorio.

## Arquitectura de contenidos
- `index.html`: portada, síntesis del mapeo y presentación de la iniciativa. Agenda y actualidad se muestran únicamente con registros publicados.
- `noticia.html`: ficha pública para noticias aprobadas.
- `content/sitio.json`: introducción, contacto oficial, Instagram e informe.
- `content/agenda.json`: actividades editables, publicadas solo con `publicado: true`.
- `content/noticias.json`: noticias editables, publicadas solo con `publicado: true`.
- `.pages.yml`: esquema editorial preparado para un futuro CMS; no implica que exista un panel activo.

## Datos y criterios editoriales
- El mapeo actualmente visible corresponde a **352 respuestas** del informe exploratorio original. No confundir con una base posterior de formulario, ni presentar como censo de todas las iniciativas.
- No publicar noticias, actividades o funciones de participación que no estén verificadas.
- No divulgar datos personales o fichas identificables del mapeo sin consentimiento.
- Las definiciones de gobernanza deben corresponder a acuerdos documentados.
- El informe del mapeo figura enlazado en el sitio: https://drive.google.com/file/d/1N3PSCy8HWKX1rpr0u7PnchMHRvWD5v2Q/view

## Pruebas
La validación estructural se realiza con:

```sh
python3 scripts/validar.py
```

Para revisar la carga de archivos JSON localmente:

```sh
python3 -m http.server 8080
```

Y abrir `http://localhost:8080`.

## Diseño y criterio editorial
La portada prioriza una propuesta clara, tres hallazgos respaldados por el mapeo y el papel de la iniciativa. La lectura profunda se ofrece mediante el informe completo; se evitan secciones vacías y textos redundantes. 

Se conservan como base los activos oficiales de Pucón Creativo. Festival Reino Fungi aparece como antecedente de articulación, no como marca principal del sitio. El archivo `docs/BASE-DISENO.md` documenta el punto de partida y `docs/EVOLUCION-WEB-2026.md` describe la iteración de mejora propuesta.

## Pendientes estratégicos
Validar contacto institucional, identidad final, contenidos de agenda y actualidad, esquema real de gobernanza y protocolo para incorporar fichas públicas de iniciativas creativas.
