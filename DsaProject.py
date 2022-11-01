class menuItem:
    def __init__(self, name,price, Item_Id):
        self.name=name
        self.price=price
        self.Item_Id=Item_Id

class menu:
    menulist=[]

    def addItem(self, itemName,itemPrice,Item_Id):
        newItem=menuItem(itemName,itemPrice,Item_Id)
        if menu.UniqueIdchecker(self,newItem):
            menu.menulist.append(newItem)
## here is the sorter you change it below
            if len(menu.menulist)>1:
                array=menu.menulist
                menu.menulist=menu.mergeSort(self,array)
                print("Menu added successfully! ")
        else:
            print("                                                     ")
            print( "you are trying to add item with the existing id number \n try again with different id number")
            print("                                                     ")

    def UniqueIdchecker(self,item):
        count=1
        for i in self.menulist:
            if i.Item_Id==item.Item_Id:
                count+=1
        if count>=2:
            return False
        else:
            return True
                
                
                 
##create the sort here and call it in the addItem function

# MergeSort in Python


    def mergeSort(self,array):
        if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
            r = len(array)//2
            L = array[:r]
            M = array[r:]

        # Sort the two halves
            self.mergeSort(L)
            self.mergeSort(M)

            i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
            while i < len(L) and j < len(M):
                if L[i].name < M[j].name:
                    array[k] = L[i]
                    i += 1
                elif L[i].name >= M[j].name:
                    array[k] = M[j]
                    j += 1
                k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1

            while j < len(M):
                array[k] = M[j]
                j += 1
                k += 1
            return array
    
        

## the function below is used to show all items on the menu        
    
    def showAll(self):
        for i in menu.menulist:
            print("##############################################")
            print("                              ")
            print("name: ",i.name)
            print("price: ",i.price)
            print("item id: ",i.Item_Id)
            print("                              ")

## the function below allows us to find items we want based on the name and
## it works in binary fashion            

    def searchItem(self,name):
        lo=0
        hi=len(menu.menulist)-1
        while lo<=hi:
            mid=(lo+hi)//2
            if menu.menulist[mid].name==name:
       
                 print("name: ",menu.menulist[mid].name)
                 print("price: ",menu.menulist[mid].price)
                 print("itemId: ",menu.menulist[mid].Item_Id)

                 return menu.menulist[mid].name 
                 break
        
            elif menu.menulist[mid].name<name:
                lo=mid+1
            elif menu.menulist[mid].name>name:
                hi=mid-1
        if lo>hi:
            print("Sorry, the item you need does not exist on this menu")



##  this is  seacrh the index of item to be removed in binary and return the index to help the remove function

    def IndexFinder(self,name):
        lo=0
        hi=len(menu.menulist)-1
        while lo<=hi:
            mid=(lo+hi)//2
            if menu.menulist[mid].name==name:
                return mid
                break
        
            elif menu.menulist[mid].name<name:
                lo=mid+1
            elif menu.menulist[mid].name>name:
                hi=mid-1

        if lo>hi:
            return None
## the function below remove the item from the menu 
            
    def RemoveItem(self,name):
        Indexof_item_tobe_removed=menu.IndexFinder(self,name)
        if Indexof_item_tobe_removed!=None:
            if len(menu.menulist)>0:
                menu.menulist.pop(Indexof_item_tobe_removed)
            else:
                print("                               ")
                print("there is no item on the menu")
                print("                               ")
        else:
            print("                                               ")
            print("the item you need to remove doesnot exist on the list")
            print("                                               ")
                
                
##  the function below is used to update the price of the the item
    def UpdatePrice(self,name,price):
        Index_of_item_tobe_updated=menu.IndexFinder(self,name)
        if  Index_of_item_tobe_updated!= None:
            menu.menulist[Index_of_item_tobe_updated].price=price
            
        
        

## presentation layer
##


cus = menu()     
while True:
    print(" 1. Add Menu\n 2. Search Menu\n 3. Delete the Menu \n 4. display Menu \n 5. Update price \n 6. Exit")
    ch = input("Enter your Choice: ")

    if ch=='1':
        
        fname= str(input("Enter Name of the Food: "))
        fprice=int(input("Enter the price: "))
        fId=int(input("Enter food id: "))
        cus.addItem(fname,fprice,fId)   
        
    elif (ch == '2'):
        
        fname=input("Enter the name name the food you want to check: ")
        cus.searchItem(fname)
    elif (ch == '3'):
        
        fname=input("Enter the name of the food you want to delete: ")
        cus.RemoveItem(fname)
    elif (ch == '4'):
        
        print(cus.showAll())
    elif(ch=='5'):
        updatedItemName=str(input("Enter the name of item you want to update price: "))
        updatedItemPrice=int(input("Enter new price: "))
        cus.UpdatePrice(updatedItemName,updatedItemPrice)
        

    elif(ch=='6'):
        exit()
    else:
        print("Invalid Input")
        exit()
