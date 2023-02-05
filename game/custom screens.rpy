# Custom screens for the apartment image button use.

screen apartment():
    add "gui/images/apartment bg.png"

    # Bike
    imagebutton:
        xpos 0
        ypos 506
        idle "gui/images/bike_idle.png"
        hover "gui/images/bike_hover.png"
        action Jump("bike")

    # Book
    imagebutton:
        xpos 1265
        ypos 883
        idle "gui/images/book_idle.png"
        hover "gui/images/book_hover.png"
        action Jump("mainroom")

    # Calendar
    imagebutton:
        xpos 1334
        ypos 406
        idle "gui/images/calender_idle.png"
        hover "gui/images/calender_hover.png"
        action Jump("calendar")

    # Clock
    imagebutton:
        xpos 931
        ypos 195
        idle "gui/images/clock_idle.png"
        hover "gui/images/clock_hover.png"
        action Jump("clock")
        
    # Notebook
    imagebutton:
        xpos 1287
        ypos 679
        idle "gui/images/notebook_idle.png"
        hover "gui/images/notebook_hover.png"
        action Jump("notebook")

    # Pamphlet
    imagebutton:
        xpos 1555
        ypos 657
        idle "gui/images/pamphlet_idle.png"
        hover "gui/images/pamphlet_hover.png"
        action Jump("pamphlet")

    # Photographs
    imagebutton:
        xpos 1465
        ypos 387
        idle "gui/images/photographs_idle.png"
        hover "gui/images/photographs_hover.png"
        action Jump("photograph")

    # camera
    imagebutton:
        xpos 659
        ypos 725
        idle "gui/images/camera_idle.png"
        hover "gui/images/camera_hover.png"
        action Jump("camerascene")

    # Receipts NO NEED
    # imagebutton:
    #     xpos 1060
    #     ypos 392
    #     idle "gui/images/receipts_idle.png"
    #     hover "gui/images/receipts_hover.png"
    #     action Jump("mainroom")