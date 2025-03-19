# $Id: test_strictly_increasing.py,v 1.1 2019/01/24 16:04:20 leavens Exp leavens $
import sys
sys.path.append('/path/to/directory')  # Replace with the actual path
from strictly_increasing import strictly_increasing


def test_strictly_increasing():
    assert strictly_increasing(43, 44, 45, 46)
    assert strictly_increasing(65, 500, 4000, 30000)
    assert strictly_increasing(-2.1, -1.0, 0, 1.345687912)
    assert strictly_increasing(-20, -10, -1, 0.532)
    # however, note:
    assert not strictly_increasing(0, 0, 1, 2)
    assert not strictly_increasing(91, 92, 92, 93)
    assert not strictly_increasing(99, 3, 55, 1)
    assert not strictly_increasing(999, 888.9, 777.885, 777.888)
    assert not strictly_increasing(23, 42, 59, 59)
    assert not strictly_increasing(39, 39, 39, 40)
    assert not strictly_increasing(1, 0.5, 0.25, 0.125)