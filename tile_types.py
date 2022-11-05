#-------------------------------------------------------------------------------
# Name:        Tile Types
# Purpose:
#
# Author:      davidelliott
#
# Created:     03/11/2022
# Copyright:   (c) davidelliott 2022
# License:     
#-------------------------------------------------------------------------------
from typing import Tuple

import numpy as np

graphic_dt = np.dtype(
    [
        ("ch", np.int32),
        ("fg", "3B"),
        ("bg", "3B"),
    ]
)

tile_dt =  np.dtype(
[
    ("walkable", np.bool),
    ("transparent", np.bool),
    ("dark", graphic_dt),
]
)

