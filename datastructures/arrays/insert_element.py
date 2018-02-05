def insert(arr, element):
    arr.append(element)
 
# declaring array and key to insert 
arr = [12, 16, 20, 40, 50, 70]
key = 26
  
# array before inserting an element
print ("Before Inserting: ")
print (arr)
  
# array after Inserting element 
insert(arr, key)
print("After Inserting: ")
print (arr)