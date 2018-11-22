no_of_processes=0
theFile = open("sjf.txt" , "r")
theInts = []
for val in theFile.read().split():
	theInts.append(int(val))
	no_of_processes = no_of_processes + 1
theFile.close()
print(no_of_processes)
div = int(no_of_processes/3)
process = [0]*div
arrival_time = [0]*div
burst_time = [0]*div
p=0
a=0
b=0
for i in range(no_of_processes):
	if i%3==0:
		process[p] = theInts[i]
		p = p + 1
	if i%3==1:
		arrival_time[a] = theInts[i]
		a = a+1
	if i%3==2:
		burst_time[b] = theInts[i]
		b=b+1
for i in range(div):
	print(process[i] ,  end=" ")
print("\n")
for i in range(div):
	print(arrival_time[i] ,  end=" ")
print("\n")
for i in range(div):
	print(burst_time[i] ,  end=" ")
print("\n")

check=0
turnaround_time=0;
check_wasse =0
temp=0
count=0	
average_turnaround_time=0
for i in range(no_of_processes):
	if i==0:
		check = check +arrival_time[0] +burst_time[0]
	else:
		check=check+burst_time[i]
	turnaround_time = check-arrival_time[i]
	check_wasse=check-(no_of_processes-i)
	count=0
	x=i
	while arrival_time[x]<=check and x<no_of_processes and check<=(arrival_time[no_of_processes-1]+burst_time[i]):
		count=count+1
		x=x+1
	if count+i+1 == no_of_processes or count+i+1 > no_of_processes:
		j=i+1
		for j in range(no_of_processes):
			y=burst_time[j]
			k=j+1	
			for k in range(no_of_processes):
				if y>burst_time[k]:
					temp=burst_time[k]
					burst_time[k]=burst_time[j]
					burst_time[j]=temp
					temp=arrival_time[k]
					arrival_time[k]=arrival_time[j]
					arrival_time[j]=temp
					temp=process[k]
					process[k]=process[j]
					process[j]=temp
	else:
		j=i+1
		count1=count+i+1
		for j in range(count1):
			y=burst_time[j]
			k=j+1	
			for k in range(count1):
				if y>burst_time[k]:
					temp=burst_time[k]
					burst_time[k]=burst_time[j]
					burst_time[j]=temp
					temp=arrival_time[k]
					arrival_time[k]=arrival_time[j]
					arrival_time[j]=temp
					temp=process[k]
					process[k]=process[j]
					process[j]=temp
	average_turnaround_time = average_turnaround_time +turnaround_time		
print("average turnaround time: ", average_turnaround_time)		
