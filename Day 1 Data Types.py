#!/usr/bin/env python
# coding: utf-8

#  Python Fundamental Data Types - immutable

# In[1]:


print("Welcome")


# In[2]:


a=10
type(a)


# In[3]:


a=10
print(type(a))


# In[4]:


a=10
print(type(a))
print(a)


# In[5]:


a=10.0
type(a)


# In[6]:


print(a)


# In[7]:


b="python"
print(type(b))


# In[13]:


print(b)


# In[14]:


b='python'
print(b)
b='''python'''
print(b)
b="""python"""
print(b)


# In[15]:


a="true"


# In[16]:


type(a)


# In[17]:


a=True


# In[18]:


type(a)


# In[19]:


b='python'
print(b)
b='''python'''
print(b)
b="""python"""
print(b)


# In[20]:


a=False
type(a)


# In[21]:


a="""False"""
type(a)


# In[22]:


a=10
b=20
c=a>b
print(c)


# In[23]:


print(True+True)


# In[24]:


print(False+True+False)


# In[25]:


print(True-False)


# In[26]:


c=10+20i
print(c)


# In[27]:


c=10+20j
print(c)
print(type(c))


# In[28]:


a=10
print(id(a))


# In[29]:


b=10
print(id(b))


# In[30]:


a=20
print(id(a))


# In[31]:


s="Data Engineering"
print9s[-2]


# In[32]:


s="Data Engineering"
print(s[-2])


# In[33]:


s[2]


# In[34]:


s[0:4]


# Slicing and Indexing

# In[35]:


s="abcdefghijklmnopqrstuvwxyz"
s[13:16]


# In[36]:


s[12:16]


# In[37]:


s[12:15]


# In[38]:


s[-3:-1]


# In[39]:


s[-3:]


# In[40]:


s[:14]


# In[41]:


s[3:1000]


# In[44]:


s[-1000:-3]


# Python Operators

# Arithmetic Operators
# Relational or Comparison Operators
# Logical Operators

# In[45]:


a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)


# In[46]:


