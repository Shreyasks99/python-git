'''3.	Write a program to determine the work hours of the day entered based on the timetable provided below.

Mon	Tue	Wed	Thu	Fri	Sat	Sun
3	3	3	3	3	3	0
2	2	2	2	2	1	0
2	2	2	1	1	0	0
'''	

list_1 = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

list_2 = [3,3,3,3,3,3,0]
list_3 = [2,2,2,2,2,1,0]
list_4 = [2,2,2,1,1,0,0]

name = input("Enter the name of the day:")

nam = list_1.index(name)

lst = [i for i in zip(list_2,list_3,list_4)]

print(lst[nam])



