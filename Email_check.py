# Email= input("Enter your Email :- ")
# k,j,d=0,0,0
# if len(email)>=6:
#     if email[0].isalpha():  #2
#         if ("@l" in email ) and (email.count("@")==1):  #3
#             if(email[-4]==".")^ (email[-3]=="."): 
#                 for i in email:
#                     if i==i.isspace():
#                         k=1
#                     elif i.isalpha():
#                         if i.isupper():
#                             j=1
#                     elif i.isdigit():
#                         continue
#                     elif i in "_@.":
#                         continue
#                     else:
#                         d=1

#                 if k==1 or j==1 or d==1:
#                     print("Wrong Email 5")
#             else:
#                 print("  wrong Email 4")
#         else:
#             print("wrong Email 3")
#     else:
#         print("Wrong Email 2")    
# else:
#     print("wromg Email 1 ")
                      


email = input("Enter your Email :- ")
k, j, d = 0, 0, 0

if len(email) >= 6:
    if email[0].isalpha():  # Check if the first character is a letter
        if ("@" in email) and (email.count("@") == 1):  # Check if there is exactly one "@" symbol
            if (email[-4] == ".") ^ (email[-3] == "."):  # Check if the domain ends with ".xxx" or ".xx"
                for i in email:
                    if i.isspace():  # Check for any spaces
                        k = 1
                    elif i.isalpha():  # Check if the character is a letter
                        if i.isupper():  # Check if the letter is uppercase
                            j = 1
                    elif i.isdigit():  # Check if the character is a digit
                        continue
                    elif i in "_@.":  # Allowable special characters
                        continue
                    else:  # Any other character is invalid
                        d = 1

                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email 5")
                else:
                    print("Valid Email")
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")

            