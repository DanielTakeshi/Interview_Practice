""" Test question 01 for trees. """

from trees import BinaryTree
from trees import BinaryNode

def case01():
    print("\nA balanced tree (in fact, perfectly balanced):\n")
    n1 = BinaryNode(item="Adam")
    n2 = BinaryNode(item="Barry")
    n3 = BinaryNode(item="Charles")
    n4 = BinaryNode(item="Daniel")
    n5 = BinaryNode(item="Edward", lchild=n1, rchild=n2)
    n6 = BinaryNode(item="Frank", lchild=n3, rchild=n4)
    n7 = BinaryNode(item="Greg", lchild=n5, rchild=n6)
    bt = BinaryTree(root=n7)
    print("Balanced = {}.".format(bt.is_balanced()))
    bt.pretty_print()

def case02():
    print("\nAn unbalanced tree (in fact, perfectly unbalanced):\n")
    n1 = BinaryNode(item="Adam")
    n2 = BinaryNode(item="Barry", lchild=n1)
    n3 = BinaryNode(item="Charles", lchild=n2)
    n4 = BinaryNode(item="Daniel", lchild=n3)
    n5 = BinaryNode(item="Edward", lchild=n4)
    n6 = BinaryNode(item="Frank", lchild=n5)
    n7 = BinaryNode(item="Greg", lchild=n6)
    bt = BinaryTree(root=n7)
    print("Balanced = {}.".format(bt.is_balanced()))
    bt.pretty_print()

def case03():
    print("\nA balanced tree (but not perfectly balanced):\n")
    n0 = BinaryNode(item="Ziang")
    n1 = BinaryNode(item="Adam",rchild=n0)
    n2 = BinaryNode(item="Barry")
    n3 = BinaryNode(item="Charles")
    n4 = BinaryNode(item="Daniel")
    n5 = BinaryNode(item="Edward", lchild=n1, rchild=n2)
    n6 = BinaryNode(item="Frank", lchild=n3, rchild=n4)
    n7 = BinaryNode(item="Greg", lchild=n5, rchild=n6)
    bt = BinaryTree(root=n7)
    print("Balanced = {}.".format(bt.is_balanced()))
    bt.pretty_print()

def case04():
    print("\nAn unbalanced tree (but not perfectly unbalanced):\n")
    n00 = BinaryNode(item="Yang")
    n0 = BinaryNode(item="Ziang",lchild=n00)
    n1 = BinaryNode(item="Adam",rchild=n0)
    n2 = BinaryNode(item="Barry")
    n3 = BinaryNode(item="Charles")
    n4 = BinaryNode(item="Daniel")
    n5 = BinaryNode(item="Edward", lchild=n1, rchild=n2)
    n6 = BinaryNode(item="Frank", lchild=n3, rchild=n4)
    n7 = BinaryNode(item="Greg", lchild=n5, rchild=n6)
    bt = BinaryTree(root=n7)
    print("Balanced = {}.".format(bt.is_balanced()))
    bt.pretty_print()

def case05():
    print("\nA base case:\n")
    n0 = BinaryNode(item="Ziang")
    n1 = BinaryNode(item="Adam")
    n2 = BinaryNode(item="Barry",lchild=n0,rchild=n1)
    bt = BinaryTree(root=n2)
    print("Balanced = {}.".format(bt.is_balanced()))
    bt.pretty_print()

def case06():
    print("\nAn even simpler base case:\n")
    n0 = BinaryNode(item="Jeff")
    bt = BinaryTree(root=n0)
    print("Balanced = {}.".format(bt.is_balanced()))
    bt.pretty_print()

if __name__ == "__main__":
    case01()
    case02()
    case03()
    case04()
    case05()
    case06()
