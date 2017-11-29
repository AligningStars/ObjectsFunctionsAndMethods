"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Cheryl.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:

    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    width = 800
    height = 900
    window = rg.RoseWindow(width, height)

    center = rg.Point(300, 300)
    radius = 100
    daisy = rg.Circle(center, radius)
    daisy.fill_color = 'azure'
    daisy.attach_to(window)

    lazy_center = rg.Point(500, 600)
    lazy_radius = 160
    lazy = rg.Circle(lazy_center, lazy_radius)
    lazy.fill_color = 'lavender'
    lazy.attach_to(window)

    window.render()

    window.close_on_mouse_click()
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------


def circle_and_rectangle():
    width = 800
    height = 500
    window = rg.RoseWindow(width, height)

    center = rg.Point(200, 200)
    radius = 80

    circle = rg.Circle(center, radius)
    thickness = circle.outline_thickness
    color = circle.fill_color = 'DarkSeaGreen'
    circle.attach_to(window)
    print(thickness, '\n', color, '\n', center, '\n', center.x, '\n',
          center.y, '\n')

    corner1 = rg.Point(500, 100)
    corner2 = rg.Point(700, 300)
    rectangle = rg.Rectangle(corner1, corner2)
    center = rectangle.get_center()
    thickness = rectangle.outline_thickness
    fill_color = rectangle.fill_color = 'DarkKhaki'
    rectangle.attach_to(window)
    print(thickness, '\n', fill_color, '\n', center, '\n', center.x, '\n',
          center.y, '\n')

    window.render()

    window.close_on_mouse_click()
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


def lines():
    width = 700
    height = 500
    window = rg.RoseWindow(width, height)

    start = rg.Point(100, 100)
    end = rg.Point(200, 200)
    line = rg.Line(start, end)
    line.attach_to(window)

    left = rg.Point(300, 300)
    right = rg.Point(400, 100)
    thread = rg.Line(right, left)
    thread.attach_to(window)
    thread.thickness = 4
    thread.color = 'DarkSalmon'
    point = thread.get_midpoint()
    print(point, '\n', point.x, '\n', point.y)

    window.render()

    window.close_on_mouse_click()

    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()

