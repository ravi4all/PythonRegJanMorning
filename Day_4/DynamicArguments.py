# Dynamic Arguments
# *args  -  Convert Data to tuples
# **kwargs   - Convert Data to Dictionary

def emp(id,name,age,*address):
    print("Id: {}, Name: {}, Age: {}".format(id,name,age))

    #print("Address: {}".format(address))

    print(type(address))
    for i,addr in enumerate(address):
        print("Address {} {}".format(i+1, addr))

#emp(101,'Ram',26,['xyz','abc'])
#emp(101,'Ram',26,'xyz','abc')
#emp(102,'Shyam',28,'rohini','rithala','noida')

def emp_details(*address,**details):
    print(address)
    print(details)

emp_details('Delhi','Noida',name="Ram",age=25,salary=25000)

