"I confirm that this submission is my own work and is consistent with the Queen's regulations on Academic Integrity"
"Terence Jiang(20353261)"
import random 
    
class listNode:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

class BinarySearchTreeVertex:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.current = None

    def insert(self, x):
        newNode = BinarySearchTreeVertex(x)
        
        if (self.root == None):
            self.root = newNode  # If binary tree is empty, make node as root
            #print('the root is',x)  # used for testing insert
        else:
            current = self.root
            done = False

            while not done:
                if(current.value < x):
                    if(current.right == None):
                        current.right = newNode  # If current node is smaller than the value and there is nothing on the right, add to the right of node
                        done = True
                        #print(x,"is right of node", current.value)  # used for testing insert
                    else:
                        current = current.right  # If there is a node in the right position already, keep going right
                else:
                    if(current.left == None):  
                        current.left = newNode  # Add to the left of node if it is epty
                        done = True
                        #print(x,"is left of node", current.value)  # used for testing insert
                    else:
                        current = current.left  # If there is a node in the left position already, keep going left

    def height(self):
        if (self.root == None):
            return -1  # Return height of -1 as binary search tree is empty
        else:
            return self.heightRecursive(self.root)

    def heightRecursive(self, v):
        if (v == None):
            return -1  
        else:
            #Recursively call the function to calculate height of the left and right side of nodes. Then get the largest value of either height and add 1
            leftHeight = self.heightRecursive(v.left)
            rightHeight = self.heightRecursive(v.right)
            return 1+max(leftHeight,rightHeight)      
    
    def total_height(self):
        if (self.root == None):
            return -1  # Return height of -1 as binary search tree is empty
        else:
            sum = 0
            return self.totalHeightRecursive(self.root, sum)
    
    def totalHeightRecursive(self,v, sum):
        if(v==None):
            return 0
        
        #Recursively call the function to calculate height of the left and right side of nodes. Then get the largest value of either height and add 1
        leftHeight = self.totalHeightRecursive(v.left, sum)
        rightHeight = self.totalHeightRecursive(v.right, sum)
        height = max(leftHeight, rightHeight) + 1

        #keep adding the heights to the sum to get total height
        sum = sum + height
        return height

def pseudoRandomPermutation(n):
    randomPermutation = []
    for i in range (1,n+1):
        randomPermutation.append(i) #  Add values of n into list

    random.shuffle(randomPermutation) #  Shuffle values so it is random
    head = listNode(randomPermutation[0])
    curr = head
    #Turn the list into a linked list
    for val in range(1, len(randomPermutation)):
        newNode = listNode(randomPermutation[val])
        curr.next = newNode
        curr = newNode
    return head
# Used to show evidence of working pseudo-random permutation
def printPerm(head):
    current = head
    while current is not None:
        if(current.next == None):
            print(current.value, "linked to: ", None)
        else:
            print(current.value, "linked to: ", current.next.value)
        current = current.next

for n in [100,200,300,400,500,600,700,800,900,1000]:
    totalHeight=0
    for trial in range(500):
        permutation = pseudoRandomPermutation(n)
        bst = BinarySearchTree()
        current = permutation
        while current:
            bst.insert(current.value)
            current = current.next  # Create binary search tree with values in linked list
        totalHeight +=bst.height()  # Keep adding the heights to get a total value
    print(totalHeight/500, end= ' ')

