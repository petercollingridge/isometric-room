import math
from draw_svg import SVG

THETA = math.atan(math.sin(math.pi / 6))
DX = math.cos(THETA)
DY = math.sin(THETA)


def draw_wall(svg, x, y, width, height, direction = None, attrs = None):
    """ Draw a vertical wall rectangle in isometric view """
    if not attrs:
        attrs = {}

    dx = width * DX if direction % 2 else width * -DX
    dy = width * DY if direction < 2 else width * -DY
    attrs['d'] = f"M{x} {y}v{height}l{dx} {dy}v{-height}z"
    svg.add('path', attrs)


def draw_wall_outline(svg, x, y, width, height, thickness, direction = None, attrs = None):
    """ Draw a vertical wall rectangle with a cut-out in isometric view """
    if not attrs:
        attrs = {}

    dx = width * DX if direction % 2 else width * -DX
    dy = width * DY if direction < 2 else width * -DY
    d = f"M{x} {y}v{height}l{dx} {dy}v{-height}z"

    x -= thickness * DX
    y += thickness * DY + thickness
    dx += thickness * 2 * DX
    dy -= thickness * 2 * DY
    height -= thickness * 2
    d += f"M{x} {y}l{dx} {dy}v{height}l{-dx} {-dy}z"

    attrs['d'] = d
    svg.add('path', attrs)


def draw_floor(svg, x, y, width, height, attrs = None):
    """ Draw a horizontal (floor) rectangle in isometric view """
    if not attrs:
        attrs = {}

    dx1 = width * DX
    dy1 = width * DY
    dx2 = height * DX
    dy2 = height * DY
    attrs['d'] = f"M{x} {y}l{dx1} {dy1} {-dx2} {dy2} {-dx1} {-dy1}z"
    svg.add('path', attrs)


def draw_L_shape(svg, x, y, d1, d2, d3, attrs = None):
    if not attrs:
        attrs = {}

    dx1 = d1 * DX
    dy1 = d1 * DY
    dx2 = d2 * DX
    dy2 = d2 * DY
    dx3 = d3 * DX
    dy3 = d3 * DY
    attrs['d'] = f"M{x} {y}l{-dx1} {dy1} {-dx3} {-dy3} {dx1 + dx3} {-dy1 -dy3} {dx2 + dx3} {dy2 + dy3} {-dx3} {dy3}z"
    svg.add('path', attrs)


def draw_background(svg, width, height):
    y1 = 16
    wall_width = width * 0.50
    wall_height = height * 0.48
    wall_thick = 12

    # left wall
    draw_wall(svg, width * 0.5, y1, wall_width, wall_height, 0, {'class': 'wall-1'})
    draw_wall(svg, width * 0.5 - DX * wall_width, y1 + wall_width * DY, wall_thick, wall_height + 8, 4, {'class': 'wall-2'})

    draw_wall(svg, width * 0.5, y1, wall_width, wall_height, 1, {'class': 'wall-2'})
    draw_wall(svg, width * 0.5 + DX * wall_width, y1 + wall_width * DY, wall_thick, wall_height + 8, 3, {'class': 'wall-1'})

    draw_L_shape(svg, width * 0.5, y1, wall_width, wall_width, wall_thick, {'class': 'wall-3'})

    # floor
    draw_floor(svg, width * 0.5, y1 + wall_height, wall_width, wall_width, {'class': 'floor'})
    floor_y = y1 + wall_height + (wall_width * DY) * 2
    draw_wall(svg, width * 0.5,floor_y, wall_width, 8, 3, {'class': 'floor'})
    draw_wall(svg, width * 0.5,floor_y, wall_width, 8, 4, {'class': 'floor'})


def draw_frame():
    frame_width = 35
    frame_height = 50
    frame_thick = 2
    frame_border = 5

    img_border = 2
    svg_width = math.ceil((frame_width + frame_thick) * DX + img_border * 2)
    svg_height = math.ceil(frame_width * DY + frame_height + img_border * 2)
    view_box = f"0 0 {svg_width} {svg_height}"
    # svg = SVG({'width': svg_width, 'height': svg_height})
    svg = SVG({'viewBox': view_box})

    svg.rect(0, 0, svg_width, svg_height, fill='#f8f8f8')

    # Start at top right corner, giving a 2px border
    x = frame_width * DX + img_border
    y = img_border

    top_colour = 'rgb(248, 190, 105)'
    front_colour = 'rgb(234, 169, 83)'
    side_colour = 'rgb(220, 155, 60)'

    # Backing / img
    draw_wall(svg, x, y, frame_width, frame_height, 0, {'fill': '#e8e8ff'})

    # Upper edge
    draw_floor(svg, x, y, frame_thick, frame_width, {'fill': top_colour})

    # Lower, inner edge
    draw_floor(svg, x, y + frame_height - frame_border, frame_thick, frame_width, {'fill': top_colour})

    # Front face
    front_x = x + DX * frame_thick
    front_y = y + DY * frame_thick

    # Left edge
    x1 = front_x - frame_width * DX
    y1 = front_y + frame_width * DY
    draw_wall(svg, x1, y1, frame_thick, frame_height, 2, {'fill': side_colour})

   # Inner right edge
    x2 = front_x - frame_border * DX
    y2 = front_y + frame_border * DY + frame_border
    draw_wall(svg, x2, y2, frame_thick, frame_height - frame_border * 2, 2, {'fill': side_colour})

    draw_wall_outline(svg, front_x, front_y, frame_width, frame_height, frame_border, 0, {'fill': front_colour})

    svg.write("picture.svg")


def main():
    width = 600
    height = 600
    svg = SVG({'width': width, 'height': height})
    svg.add_style('.wall-1', {'stroke': '#bb8', 'fill': '#ffd'})
    svg.add_style('.wall-2', {'stroke': '#bb8', 'fill': '#eec'})
    svg.add_style('.wall-3', {'stroke': '#bb8', 'fill': '#ffe'})
    svg.add_style('.floor', {'stroke': '#b61', 'fill': '#d82'})

    draw_background(svg, width, height)
    svg.write("room.svg")


if __name__ == '__main__':
    # main()
    draw_frame()
