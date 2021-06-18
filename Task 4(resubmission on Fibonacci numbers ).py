#!/usr/bin/env python
# coding: utf-8


# In[17]:


# Write a Python Program for Fibonacci numbers.
n_terms = int(input("number of terms (Should be greater than zero): "))
#n1= first digit, n2= second digit, initial_terms = no of terms in the series at starting
n1,n2=0,1
initial_terms=0
if n_terms == 1: 
   print("Fibonacci sequence upto {} term is: ".format(n_terms), n1)
else:
   print("Fibonacci numbers upto {} term is :".format(n_terms))
   while initial_terms < n_terms:
       print(n1)
       n3 = n1 + n2
       n1 = n2
       n2 = n3
       initial_terms += 1


# In[ ]:




