#strings


var1 = 'Hello World!'
var2 = "Python Programming"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

#tuple


tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print ("tup1[0]: ", tup1[0]);
print ("tup2[1:5]: ", tup2[1:5]);



#adding item to a set


Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
 
Days.add("Sun")
print(Days)


#removing items from set


Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
 
Days.discard("Sun")
print(Days)


#creating a set


Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
print(Days)
print(Months)
print(Dates)


#union of sets


DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA|DaysB
print(AllDays)


#intersection of sets



DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA & DaysB
print(AllDays)


#compare sets



DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)



#dictionary


dict = {'Name': 'Catherine shijehi', 'Age': 20, 'Nationality': 'Kenyan', 'Address': '25546',}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
print ("dict['Nationality']: ", dict['Nationality'])
print ("dict['Address']: ", dict['Address'])