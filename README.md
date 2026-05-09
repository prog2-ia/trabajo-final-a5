# 🧪 Sistema de Gestión de Inventario de Laboratorio (A5)

Este proyecto es una aplicación de consola desarrollada en **Python** diseñada para la gestión integral de activos en un entorno de laboratorio. Permite el control estricto de equipamiento técnico y consumibles químicos, garantizando la trazabilidad mediante un sistema de auditoría y persistencia de datos.

##  Objetivo del Proyecto
El objetivo principal es digitalizar la administración de un laboratorio para reducir errores humanos y garantizar el cumplimiento de normativas de seguridad. El sistema permite:
* **Gestión de Stock:** Controlar la ubicación y cantidad exacta de equipos y reactivos.
* **Trazabilidad:** Registrar cada movimiento, creación o eliminación mediante logs de auditoría cronológicos.
* **Seguridad Científica:** Validar automáticamente fechas de caducidad de lotes y estados de mantenimiento de equipos.
* **Persistencia:** Mantener la integridad de los datos entre sesiones de uso mediante serialización de objetos.

##  Estructura del Proyecto
* `main.py`: Orquestador principal y sistema de menús.
* `clases/`:
    * `item.py`: Clase base abstracta.
    * `almacen.py`: Gestión de inventarios y lógica de stock.
    * `lote.py`: Control de identificadores y caducidades.
    * `items/`: Especializaciones (Equipos, Consumibles, Reactivos).
* `funciones.py`: Motor de validación de entradas y persistencia de archivos.
* `registro.py`: Sistema de escritura de logs de auditoría.
* `logs/auditoria.txt`: Historial en texto plano de todas las operaciones realizadas.

##  Ejemplo de Uso

1. **Crear un Almacén:**
   - Seleccionar `Almacén [1]` > `Crear nuevo [1]`.
   - Introducir código de 5 caracteres (ej: `ALM01`).
   
2. **Añadir Equipamiento:**
   - Seleccionar `Equipamiento [2]` > `Traer nuevo [1]`.
   - Elegir `Definir centrifugadora [2]`.
   - Configurar nombre y RPM (ej: `15000`).
   - Asignar la cantidad deseada al almacén `ALM01`.

3. **Gestión de Lotes:**
   - Seleccionar `Consumibles [3]` > `Traer nuevo lote [1]`.
   - Definir ID de lote (formato `00-ABC`) y fecha de caducidad.
   - Los reactivos se agrupan bajo este lote para una retirada masiva en caso de vencimiento.

##  Requisitos e Instalación
* **Python 3.10** o superior.
* No requiere librerías externas (Standard Library).
* Clonar el repositorio y ejecutar:
  ```bash
  git clone [https://github.com/prog2-ia/trabajo-final-a5.git](https://github.com/prog2-ia/trabajo-final-a5.git)
  python main.py

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/09uckVan)
