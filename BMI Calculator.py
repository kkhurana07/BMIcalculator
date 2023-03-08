#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator

# https://mercer-health.com/#:~:text=Body%20Mass%20Index%2C%20or%20BMI,inches%20x%20height%20in%20inches
#     

# In[ ]:


name = input("Enter your name: ")
weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)

if BMI > 0:
    if (BMI < 18.5):
        print(name +", you are underweight.")
    elif (BMI <= 24.9):
        print(name +", you are normalweight.")
    elif (BMI < 29.5):
        print(name +", you are overrweight.")
    elif (BMI < 34.9):
        print(name +", you are obese.")
    elif (BMI < 39.9):
        print(name +", you are severly obese.")
    else:
        print(name +", you are morbidly obese.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




