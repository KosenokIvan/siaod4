from typing import Iterable, Optional


class BinaryTree:

    NAME = "Бинарное дерево"

    def __init__(self, collection: Optional[Iterable] = None):
        self._head_node = BinaryTreeNode()
        for el in collection:
            self.add_element(el)

    def add_element(self, el):
        node = self._head_node
        while True:
            if node.value is None:
                node.value = el
                break
            if el < node.value:
                if node.left is None:
                    node.left = BinaryTreeNode(el)
                    break
                node = node.left
            else:
                if node.right is None:
                    node.right = BinaryTreeNode(el)
                    break
                node = node.right

    def find_element(self, el):
        node = self._head_node
        while True:
            if node.value is None:
                return False
            if node.value == el:
                return True
            elif el < node.value:
                if node.left is None:
                    return False
                node = node.left
            else:
                if node.right is None:
                    return False
                node = node.right

    def delete_element(self, el):
        node = self._head_node
        prev_node = None
        prev_node_dir_is_left = True
        while True:
            if node.value is None:
                break
            if node.value == el:
                if node.left is None and node.right is None:
                    if prev_node is None:  # deleted node is head
                        node.value = None
                    elif prev_node_dir_is_left:
                        prev_node.left = None
                    else:
                        prev_node.right = None
                elif node.left is None:
                    if prev_node is None:  # deleted node is head
                        self._head_node = node.right
                    elif prev_node_dir_is_left:
                        prev_node.left = node.right
                    else:
                        prev_node.right = node.right
                elif node.right is None:
                    if prev_node is None:  # deleted node is head
                        self._head_node = node.left
                    elif prev_node_dir_is_left:
                        prev_node.left = node.left
                    else:
                        prev_node.right = node.left
                else:
                    min_node = node.right
                    while min_node.left is not None:
                        min_node = min_node.left
                    self.delete_element(min_node.value)
                    node.value = min_node.value
                break
            elif el < node.value:
                if node.left is None:
                    break
                prev_node = node
                prev_node_dir_is_left = True
                node = node.left
            else:
                if node.right is None:
                    break
                prev_node = node
                prev_node_dir_is_left = False
                node = node.right


class BinaryTreeNode:
    def __init__(self, value=None, left=None, right=None):
        self._value = value
        self._left: Optional[BinaryTreeNode] = left
        self._right: Optional[BinaryTreeNode] = right

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node


if __name__ == '__main__':
    arr = [4, 8, 34, -6, 11, 7, 1, 0, -5, 2]
    searcher = BinaryTree(arr)
    print(searcher.find_element(7))
    print(searcher.find_element(-1))
    searcher.add_element(-1)
    searcher.add_element(-8)
    print(searcher.find_element(-1))
    searcher.delete_element(8)
    print(searcher.find_element(8))
    searcher.delete_element(4)
    print(searcher.find_element(4))
    print(searcher.find_element(-6))
    print(searcher.find_element(7))