a=3
b=2
print(a/b)
print(a//b)


# In[47]:


a=3
b=2.0
print(a/b)
print(a//b)


# In[48]:


print(a%b)


# In[49]:


a=3
b=2
print(a%b)


# In[50]:


a=20
b=10
print(a>b)
print(a>=b)


# In[51]:


a=True
b=False
print(a and b)


# In[52]:


a=True
b=False
c=True
print(a and c)
print(b or c)
print(a or c)


# In[55]:


is_geological_survey_complete = True
is_environmental_clearance_received = True
is_market_demand_high = False


# In[56]:


should_start_drilling = is_geological_survey_complete and is_environmental_clearance_received and is_market_demand_high


# In[57]:


print(should_start_drilling)


# In[59]:


print("Should we start drilling?",should_start_drilling)


# In[60]:


# Boolean Variables
HasExplorationPermit = True
HasDrillingRights = True
HasEnvironmentalApproval = False
HasOilDiscovery = True

 

# Logical Operations
IsExplorationAllowed = HasExplorationPermit and HasDrillingRights and not HasEnvironmentalApproval
IsDiscoveryProfitable = HasOilDiscovery and (HasExplorationPermit or HasDrillingRights)


# In[61]:


print(IsExplorationAllowed)
print(IsDiscoveryProfitable)


# In[62]:


10+20


# In[63]:


"ten"+"twenty"


# In[64]:


"ten"*"twenty"


# In[65]:


10*20


# In[66]:


"ten"*20


# In[67]:


"ten"+10


# In[68]:


"ten"+'10'


# In[70]:


10**2


# List:
# 0. enclosed in [ ]
# 1. accepts heterogeneous objects
# 2. accepts duplicate values
# 3. mutable data type
# 4. Indexing and slicing are possible
# 5. Order is preserved

# In[71]:


a=[10,"python",10,19.5,True]
print(a)
print(type(a))


# In[72]:


a[0]


# In[73]:


a[-1]


# In[74]:


a[1:3]


# In[75]:


id(a)


# In[76]:


a.append(999)


# In[77]:


print(a)


# In[78]:


id(a)


# In[79]:


a.remove(10)


# In[80]:


print(a)


# Tuple:
# 1. Enclosed in ( )
# 2. Exactly same as LIST, only diff is tuple is immutable

# In[81]:


a=("Well A","2023-09-15","Pipeline",True,100,100)


# In[82]:


type(a)


# In[83]:


print(a)


# In[84]:


a[2]


# In[85]:


a[-4]


# In[86]:


a.append(777)


# In[87]:


name="naval"
dept="Data Engineer"
print("I am {} working as {}".format(name,dept))


# In[89]:


print(f"I am {name} working as {dept}")


# In[90]:


print("I am %s working as %s" %(name,dept))


# In[91]:


# Employee details
name = "John Doe"
job_title = "Senior Geologist"
department = "Geology"
email = "johndoe@email.com"
phone = "123-456-7890

Employee Information:
Name: John Doe
Job Title: Senior Geologist
Department: Geology
Email: johndoe@email.com
Phone: 123-456-7890

print(f"Employee Information:\nName: {name}\nJob Title: {job_title}\nDepartment: {department}\nEmail: {email}\nPhone: {phone}")


# In[93]:


# Employee details
name = "John Doe"
job_title = "Senior Geologist"
department = "Geology"
email = "johndoe@email.com"
phone = "123-456-7890"

print(f"Employee Information:\nName: {name}\nJob Title: {job_title}\nDepartment: {department}\nEmail: {email}\nPhone: {phone}")


# SET:
# 0. Enclosed in { }
# 1. Heterogeneous Object
# 2. Duplicates are not allowed
# 3. Order is not preserved
# 4. Slicing and Indexing are not possible
# 5. Mutable

# In[94]:


c={10,10.5,"Shell",True,True,10,10,10,"Python"}


# In[95]:


print(c)


# In[96]:


print(id(c))


# In[97]:


c.add(55)


# In[98]:


print(c)
print(id(c))


# Dictionary: dict
# 0. { }
# 1. Key Value
# 2. Heterogeneous Objects
# 3. Duplicate key is not allowed, duplicate value is accepted
# 4. Mutable

# In[105]:


d={"location":"WellA","Start_date":"2023-1-1","Duration":45,"End":True}


# In[106]:


type(d)


# In[107]:


print(d)


# In[108]:


d['location']="WellB"


# In[109]:


print(d)


# Membership Operators: in, not in

# In[110]:


xyz = ["hey","hie",10,12]
print("hey" in xyz)


# In[111]:


print("hey" not in xyz)


# In[112]:


print("heya" not in xyz)


# In[113]:


s="python"
print('p' in s)


# In[114]:


# List of Equipment
refineryEquipment = ["Crude Distillation Unit", "Catalytic Cracking Unit", "Hydrotreating Unit", "FCC Unit"]

 

# Membership Operator
IsUnitInstalled = "Hydrotreating Unit" in refineryEquipment
IsUnitObsolete = "Thermal Cracking Unit" not in refineryEquipment

 

print("Is Hydrotreating Unit installed?", IsUnitInstalled)
print("Is Thermal Cracking Unit obsolete?", IsUnitObsolete)


# In[115]:


employees = [
    "John Doe, Senior Geologist, Geology, johndoe@email.com, 123-456-7890",
    "Jane Smith, Drilling Engineer, Drilling, janesmith@email.com, 987-654-3210",
    "Bob Johnson, Reservoir Engineer, Reservoir Engineering, bobjohnson@email.com, 456-789-0123",
    "Alice Brown, Petrophysicist, Petrophysics, alicebrown@email.com, 789-012-3456"
]


# In[116]:


employees[0]


# In[117]:


employees.append("Eva Green, Drilling Technician, Drilling, evagreen@email.com, 111-222-3333")


# In[118]:


print(employees)


# Flow Control
# Selection Statement

# In[122]:


age=22
if(age>18):
    print("Eligible")
else:
    print("Not Eligible")


# In[123]:


current_fuel_level=input("enter current fuel level")
print(current_fuel_level)
print(type(current_fuel_level))


# In[126]:


low_fuel_threshold=1000
critical_fuel_threshold=500
current_fuel_level=int(input("enter current fuel level"))


# In[127]:


if(current_fuel_level<critical_fuel_threshold):
    print("Current Fuel Level Reached. Take Immediate Action")

elif(current_fuel_level<low_fuel_threshold):
    print("Send_fuel_low alter")

else:
    print("continue fueling")


# In[128]:


range(9)


# In[131]:


n=range(9)
for i in n:
    print(i)


# In[132]:


for i in range(12):
    print(i)


# In[133]:


for i in range(5,12):
    print(i)


# In[136]:


for i in range(5,51,5):
    print(i)


# In[137]:


l1=['a','b','c']
l2=["Sales","IT","Finance"]


# In[138]:


l=zip(l1,l2)


# In[139]:


print(l)


# In[140]:


l=list(zip(l1,l2))


# In[141]:


print(l)


# In[163]:


oil_gas_data = [
    ("Field A", "Texas", 500000),
    ("Field B", "Alaska", 800000),
    ("Field C", "North Sea", 300000),
    ("Field D", "Gulf of Mexico", 600000),
]


# In[164]:


field_name,location,reserves = zip(*oil_gas_data)


# In[165]:


print(field_name)
print(location)


# In[166]:


print(reserves)


# In[154]:


i=enumerate(location)


# In[155]:


print(i)


# In[156]:


e=list(enumerate(location))


# In[157]:


print(e)


# In[158]:


g=list(enumerate(field_name))
print(g)


# In[159]:


for index, field_data in enumerate(oil_gas_data):
    field_name, location, reserve = field_data
    print(f"Field {index+1}: {field_name} is located in {location} with reserves of {reserve} barrels.")


# In[167]:


print(location)


# In[168]:


from collections import Counter
count_location=Counter(location)
print(count_location)


# In[ ]:




