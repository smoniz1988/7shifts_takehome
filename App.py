"""
Hello! Hope all is well and that everyone is staying safe.
Thank you for the opportunity to take this technical interview!
start time: 2:44 pm
end time: 3:48 pm
"""
from StringCalculator import StringCalculator

print("-----------------------------------------------")
print("Empty strings should return 0")
print("Passed" if StringCalculator.add("") == 0 else "Failed")
print("-----------------------------------------------")

print("1,2,5 Expected Result 8")
print("Passed" if StringCalculator.add("1,2,5") == 8 else "Failed")
print("-----------------------------------------------")

print("Change Add Method to handle new lines. Example \"1\\n,2,3\" Result = 6")
print("Passed" if StringCalculator.add("1\n,2,3") == 6 else "Failed")
print("-----------------------------------------------")

print("Example 2 \"1,\\n2,4\" Result = 7")
print("Passed" if StringCalculator.add("1,\n2,4") == 7 else "Failed")
print("-----------------------------------------------")

print("Format //delimiter\\n delimiter separated numbers. Example: //;\\n1;3;4")
print("Passed" if StringCalculator.add("//;\n1;3;4") == 8 else "Failed")
print("-----------------------------------------------")

print("Another example: //$\\n1$2$3 Result:6")
print("Passed" if StringCalculator.add("//$\n1$2$3") == 6 else "Failed")
print("-----------------------------------------------")

print("Another example: //@\\n2@3@8 Result:13")
print("Passed" if StringCalculator.add("//@\n2@3@8") == 13 else "Failed")
print("-----------------------------------------------")

print("Calling Add with negative numbers should throw exception")
try:
    StringCalculator.add("5, -100, 85, -3")
except Exception as e:
    print(str(e))
print("-----------------------------------------------")

print("Numbers >1000 should be ignored e.g 2, 1001 Result 2")
print("Passed" if StringCalculator.add("2,1001") == 2 else "Failed")
print("-----------------------------------------------")

print("Arbitrary Length Delim: e.g. //***\\n1***2***3 Result 6")
print("Passed" if StringCalculator.add("//***\n1***2***3") == 6 else "Failed")
print("-----------------------------------------------")

print("Allow for multiple delimeters (arbitrary length) e.g. //$,@\\n1$2@3 Result 6")
print("Passed" if StringCalculator.add("//$,@\n1$2@3") == 6 else "Failed")
print("-----------------------------------------------")


