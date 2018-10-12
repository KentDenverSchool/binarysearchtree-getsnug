class Node:
	def __init__(self, key, value, upPointer, downPointer):
		self.upPointer = upPointer
		self.downPointer = downPointer
		self.key = key
		self.value = value
		self.size = 0

	def __repr__(self):
		return "Node{"+"key="+str(self.getKey())+", value="+str(self.getValue())+"}"
	def getKey(self):
		return self.key
	def setKey(self, key):
		self.key = key
	def getValue(self):
		return self.value
	def setValue(self, newVal):
		self.value = newVal
	def setUp(self, x):
		self.upPointer = x
	def getUp(self):
		return self.upPointer
	def getDown(self):
		return self.downPointer
	def setDown(self, x):
		self.downPointer = x
	def setSize(self, newSize):
		self.size = newSize
	def getSize(self):
		self.size = 1
		if(self.getDown()!=None):
			self.size += self.getDown().getSize()
		if(self.getUp()!=None):
	 	 	self.size += self.getUp().getSize()
	 	return self.size

class BST():
	def __init__(self):
		self.root = Node(None, None, None, None)
	def size(self):
		return self.__recSize(self.root)
	def __recSize(self, node):
		return node.getSize() + 1
	def isEmpty(self):
		return self.size()==0
	def put(self, key, val):
		x = self.__recPut(self.root, key, val)
		self.root = x
	def __recPut(self, node, key, value):
		if(node.getKey() == None):
			node = Node(key, value, None, None)
			return node;
			# node.setKey(key)
			# node.setValue(value)
		else:
			if(key >= node.getKey()):
				if (node.getUp()==None):
					node.setUp(Node(key, value, None, None))
					return node
				else:
					node.setUp(self.__recPut(node.getUp(), key, value))
					return node
			#this will check for all values less than
			else:
				if(node.getDown()==None):
					node.setDown(Node(key, value, None, None))
					return node
				else:
					node.setDown(self.__recPut(node.getDown(), key, value))
					return node
	def get(self, key):
		return self.__recGet(self.root, key)
	def __recGet(self, node, key):
		#checks if equals
		if(key==node.getKey()):
			return node.getValue()
		#checks higher values
		elif(node.getUp() != None and key>node.getKey()):
			return self.__recGet(node.getUp(), key)
		#checks less values
		elif(node.getDown() != None and key<node.getKey()):
			return self.__recGet(node.getDown(), key)
		else:
			return -1

	def contains(self, key):
		return self.get(key) != -1
	def remove(self, key):
		v = self.get(key)
		self.root = self.__recRemove(self.root, key)
		print(self.root)
		return v;
	def __recRemove(self, node, key):
		if(node==None):
			return None
		if(key<node.getKey()):
			node.setDown(self.__recRemove(node.getDown(), key))
		elif(key>node.getKey()):
			node.setUp(self.__recRemove(node.getUp(), key))
		else:
			if(node.getUp()==None):
				return node.getDown()
			if(node.getDown()==None):
				return node.getUp()
			else:
				dwn = node.getDown()
				node = node.getUp()
				node.setDown(dwn)
		#node.setSize(node.getUp().size() + self.node.getDown().size() + 1)
		return node

	def minimum(self):
		return self.__recMin(self.root).getKey()

	def __recMin(self, node):
		if(node.getDown() != None):
			return self.__recMin(node.getDown())
		else:
			return node

	def maximum(self):
		return self.__recMax(self.root).getKey()

	def __recMax(self, node):
		if(node.getUp() != None):
			return self.__recMax(node.getUp())
		else:
			return node

	def __repr__(self):
		temp = self.__toString(self.root)
		temp = temp[0:(len(temp)-2)]
		return "{"+temp+"}"
	def getRoot(self):
		return self.root
	def setRoot(self, x):
		root.setKey(x)
	def __toString(self, node):
		if(node==None):
			return ""
		else:
			return str(self.__toString(node.getDown())) + str(node.getKey()) + "=" + str(node.getValue()) + ", " + str(self.__toString(node.getUp()))
