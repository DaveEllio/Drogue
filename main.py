#-------------------------------------------------------------------------------
# Name:        Main
# Purpose:
#
# Author:      davidelliott
#
# Created:     03/11/2022
# Copyright:   (c) davidelliott 2022
# License:     BSD License
#-------------------------------------------------------------------------------
#imports tcod library
import tcod


from engine import Engine
from entity import Entity
from input_handlers import EventHandler

#Defines Main
def main() -> None:
    #initial variables
    screen_width = 80
    screen_height = 50


    tileset = tcod.tileset.load_tilesheet(
        "terminal12x12_gs_ro.png", 16, 16, tcod.tileset.CHARMAP_CP437
    )

    #initializes eventhandler
    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "¥", (255, 255, 0))
    entities = {npc, player}

    engine = Engine(entities=entities, event_handler=event_handler, player=player)
    #initializes the terminal window
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Drogue",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:

            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)

if __name__ == "__main__":
    main()