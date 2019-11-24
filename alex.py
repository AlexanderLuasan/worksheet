


#A = list of task
#n =  number of tasks
#totalTime = the max time given to the whole tasks
taskList = None #
data = {}
def tasks(A,n,totalTime):
	global taskList
	taskList=None
	global data
	data.clear()
	taskList=A
	sortlist = []
	#sort by endtime
	print("in:",taskList)
	for i in range(len(taskList)):
		sortlist.append(tuple([taskList[i][1],taskList[i]]))
	sortlist.sort();
	taskList.append(None)
	for i in range(len(sortlist)):
		taskList[i+1] = sortlist[i][1]
	taskList[0] = None
	print("processed:",taskList)

	for d_l in range(totalTime+1):
		for n_o_t in range(len(taskList)):
			data[(n_o_t,d_l)] = subProblem(n_o_t,d_l)
	print("data:",data)
	#print(backTrack(len(taskList)-1,totalTime))
	return backTrack(len(taskList)-1,totalTime)

def backTrack(tasks,deadline):
	Done = False
	endingTasks = []
	while not Done:

		location=data[(tasks,deadline)]
		direction = location[1]
		print(tasks,deadline,direction)
		if(direction == 'U'):
			tasks-=1
		if(direction == 'L'):
			deadline-=1
		if(direction == 'J'):
			tasks-=1
			deadline-=taskList[tasks+1][0]

			endingTasks.append(taskList[tasks+1])

		if(tasks == 0 or deadline == 0):
			return endingTasks

#numberOftasks = only consider the first n tasks
#
def subProblem(numberOftasks,deadline):
	if(numberOftasks==0):
		return [0,'U']
	
	#check the deadline
	if(taskList[numberOftasks][1]<deadline):
		up = 0
		try:
			up = data[(numberOftasks-1,deadline)][0]
		except KeyError:
			pass
		left = 0
		try:
			left = data[(numberOftasks,deadline-1)][0]
		except KeyError:
			pass
		if(up>left):
			return [up,"U"]
		else:
			return [left,"L"]
	else:
		jump = -1000
		try:
			jump = data[(numberOftasks-1,deadline - taskList[numberOftasks][0])][0]
			jump += taskList[numberOftasks][0]
		except KeyError:
			pass
		up = 0
		try:
			up = data[(numberOftasks-1,deadline)][0]
		except KeyError:
			pass
		left = 0
		try:
			left = data[(numberOftasks,deadline-1)][0]
		except KeyError:
			pass
		if(jump>=up and jump>=left):
			return [jump,"J"]
		elif(up>left):
			return [up,"U"]
		else:
			return [left,"L"]