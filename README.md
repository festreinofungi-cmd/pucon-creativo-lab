# Pucón Creativo — Laboratorio de diseño web

Este repositorio es el **laboratorio de diseño y prototipado**, no el sitio público definitivo de Pucón Creativo.

## Estado

- Versión base: prototipo visual con identidad gráfica proporcionada para Pucón Creativo.
- Secciones: portada, presentación, ecosistema, mapeo, agenda, gobernanza, noticias y participación.
- Datos del mapeo: **352 respuestas** y porcentajes publicados en el resumen/informe del mapeo. No confundir con la base de formularios actualizada posteriormente.
- Noticias y agenda: estructura preparada, **sin publicaciones inventadas** (`content/agenda.json`, `content/noticias.json`).
- Sitio público `puconcreativo.cl`: **no conectado**. No hay archivo `CNAME` ni cambio de DNS.
- Directorio de documentos: reservado para entregables públicos aprobados.

## Cómo ver el prototipo

### Abrir localmente

Para visualizar también las listas de noticias y agenda (que usan `fetch()`), iniciar un servidor estático en la carpeta raíz:

```sh
python3 -m http.server 8080
```

Luego abrir `http://localhost:8080`.

### Vista de prueba con GitHub Pages

Cuando decidamos activar la vista de laboratorio, ir a `Settings → Pages → Build and deployment`, elegir `Deploy from a branch`, rama `main` y carpeta `/ (root)`. La URL de pruebas será:

**https://festreinofungi-cmd.github.io/pucon-creativo-lab/**

Esta es solo una dirección de pruebas independiente del dominio oficial. Cada actualización de la rama `main` se publicará automáticamente en Pages una vez habilitado.

## Edición de diseño desde ChatGPT / GitHub

Los cambios de diseño se trabajarán en ramas `diseno/...`, se revisarán mediante pull requests y se integrarán en `main` una vez aprobados. Se recomienda verificar móvil y escritorio antes de integrar.

## Edición de contenido (preparada, no activada)

El archivo `.pages.yml` define un esquema futuro para Pages CMS. Durante la etapa de diseño, los campos y el funcionamiento editorial pueden modificarse.

## Fuentes y cuidados

- Informe de mapeo: https://drive.google.com/file/d/1N3PSCy8HWKX1rpr0u7PnchMHRvWD5v2Q/view
- Resultados exploratorios con convocatoria voluntaria; no constituyen un censo de todas las iniciativas de Pucón.
- **No** subir datos personales de las respuestas del mapeo a este repositorio público.
- Imágenes de identidad: entregadas para este proyecto por el equipo.
- No conectar `puconcreativo.cl` ni configurar DNS hasta tener una versión aprobada.

## Pendientes de diseño

1. Afinar dirección de arte, proporciones y composición de la portada.
2. Revisar toda la experiencia móvil, navegación y accesibilidad.
3. Validar narrativa institucional, gobernanza y llamados a participar.
4. Decidir visualizaciones y profundidad de los datos del mapeo.
5. Diseñar fichas de noticias y actividades y el futuro directorio.
6. Aprobar textos, créditos, recursos gráficos y documentos públicos antes del lanzamiento.
