#Understand the Problem
'''
input: (int) 6 numbers from the user
output: (string) message that describes whether the sixth number appears among the first five.
explicit rules:
-6th number is compared to the other 5 numbers
implicit rules:
remaining questions:
-What if the user enters a non int value?
'''
#Write Examples and Test Cases
'''
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23.

Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 18

18 isn't in 25,15,20,17,23.
observations:
don't plan on non int input from the user
'''
#Data Structure
'''
list []
'''
#Algorithm
'''
1. Get 6 different inputs from the user
2. Compare the final input to other 5 inputs
3. Print message to screen.

Set a input_list to empty
    ask the user for input
    append input to list
    repeat 5 times
ask user for final input
compare final input to input list
print message to screen
'''
input_list = []
input_list.append(input("Please enter the 1st number: "))
input_list.append(input("Please enter the 2nd number: "))
input_list.append(input("Please enter the 3rd number: "))
input_list.append(input("Please enter the 4th number: "))
input_list.append(input("Please enter the 5th number: "))
final_num = input("Please enter the final number: ")
if final_num in input_list:
    print(f"{final_num} is indeed in {' '.join(input_list)}")
else:
    print(f"{final_num} is not in {' '.join(input_list)}")

