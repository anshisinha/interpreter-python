from dataclasses import dataclass

@dataclass
#the parser will build up a tree 
#this class is created for the number node in the tree
class NumberNode:
	value: any

	#representation constructor which will 
	#return the value as a string
	def __repr__(self):
		return f"{self.value}"

@dataclass
#operation classes
#class for adding 2 nodes together
class AddNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}+{self.node_b})"

@dataclass
#class for subtracing
class SubtractNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}-{self.node_b})"

@dataclass
#class for Multiplying
class MultiplyNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}*{self.node_b})"

@dataclass
#class for division
class DivideNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}/{self.node_b})"

#classes for terms like +4, -5
@dataclass
class PlusNode:
	node: any

	def __repr__(self):
		return f"(+{self.node})"

@dataclass
class MinusNode:
	node: any

	def __repr__(self):
		return f"(-{self.node})"
		


