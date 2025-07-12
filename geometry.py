#
#Оставь надежду, всяк сюда входящий. Я сам не знаю как в этом работать

class point:

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
	def sum_point_to_point(self, p):
		sx = self.x+p.x
		sy = self.y+p.y
		sz = self.z+p.z
		nvector = vector(sx, sy, sz)

		return(nvector)

	def dev_point_from_point(self, p):
		sx = self.x-p.x
		sy = self.y-p.y
		sz = self.z-p.z
		nvector = vector(sx, sy, sz)

		return(nvector)
	
	def sum_vector_to_point(self, v):
		sx = self.x+v.xf
		sy = self.y+v.yf
		sz = self.z+v.zf
		npoint = point(sx, sy, sz)
		
		return(npoint)
	
	def dev_vector_from_point(self, v):
		sx = self.x-v.xf
		sy = self.y-v.yf
		sz = self.z-v.zf
		npoint = point(sx, sy, sz)
	
		return(npoint)

	def draw(self):
		return(self.x, self.y, self.z)

class vector:

	def __init__(self, xf, yf, zf):
		self.xf = xf
		self.yf = yf
		self.zf = zf
	
	def sum_vector_to_vector(self, v):
		sxf = self.xf+v.xf
		syf = self.yf+v.yf
		szf = self.zf+v.zf
		svector = vector(sxf, syf, szf)
		return(svector)
	
	def dev_vector_from_vector(self, v):
		sxf = self.xf-v.xf
		syf = self.yf-v.yf
		szf = self.zf-v.zf
		svector = vector(sxf, syf, szf)
		return(svector)

	def draw(self):
		return(self.xf, self.yf, self.zf)
