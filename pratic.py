fruit = "orange"
if fruit.lower() != "apple".lower() and fruit.lower() != "orange".lower():
    print("I don't like it.")
else:
    print("I like it.")    
    
num = 2
if num == 1 or num == 2:
    print("yes")
else:
    print("No")        

age = 21
if age < 18 and not age > 100:
    print("underage")   
else:     
    print("Old enough")