from .balcony import register_balcony, unregister_balcony
from .curvedarray import register_curved_array, unregister_curved_array
from .door import register_door, unregister_door
from .fill import register_fill, unregister_fill
from .floor import register_floor, unregister_floor
from .floorplan import register_floorplan, unregister_floorplan
from .generic import register_generic, unregister_generic
from .material import register_material, unregister_material
from .multigroup import register_multigroup, unregister_multigroup
from .railing import register_railing, unregister_railing
from .road import register_road, unregister_road
from .roof import register_roof, unregister_roof
from .stairs import register_stairs, unregister_stairs
from .window import register_window, unregister_window

# -- ORDER MATTERS --
register_funcs = (
    register_generic,
    register_material,
    register_railing,
    register_balcony,
    register_fill,
    register_door,
    register_floor,
    register_window,
    register_floorplan,
    register_stairs,
    register_roof,
    register_multigroup,
    register_road,
    register_curved_array,
)

unregister_funcs = (
    unregister_generic,
    unregister_material,
    unregister_railing,
    unregister_balcony,
    unregister_fill,
    unregister_door,
    unregister_floor,
    unregister_window,
    unregister_floorplan,
    unregister_stairs,
    unregister_roof,
    unregister_multigroup,
    unregister_road,
    unregister_curved_array,
)


def register_core():
    for func in register_funcs:
        func()


def unregister_core():
    for func in unregister_funcs:
        func()
