#-------------------------------------------------------------------------------
# Name:        Actions
# Purpose:
#
# Author:      davidelliott
#
# Created:     03/11/2022
# Copyright:   (c) davidelliott 2022
# License:     BSD License
#-------------------------------------------------------------------------------
class Action:
    pass

class EscapeAction(Action):
    pass

class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy
