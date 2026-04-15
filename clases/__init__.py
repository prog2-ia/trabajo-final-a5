from .almacen import Inventario
from .items.lote import Lote
from .item import Item
from .registro import Registro

# Subsclases de Item

from .items.equipo import Equipo

from .items.equipos.termico import EquipoTermico
from .items.equipos.medida import EquipoMedida
from .items.equipos.centrifugadora import Centrifugadora


from .items.consumible import Consumible

from .items.consumibles.reactivoLiquido import ReactivoLiquido
from .items.consumibles.reactivoSolido import ReactivoSolido  