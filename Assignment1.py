import random
import time

ListName = input("Enter a Name for list of programming languages you hope to learn:")
userList = []
userInput = input("\nEnter string to store in thematic list: ")
userList.append(userInput.capitalize())


while True:
    userInput = input("Enter another value or enter 'q' for exit: ")
    if userInput.lower() == 'q':
        break;
    else:
        userList.append(userInput.capitalize())

print('Your list details : \n', ListName, ": " , userList)

userListLen = []
for ele in userList:
    userListLen.append(len(ele))
print("\nThe length of each element in your list is: ")

for l in range(0,len(userList)-1):
    print(userList[l],": ", userListLen[l])




random_num = random.randint(0, len(userList) - 1)
print("\n\nNow is time to play a game. Enter a character of your choice to search in the list you just created. \n" \
      "Search engine will randomly select one item then will check if the character you entered found in the item of your list\n" \
      "Lets play :)")
char = input("Enter a character: ")

if char.lower() in userList[random_num] or char.upper() in userList[random_num]:
    print("Searching...Please wait")
    time.sleep(3)
    print("\nThe character you enetered found in the ",ListName,"list by randomly selected index",userList[random_num])
else:
    print("\nThe character you enetered NOT found in the ",ListName,", randomly selected index",userList[random_num])
