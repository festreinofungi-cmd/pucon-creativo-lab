# Pucón Creativo — dirección editorial simplificada

## Criterio principal
El sitio debe comunicar una propuesta de valor, aportar evidencia y explicar la acción de la iniciativa. No debe reproducir un informe institucional completo en la portada.

## Estructura pública de esta iteración
1. **Portada:** «El territorio también crea.» Un texto de una oración y dos accesos: mapeo e iniciativa.
2. **Mapeo:** tres hallazgos de mayor utilidad para comprender las necesidades del ecosistema, respaldados por el informe de 352 respuestas. Enlace al informe íntegro.
3. **La iniciativa:** dos párrafos que explican su rol en términos de información, articulación y desarrollo territorial.

## Qué se eliminó de la página principal
- Doble navegación en tarjetas y titulares que repetían el propósito.
- Bloques separados de «qué es», «ecosistema» y misión/visión provisionales.
- Despliegue íntegro de 4 gráficos con numerosas categorías y notas repetidas.
- Sección de gobernanza con esquema aún no aprobado.
- Pantallas vacías de agenda, actualidad y participación, que ocupaban espacio sin entregar un servicio.

La agenda y actualidad se conservan en la arquitectura del código, pero solo aparecen cuando existe material marcado como `publicado: true`. Los canales de contacto no se muestran mientras permanezcan vacíos en `content/sitio.json`.

## Principios de redacción
- Una idea por bloque, sin adjetivación institucional innecesaria.
- Priorizar conceptos concretos: información territorial, vínculos entre iniciativas, prioridades del mapeo.
- Evitar duplicar «reconocer, conectar y proyectar» o «encuentro, información y colaboración» en cada sección.
- No presentar como acordada una estructura de gobernanza conceptual.
- No inventar actividades, noticias, contactos, ni convertir una muestra voluntaria en censo.

## Datos destacados
- **68,4 %:** no participa en redes.
- **52 %:** indica difusión y visibilidad como prioridad.
- **48,6 %:** prioriza nuevos públicos o clientes.
- **352:** tamaño de la muestra exploratoria; no se exhibe como indicador de cobertura comunal.

## Identidad y publicación
Se conserva el logotipo, la pieza gráfica territorial y la paleta base azul/rosa, con mayor espacio en blanco y menor densidad de componentes. Todo permanece en la rama `diseno/evolucion-plataforma-2026`; la rama pública `main` no se altera hasta aprobar el PR.

## Pendientes para una etapa funcional
Validar canal oficial de contacto, actividades reales, noticias y acuerdos de gobernanza. Un directorio de iniciativas requiere consentimiento explícito y protocolo de actualización. El análisis más completo debe vivir en documentos de consulta o páginas secundarias, no sobrecargar la portada.

## Revisión requerida
Comprobar funcionamiento en móvil/escritorio, enlaces de ancla, carga de activos, publicación condicional de contenidos, accesibilidad del menú y diseño antes de integrar los cambios.
