exp = [2340,2500,2100,3100,2900]
total = 0
for i in range(len(exp)):
    print("month:",(i+1),"Expense:",exp[i])
    total = total + exp[i]
    print('Total expense is :',total)



for  i in range (1,10):
    if i%2==0:
        continue
    print(i*i)





# cal = cal.month(2016,1)
# print(cal)













key_location = "chair"
location = ["garage","living room", "chair", "closet"]
for i in location:
    if i==key_location:
        print("key is not found in ",i)
        break
    else:
        print("key is not found in ",i)
