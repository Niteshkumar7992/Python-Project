indian = ["samosa ","daal","naan","puri sabji"]
chinese = ["egg role","pot sticker","fried rice"]
italian = ["pizza","pasta", "risotto"]
dish  = input("Enter a dish name : ")
if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")

elif dish in italian:
    print("italian")
else: 
    print("Based on little knowledge I have don know which cuisine is ",dish)        