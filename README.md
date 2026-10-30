# DummyJSON API Testing — QA de comercio electrónico

Proyecto independiente de **Johanna Vásquez**, orientado a demostrar habilidades
de **QA Engineer Jr.** en análisis, diseño de casos, ejecución y automatización
de pruebas de API.

## 1. Contexto y objetivo

DummyJSON simula recursos comunes de una tienda en línea: catálogo,
carritos y acceso de usuarios. El objetivo es verificar respuestas HTTP,
estructuras JSON, filtros, reglas de negocio y manejo de escenarios negativos.

Este proyecto usa una API pública de demostración, **no un sistema productivo**.

## 2. Alcance y herramientas

- **19 casos de prueba:** 12 de productos, 4 de carritos y 3 de autenticación.
- **Métodos HTTP:** GET, POST, PUT y DELETE.
- **Python + Requests + pytest:** ejecución automatizada con aserciones.
- **Postman:** colección importable con las mismas 19 identificaciones de casos.
- **Diseño QA:** partición de equivalencia, paginación, escenarios negativos y consistencia de datos.

## 3. Estructura

```text
dummyjson-api-qa/
├── README.md
├── requirements.txt
├── pytest.ini
├── .gitignore
├── .github/workflows/api-tests.yml
├── tests/
│   ├── conftest.py
│   ├── test_products.py
│   ├── test_carts.py
│   └── test_auth.py
├── postman/
│   └── DummyJSON_QA.postman_collection.json
└── docs/
    ├── matriz_casos.csv
    ├── estrategia_pruebas.md
    ├── reporte_ejecucion.md
    └── plantilla_bug.md
```

## 4. Ejecutar las pruebas con Python

Se recomienda Python 3.10 o superior, acceso a Internet y una terminal.

```bash
git clone https://github.com/Johanna-80/dummyjson-api-qa.git
cd dummyjson-api-qa
python -m pip install -r requirements.txt
python -m pytest -v
```

El enlace de clonación será válido **después de crear el repositorio** con
ese nombre en la cuenta indicada. En Windows, el comando puede ser `py -m pytest -v`.

Ejecutar un módulo:

```bash
python -m pytest tests/test_products.py -v
```

Filtrar casos:

```bash
python -m pytest -m auth -v
python -m pytest -m escritura -v
```

La URL pública se puede cambiar mediante la variable opcional
`DUMMYJSON_BASE_URL`. No se necesita una clave propia de API.

## 5. Ejecutar con Postman

1. Abrir Postman y pulsar **Import**.
2. Elegir `postman/DummyJSON_QA.postman_collection.json`.
3. Ejecutar los grupos **Productos**, **Carritos** y **Autenticación**.
4. En Autenticación, ejecutar primero `A01` (login correcto), que guarda
   temporalmente `accessToken` como variable de colección; luego ejecutar `A03`.
5. Inspeccionar **Test Results** para comparar cada aserción.

La colección emplea el usuario de demostración publicado por DummyJSON.
No exportar ni publicar una colección con tokens de sesión reales guardados.

## 6. Resultados

**Ejecución automatizada verificada (29-10-2026): 19/19 casos aprobados.**
Ver [reporte de ejecución](docs/reporte_ejecucion.md). Los resultados no
implican que el servicio no tenga defectos.

Las operaciones de creación, actualización y eliminación en DummyJSON son
**simulaciones**: devuelven datos como si se hubieran realizado, pero **no
persisten** en el servidor. Por ello, ningún test afirma persistencia real.

### Integración continua

El proyecto incluye un flujo de **GitHub Actions** que ejecuta pytest al
subir cambios a `main`, abrir un Pull Request o activarlo manualmente.
Genera un resultado JUnit descargable desde la ejecución. Un fallo de red
puede afectar una prueba de integración incluso si el código no cambió.

## 7. Evidencia y metodología

- [Matriz de casos](docs/matriz_casos.csv)
- [Estrategia de pruebas](docs/estrategia_pruebas.md)
- [Reporte de ejecución](docs/reporte_ejecucion.md)
- [Plantilla para documentar defectos](docs/plantilla_bug.md)

## 8. Fuentes oficiales

- [DummyJSON — Productos](https://dummyjson.com/docs/products)
- [DummyJSON — Carritos](https://dummyjson.com/docs/carts)
- [DummyJSON — Autenticación](https://dummyjson.com/docs/auth)

## 9. Próximas mejoras

- Capturas reales de Postman y del reporte de pytest.
- Revisar la primera ejecución de GitHub Actions después de publicarlo.
- Casos adicionales de límites inválidos cuando exista un contrato explícito
  que respalde el resultado esperado.

---

**Nota de autoría:** proyecto de práctica independiente; no está afiliado
ni certificado por DummyJSON.
