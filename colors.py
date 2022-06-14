MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]
COLOR_PAIRS = {
    pair_number + 1: color_pair
    for pair_number, color_pair in enumerate(
        [
            (major_color, minor_color)
            for major_color in MAJOR_COLORS
            for minor_color in MINOR_COLORS
        ]
    )
}
