


#A = list of task
#n =  number of tasks
#totalTime = the max time given to the whole tasks
taskList = None #
data = {}
def tasks(A,n,totalTime):
	taskList=A
	print("test")


#numberOftasks = only consider the first n tasks
#
def subProblem(numberOftasks,deadline):
	
	#check the deadline
	if(taskList[numberOftasks][1]>deadline):
		up = data[(numberOftasks-1,deadline)][0]
		left = data[(numberOftasks,deadline-1)][0]
		if(up>left):
			return [up,"U"]
		else:
			return [left,"L"]
	else:
		jump = data[(numberOftasks-1,deadline - taskList[numberOftasks][0])][0]
		jump += taskList[numberOftasks][0]
		up = data[(numberOftasks-1,deadline)][0]
		left = data[(numberOftasks,deadline-1)][0]
		if(jump>up and jump>left):
			return [jump,"J"]
		else if(up>left):
			return [up,"U"]
		else:
			return [left,"L"]