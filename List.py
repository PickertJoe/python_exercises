# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:52:58 2019

@author: Joe
"""
#Creating a simple list of friend names
friends = ["Ben","Yarden","Michael"]

print(friends)
#Adding Gabi's name to the end of the list
friends.append("Gabi")

print(friends)
#Adding Abby's name between Ben and Yarden in the list
friends.insert(1,"Abby")

print(friends)
#Removing Yarden's name from the list
del friends[2]

print(friends)
#Creating a new pop list
oldest=friends.pop(0)
message="The oldest friend I have is " + oldest + "."
print(message)

#Creating a list of dinner guests
dinner= ["Julius Ceasar", "Marcus Crassus" , "Gnaeus Pompeius"]
invitation= "\nDearest " + dinner[0] + ",\nWould you do me the \
pleasure of joining me at my villa in Campania for \
Saturnalia? \nI can assure you that my wines are of\
 the finest vintage and my vomitorium of the most sublime\
 quality.\nI look forward to your response!\nYours truly,\n\
    Joe\n\n"
    
print(invitation)
#Pompeius Magnus is in the dog house
#Better invite Mark Antony instead
del dinner[2]
dinner.append("Mark Antony")
print(dinner)
#Turns out Cato found out about our party and is quite
#Cross the he wasn't invited. Better add him to the list
dinner.insert(1, "Marcus Porcious Cato")
print(dinner)