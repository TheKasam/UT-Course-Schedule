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
        self.tree = LinkedList()
        self.preOrderLst = []
        self.isoLst = []

        self.getNodesTree(pyTree,self.tree)
        self.getTreeStruct(self.tree)
        self.isoLst.append('done')

    def getHeadElement(self,pyTree):
        element = ''
        childLst = ''
        addElement = True
        for x in pyTree:
            if x == ',' and addElement == True:
                addElement = False
                continue
            if addElement:
                element += x
            else:
                childLst += x
        #print(element,'asdf',childLst)
        return (element,childLst)
#[1,[[2,[]],[3,[[5,[]],[6,[[10,[]]]]]],[4,[[7,[]],[8,[]],[9,[]]]]]]

    def getNodesTree(self,pyTree,tree):
        if pyTree == '':
            return
        else:
            #1. layer
            pyTree = pyTree[1:-1]
            #2. head
            elementHead,childrenLst = self.getHeadElement(pyTree)
            currentNode = tree.addLast(elementHead)

            #3. if children
            if len(childrenLst) > 2:
                #get children
                childTree = LinkedList()
                currentNode.setSubTree(childTree)

                children = childrenLst[1:-1]
                childrenLst = self.getChildren(children)
                #loop
                for child in childrenLst:
                    #print('child  ' + child )
                    self.getNodesTree(child,childTree)
                #print('for loop returned')
                return

            else:
                #print('returned')
                return

    def getChildren(self,children):
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

    def preOrder(self):
        self.preOrderCall(self.tree,self.tree.head)
        return self.preOrderLst

    def preOrderCall(self,tree,current):

        if current == None:
            #print('up')
            return
        else:
            data = current.getData()
            self.preOrderLst.append(data)
            #print(data)
            if current.getSubTree() != None:
                subTree = current.getSubTree()
                #print('down left')
                self.preOrderCall(subTree,subTree.head)
            self.preOrderCall(tree,current.getNext())


    def getTreeStruct(self,tree):
        self.getTreeStructCall(tree,tree.head)

    def getTreeStructCall(self,tree,current):
        if current == None:
            self.isoLst.append('up ')
            return
        else:
            data = current.getData()
            #self.preOrderLst.append(data)
            self.isoLst.append('node ')
            if current.getSubTree() != None:
                subTree = current.getSubTree()
                #print('down left')
                self.isoLst.append('downleft ')
                self.getTreeStructCall(subTree,subTree.head)
            self.getTreeStructCall(tree,current.getNext())

    def isIsomorphicTo(self,other):  #return True if the tree "self" has the same structure as the

        self.getTreeStruct(other)

        newIsoLst = []
        otherLst = []
        addToOther = False
        for x in self.isoLst:
            if x == 'done':
                addToOther = True
                continue

            if addToOther:
                otherLst.append(x)
            else:
                newIsoLst.append(x)


        if len(newIsoLst) != len(otherLst):
            return False
        else:
            if len(newIsoLst) > len(otherLst):
                for x in len(newIsoLst):
                    if newIsoLst[x] != otherLst[x]:
                        return False
            if len(newIsoLst) < len(otherLst):
                for x in len(otherLst):
                    if newIsoLst[x] != otherLst[x]:
                        return False
        return True

def removeSpaces(stringu):
    newStringu = ''
    for x in stringu:
        if x != ' ':
            newStringu += x
    return newStringu


def main():
    inputFile = open('MultiwayTreeInput.txt','r')

    print()
    line = inputFile.readline()
    count = 1
    while line != '':

        print('Tree '+str(count)+':  '+line, end='')
        treeOne = MultiwayTree(removeSpaces(line))
        print('Tree '+str(count)+' preorder:   ' + str(treeOne.preOrder()))
        print()


        line = inputFile.readline()
        count +=1
        print('Tree '+str(count)+':  '+line, end='')
        treeTwo = MultiwayTree(removeSpaces(line))
        print('Tree '+str(count)+' preorder:   ' + str(treeTwo.preOrder()))
        print()

        if treeOne.isIsomorphicTo(treeTwo.tree):
            print('Tree ' + str(count-1) + ' is isomorphic to Tree ' + str(count))
        else:
            print('Tree ' + str(count-1) + ' is not isomorphic to Tree ' + str(count))

        count +=1
        line = inputFile.readline()
        print()

main()
