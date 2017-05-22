from node import Node
class DoublyLinkedList(object):
	def __init__(self, input = None):
		self.head = None
		self.tail = None
		# root is WIP
		self.root = None
		# used to create a doublylinkedlist with input []
		if input != None and isinstance(input, list):
			for i in input:
				self.inject(i)

	# print(self) and str(self) 
	# returns to a [] list form, instead of object id
	def __str__(self):
		cur = self.head
		contents = '['
		cur = self.head
		while (cur != None):
			tempString = ''
			if cur.nr != None:
				tempString = ', '
			contents += str(cur) + tempString
			cur = cur.nr
		contents += ']'
		return str(contents)

	# makes len(self) return list length
	def __len__(self):
		cur = self.head
		length = 0
		while cur != None:
			length += 1
			cur = cur.nr
		return int(length)

	# creates an iterator iter(self) and also used in 
	# for loops: (for i in self:)
	def __iter__(self):
		if self.head != None:
			for cur in self.head:
				yield cur

	# reversed(self) returns a reversed iterator^ of self; WIP
	def __reversed__(self):
		for cur in reversed(self.tail):
			yield cur

	# self[key] returns object at position (key)
	def __getitem__(self, key):
		for i in self:
			if i.pos == key:
				return i

	# usage: self[key] = value
	# used to assign values to a key position
	def __setitem__(self, key, value):
		if len(self) < key:
			print('Index is beyond range of list.')
			return False
		else:
			cur = self.head
			while cur.pos != key:
				cur =  cur.nr
			cur.car = value

	# usage: (if value in self:)
	# returns true if self has a node with cargo (value)
	def __contains__(self, value):
		for cur in self:
			if int(cur) == value:
				return True
		return False

	# turns list into an empty list
	def clear(self):
		self.__init__()

	# self.isEmpty() returns True if empty
	def isEmpty(self):
		if len(self) == 0:
			return True
		return False

	# used for get- and setitem methods
	def update(self):
		i = 0
		for cur in self:
			cur.pos = i
			i += 1

	def insertAfter(self, node, newnode):
		newnode.prv(node)
		if (node.nr == None):
			newnode.nxt(node.nr)
			self.tail = newnode
		else:
			newnode.nxt(node.nr)
			newnode.nr.prv(newnode)
		node.nxt(newnode)


	def insertBefore(self, node, newnode):
		newnode.nxt(node)
		if (node.nl == None):
			newnode.prv(node.nr)
			self.head = newnode
		else:
			newnode.prv(node.nr)
			newnode.nl.nxt(newnode)
		node.prv(newnode)

	def insertBeginning(self, newnode):
		if (self.head == None):
			self.head = newnode
			self.tail = newnode
			newnode.prv(None)
			newnode.nxt(None)
		else:
			self.insertBefore(self.head, newnode)

	def insertEnd(self, newnode):
		if (self.tail == None):
			self.insertBeginning(newnode)
		else:
			self.insertAfter(self.tail, newnode)

	# removes node from list
	def remove(self, node):
		if (node.nl == None):
			self.head = node.nr
		else:
			node.nl.nxt(node.nr)
		if (node.nr == None):
			self.tail = node.nl
		else:
			node.nr.prv(node.nl)

	# adds element at end of list
	def inject(self, cargo):
		newnode = Node(cargo)
		newnode.pos = len(self) + 1
		self.insertEnd(newnode)

	# inserts element at beginning
	def push(self, cargo):
		newnode = Node(cargo)
		self.insertBeginning(newnode)

	# retrieves and removes last element
	def eject(self):
		#remove and get cargo of last
		cargo = self.tail.car
		self.remove(self.tail)
		if (cargo != None):
			return cargo

	# retrieves and removes first element
	def pop(self):
		cargo = self.head.car
		self.remove(self.head)
		if cargo != None:
			return cargo

	# retrieves cargo and removes node from list
	def poll(self, node):
		cargo = node.car
		self.remove(node)
		if cargo != None:
			return cargo

	# SWAPS node WITH THE NODE TO THE RIGHT OF node
	def shift(self, node):
		if (node.nr == None):
			return False
		elif(node.nl == None):
			node.nr.prv(node.nl)
			node.prv(node.nr)
			node.nxt(node.nr.nr)
			node.nr.prv(node)
			node.nl.nxt(node)
			self.head = node.nl
			return True
		elif(node.nr.nr == None):
			node.nl.nxt(node.nr)
			node.nr.prv(node.nl)
			node.prv(node.nr)
			node.nxt(node.nr.nr)
			node.nl.nxt(node)
			self.tail = node
			return True
		else:
			node.nl.nxt(node.nr)
			node.nr.prv(node.nl)
			node.prv(node.nr)
			node.nxt(node.nr.nr)
			node.nr.prv(node)
			node.nl.nxt(node)
			return True

	# SWAPS node WITH THE NODE TO THE LEFT OF node
	def shiftLeft(self, node):
		if(node.nl == None):
			return False
		elif(node.nr == None):
			node.nl.nxt(node.nr)
			node.nxt(node.nl)
			node.prv(node.nl.nl)
			node.nr.prv(node)
			node.nl.nxt(node)
			self.tail = node.nr
			return True
		elif(node.nl.nl == None):
			node.nr.prv(node.nl)
			node.nl.nxt(node.nr)
			node.nxt(node.nl)
			node.prv(node.nl.nl)
			node.nr.prv(node)
			self.head = node
			return True
		else:
			node.nr.prv(node.nl)
			node.nl.nxt(node.nr)
			node.nxt(node.nl)
			node.prv(node.nl.nl)
			node.nl.nxt(node)
			node.nr.prv(node)
			return True

	# assimilates other list into self
	def assimilate(self, other):
		while other.head != None:
			self.inject(other.pop())
		other = None
		self.update()

	# copies list other into self; WIP
	def copy(self, start = None, end = None):
		output = super().__init__()
		if self.head == None:
			return output
		for cur in self:
			output.inject(int(cur))
		return output

	# BUBBLESORT
	def bubblesort(self):
		x = 0
		for i in range(len(self) - x):
			cur = self.tail
			while cur.nl != None:
				if(cur < cur.nl):
					self.shiftLeft(cur)
				else:
					cur = cur.nl
			x += 1
		self.update()
	#

	# QUICKSORT
	def quicksort(self, lo, hi):
		if lo < hi:
			p = self.qPartition(lo, hi)
			self.quicksort(lo, p - 1)
			self.quicksort(p + 1, hi)

	def qPartition(self, lo, hi):
		pivot = self[hi]
		i = lo - 1
		for j in range(lo, hi):
			if self[j] <= pivot:
				i += 1
				self[i].swap(self[j])
		self[i+1].swap(self[hi])
		return i + 1
	#

	# MERGESORT; WIP
	def mergesort(self):
		if len(self) >= 1:
			return self
		mid = len(self)/2
		left = self[0:mid]
		right = self[mid:]
		left.mergesort()
		right.mergesort()
		left.merge(right)
		self.merge(left)

	def merge(self, other):
		result = super().__init__()
		while self.head != None and other.head != None:
			if self.head <= other.head:
				result.inject(self.pop())
				self.update()
			else:
				result.inject(other.pop())
				other.update()
		while not self.isEmpty():
			result.inject(self.pop())
		while not right.isEmpty():
			result.inject(right.pop())
		return result
	#

	# HEAPSORT; WIP
	def heapsort(self):
		end = len(self)
		start = end // 2 - 1
		for i in range(start, -1, -1):
			self.heapify(end, i)
		for i in range(end - 1, 0, -1):
			self.swap(i, 0)
			self.heapify(i, 0)

	def heapify(self, end, i):
		l = 2*i + 1
		r = 2*i + 2
		max = i
		if l < end and self[i] < self[l]:
			max = l
		if r < end and self[max] < self[r]:
			max = r
		if max != i:
			self.swap(i, max)
			self.heapify(end, max)

	def swap(self, i, j):
		self[i], self[j] = self[j], self[i]

	#

	# SELECTION SORT
	def sel(self):
		for el in self:
			lo = el
			for cur in el:
				if lo > cur:
					lo = cur
			el.swap(lo)
	#

	# INSERTION SORT
	def ins(self):
		for i in range(1, len(self)):
			j = i + 1
			while j > 1 and self[j-1] > self[j]:
				self[j].swap(self[j-1])
				j -= 1

	#