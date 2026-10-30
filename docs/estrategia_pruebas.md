# Estrategia de pruebas de API

## Contexto de negocio

Una plataforma de comercio electrónico necesita mostrar productos, facilitar
búsquedas, administrar carritos y controlar el acceso de usuarios. Esta
práctica independiente de QA verifica contratos de respuesta de una API
de demostración que representa esos flujos.

## Objetivo

Detectar discrepancias entre los resultados esperados y los observados al
interactuar con los endpoints de **DummyJSON**. Practicar el análisis de
requisitos, la formulación de aserciones, el diseño de escenarios negativos
y la automatización de pruebas repetibles.

## Alcance

| Módulo | Recursos | Métodos cubiertos |
|---|---|---|
| Catálogo | `/products`, búsqueda, categorías | GET, POST, PUT, DELETE |
| Carritos | `/carts`, `/carts/user/:id` | GET, POST |
| Autenticación | `/auth/login`, `/auth/me` | POST, GET |

### Fuera de alcance

- Persistencia real en base de datos: DummyJSON **simula** modificaciones.
- Pruebas de carga, penetración y rendimiento con umbrales de producción.
- Validar el diseño visual de una página (este proyecto prueba API, no UI).
- Afirmar que no existen errores en toda la plataforma.

## Técnicas

- **Partición de equivalencia:** ID válido frente a inexistente; credencial
  correcta frente a incorrecta; búsqueda con y sin coincidencias.
- **Valores límite / paginación:** subconjuntos con `limit` y `skip`.
- **Reglas de negocio:** coherencia entre `totalQuantity` y las cantidades
  de los productos de un carrito.
- **Contrato JSON:** claves, tipos y códigos HTTP.

## Criterios de aceptación

Cada caso es aprobado cuando el estado HTTP y las aserciones documentadas
coinciden con la respuesta. Un fallo se analiza antes de declararlo defecto:
puede ser un error del caso, una alteración de datos de demostración,
un límite de servicio o un cambio de contrato.

## Evidencia y trazabilidad

- La matriz [`matriz_casos.csv`](matriz_casos.csv) identifica los 19 casos.
- Las pruebas automatizadas siguen los IDs `P`, `C` y `A`.
- La colección Postman emplea los mismos identificadores.
- El reporte de ejecución documenta el resultado observado y el entorno.

## Riesgos y limitaciones

1. Es un servicio externo: una caída de red genera fallos de transporte.
2. Los datos pueden cambiar; evitamos comparar títulos o precios variables,
   salvo valores que enviamos en operaciones simuladas.
3. Las credenciales de demostración son públicas: no son una política
   de seguridad recomendada para aplicaciones reales.
4. Los tokens son temporales y nunca deben guardarse en GitHub.
