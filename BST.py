class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def Insert(self,value):
        self.root =  self.__Insert(self.root,value)

    def __Insert(self,root,value):
        if root == None:
            root = Node(value)
        else:
            if value < root.value:
                root.left = self.__Insert(root.left, value)
            else:
                root.right = self.__Insert(root.right, value)
        return root

    def Inorder(self):
        return self.__Inorder(self.root)

    def __Inorder(self,root):
        if root:
            print(root.value)
            self.__Inorder(root.left)
            self.__Inorder(root.right)

    def Height(self):
        return self.__Height(self.root)

    def __Height(self,root):
        if root == None:
            return -1
        return max(self.__Height(root.left) , self.__Height(root.right)) + 1

    def mini(self):
        x = self.__mini(self.root)
        return x.value

    def __mini(self,root):
        while root:
            if root.left == None:
                break
            else:
                root = root.left
        return root

    def maxi(self):
        x = self.__maxi(self.root)
        return x.value

    def __maxi(self,root):
        while root:
            if root.right == None:
                break
            else:
                root = root.right
        return root

    def successor(self):
        x = self.__successor(self.root)
        z = x.value
        return z

    def __successor(self,root):
        return self.__mini(root.right)

    def predecessor(self):
        x = self.__predecessor(self.root)
        y = x.value
        return y

    def __predecessor(self,root):
        return self.__maxi(root.left)

    def MiniValueFind(self, node):
        temporary = node
        while (temporary.left is not None):
            temporary = temporary.left

        return temporary

    def Delete(self, val):
        self.root = self.__Delete(self.root, val)

    def __Delete(self, node, val):
        if node == None:
            return node
        elif val < node.val:
            node.left = self.__Delete(node.left, val)
        elif val > node.val:
            node.right = self.__Delete(node.right, val)
        else:
            if node.left == None:
                extra = node.right
                node = None
                return extra
            elif node.right == None:
                extra = node.left
                root = None
                return extra
            extra = self.MiniValueFind(node.right)
            node.val = extra.val
            node.right = self.__Delete(node.right, extra.val)
        return node



a = BST()
a.Insert(10)
a.Insert(12)
a.Insert(9)
a.Insert(3)
a.Insert(11)
a.Insert(2)
a.Inorder()
print('Height is ' , a.Height())
print('minimum value is ' , a.mini())
print('maximum value is ' , a.maxi())
print('Successor is' , a.successor())
print('predecessor is ' , a.predecessor())