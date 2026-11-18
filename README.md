# DummyJSON | API Testing con Python y Postman

Pruebas de una API de comercio electrónico: catálogo de productos, carritos y autenticación. El repositorio incluye código Python, una colección Postman y ejecución continua con GitHub Actions.

## Resumen

Diseñé una suite que valida respuestas HTTP, contenido JSON, búsqueda, ordenamiento y escenarios negativos. Uso una API pública de demostración para que las pruebas puedan repetirse.

## Alcance

- **Productos:** 12 casos, incluyendo búsquedas, paginación y operaciones de escritura simuladas.
- **Carritos:** 4 casos de consulta y validación de datos.
- **Autenticación:** 3 casos de inicio de sesión y acceso autenticado.
- **Métodos:** GET, POST, PUT y DELETE. Las operaciones de escritura de DummyJSON no persisten.

## Herramientas

`Python` · `Requests` · `pytest` · `Postman` · `JSON` · `GitHub Actions`

## Cómo ejecutar o revisar

Con Python 3.10 o superior y conexión a Internet:

```bash
git clone https://github.com/Johanna-80/dummyjson-api-qa.git
cd dummyjson-api-qa
python -m pip install -r requirements.txt
python -m pytest -v
```

Para revisar las solicitudes en Postman, importa [`postman/DummyJSON_QA.postman_collection.json`](postman/DummyJSON_QA.postman_collection.json). Ejecuta primero el caso de login correcto si vas a comprobar una ruta que exige token. No publiques tokens reales.

## Evidencias y resultados

- **19 de 19 pruebas automatizadas aprobadas** en una ejecución documentada. No representa el estado actual del servicio.
- [Ejecución exitosa de GitHub Actions (30/10/2026)](https://github.com/Johanna-80/dummyjson-api-qa/actions/runs/41006876260).
- [Matriz de 19 casos](docs/matriz_casos.csv), [estrategia](docs/estrategia_pruebas.md) y [reporte detallado](docs/reporte_ejecucion.md).
- **19 solicitudes Postman con aserciones** preparadas; su ejecución dentro de Postman sigue pendiente de verificación independiente.

## Estructura

```text
.github/workflows/api-tests.yml   # CI
postman/                           # Colección Postman
tests/                             # Productos, carritos y autenticación
docs/                              # Estrategia, casos y resultados
requirements.txt                   # Dependencias
pytest.ini                         # Configuración pytest
```

## Limitaciones

DummyJSON es un servicio de demostración. POST/PUT/DELETE devuelven respuestas simuladas; la suite no afirma que los cambios se guarden. Una ejecución correcta tampoco prueba que la API esté libre de defectos. No se reportaron defectos confirmados en la ejecución documentada.

## Próximos pasos

- Ejecutar y registrar la colección Postman con capturas propias.
- Añadir casos cuando exista una especificación de respuesta que permita definir expectativas claras.

---
**Johanna Vásquez** · [Portafolio web](https://johanna-80.github.io/) · [Perfil GitHub](https://github.com/Johanna-80)
