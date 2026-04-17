from .almacen import Inventario, mostrar_almacenes, crear_almacen, acceso_almacen, eliminar_almacen
from .items.lote import Lote
from .item import Item
from .registro import Registro, escribir_creado_almacen, escribir_eliminado_almacen

# Subsclases de Item

from .items.equipo import Equipo

from .items.equipos.termico import EquipoTermico
from .items.equipos.medida import EquipoMedida
from .items.equipos.centrifugadora import Centrifugadora


from .items.consumible import Consumible

from .items.consumibles.reactivoLiquido import ReactivoLiquido
from .items.consumibles.reactivoSolido import ReactivoSolido  