#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Python program to find the largest item from a given list using a loop.
================================================================================'''

def Find_Largest_Item_in_List(List):
    
    if len(List) == 0 :
        return None
    
    Largest_Item = List[0]
    for item in List:
        if item > Largest_Item :
            Largest_Item = item
            
    return Largest_Item



List_Numbers = [20, 4, 30, 45, 90, 40, 100, 10]
Largest = Find_Largest_Item_in_List(List_Numbers)
print("The Largest Number in the List is : ", Largest)