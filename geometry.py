#import libs
#Оставь надежду, всяк сюда входящий. Я не знаю как в этом работать

class point:

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
	def sum_point_to_point(self, x1, y1, z1):
		sx = self.x+x1
		sy = self.y+y1
		sz = self.z+z1
		nvector = vector(sx, sy, sz)

		return(nvector)

	def dev_point_to_point(self, x1, y1, z1):
		sx = self.x-x1
		sy = self.y-y1
		sz = self.z-z1
		nvector = vector(sx, sy, sz)

		return(nvector)

	def draw(self):
		return(self.x, self.y, self.z)

class vector:

	def __init__(self, xf, yf, zf):
		self.xf = xf
		self.yf = yf
		self.zf = zf

	def sum_vector_to_point(self, x1f, y1f, z1f):
		sxf = self.xf+x1f
		syf = self.yf+y1f
		szf = self.zf+z1f
		npoint = point(sxf, syf, szf)
		
		return(npoint)
	
	def dev_vector_to_vector(self, x1f, y1f, z1f):
		sxf = self.xf-x1f
		syf = self.yf-y1f
		szf = self.zf-z1f
		svector = vector(sxf, syf, szf)

	def draw(self):
		return(self.xf, self.yf, self.zf)
