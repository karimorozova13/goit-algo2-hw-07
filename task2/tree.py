class Node:
    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        """Вставка нового елемента в дерево."""
        if self.root is None:
            self.root = Node(key, value)
        else:
            self.root = self._insert_node(self.root, key, value)
            self._splay(self.root, key)

    def _insert_node(self, node, key, value):
        """Рекурсивна вставка елемента в дерево."""
        if node is None:
            return Node(key, value)
        if key < node.key:
            node.left = self._insert_node(node.left, key, value)
            node.left.parent = node
        elif key > node.key:
            node.right = self._insert_node(node.right, key, value)
            node.right.parent = node
        return node

    def find(self, key):
        """Пошук елемента в дереві із застосуванням сплаювання."""

        node = self._find(self.root, key)
        if node:
            self._splay(self.root, key)
            return node.value
        return None
    
    def _find(self, node, key):
        """Рекурсивний пошук вузла."""
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._find(node.left, key)
        return self._find(node.right, key)

    def _splay(self, node, key):
        """Сплаювання вузла `key` до кореня."""
        if node is None or node.key == key:
            return
        if key < node.key:
            if node.left is None:
                return
            if key < node.left.key:
                self._splay(node.left.left, key)
                node = self._rotate_right(node)
            elif key > node.left.key:
                self._splay(node.left.right, key)
                if node.left.right:
                    node.left = self._rotate_left(node.left)
            node = self._rotate_right(node)
        else:
            if node.right is None:
                return
            if key > node.right.key:
                self._splay(node.right.right, key)
                node = self._rotate_left(node)
            elif key < node.right.key:
                self._splay(node.right.left, key)
                if node.right.left:
                    node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)
        self.root = node

    def _rotate_right(self, node):
        """Права ротація."""
        left_child = node.left
        if left_child is None:
            return node
        node.left = left_child.right
        left_child.right = node
        return left_child

    def _rotate_left(self, node):
        """Ліва ротація."""
        right_child = node.right
        if right_child is None:
            return node
        node.right = right_child.left
        right_child.left = node
        return right_child

