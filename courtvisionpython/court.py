import matplotlib.patches as patches
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


def draw_rectangle(ax, x, y, width, height, **kwargs):
    rectangle = patches.Rectangle((x, y), width, height, **kwargs)
    ax.add_patch(rectangle)
    return rectangle


def draw_line(ax, x, y, **kwargs):
    line = Line2D(x, y, **kwargs)
    ax.add_artist(line)
    return line


def court(court_color="#3B82C2",
          surface_color="#56A45D",
          line_color="white",
          line_width=2,
          size=(11, 6),
          equal_aspect=False,
          axis=False,
          aspect="full"):
    """
    Draw a tennis court.

    Parameters
    ----------
    court_color: str
        Court color
    surface_color: str
        Outside color
    line_color: str
        Line color
    line_width:float
        Line width
    size: tuple
        figure size default = (11,6)
    equal_aspect: bool
        Preserve aspect ratio
    axis: bool
        Display axis
    aspect: str
        display a full or half court: options are full or half

    Returns
    -------
    A figure and an axis: tuple
        matplotlib (fig, axis)

    """
    length = 23.77
    width = 8.23
    alley = 1.372
    service_block_length = 6.4

    full_length = length + 8
    full_width = width + 4.5

    x0 = -full_length/2
    x1 = full_length/2
    x0_surface = -length / 2
    x1_surface = length / 2

    y0 = -full_width / 2
    y1 = full_width/2
    y0_surface = -width / 2
    y1_surface = width / 2

    x_center = 0
    y_center = 0

    fig, ax = plt.subplots(figsize=size)

    # Court and surface
    draw_rectangle(ax, x=x0, y=y0, width=full_length, height=full_width, color=surface_color)
    draw_rectangle(ax, x=x0_surface, y=y0_surface, width=length, height=width,
                   color=court_color, linewidth=line_width, ec=line_color)

    # Service blocks
    draw_rectangle(ax, x=x_center, y=y0_surface, width=service_block_length,
                   height=width, color=court_color, linewidth=line_width, ec=line_color)
    draw_rectangle(ax, x=-service_block_length, y=y0_surface, width=service_block_length,
                   height=width, color=court_color, linewidth=line_width, ec=line_color)

    # Alleys
    draw_rectangle(ax, x=x0_surface, y=y1_surface, width=length, height=alley,
                   color=court_color, linewidth=line_width, ec=line_color)
    draw_rectangle(ax, x=x0_surface, y=y0_surface-alley, width=length, height=alley,
                   color=court_color, linewidth=line_width, ec=line_color)

    # Center small line
    draw_line(ax, [x0_surface, x0_surface+0.3], [y_center, y_center], color=line_color, linewidth=line_width)
    draw_line(ax, [x1_surface, x1_surface-0.3], [y_center, y_center], color=line_color, linewidth=line_width)
    # Net
    draw_line(ax, [0, 0], [y0_surface-2, y1_surface+2], color=line_color, linewidth=line_width+2)

    # Center line
    draw_line(ax, [-service_block_length, service_block_length],
              [y_center, y_center], color=line_color, linewidth=line_width)

    ax.set_xlim([x0, x1])
    ax.set_ylim([y0, y1])
    if not axis:
        plt.axis('off')
    if equal_aspect:
        ax.set_aspect("equal")

    if aspect == "half":
        ax.set_xlim(x_center-3, x1)

    plt.tight_layout()

    return fig, ax
