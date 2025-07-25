#
#Оставь надежду, всяк сюда входящий. Я сам не знаю как в этом работать

#Создаём класс точки, у неё 3 параметра x, y, z
class point:

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
	#Сумма\разность точек даёт вектор
	def add_point_to_point(self, p):
		sx = self.x+p.x
		sy = self.y+p.y
		sz = self.z+p.z
		nvector = vector(sx, sy, sz)

		return(nvector)

	def sub_point_from_point(self, p):
		sx = self.x-p.x
		sy = self.y-p.y
		sz = self.z-p.z
		nvector = vector(sx, sy, sz)

		return(nvector)
	
	#Сумма\разность точки и ветора даёт точку
	def add_vector_to_point(self, v):
		sx = self.x+v.xf
		sy = self.y+v.yf
		sz = self.z+v.zf
		npoint = point(sx, sy, sz)
		
		return(npoint)
	
	def sub_vector_from_point(self, v):
		sx = self.x-v.xf
		sy = self.y-v.yf
		sz = self.z-v.zf
		npoint = point(sx, sy, sz)
	
		return(npoint)

	#Функция возврата
	def draw(self):
		return(self.x, self.y, self.z)

#Класс вектора, принимает x, y, z
class vector:

	def __init__(self, xf, yf, zf):
		self.xf = xf
		self.yf = yf
		self.zf = zf
	
	#Сумма/разность векторов даёт вектор
	def add_vector_to_vector(self, v):
		sxf = self.xf+v.xf
		syf = self.yf+v.yf
		szf = self.zf+v.zf
		svector = vector(sxf, syf, szf)
		return(svector)
	
	def sub_vector_from_vector(self, v):
		sxf = self.xf-v.xf
		syf = self.yf-v.yf
		szf = self.zf-v.zf
		svector = vector(sxf, syf, szf)
		return(svector)

	#Функция возврата
	def draw(self):
		return(self.xf, self.yf, self.zf)

#Класс 2д вектора, принимает x, y
class vector_plain:

	def __init__(self, xp, yp):
		self.x = xp
		self.y = yp

	#Функция возврата
	def draw(self):
	 	return(self.x, self.y)

#Класс мат.функций, не имеет переменных которые надо создать в конструкторе, пока нет
class math:

	def __init__():
		#Опа, а тут нихуя нет
		pass

	#Функция перевода вектора из 3д в 2д(рабочая)
	def vector_to_plain(v):

		xp = v.yf*v.zf
		yp = v.xf*v.zf*(-1)
		n = vector_plain(xp, yp)
		return(n)
	
	#Допилим другие ф-ции по мере надобности
