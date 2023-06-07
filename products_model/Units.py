from edg_core import *

import math

MNewton = LiteralConstructor(1e6, 'N')
kNewton = LiteralConstructor(1e3, 'N')
Newton = LiteralConstructor(1, 'N')
mNewton = LiteralConstructor(1e-3, 'N')
uNewton = LiteralConstructor(1e-6, 'N')
nNewton = LiteralConstructor(1e-9, 'N')

Second = LiteralConstructor(1, 'S')
mSecond = LiteralConstructor(1e-3, 'S')
uSecond = LiteralConstructor(1e-6, 'S')
nSecond = LiteralConstructor(1e-9, 'S')


class UnitUtils:
  PREFIXES_POW3_HIGH = ['k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
  PREFIXES_POW3_LOW = ['m', 'u', 'n', 'p', 'f', 'a', 'z', 'y']

  @classmethod
  def num_to_prefix(cls, num: float, figs: int) -> str:
    if num == 0:
      return '0'
    elif num == -float('inf'):
      return '-inf'
    elif num == float('inf'):
      return 'inf'
    elif num < 0:
      sign = '-'
      num = -num
    else:
      sign = ''

    num_pwr3 = math.floor(math.log10(num) / 3)
    if num_pwr3 < 0:
      prefix_set = cls.PREFIXES_POW3_LOW
      num_pwr3_sign = -1
    else:
      prefix_set = cls.PREFIXES_POW3_HIGH
      num_pwr3_sign = 1
    num_pwr3 *= num_pwr3_sign

    if num_pwr3 > len(prefix_set) + 1:  # clip to top number
      num_pwr3 = len(prefix_set) + 1
    if num_pwr3 == 0:
      prefix = ''
    else:
      prefix = prefix_set[num_pwr3 - 1]

    num_prefix = num * 10**(-1 * num_pwr3_sign * num_pwr3 * 3)
    return f"{sign}{num_prefix:0.{figs}g}{prefix}"
