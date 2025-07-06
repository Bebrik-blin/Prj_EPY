#import libs

class point:

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
	def sum_point_to_point(self, x1, y1, z1):
		sx = self.x+x1
		sy = self.y+y1
		sz = self.z+z1
		spoint = point(sx, sy, sz)

		return(spoint)

	def dev_point_to_point(self, x1, y1, z1):
		sx = self.x-x1
		sy = self.y-y1
		sz = self.z-z1
		spoint = point(sx, sy, sz)

		return(spoint)

	def draw(self):
		print(self.x, self.y, self.z)

class vector:

	def __init__(self,x, y, z, xf, yf, zf):
		self.x = x
		self.y = y
		self.z = z
		self.xf = xf
		self.yf = yf
		self.zf = zf

	def sum_vector_to_point(self, x1f, y1f, z1f):
		sxf = self.xf+x1f
		syf = self.yf+y1f
		szf = self.zf+z1f
		svector = vector(self.x, self.y, self.z ,sxf, syf, szf)
		
		return(svector)
	
	def dev_vector_to_vector(self, x1f, y1f, z1f):
		sxf = self.xf-x1f
		syf = self.yf-y1f
		szf = self.zf-z1f
		svector = vector(self.x, self.y, self.z ,sxf, syf, szf)

	def draw(self):
		print(self.xf, self.yf, self.zf)
