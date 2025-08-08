import setts as s

class render:

	def __init__(self):

		s.p.init()

		self.width = s.width
		self.running = True
		self.file_name = s.file_name
		self.framerate = s.frames

	def reader(self):
		rewfigurs = []

		with open(self.file_name, "r") as file:
			for line in file:
				nstr = file.readline()
				if(nstr[0] == "#"):
					pass

				else:
					rewfigurs.append(line)
		
		finv = []
		for i in rewfigurs:
			mv = []
			s = i[1, ]
			mv = s.split(";")
			finv.append(mv)
		
		return(finv)

	def redraw(self, renf):
		self.screen.fill(s.BLACK)
		for i in renf:
			s.pygame.draw.line(self.screen, s.WHITE, [0, 0, 0], s.geometry.math.vector_to_plain(s.geometry.vector(i)))
			


	def start(self):
		screen = s.pygame.display.set_mode(self.width)
		self.screen = screen
		renf = render.reader(self)

		while self.running:
			for e in s.pygame.event.get():
				if s.pygame.event.type == s.pygame.QUIT:
					self.running = False
				
				else:
					render.redraw(renf)

		s.pygame.quit()
