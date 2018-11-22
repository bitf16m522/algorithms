no_of_processes=0
theFile = open("new.txt", "r")
theInts = []
count=0
for val in theFile.read().split():
	theInts.append(int(val))
	no_of_processes= no_of_processes+1	
theFile.close()
print(no_of_processes)
div=int(no_of_processes/2)
arrival_time = [0]*div
burst_time = [0]*div
waiting_time=0
waiting_check=0
average_waiting_time=0
turnarount_check=0
turnarount_time=0
average_turnarount_time=0
r=0
e=0
for i in range(no_of_processes):
	if i%2!=0:
		burst_time[r]=theInts[i]
		r=r+1
	else:
		arrival_time[e]=theInts[i]
		e=e+1
for i in range(div):
	print(arrival_time[i] , end=" ")
print("\n")
for i in range(div):
	print(burst_time[i], end=" ")
j=0
	
for i in range(arrival_time[len(arrival_time)-1]+1):
	if i==arrival_time[j]:
		if j==0:
			turnarount_check = turnarount_check+i+burst_time[j]
			waiting_check = waiting_check + i
		else:
			turnarount_check = turnarount_check + burst_time[j]
			waiting_check = waiting_check + burst_time[j-1]
		waiting_time = waiting_check - arrival_time[j]
		average_waiting_time=average_waiting_time+waiting_time		
		turnarount_time = turnarount_check - arrival_time[j]
		average_turnarount_time = average_turnarount_time + turnarount_time		
		j=j+1
print("average wating time is ",average_waiting_time / div)	
print("average turnarount time is ",average_turnarount_time / div)	
