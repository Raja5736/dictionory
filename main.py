#Write a program to create a dictionary and perform the following operations on that dictionary

aboutme={"name":"Raja Huzaifa",
         "age":12,
         "school":"Harmain",
         "hobby":["cricket","code","read"]

         }
print(f"My name is",aboutme["name"])
aboutme["school"]="Usman public"
print("My school name is",aboutme["school"])
aboutme.pop("age")
for key,value in aboutme.items():
    print(f"{key} {value}")
