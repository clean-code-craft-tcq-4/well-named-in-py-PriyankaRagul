import colors
def print_manual(headers, rows):
    print("Color code Manual")
    print()
    format_row = "{:^15}" * (len(headers))
    print(format_row.format(*headers))

    for row in rows:
        print(format_row.format(*row))

def color_to_string(major_color, minor_color):
  return f'{major_color} {minor_color}'

def print_reference_manual():
    headers = ["pair_no", "Major_Color", "Minor_Color"]
    rows = [
        (pair_number,) + (color_pair) for pair_number, color_pair in COLOR_PAIRS.items()
    ]
    print_manual(headers, rows)
