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
| PB-003 | 2 | [#3](https://github.com/INGENIERO-JUAN/CICD/issues/3) | Exponer `resta()` en frontend (rollout 10%) | 🟢 | En progreso |
| PB-004 | — | [#4](https://github.com/INGENIERO-JUAN/CICD/issues/4) | Epic: operaciones avanzadas + 100% | 🟢 | Re-sliceado |
| PB-004a | 3 | [#9](https://github.com/INGENIERO-JUAN/CICD/issues/9) | Método `multiplicar()` con toggle 0% | 🟢 | Listo |
| PB-004b | 4 | [#10](https://github.com/INGENIERO-JUAN/CICD/issues/10) | Método `dividir()` con manejo de errores (toggle 0%) | 🟢 | Listo |
| PB-004c | 5 | [#11](https://github.com/INGENIERO-JUAN/CICD/issues/11) | Historial en memoria + elevación toggles al 100% | 🟢 | Listo |
| PB-005 | 6 | [#12](https://github.com/INGENIERO-JUAN/CICD/issues/12) | Integración ConfigCat SDK en Python | 🟢 | En progreso |
| PB-006 | 7 | [#13](https://github.com/INGENIERO-JUAN/CICD/issues/13) | Webhook CD hacia Render (post GHCR) | 🟡 | Backlog |
| PB-007 | 8 | [#14](https://github.com/INGENIERO-JUAN/CICD/issues/14) | Métricas DORA (deployment frequency, lead time) | 🟡 | Backlog |

---

## Detalle de historias

### PB-001 — Suma (baseline)

- **Como** usuario, **quiero** sumar dos enteros, **para** usar la calculadora mínima desplegable.
- **AC:** `Calculator().suma(a, b)`; tests en CI; en `main`.
- **Toggle:** N/A (funcionalidad base).
- **Notas:** API `GET /api/suma` y UI en `src/static/`.

---

### PB-002 — `resta()` backend detrás del toggle

- **Issue:** [#2](https://github.com/INGENIERO-JUAN/CICD/issues/2) — Project: **In Progress**
- **Como** desarrollador, **quiero** implementar `resta()` con feature flag apagado, **para** integrar la lógica a `main` sin exponerla aún.
- **AC en producción:**
  1. Método `resta(a, b)` en `src/main.py`.
  2. Test unitario en `src/tests.py`; job `test` en verde (ruff + pytest).
  3. Flag `feature-resta` en ConfigCat en **0%** (dashboard + `CONFIGCAT_SDK_KEY` en Render).
- **Toggle:** `feature-resta` → rollout **0%**.
- **Avance:** lógica, API `/api/resta` (403 sin flag) y SDK en `src/feature_flags.py`. **Pendiente:** crear flag en ConfigCat y cerrar issue.

---

### PB-003 — Frontend resta con rollout interno

- **Issue:** [#3](https://github.com/INGENIERO-JUAN/CICD/issues/3) — bloqueada por #2 hasta toggle operativo; UI base en repo.
- **Como** Product Owner, **quiero** la resta visible solo al 10% de usuarios, **para** validar UX y telemetría en producción.
- **AC en producción:**
  1. UI en `src/static/index.html` + `script.js` conectada a `/api/resta`.
  2. Regla de segmentación **10%** en ConfigCat.
  3. Sin errores en consola ni alertas en producción.
- **Toggle:** `feature-resta` → rollout **10%** (segmento interno).
- **Avance:** botón resta oculto hasta `feature_resta` en `/api/flags`. **Pendiente:** rollout 10% en ConfigCat.

---

### PB-004 — Epic (#4) y sub-issues

- **Epic:** [#4](https://github.com/INGENIERO-JUAN/CICD/issues/4) con sub-issues [#9](https://github.com/INGENIERO-JUAN/CICD/issues/9), [#10](https://github.com/INGENIERO-JUAN/CICD/issues/10), [#11](https://github.com/INGENIERO-JUAN/CICD/issues/11).
- Cadena: #10 bloqueada por #9; #11 bloqueada por #10.

#### PB-004a — [#9](https://github.com/INGENIERO-JUAN/CICD/issues/9) Multiplicación

- **Toggle:** `toggle_multiplicacion` → **0%**.

#### PB-004b — [#10](https://github.com/INGENIERO-JUAN/CICD/issues/10) División

- **Toggle:** `toggle_division` → **0%**.

#### PB-004c — [#11](https://github.com/INGENIERO-JUAN/CICD/issues/11) Historial y 100%

- **Toggle:** `toggle_calculadora_completa` (10% → **100%**).

---

### PB-005 a PB-007 — Infraestructura

| ID | Issue | Descripción | Estado |
| :--- | :--- | :--- | :--- |
| PB-005 | [#12](https://github.com/INGENIERO-JUAN/CICD/issues/12) | `configcat-client`, módulo `feature_flags.py`, var `CONFIGCAT_SDK_KEY` | Código en repo; cerrar al validar en prod |
| PB-006 | [#13](https://github.com/INGENIERO-JUAN/CICD/issues/13) | Webhook Render tras `build_and_push` | Backlog |
| PB-007 | [#14](https://github.com/INGENIERO-JUAN/CICD/issues/14) | Métricas DORA | Backlog |

---

## Sprint Backlog — Sprint 1 (flujo continuo)

| Orden | Item | Entregable esperado | Día orientativo |
| :---: | :--- | :--- | :---: |
| 1 | PB-002 | PR: `resta()` + tests + ConfigCat 0% | 1–2 |
| 2 | PB-003 | PR: UI resta + rollout 10% | 2–3 |
| 3 | PB-004a (#9) | PR: `multiplicar()` + toggle 0% | 3–4 |
| 4 | PB-004b (#10) | PR: `dividir()` + toggle 0% | 4 |
| 5 | PB-004c (#11) | PR: historial + toggles 100% | 5+ |

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
- GitHub Project: [@INGENIERO-JUAN's TBD Lab - Sprint 1](https://github.com/users/INGENIERO-JUAN/projects/1) — issues #2–#14; #2 **In Progress**; epic #4 con sub-issues #9–#11
