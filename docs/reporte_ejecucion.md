# Reporte de ejecución automatizada

**Fecha de referencia:** 29 de octubre de 2026  
**Sistema bajo prueba:** DummyJSON (`https://dummyjson.com`)  
**Herramientas:** Python 3.12, pytest 9.2.0 y Requests 2.34.2.

## Resumen

| Métrica | Resultado |
|---|---:|
| Casos automatizados ejecutados | 19 |
| Aprobados | 19 |
| Fallidos | 0 |
| Errores de preparación | 0 |
| Duración observada | 5,06 s |

Comando utilizado desde la raíz del proyecto:

```bash
python -m pytest -q --tb=short
```

Resultado de la ejecución observada:

```text
tests/test_auth.py ...
tests/test_carts.py ....
tests/test_products.py ............
19 passed in 5.06s
```

**Interpretación:** las 19 comprobaciones cumplieron sus expectativas en esa
ejecución. Esto no demuestra ausencia de defectos ni garantiza que sigan
aprobando después de cambios en el proveedor.

Las solicitudes POST/PUT/DELETE son **simuladas**. En ningún momento se
validó persistencia real de altas, cambios o eliminaciones.

## Postman

Se entrega una colección Postman importable con 19 solicitudes y aserciones.
Su ejecución desde la aplicación Postman queda pendiente de validación
por la autora antes de presentar resultados específicos de esa herramienta.

## Registro de defectos

No se confirma ningún defecto del proveedor durante esta ejecución. Si
se observa una discrepancia reproducible, documentarla con el formato de
`docs/plantilla_bug.md` antes de afirmar que es un bug.
