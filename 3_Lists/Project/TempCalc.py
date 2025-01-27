'''
Topic: Array and List based Python project
Task: Take three inputs from user: 
    1.  Number of days
    2.  Each day's temperature
Output: There should be two outputs:
    1.  Average Temperature of those days
    2.  How many days had higher than average temperature

'''

#taking user inputs
days=int(input("How many day's temperature do you have: "))
collector=[]

for day in range(1,days+1):
    temp=int(input(f"What is the temperature of Day {day}: "))
    collector.append(temp)


#computing the average and the count of days where temp is higher than average temp
average_temp=sum(collector)*1.00/len(collector)
above_avg=[x for x in collector if x>average_temp]

#printing out the results
print(f"The average temperature of {days} days is: "+str(average_temp))
print(f"Number of days with temperature above average: "+str(len(above_avg)))