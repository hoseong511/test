#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Employee(object):
    
    raise_amount = 1.1
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@schoolofweb.net'
        
    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Sanghee', 'Lee', 50000)
emp_2 = Employee("minjung", 'kim', 60000)

emp_1.raise_amount = 1.2
print (emp_1.pay , "인상률 ", (emp_1.raise_amount - 1) * 100 , "%")
emp_1.apply_raise()
print (emp_1.pay)

print(emp_2.pay, "인상률 ", (emp_2.raise_amount - 1) * 100 , "%")
emp_2.apply_raise()
print(emp_2.pay)

