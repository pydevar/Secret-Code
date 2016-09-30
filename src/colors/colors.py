class Colors(object):

	def __init__(self):
		self.color={0: "imgs/default.png",
				   1: "imgs/blue.png",
				   2: "imgs/green.png",
				   3: "imgs/red.png",
				   4: "imgs/orange.png",
				   5: "imgs/pink.png",
				   6: "imgs/purple.png",
				   7: "imgs/white.png",
				   8: "imgs/yellow.png"}

	def get_color(self,id):

		return self.color.get(id)

	def get_dictionary(self):
		return self.color.iteritems()