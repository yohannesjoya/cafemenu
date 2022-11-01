This simple python project is online restaurant menu simulation which uses simple data structure to add , delete,  display the menu and update the price 
#This program has two class one menuItem and menu. The menuItem used to create the food object(new food item). 

#The menu class contains 5 main functions: -
A.addItem: used to add food item in sorted form to the list
This function uses mergesort function (which works in O(nlogn)) 
B. SearchItem: used to search good item or checks whether the food a customer inserted exists or not.
This function implements binary search which operates with O(logn). 
C. indexFinder: This function takes the food item name and used to find the index of the food item you want to delete or update .
This function implements binary search to find the index. 
D. RemoveItem: this function used to delete food item from the list using the index found from the RemoveindexFinder function.
E.UpdatePrice: this function takes the name of the item to be updated and the new price the uses the indexfinder function to finfd the item and update it.
F.showAll: use to display all food items found in the list.
# it has mergesort function which is useful for the sorting.