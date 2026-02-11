#Create and AccessDictionaryElements

student = {
 "roll_no": 101, 
 "name": "Amit", 
 "marks": 85 
} 
print("Dictionary:", student) 
print("Name:", student["name"]) 
print("Marks:", student.get("marks")) 
print() 

#Update Dictionary 
print("2. Update Dictionary") 
student["marks"] = 90            
student["grade"] = "A"           
print("Updated Dictionary:", student) 
print() 

#Removing Elements 
print("3. Removing Elements") 
removed_value = student.pop("grade")   
print("Removed Value:", removed_value) 
print("After Removing 'grade':", student) 
student.popitem()                
print("After popitem():", student) 
print() 

#Merging Dictionaries 
print("4. Merging Dictionaries") 
dict1 = {"a": 1, "b": 2} 
dict2 = {"c": 3, "d": 4} 

merged_dict = dict1 | dict2      
print("First Dictionary:", dict1) 
print("Second Dictionary:", dict2) 
print("Merged Dictionary:", merged_dict) 