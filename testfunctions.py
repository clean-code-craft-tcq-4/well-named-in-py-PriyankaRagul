import utilities;
def test_number_to_color(pair_number,
                        expected_major_color, expected_minor_color):
  major_color, minor_color = get_color_from_pairnumber(pair_number)
  if major_color == expected_major_color and minor_color == expected_minor_color: 		
  	print("Number to Color Pass");
  else:
  	print("Number to Color Fail");
  assert(major_color == expected_major_color)
  assert(minor_color == expected_minor_color)
  
  def test_color_to_number(major_color, minor_color, expected_pair_number):
  pair_number = get_pairnumber_from_color(major_color, minor_color)
  if pair_number == expected_pair_number:
  	print("Color to number pass")
  else:
  	print("Color to number Fail")
  assert(pair_number == expected_pair_number)
