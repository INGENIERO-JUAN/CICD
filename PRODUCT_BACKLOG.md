# Product Backlog — Calculadora CICD (TBD + CD)

**Repositorio:** INGENIERO-JUAN/CICD  
**Sprint actual:** Sprint 1 — TBD Lab  
**Última actualización:** 2026-09-26

Documento vivo del **Product Backlog** adaptado a Trunk-Based Development: historias sliceadas, feature toggles y criterios de aceptación validables en producción. Complementa [`SCRUM_TBD_PLAYBOOK.md`](SCRUM_TBD_PLAYBOOK.md) (Taller 4).

---

## Sprint Goal

> Al final del sprint los usuarios podrán realizar sumas y restas interactivas en producción; las operaciones avanzadas (multiplicación y división) seguirán protegidas detrás de feature toggles hasta su validación.

---

## Leyenda de estado

| Estado | Significado |
| :--- | :--- |
| `Hecho` | Integrado en `main`, DoD técnico cumplido |
| `En progreso` | Código o PR en curso |
| `Listo` | Cumple DoR; puede entrar al sprint |
| `Re-sliceado` | Historia grande dividida en incrementos atómicos |
| `Backlog` | Priorizado pero no iniciado |

---

## Product Backlog (priorizado)

| ID | Prioridad | Issue GitHub | Título | Estado TBD | Estado |
| :---: | :---: | :---: | :--- | :---: | :--- |
| PB-001 | — | — | `suma()` en Calculator (línea base) | 🟢 | Hecho |
| PB-002 | 1 | [#2](https://github.com/INGENIERO-JUAN/CICD/issues/2) | Método `resta()` con toggle apagado (0%) | 🟢 | En progreso |
| PB-003 | 2 | [#3](https://github.com/INGENIERO-JUAN/CICD/issues/3) | Exponer `resta()` en frontend (rollout 10%) | 🟢 | Listo |
| PB-004a | 3 | [#4](https://github.com/INGENIERO-JUAN/CICD/issues/4) | Método `multiplicar()` con toggle 0% | 🟢 | Re-sliceado |
| PB-004b | 4 | [#4](https://github.com/INGENIERO-JUAN/CICD/issues/4) | Método `dividir()` con manejo de errores (toggle 0%) | 🟢 | Re-sliceado |
| PB-004c | 5 | [#4](https://github.com/INGENIERO-JUAN/CICD/issues/4) | Historial en memoria + elevación toggles al 100% | 🟢 | Re-sliceado |
| PB-005 | 6 | — | Integración ConfigCat SDK en Python | 🟡 | Backlog |
| PB-006 | 7 | — | Webhook CD hacia Render (post GHCR) | 🟡 | Backlog |
| PB-007 | 8 | — | Métricas DORA (deployment frequency, lead time) | 🟡 | Backlog |

---

## Detalle de historias

### PB-001 — Suma (baseline)

- **Como** usuario, **quiero** sumar dos enteros, **para** usar la calculadora mínima desplegable.
- **AC:** `Calculator().suma(a, b)`; tests en CI; en `main`.
- **Toggle:** N/A (funcionalidad base).
- **Notas:** Implementado en `src/main.py` y `src/tests.py`.

---

### PB-002 — `resta()` backend detrás del toggle

- **Issue:** [#2](https://github.com/INGENIERO-JUAN/CICD/issues/2)
- **Como** desarrollador, **quiero** implementar `resta()` con feature flag apagado, **para** integrar la lógica a `main` sin exponerla aún.
- **AC en producción:**
  1. Método `resta(a, b)` en `src/main.py`.
  2. Test unitario en `src/tests.py`; job `test` en verde (ruff + pytest).
  3. Flag `feature-resta` en ConfigCat en **0%**.
- **Toggle:** `feature-resta` → rollout **0%**.
- **Semáforo TBD:** tamaño 🟢 | verticalidad 🟢 | toggle 🟢 | validación prod 🟢 → **Lista para TBD**.
- **Avance:** método y test presentes en repo; pendiente flag ConfigCat y cierre de issue.

---

### PB-003 — Frontend resta con rollout interno

- **Issue:** [#3](https://github.com/INGENIERO-JUAN/CICD/issues/3)
- **Como** Product Owner, **quiero** la resta visible solo al 10% de usuarios, **para** validar UX y telemetría en producción.
- **AC en producción:**
  1. UI conectada al endpoint / lógica de resta.
  2. Regla de segmentación **10%** en ConfigCat.
  3. Sin errores en consola ni alertas en producción.
- **Toggle:** `feature-resta` → rollout **10%** (segmento interno).
- **Semáforo TBD:** 🟢 **Lista para TBD**.
- **Dependencia:** PB-002 integrado en `main` con toggle operativo.

---

### PB-004 — Epic original (re-sliceada)

- **Issue:** [#4](https://github.com/INGENIERO-JUAN/CICD/issues/4) — monolito 🔴 **Necesita re-sliceado** (ver playbook §5.1).
- Se trabaja como tres incrementos verticales (PB-004a → PB-004c).

#### PB-004a — Multiplicación

- **Como** desarrollador, **quiero** `multiplicar(a, b)` detrás de toggle 0%, **para** integrar sin activar en UI.
- **AC:** producto aritmético correcto; pytest + ruff en CI; desplegado en `main` sin romper operaciones existentes.
- **Toggle:** `toggle_multiplicacion` → **0%**.
- **Estimación TBD:** ~2 h | **≤ 1 día:** sí.

#### PB-004b — División con casos borde

- **Como** desarrollador, **quiero** `dividir(a, b)` con control de división por cero, **para** evitar fallos en producción.
- **AC:** `dividir(10, 2) == 5`; `dividir(5, 0)` → `ValueError("No se puede dividir por cero")`; casos borde en CI.
- **Toggle:** `toggle_division` → **0%**.
- **Estimación TBD:** ~3 h | **≤ 1 día:** sí.

#### PB-004c — Historial y lanzamiento 100%

- **Como** usuario final, **quiero** historial de operaciones y calculadora completa estable, **para** usar todas las funciones validadas.
- **AC:** historial en memoria por operación exitosa; toggles al **100%** sin degradación; plan de retiro de toggles post-estabilización.
- **Toggle:** `toggle_calculadora_completa` (10% → **100%**).
- **Estimación TBD:** ~4 h | **≤ 1 día:** sí.

---

### PB-005 a PB-007 — Infraestructura y métricas

Items de la hoja de ruta (playbook §4.5):

| ID | Descripción | Valor |
| :--- | :--- | :--- |
| PB-005 | SDK `configcat-client` en runtime Python | Desacoplar despliegue de activación |
| PB-006 | Webhook Render tras `build_and_push` | CD end-to-end |
| PB-007 | Medición DORA | Retrospective basada en datos |

---

## Sprint Backlog — Sprint 1 (flujo continuo)

Integraciones planificadas hacia `main` (no paquete cerrado de 2 semanas):

| Orden | Item | Entregable esperado | Día orientativo |
| :---: | :--- | :--- | :---: |
| 1 | PB-002 | PR: `resta()` + tests + ConfigCat 0% | 1–2 |
| 2 | PB-003 | PR: UI resta + rollout 10% | 2–3 |
| 3 | PB-004a | PR: `multiplicar()` + toggle 0% | 3–4 |
| 4 | PB-004b | PR: `dividir()` + toggle 0% | 4 |
| 5 | PB-004c | PR: historial + toggles 100% | 5+ |

**Capacidad (buffer de flujo):** 60% código · 20% review · 10% CI/CD · 10% contingencia (*stop the line*).

---

## Definition of Ready (DoR) — checklist por ítem

Un ítem entra al Sprint Backlog solo si:

- [ ] Tamaño **≤ 1 día** de desarrollo
- [ ] Criterios de aceptación verificables en **producción**
- [ ] Nombre de toggle y **% inicial** definidos
- [ ] Sin dependencias externas bloqueantes
- [ ] Estrategia de pruebas unitarias acordada

---

## Enlaces

- Tablero Miro / taller: [`miro_board.html`](miro_board.html)
- Reglamento del equipo: [`SCRUM_TBD_PLAYBOOK.md`](SCRUM_TBD_PLAYBOOK.md)
- GitHub Project: *@INGENIERO-JUAN's TBD Lab - Sprint 1* (issues #2–#4 en columna Todo)
