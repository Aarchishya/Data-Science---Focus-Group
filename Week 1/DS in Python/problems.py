# Q1
shopping_list=["milk","bread","eggs"]
shopping_list.append("butter")
print(shopping_list)
shopping_list.remove("bread")
print(shopping_list)

# Q2
books={"title" : "Hunger Games",
       "author" : "Suzanne Collins",
       "year": "2009"}
books["year"]="2008"
print(books)
books["genre"]="Fiction"
print(books)

# Q3
nos={1, 2, 2, 3, 4, 4, 5}
print(nos)
nos1={4, 5, 6, 7}
print(nos|nos1)

# Q4
person_info=("John",25,"Developer")
x,y,z=person_info
print(x)
print(y)
print(z)
