# Pucón Creativo — sistema web con identidad del proyecto

**Estado:** especificación para mockup y revisión. No sustituye el manual de marca aprobado ni autoriza publicar cambios en `main`.

## Fuentes verificadas
- `assets/logo-pucon-creativo.png`: logotipo original con trazos topográficos y denominación «Pucón Creativo / Red de Economías Creativas».
- `assets/banner-pucon-creativo.jpg`: gráfica de portada del volcán Rukapillán con logotipo y firma ministerial. **Debe conservarse como banner destacado.**
- FUP «Creación Red de Territorio Creativo Pucón», folio 800023, postulado a «Economía Creativa / Creación y Fortalecimiento de la Red de Gestión en el Ecosistema Creativo 2025 / Creación».
- Documento «MV01_Lineamientos estratégicos de comunicación y diseño – Pucón Creativo», capítulo 6 y 7: territorio habitado, cartografía, curvas de nivel, nodos, tramas, rutas y sistema visual.
- «MV02_Plan de Comunicaciones Pucón Creativo»: firma editorial del financiamiento.
- Instagram difundido públicamente: `@pucon.creativo`. Correo usado en convocatoria pública: `redpuconcreativo@gmail.com` (validar vigencia).

## Reglas visuales no negociables
1. Usar el archivo del logotipo **sin redibujarlo ni alterarlo**; mantener área de respeto y legibilidad.
2. Mantener el **banner original del volcán** visible en la portada, sin recorte que elimine los logos o firma institucional. Optimizar su visualización en móvil sin borrar créditos.
3. Sistema de recursos gráficos subordinados a la identidad: trazos concéntricos, rutas, líneas topográficas y nodos. No generar símbolos ajenos que compitan con la marca. Diseñar iconos que compartan grosor, extremos y geometría.
4. Emplear azul profundo y rosa del sistema real, fondos cálidos y fotografía documental; no sustituir fotografías de actividades por una nueva gráfica sintética.
5. El video y las fotografías son pruebas de actividad territorial. Mostrarlos solo cuando existan archivos aprobados, con créditos y permisos.
6. Una idea editorial por pantalla y enlaces a niveles de profundidad. No llenar la portada con misión/visión, organigrama provisional y datos repetidos.

## Arquitectura priorizada de homepage
- **Cabecera:** logotipo original, navegación sobria («Mapeo», «La Red», «Actualidad», «Contacto») y enlace visible a Instagram.
- **Portada:** banner oficial + texto de propósito de una frase + una acción principal.
- **Mapeo:** máximo tres hallazgos relevantes, con fuente, alcance y acceso al informe completo.
- **En movimiento:** un clip principal o historia visual destacada; ocultar mientras no haya medios aprobados. Evitar carruseles automáticos.
- **Contacto:** correo público y formulario con Nombre, Correo, Motivo (opcional) y Mensaje; consentimiento y aviso básico de privacidad; captación y protección antispam.
- **Pie institucional:** logo Pucón Creativo, bloque «Alianzas y red» con logos de Red Nacional de Territorios Creativos, CRTIC Pucón, Municipalidad de Pucón y Festival Reino Fungi; bloque separado y de jerarquía diferenciada para la firma del Ministerio.

## Contacto e integración
- Instagram: vínculo directo a `https://www.instagram.com/pucon.creativo/`. Se puede añadir una selección editorial de tres publicaciones o clips aprobados, pero **no** un feed automático invasivo por defecto.
- Correo público reportado en fuentes externas: `redpuconcreativo@gmail.com`. Antes de configurarlo en producción, confirmar con el equipo que sigue siendo la casilla operativa.
- GitHub Pages es estático: un formulario funcional necesita endpoint y validación en servidor. Alternativas: un receptor basado en Cloudflare Workers o un formulario Google administrado por la organización. No desplegar un formulario que simula envío ni almacenar datos de participantes en GitHub público.
- Media: almacenar solo fotos y clips con derechos aclarados, formato web, descripciones alternativas y opción reproducir voluntaria, sin autoplay con sonido.

## Identidad de financiamiento: punto a verificar
- FUP folio 800023: Convocatoria **2025**.
- Plan de comunicaciones indica literalmente: «Proyecto financiado por la Convocatoria 2025 para la Creación y Fortalecimiento de Redes de Gestión en el Ecosistema Creativo, del Ministerio de las Culturas, las Artes y el Patrimonio».
- La leyenda visible en el **banner actual** menciona «Redes de Gestión en el Ecosistema Creativo 2026». Existe discrepancia año/nombre respecto del FUP y del plan. **No modificar la pieza sin comprobar el convenio, resolución, archivo de marca ministerial y piezas ya aprobadas.**
- La firma ministerial requiere el logo oficial y un bloque institucional diferenciado del grupo de aliados. No usar el logo de un tercero como sustituto de financiador.

## Revisión y criterios de aceptación
- Pie institucional con proporción, área de respeto, lectura en móvil y separación entre «alianzas» y «financiamiento».
- Banner sin cortes sobre créditos en 320–1440 px.
- Iconografía 1, 2 o 3 signos auxiliares derivados del lenguaje topográfico; no iconos decorativos repetidos.
- Portada con <= 3 acciones visibles antes del primer scroll.
- Formulario con validación, confirmación real del servidor, política de datos y antispam antes de integrarlo a `main`.
- En `main` no se modifica nada hasta validar los insumos oficiales y revisar visualmente el prototipo.
