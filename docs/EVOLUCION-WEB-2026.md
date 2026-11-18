# Pucón Creativo — Evolución de experiencia web (noviembre de 2026)

## Propósito
Convertir el sitio público en una puerta de acceso a información territorial, oportunidades y colaboración. La publicación debe ser útil para iniciativas creativas, públicos, organizaciones e instituciones de la comuna.

## Alcance de esta primera iteración (rama de diseño)
- **No se modifica `main` ni el dominio público** hasta revisión y aprobación del pull request.
- Se conserva la marca gráfica y los colores de partida. Se agrega una capa editorial y responsiva.
- La portada ofrece tres rutas directas: ecosistema, mapeo y articulación.
- El mapeo señala su alcance metodológico junto a las cifras, y no solo en la letra pequeña del informe.
- Se mejora la accesibilidad: enlace «saltar al contenido», navegación por teclado de pestañas, controles del menú móvil, foco visible y ocultamiento coherente de paneles.
- Se añaden metadatos para compartir, favicon, URL canónica y estilo consistente.
- Los mensajes sin contenidos editorialmente aprobados se presentan como secciones en preparación, sin actividades o noticias inventadas.

## Pendientes editoriales imprescindibles antes de una versión pública completa
1. **Participación funcional:** aprobar correo de contacto institucional y perfiles oficiales. Hoy `content/sitio.json` tiene ambos campos vacíos; nunca se sustituirán por datos personales.
2. **Agenda:** integrar solo actividades verificadas y con datos de fecha, lugar y organizador comprobados.
3. **Actualidad:** publicar notas con antecedentes, fuente, imágenes autorizadas y revisión editorial.
4. **Gobernanza:** definir estructura y organizaciones efectivamente formalizadas. Los textos conceptuales no representan órganos ya acordados.
5. **Datos y directorio:** respetar el corte de 352 respuestas y su carácter voluntario. Para exponer fichas nominativas se requiere consentimiento y protocolo de actualización.
6. **Identidad:** validar sistema visual, créditos y tratamiento de marcas secundarias con el equipo antes de consolidar versión final.
7. **Mantenimiento:** asignar responsables de agenda, noticias, contactos, calidad y respaldos de archivos.

## Criterios de revisión de esta rama
- Comprobar portada, navegación, sección de datos y enlaces de informe en móvil, tablet y escritorio.
- Verificar foco de teclado, Escape en menú, flechas y Home/End en pestañas.
- Validar que los JSON vacíos produzcan estados honestos, sin errores ni información ficticia.
- Confirmar carga relativa de activos desde `/`, URL canónica del dominio y compatibilidad con GitHub Pages.
- Aprobar narrativa antes de integrar en `main`.

## Siguiente etapa recomendada
Con la identidad y los canales institucionales validados, desarrollar una agenda realmente activa, recursos descargables, un directorio voluntario de iniciativas y fichas públicas con buscador y filtros, junto a una gobernanza editorial explícita. El diseño debe responder a esas funciones, no anteponerse a ellas.
