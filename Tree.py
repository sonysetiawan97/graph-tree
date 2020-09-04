"""
Binary tree is some structure data which each node have the most 2 child.

Example:
|Left_Child|Parent|Right_Child|

Another example:
	 8
    /\
   2  5
  /	   \
 1      8
in this case 8 is parent(node), 2 as left_child, 5 as right_child.
And 2 have more child which is 1 left_child.
Also 5 have more child which is 8 as right_child.

Binary Tree read is from top-left-right.

entering is for choose node
leaving is for move to parent
at is print at that node

so, read that example will be like this:

entering 8 (root/parent)
entering 2 (move to left_node from 8)
entering 1 (move to left_node from 2)
at 1 (print 1 - this node is left_node from 2)
leaving 1 (move to parent 2)
at 2 (print 2 - this node is left_node from 8)
leaving 2 (move to parent 8)
at 8 (print 8 - this node is root/parent)
entering 5 (move to right_node from 8)
at 5 (print 5 - this node is right node from 8)
entering 8 (move to right_node from 5)
at 8 (print 8 - this node is right node from 5)
leaving 8 (move to parent 5 )
leaving 5 (move to parent 8)
leaving 8 (move to parent - this node is root/parent)

done

"""

#Binary tree program(Using OOP-Oriented object programming)
import os #called some library for os syntax

#create some class(object)
class BinaryTree:
	#constructor for Binary tree
    def __init__(self, key=None):
        self.key = key #node(root)
        self.left = None #left_node
        self.right = None #right_node
 
 	#setter for node/root
    def set_root(self, key):
        self.key = key #self object will valued by key passing data
    
    #setter for left_node
    def insert_left(self, new_node):
        self.left = new_node #self object will valued by new_node passing data

    #setter for right_node
    def insert_right(self, new_node):
        self.right = new_node #self object will valued by new_node passing data
 	
 	#Finding some value on binary tree
    def search(self, key):
        if self.key == key: #if self object value key == key from passing daya True then
            return self #give value of this object
        if self.left is not None: #if self object value left is not empty then
            temp =  self.left.search(key) #valued of temp is valued this object by key value
            if temp is not None: #if valued time is not empty then
                return temp #give valued temp
        if self.right is not None: #if self object value right is not empty then
            temp =  self.right.search(key) #valued of temp is valued this object by key value
            return temp #give valued temp
        return None

    #Print the binary tree
    def depth_first(self):
        print('entering {}...'.format(self.key)) #print chosen of the binary tree
        if self.left is not None: #if value of self object didn't empty then
            self.left.depth_first() #recursive function. called depth_first() function
        print('at {}...'.format(self.key)) #print value of the binary tree
        if self.right is not None: #if value of self object didn't empty then
            self.right.depth_first() #recursive function. called depth_first() function
        print('leaving {}...'.format(self.key)) #print going to the parent of the binary tree

btree = None #declare variable btree

def menu():
	print("=-=-= Binary Tree =-=-=")
	print("=======================")
	print("Binary tree:")
	if btree is not None:
		btree.depth_first()
	print()
	print("=======================")
	print("*note: if insert couple times at root it will be new tree for last input")
	print("1. insert <data> at root(node)")
	print("2. insert <data> left of <data>")
	print("3. insert <data> right of <data>")
	print("4. quit")

while True:
	os.system("cls") #clear cmd screen

	menu()

	choice=int(input("Your choice[1-4]:"))
	if choice==1: #if choice==1 true then
		x=int(input("Your input: ")) #x valued by user input
		new_node=BinaryTree(x) #create new BinaryTree with name new_node
		btree = new_node #btree have new_node value
		print("Data inserted to tree")
		input("press enter to continue...")
	elif choice==2: #if choice==2 then
		key=int(input("Your root parent: ")) #key valued by user input
		ref_node = None #declare variable ref_node
		if btree is not None: #if btree is not empty true then
			ref_node = btree.search(key) #ref_node valued is btree.search(key)
		if ref_node is None: #if ref_node true is empty then
			print("No such key")
			input("press enter to continue...")
		else: #if ref_node is none false then
			y=int(input("Your input: ")) #y valued by user input
			new_node=BinaryTree(y)  #create new BinaryTree object valued by y
			ref_node.insert_left(new_node) #insert to left node
			print("Data inserted to tree")
			input("press enter to continue...")
	elif choice==3: #if choice==3 true then
		key=int(input("Your root parent: "))
		ref_node = None
		if btree is not None:
			ref_node = btree.search(key)
		if ref_node is None:
			print("No such key")
			input("press enter to continue...")
		else:
			y=int(input("Your input: ")) #y valued by user input
			new_node=BinaryTree(y) #create new BinaryTree object valued by y
			ref_node.insert_right(new_node) #insert to right node
			print("Data inserted to tree")
			input("press enter to continue...")
	elif choice==4: #if choice==4 true then
		os.system("cls") #clear cmd screen
		break #quit looping
	else: #if all if false then
		print("Wrong input")
		input("press enter to continue...")
		os.system("cls")