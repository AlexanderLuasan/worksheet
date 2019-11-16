
import alex


class task:
	def __init__(t,d,p):
		self.time = t
		self.deadline = d
		self.profit = p

def main():
	test1 = [[2,4,1],[1,3,2],[2,2,2]]
	print(alex.tasks(test1,len(test1),5));
	print("hello")



if __name__ == '__main__':
	main()