# Roadmap | Proyecto Repo-Guardian

Este documento organiza las tareas del proyecto por épica técnica, indicando su tipo, prioridad estimada y estado en el tablero Kanban.

| Épica           | Tarea                                        | Código | Tipo   | Prioridad | Kanban      |
|----------------|-----------------------------------------------|--------|--------|-----------|-------------|
| E-01 Setup      | Crear repositorio y README.md                 | RX-01  | feat   | Alta      | Done        |
| E-01 Setup      | Diagrama contextual PlantUML                  | RX-02  | docs   | Media     | Done        |
| E-01 Setup      | Configurar CI (ci.yml)                        | RX-03  | chore  | Alta      | In-Progress |
| E-01 Setup      | Crear plantillas de issue/PR                  | RX-04  | docs   | Alta      | Done        |
| E-01 Setup      | Escribir Roadmap.md inicial                   | RX-05  | docs   | Alta      | Done        |
| E-01 Setup      | Crear estructura de carpetas                  | RX-06  | chore  | Alta      | Backlog     |
| E-02 Escáner    | Leer objetos sueltos (`read_loose`)           | RX-07  | feat   | Alta      | Backlog     |
| E-02 Escáner    | Leer objetos en packfiles                     | RX-08  | feat   | Alta      | Backlog     |
| E-02 Escáner    | Validar tipo y CRC                            | RX-09  | fix    | Alta      | Backlog     |
| E-02 Escáner    | Crear fixture `corrupt-blob.git`              | RX-10  | test   | Media     | Backlog     |
| E-02 Escáner    | Añadir escenario BDD: "blob corrupto"         | RX-11  | test   | Alta      | Backlog     |
| E-03 DAG        | Implementar construcción de DAG               | RX-12  | feat   | Alta      | Backlog     |
| E-03 DAG        | Añadir número de generación                   | RX-13  | feat   | Media     | Backlog     |
| E-03 DAG        | Detectar reescrituras con Jaro-Winkler        | RX-14  | feat   | Media     | Backlog     |
| E-03 DAG        | Crear archivo `dag_rewrite.feature` (BDD)     | RX-15  | test   | Media     | Backlog     |
| E-04 Reparación | Rebase de recuperación (`repair.py`)          | RX-16  | feat   | Alta      | Backlog     |
| E-04 Reparación | Crear script `scan-repo.sh`                   | RX-17  | feat   | Media     | Backlog     |
| E-04 Reparación | Hook `post-merge`                             | RX-18  | chore  | Media     | Backlog     |
| E-04 Reparación | Exportar DAG como `.graphml` con `networkx`   | RX-19  | feat   | Alta      | Backlog     |
| E-05 CLI/TUI    | Diseñar CLI inicial con `argparse`            | RX-20  | feat   | Alta      | Backlog     |
| E-05 CLI/TUI    | Implementar TUI básica (`rich` / `curses`)    | RX-21  | feat   | Media     | Backlog     |
| E-05 CLI/TUI    | Agregar barra de progreso y comandos          | RX-22  | feat   | Media     | Backlog     |
| E-05 CLI/TUI    | Capturar errores visualmente                  | RX-23  | fix    | Media     | Backlog     |
| E-06 Pruebas    | Escribir pruebas de integración               | RX-24  | test   | Alta      | Backlog     |
| E-06 Docs       | Generar reporte de benchmarking               | RX-25  | docs   | Media     | Backlog     |
| E-06 Docs       | Publicar documentación con MkDocs             | RX-26  | docs   | Alta      | Backlog     |
| E-06 Docs       | Grabar video de demostración final            | RX-27  | docs   | Alta      | Backlog     |

