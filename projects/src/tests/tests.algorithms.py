from src.algorithms.bubble_sort import bubblesort
from src.algorithms.quick_sort import quicksort

def test_bubble_sort():
    assert bubblesort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]

def test_quick_sort():
    assert quicksort([10, 7, 8, 9, 1, 5]) == [1, 5, 7, 8, 9, 10]
