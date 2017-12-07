class Stack:

  #stack methods and structure

  def __init__(self):
    self.items = []

  def peek(self):
    return self.items[-1]

  def push(self,item):
    self.items.append(item)

  def pop(self):
    return self.items.pop(-1)

  def isEmpty(self):
    return self.items == []

  def size(self):
    return len(self.items)


#defining node class
class Node:

  def __init__ (self,initdata):
    self.data = initdata
    self.next = None  #pointer to a Node (or None if node not needed)

  def getData(self):
    return(self.data)

  def getNext(self):
    return (self.next)

  def setData(self,newData):
    self.data = newData

  def setNext(self, newNext):
    self.next = newNext

#defining linked list class
class LinkedList:

#setting head to none
  def __init__(self):
    self.head = None


  def add(self, item):
    #creating new node
    temp = Node(item)
    #setting net object for node
    temp.setNext(self.head)
    #updating head
    self.head = temp

class MultiwayTree:
[2,[]], [3, [ [5,[]], [6, [ [10,[]] ] ] ]], [4, [ [7,[]], [8,[]], [9,[]] ]]
[1, [[2,[]], [3, [ [5,[]], [6, [ [10,[]] ] ] ]], [4, [ [7,[]], [8,[]], [9,[]] ]] ]]
[1,[[2,[]],[3,[[5,[]],[6,[[10,[]]]]]],[4,[[7,[]],[8,[]],[9,[]]]]]]


        def __init__(self,pyTree):
            tree = LinkedList()

                            #how to split and get head and child
            def getNodesTree(pyTree,tree):
                pyTree = pyTree[1:-1]
                tree.head = pyTree[0]
                
                #1. layer
                #2. head
                #3. if children
                if pyTree == '':
                    return
                elif pyTree[4] !=']':
                    #1.get children
                    pyTreeChildren = pyTree[4:-1]
                    pyTreeChildren = pyTreeChildren.split('], ')
                    for child in pyTreeChildren:
                    #2. add child
                        child = child[1:]
                        childTree = LinkedList()
                        childTree.head = child[0]
                        tree.add(childTree)
                    #3. recurse child
                        getNodesTree(childTree)
                #4. else return
              #given "pyTree", a Python representation of a tree, create a node-and-pointer representation of that tree.
            if pyTree == '':
                return
            else:
                if pyTree[0] == '[':

                    pyTreeLst = pyTree[1:-1].split(',')
                    tree = LinkedList()
                    tree.head = pyTreeLst[0]
                    nodes = pyTreeLst[1][1:-1].split()

                    tree.add()


        #def preOrder(self):  print out the node-and-pointer representation of a tree using preorder.

        #def isIsomorphicTo(self,other):  return True if the tree "self" has the same structure as the
         #    tree "other", "False" otherwise.
def removeSpaces(stringu):
    newStringu = ''
    for x in stringu:
        if x != ' ':
            newStringu += x
    return newStringu



def main():
    inputFile = open('MultiwayTreeInput.txt','r')
    treeOne = inputFile.readline()
    treeOne = removeSpaces(treeOne)

    treeOne = treeOne[1:-1].split(', ')
    print(treeOne)
    nodes = treeOne[1][1:-1].split()








main()
