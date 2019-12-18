users=[]
posts=[]

Email = input("Email - ")
if Email == 'basseldahleh@gmail.com':
	print("Hey Bassel")

Password = input("Password - ")
if Password == '1234':
	print("You logged in!")

class User():
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		self.posts=[]

	def add_friend(self,email):
		self.friends_list.append(email)
		print(self.name+ " has added "+email+' as a friend')

	def remove_friend(self,email):
		self.friends_list.remove(email)
		print(self.name + " has added "+email+' as a friend')

	#def add_post(self,post_text,date):
		self.date = date
		self.post_text = post_text
		post1=Post(0, text,self.email)
		author=self.name
		posts.append(post1)
		print(self.name+' has posted '+ post_text + date)

	def create_comment(self,comment_text):
		self.comment_text=comment_text
		comment1=Post()
		self.comments.append(comment1)

	def get_userinfo(self):
		print('name: ' + self.name)
		print(' email: ' + self.email)
		print(' password: ' + self.password)
		print(' friends: ' + str(self.friends_list))
		print('posts' + str(self.posts))


class Post():
	def __init__(self,post_text,date):
		self.post_text=post_text
		self.date=date
		self.comments=[]
		self.like = 0
	def post(self):
		posts.append(post_text)
	def like_(self):
		self.liked_posts.append(self.like)
		self.like = self.like + 1

	def post_date(self):
		print('posted on ' + self.date)


class comment(Post):
	def __init__(self,comment_text):
		self.comment_text=comment_text

	def create_comment(self):
		self.comments.append(comment_text)
		print('your comment is ' + self.comment_text)

	def remove_comment(self):
		self.comments.remove(comment_text)

	def edit_comment(self,new_comment):
		self.comment_text=new_comment
		print('your comment has been changed!')


user1 = User("bassel","basseldahleh@gmail.com","1234")
user2= User("shir","shirbart@gmail.com", "1234")
#user1.add_friend
#user2.add_post("25 December", "at the beach")
