"""Example of a dictionary"""

student = {
    'name'      : 'Riccardo',
    'age'       : 0,
    'university': 'University of Padova',
    'email'     : 'riccardo.carroccio@studenti.unipd',
    'food'      : 'pizza'
}

student['course'] = 'physics'   # adding a new key-value pair
student['age']    = '25'        # changing the value of a key
del student['age']              # deleting a key-value pair

print("Printing using items():")
for i in student.items():
    print(i)
print("\nPrinting using items() with double index:")
for i,j in student.items():
    print(i,j)
print("\nPrinting using values():")
for i in student.values():
    print(i)