def isBST(bst):
	return __isBST(bst.root)
def __isBST(node):      
    # An empty tree is BST 
	if node.getDown() is not None: 
		if node.getDown().getKey() >= node.getKey():
			return False
		else:
			__isBST(node.getDown())
	elif node.getUp() is not None:
		if(node.getUp().getKey() < node.getKey()):
			return False
		else:
			__isBST(node.getUp())
	if(node.getDown() is None and node.getUp() is None):
		pass
	return True

  
    # False if this node violates min/max constraint 
	if node.getKey() < minimum or node.getKey> maximum: 
		return False
  
    # Otherwise check the subtrees recursively 
    # tightening the min or max constraint 
	return (__isBST(node.getUp(), minimum, node.getKey()-1) and
		__isBST(node.Down, node.getKey()+1, maximum)) 
def main():
	# bst = BST()
	# bst.put(4, "hello")
	# bst.put(7, "hi there")
	# bst.put(2, "hello")
	# bst.put(8, "hi there")
	# bst.put(3, "hello")
	# bst.put(2, "hi there")
	# bst.put(9, "hello")
	# bst.put(8, "hi there")
	# bst.put(10, "hello")
	# bst.put(20, "hi there")
	# bst.put(25, "hello")
	# bst.put(15, "ahoy")
	# bst.put(17, "hello")
	# bst.put(16, "hi m8")
	# bst.put(1, "hello")
	# bst.put(11, "hi there")
	# bst.put(13, "hey guys")
	# bst.put(33, "hi there")
	# print 'testing toString expected output has all keys in ascending numerical order: ' , bst
	# print 'testing maximum, expected output is "33", actual output: ', bst.maximum()
	# print 'testing minimum, expected output is "1" actual output: ', bst.minimum()
	# bst.remove(4)
	# print 'testing remove, expected output should be like toString but missing key 4 or hello', bst
	# bst.remove(2)
	# print 'testing remove expected output is like the last minus the 2 key', bst
	# bst.remove(1)
	# print 'testing remove, expected output is like the last minus the 1 key', bst
	# print 'testing get, expected output is hi m8, actual: ', bst.get(16)
	# print 'testing size, expected output is 15, actual: ', bst.size()
	bst = BST()
	bst.put(4, "hello")
	bst.put(7, "hi there")
	bst.put(2, "hello")
	bst.put(8, "hi there")
	bst.put(3, "hello")
	bst.put(2, "hi there")
	bst.put(9, "hello")
	bst.put(8, "hi there")
	bst.put(10, "hello")
	bst.put(20, "hi there")
	bst.put(25, "hello")
	bst.put(15, "ahoy")
	bst.put(17, "hello")
	bst.put(16, "hi m8")
	bst.put(1, "hello")
	bst.put(11, "hi there")
	bst.put(13, "hey guys")
	bst.put(33, "hi there")
	print('testing toString expected output has all keys in ascending numerical order: ' , bst)
	print ('testing maximum, expected output is "33", actual output: ', bst.maximum())
	print ('testing minimum, expected output is "1" actual output: ', bst.minimum())
	bst.remove(4)
	print ('testing remove, expected output should be like toString but missing key 4 or hello', bst)
	bst.remove(2)
	print ('testing remove expected output is like the last minus the 2 key', bst)
	bst.remove(1)
	print ('testing remove, expected output is like the last minus the 1 key', bst)
	print ('testing get, expected output is hi there, actual: ', bst.get(16))
	print ('testing size, expected output is 15, actual: ', bst.size())
	bst.remove(17)
	bst.remove(16)
	print ('testing size after removing 2 more, expected output is 13, actual: ', bst.size())
	bst.remove(33)
	bst.remove(15)
	print ('testing size after removing 2 more, expected output is 11, actual: ', bst.size())
	print("now it's time to test isBST(), first I'm going to test it on the one from the previous driver")
	print('expected is True, actual: ', isBST(bst))
	print("now i'm going to edit ours to make it fake...")
	bst.root.getUp().setKey(-999)
	print('expected is now False, actual: ', isBST(bst))

if __name__ == '__main__':
	main()




