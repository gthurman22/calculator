#!/usr/bin/env python
# coding: utf-8

# In[22]:


num1 = float(input("Enter the first number: "))
op = input("Enter Operator: ")
num2 = float(input("Enter the second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
        print(num1 / num2)
elif op == "*":
        print(num1 * num2)
else:
                print("Invalid operation")
        #What we're doing is getting the input from user, and using if statements to see if they want addition, division, etc.
        #operator = +, -, *, /


# In[ ]:




