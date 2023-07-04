#The list is most versatile data type available in python which can be written as a lsit of comma-seperator
#values (items)between square backets.Important thing about a list is that items in a list need not be of tha same type

myfirstlist=[1,2,3,4,5,6,7,8,9]
print(type(myfirstlist))
#we find above data type to conform that is it a list 

myfirstlist[8]
print(myfirstlist[8])
#we find above index of 8 from list
#remember that index value is start with 0 like index 0,index1,index2and so on

myfirstlist[1:4]
print(myfirstlist[1:4])
#we want to get value from 4 to 9 from list

myfirstlist[-5:]
print(myfirstlist[-5:])                  
#we do reverse index in which we get last towards first

myfirstlist.append(85)
print(myfirstlist)
#in above we add can something in list like 85
#where 85 indicates which we want to add or append


myfirstlist.insert(9,79)
print(myfirstlist)
#we can insert something in list between them as like 79
#we can do it as inert(9,79) where 9 indicate location where we want to insert and 79 inducate which we want to insert


mylastlist=myfirstlist.copy()
print(mylastlist)
#we can create a copy of our list is which 'mylastlist' is the name of our copeid list name and we print it as a output

mylastlist.clear()
print(mylastlist)
#In this command we clear our list in which output will come as empty

del mylastlist
#iN THIS COMMAND WE delete our list from program or database in which we get error from editor that list which you want is not exist

myfirstlist.remove(4)
print(myfirstlist)
#In this command we can remove an index or value from list as like '4' we write that value instead of 4 to remove it from list

myfirstlist.pop(5)
print(myfirstlist)
#in this command we remove any value from list as like remove command like we want to remove 7 we will insert 6 in pop cpmmand

myfirstlist.reverse()
print(myfirstlist)
#In this command we will reverse our list as desending towarsd assending

myfirstlist.sort()
print(myfirstlist)
#In this cammand we sort our list from lower to higher as like assendind to desebding

len(myfirstlist)
print(len(myfirstlist))
#Im this command we will check No or Quantity or Member in our list

myfirstlist[8]=57475
print(myfirstlist)
#IN THIS command we can replace value like 8



#TUPLE
#A tuple is a sequence of immutable python pbjects.Tuple are sequnece like lists.the difference between tuples and lists are ,the tuple cannot be changed unlike lists and simple parantheses
rizwanshoukat= (4,5,6,6,6,6,6,6,6,2,3)
type(rizwanshoukat)
print(type(rizwanshoukat))

rizwanshoukat.count(6)
print(rizwanshoukat.count(6))
#In this command we can count how much values in tuple

len(rizwanshoukat)
print(len(rizwanshoukat))
#In this command we can check how much value in tuple
