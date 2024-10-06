""" TUPLE """
f=('mango','apple','grapes','mango')
print(f[3])

a=f.index("grapes")
print("the number is : ",a)

b=f.count('mango')
print(b)

#changing values or names
fruits=('mango','apple','grapes','mango')
fruitList=list(fruits)          #convert tuple to list
print(fruitList)                  #we are tying this to show output as list

fruitList[1]='pineapple'     #changing name
print(fruitList)

fruitList.append('banana')    
print(fruitList)

#list to tuple
fruits=tuple(fruitList)
print(fruits)

"""SET"""
family={'dad','mom','brother','sister'}
print(family)

w={'dad','mom','me','bro',29,False,80,275}       #allowing str , boolean, integer values
print(w)

q={'dad','mom','brother','sister',99,True,99,90,97}    #doesnot allow duplicate values(d.v)
print(q)
print(len(q))      #no.of elements in set and doesnot allow the d.v

family[2]    #error(cannot show name)
print(family)

family[2]='me'    #error(cannot change name)
print(family)




