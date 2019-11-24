
import alex


class task:
	def __init__(t,d,p):
		self.time = t
		self.deadline = d
		self.profit = p

def main():
	test1 = [[2,4,1],[1,3,2],[2,2,2]]
	print(alex.tasks(test1,len(test1),4));

	test2 = [[2,5,2],[3,7,8],[1,3,1],[2,2,2],[3,4,2],[1,4,2],[3,6,4],[2,5,3]]
	print(alex.tasks(test2,len(test2),7));
	print("hello")



if __name__ == '__main__':
	main()