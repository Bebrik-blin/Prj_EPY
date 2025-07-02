import libs

class point:

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def draw(self):
		print(x, y, z)

class vector:

	def __init__(self, cords[3]):
		self.cords[3] = cords[3]

	def SumVectorToVector(self, cords1[3]):
		svector = vector(cords[0] + cords1[0], cords[1] + cords1[1], cords[2] + cords1[2])
		return(svector)

	def draw(self):
		print(cords[3])