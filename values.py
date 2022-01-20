#this class will hold the different value types 
#which interpreter is able to produce
from dataclasses import dataclass

@dataclass
class Number:
	value: any

	def __repr__(self):
		return f"{self.value}"