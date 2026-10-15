import pytest
from src.structures.linked_list import LinkedList
from src.structures.deque import Deque
from src.structures.avl_tree import AVLTree

def test_linked_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.head.data == 1
    ll.delete(2)
    assert ll.head.next.data == 3

def test_deque():
    dq = Deque()
    dq.add_rear(1)
    dq.add_front(2)
    assert dq.remove_front() == 2
    assert dq.remove_rear() == 1
    assert dq.is_empty()

def test_avl_tree():
    tree = AVLTree()
    root = None
    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        root = tree.insert(root, key)
    assert root.height == 3  