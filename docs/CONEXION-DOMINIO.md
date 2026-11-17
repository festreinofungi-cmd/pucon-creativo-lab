# Conexión de puconcreativo.cl a GitHub Pages

Esta rama PREPARA el cambio. La rama principal sigue sirviendo la URL de pruebas mientras el DNS no esté verificado.

## Configuración DNS requerida en proveedor DNS actual

| Tipo | Host | Valor |
| --- | --- | --- |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | festreinofungi-cmd.github.io |

* Mantener sin cambio registros MX/TXT (SPF/DKIM/DMARC), otros registros de correo y NS existentes.
* Verificar el proveedor que controla la zona DNS antes de modificar registros.
* Evitar A/AAAA o CNAME viejos que entren en conflicto; documentar y comprobar antes de retirarlos.
* No configurar un redirect externo a github.io.

## Secuencia

1. Confirmar los servidores NS activos y respaldar la zona DNS (MX, TXT, A, CNAME, CAA, etc.).
2. En el proveedor DNS actual, actualizar solo los registros de web según la tabla, sin tocar correo ni NS.
3. Verificar que los registros públicos resuelven correctamente.
4. Integrar `CNAME` a la rama `main`; GitHub Pages tomará el dominio `puconcreativo.cl`.
5. Verificar `https://puconcreativo.cl` y `https://www.puconcreativo.cl`, redirección consistente, HTTPS y recursos locales.
6. Confirmar que correos del dominio siguen funcionando.

Fuente de configuración: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
