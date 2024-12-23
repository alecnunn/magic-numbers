from magic_numbers import FORTY_TWO, SIXTY_NINE, FOUR_HUNDRED_AND_TWENTY
from magic_numbers import ONE_THOUSAND_THREE_HUNDRED_AND_TWELVE
from magic_numbers import FOUR_CENTILLION_SIX_SEPTENONAGINTILLION
from magic_numbers import THREE_POINT_ONE_FOUR_ONE_FIVE_NINE_TWO
from magic_numbers import ONE_POINT_ZERO_ZERO_ZERO_ZERO_ZERO_ZERO_ZERO_ZERO_ZERO_ZERO_ZERO_ONE

print(f"{FORTY_TWO = }")
print(f"{SIXTY_NINE = }")
print(f"{FOUR_HUNDRED_AND_TWENTY = }")
print(f"{ONE_THOUSAND_THREE_HUNDRED_AND_TWELVE = }")
print(f"{FOUR_CENTILLION_SIX_SEPTENONAGINTILLION = }")
print(f"{THREE_POINT_ONE_FOUR_ONE_FIVE_NINE_TWO = }")
print(f"{ONE_POINT_ZERO_ZERO_ZERO_ZERO_ZERO_ZERO_ZERO_ZERO_ZERO_ZERO_ZERO_ONE = }")

try:
	from magic_numbers import NOT_A_NUMBER
except ImportError:
	print("task failed successfully")

import magic_numbers
print(f"{magic_numbers.FIVE = }")

try:
	magic_numbers.ALSO_NOT_A_NUMBER
except AttributeError:
	print("task failed successfully (again)")
