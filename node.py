class Node(object):
	def __init__(self, cargo = None):
		# NODE LEFT
		self.nl = None
		# NODE CARGO
		self.car = cargo
		# NODE RIGHT
		self.nr = None
		# p - r are WIP
		#PARENT
		self.p = None
		#LEFTCHILD
		self.l = None
		#RIGHTCHILD
		self.r = None
		# //
		# NODE POSITION
		self.pos = 0

	def __str__(self):
		return str(self.car)

	def __int__(self):
		return int(self.car)

	def __iter__(self):
		here = self
		while here:
			yield here
			here = here.nr

	def __reversed__(self):
		here = self
		while here:
			yield here
			here = here.nl

	# self < other
	def __lt__(self, other):
		if self != None and other == None:
			return False
		elif(self == None and other != None):
			return True
		elif(self != None and other != None):
			return (int(self) < int(other))
		else:
			return False

	# self <= other
	def __le__(self, other):
		if self != None and other == None:
			return False
		elif(self == None and other != None):
			return True
		elif(self != None and other != None):
			return (int(self) <= int(other))
		else:
			return True

	# self >= other
	def __ge__(self, other):
		if self != None and other == None:
			return False
		elif(self == None and other != None):
			return True
		elif(self != None and other != None):
			return (int(self) >= int(other))
		else:
			return True

	# self > other
	def __gt__(self, other):
		if self != None and other == None:
			return True
		elif(self == None and other != None):
			return False
		elif(self != None and other != None):
			return (int(self) > int(other))
		else:
			return False

	# prnt(), lft() and rgt() are WIP
	def prnt(self, node=None):
		self.p = node

	def lft(self, node=None):
		self.l = node

	def rgt(self, node=None):
		self.r = node

	# node.next and node.prev methods
	def nxt(self, node=None):
		self.nr = node

	def prv(self, node=None):
		self.nl = node

	# swaps node self with node node2
	def swap(self, node2):
		self.car, node2.car = node2.car, self.car
