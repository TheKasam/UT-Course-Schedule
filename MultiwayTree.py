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
    self.subTree = None

  def getData(self):
    return(self.data)

  def getNext(self):
    return (self.next)

  def getSubTree(self):
    return (self.subTree)

  def setData(self,newData):
    self.data = newData

  def setNext(self, newNext):
    self.next = newNext

  def setSubTree(self, newSubTree):
    self.subTree = newSubTree

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
    return temp


  def __str__(self):

    #initing variables
    string = ""
    current = self.head
    count = 0

    #traversing though linked list
    while current != None:
      #adding next elements data to string to return
      string += current.getData() + "  "
      #adding to count for formatting purposes
      count += 1
      if count % 10 == 0:
        string += "\n"
      current = current.getNext()
    return string

  def addLast (self, item):
  # Add an item to the end of a list
  #Follow the add first method except set next at the end of the list.
    current = None
    next = self.head
    temp = Node(item)
    while next != None:
      current = next
      next = next.getNext()
  #If current is not equal to none, it is the pointer before the end, so set temp as next
    if current != None:
      current.setNext(temp)
  #otherwise your list is empty so add the new node to the end.
    else:
      self.head = temp
    return(temp)

class MultiwayTree:
#[2,[]], [3, [ [5,[]], [6, [ [10,[]] ] ] ]], [4, [ [7,[]], [8,[]], [9,[]] ]]
#[1, [[2,[]], [3, [ [5,[]], [6, [ [10,[]] ] ] ]], [4, [ [7,[]], [8,[]], [9,[]] ]] ]]
#[2,[]],    [3,[[5,[]],[6,[[10,[]]]]]],    [4,[[7,[]],[8,[]],[9,[]]]]


        def __init__(self,pyTree):
            tree = LinkedList()

            def getChildren(children):
                childrenLst = []
                child = ''
                outer = False
                inner = 0
                for x in children:
                    if x == '[':
                        outer = True
                        continue

                    if outer:
                        if x == '[':
                            inner +=1
                        elif inner > 0 and x == ']':
                            inner -= 1
                        elif inner == 0 and x == ']':
                            childrenLst.append(child)
                            child = ''
                            outer = False

                    child += x
                return childrenLst

                            #how to split and get head and child
            def getNodesTree(pyTree,tree):
                if pyTree == '':
                    return
                else:
                    pyTree = pyTree[1:-1]
                    tree.head = pyTree[0]
                    childrenLst = pyTree[2:]
                    #1. layer
                    #2. head
                    #3. if children
                    if len(childrenLst) > 2:
                        #get children
                        children = childrenLst[1:-1]
                        childrenLst = getChildren(children)
                        #loop
                        for child in childrenLst:
                            childTree = LinkedList()
                            tree.add(childTree)
                            getNodesTree(child,childTree)
                        #recurse



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

    #treeOne = treeOne[1:-1].split(', ')
    #print(treeOne)
    tOne = LinkedList()
    getNodesTree(treeOne,tOne)
    #print(tOne.head.getData())
    print(tOne.head.getSubTree().head.getData())
   # preOrder(tOne)
   # print(preOrderLst)
#[2,[]],    [3,[  [5,[]]  , [6,[[10,[]]]] ]],    [4,[[7,[]],[8,[]],[9,[]]]]
[2,[]], [3, [ [5,[]], [6, [ [10,[]] ] ] ]], [4, [ [7,[]], [8,[]], [9,[]] ]]


def getChildren(children):
    childrenLst = []
    child = ''
    outer = False
    inner = 0
    for x in children:

        if outer:
            child += x
            if x == '[':
                inner +=1
            elif inner > 0 and x == ']':
                inner -= 1
            elif inner == 0 and x == ']':
                childrenLst.append(child)
                child = ''
                outer = False

        elif x == '[':
            outer = True
            child += x


    return childrenLst

                            #how to split and get head and child
def getNodesTree(pyTree,tree):
    if pyTree == '':
        return
    else:
        pyTree = pyTree[1:-1]
        currentNode = tree.addLast(pyTree[0])
        #tree.head = pyTree[0]
        childrenLst = pyTree[2:]
        #1. layer
        #2. head
        #3. if children
        if len(childrenLst) > 2:
            #get children
            childTree = LinkedList()
            currentNode.setSubTree(childTree)

            children = childrenLst[1:-1]
            childrenLst = getChildren(children)
            #loop
            for child in childrenLst:
                print('child  ' + child )
                #childTree

                #childTree = LinkedList()
                #tree.add(childTree)
                getNodesTree(child,childTree)
            print('for loop returned')
            return
        else:
            print('returned')
            return
preOrderLst = []
def preOrder(tree):

    current = tree.head
    if current.getSubTree == None:
        return

    else:
        while current != None:


            data = current.getData()
            print(data)
            preOrderLst.append(data)
            subTree = current.getSubTree()
            preOrder(subTree)

            current = current.getNext()



main()
