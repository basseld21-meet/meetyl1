import Turtle

class ball(Turtle):
	def __init__(self,radius,color,dx,dy):
		Turtle.__init__(self):
		self.radius = radius
		self.color = color
		self.dx = dx
		self.dy = dy
		self.penup()
		self.shape(cuircle)
		self.size(radius/10)
	def move(self,screen_width,screen_height)
		current_x = X
		new_x = current_x + dx
		current_y = Y
		new_y = current_y + dy
		right_side_ball= new_x + radius 
		
