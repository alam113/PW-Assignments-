#!/usr/bin/env python
# coding: utf-8

# In[1]:


d = {}


# In[2]:


type(d)


# In[5]:


d1 = {'key' : "alam"}


# In[6]:


d1


# In[8]:


d2 = {'name' :"Moien", 'email' : "dshfuhfu@gmail.com", "number":26891}


# In[9]:


d2


# In[10]:


d3 = {234 : "sudh"}


# In[11]:


d3


# In[12]:


d4 = {234:"sudh", "@fail" : "kumar", True : 232425}


# In[13]:


d4


# In[14]:


d4[234]


# In[16]:


d4[True]


# In[17]:


d4[1]


# In[20]:


d5 = {'name':"Moien", 'mail_id':"njdfhds@vhdu", "name":"Dhingana"}


# In[21]:


d5


# In[23]:


d5['name']


# In[24]:


d6 = {"company" : "pwskills", "courses" : ['web dev', "data science", "java with DSA"]}


# In[25]:


d6


# In[29]:


d6["courses"][2]


# In[34]:


d7 = {"number" : [12,34,3,34,25], "assignments" : (1,2,3,4,5,6), "launch_date" : {28,12,14}}


# In[35]:


d7


# In[37]:


d7['mentor'] = ["sudhanshu","krish","anurag", "haider"]


# In[38]:


d7


# In[40]:


del d7['number']


# In[41]:


d7


# In[43]:


list(d7.keys())


# In[44]:


d7.values()


# In[45]:


d6.items()


# In[46]:


list(d6.items())


# In[48]:


d7.pop('assignments')


# In[49]:


d7


# In[51]:


d7.pop()


# ### Decision Making

# In[62]:


marks = int(input("enter your marks "))

if marks >= 80:
    print("you will be part A0 batch")
elif marks >= 60 and marks <80:
    print("you will be a part A1 batch")
elif marks >= 40 and marks <60:
    print("you will a part of A2 Batch")
else :
    print("you will be a part of A3 Batch")
    


# In[58]:


10 >= 80


# In[64]:


price = int(input("enter the price "))
if price > 1000:
    print("i will not purchase")
else :
    print("i will purchase")


# In[71]:


price = int(input("enter the price "))
if price > 1000:
    print("i will not purchase")
    if price > 5000:
        print("this is too much")
    elif price < 2000:
        print("it's OK")
elif price < 1000:
    print(" i'll purchase")
else :
    print("not interested")


# In[78]:


l = [1,2,3,4,5,6,7,8]


# In[79]:


l


# In[80]:


l[0] + 1


# In[81]:


l1 = []


# In[82]:


l1.append(l[0]+1)


# In[83]:


l1


# In[84]:


l = [1,2,3,4,5,6,7,8]


# In[89]:


l1 = []
for i in l :
    print(i+1)
    l1.append(i+1)
l1


# In[90]:


l


# In[91]:


l = ["sudh", "kumar", "pwskills", "course"]


# In[95]:


l1 = []
for i in l:
    print(i)
    l1.append(i.upper())


# In[96]:


l1


# In[97]:


l = [1,2,3,4,5,"sudh", "kumar", 324.25, 325, "abc"]


# In[100]:


l1_num = []
l2_str = []
for i in l:
    if type(i) == int or type(i) == float :
        l1_num.append(i)
    else:
        l2_str.append(i)


# In[102]:


l1_num


# In[104]:


l2_str


# In[ ]:




