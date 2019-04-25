from __future__ import annotations

"""
following syntax won't work in older python
it gonna lead to NameError
eather
def __init__(self, left: Node, right: Node) -> None:
NameError: name 'Node' is not defined
"""


class Node(object):
    def __init__(self, left: Node, right: Node) -> None:
        self.left = left
        self.right = right


node = Node("x", "y")
