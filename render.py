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

		return(rewfigurs)

	def redraw(self):
		self.screen.fill(s.BLACK)
			


	def start(self):
		screen = pygame.display.set_mode(self.width)
		self.screen = screen
		self.

		while self.running:
			for e in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

		pygame.quit()
