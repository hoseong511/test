#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Employee(object):
    def __inti__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@schoolofweb.net'
        
    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * 1.1)
        



# In[ ]:




