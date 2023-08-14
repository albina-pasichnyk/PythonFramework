from products_collection import ProductsCollection
from employees_collection import EmployeesCollection

# Create and Check Product Collection
products_collection = ProductsCollection()

product_list = [{'name': 'product_2', 'price': 20},
                {'name': 'product_3', 'price': 30},
                {'name': 'product_4', 'price': 40},
                {'name': 'product_5', 'price': 50}
                ]
# Insert one product and get it's value
products_collection.insert_one_product('product_1', 10)
one_product = products_collection.find_by_name('product_1')
print(one_product)

print('\n')

# Insert multiple products and get all
products_collection.insert_many_products(product_list)
list_of_products = products_collection.find({})
for product in list_of_products:
    print(product)

print('\n')

# Find all products that meet criteria "price > 30"
filtered_product_list = products_collection.filter_by_price(30)
for product in filtered_product_list:
    print(product)

print('\n')

# Update price of specific product found by name
products_collection.update_price_for_product('product_1', 99)
updated_price = products_collection.find_by_name('product_1')
print(updated_price)

print('\n')

# Delete specific product found by name & try to get it after deletion
products_collection.delete_by_name('product_2')
deleted_product = products_collection.find_by_name('product_2')
print(deleted_product)

print('\n')

# Create and Check EmployeesCollection
employees_collection = EmployeesCollection()

employees_list = [{'first_name': 'Sam', 'last_name': 'Grey', 'position': 'CEO'},
                  {'first_name': 'Beta', 'last_name': 'Street', 'position': 'AQA'},
                  {'first_name': 'Alisa', 'last_name': 'Forest', 'position': 'AQA'},
                  {'first_name': 'Anfisa', 'last_name': 'Forest', 'position': 'AQA'},
                  {'first_name': 'Mars', 'last_name': 'Angry', 'position': 'Developer'}
                  ]

# Insert list of employees
employees_collection.add_employees(employees_list)
all_employees = employees_collection.find({})
for employee in all_employees:
    print(employee)

print('\n')

# Find by specific parameter
by_first_name = employees_collection.find_by_first_name('Sam')
print(by_first_name)
by_last_name = employees_collection.find_by_last_name('Angry')
print(by_last_name)
by_position = employees_collection.find_by_position('AQA')
for employee in by_position:
    print(employee)

print('\n')

# Add one employee
employees_collection.add_employee('Jane', 'Doe', 'QA')
added_employee = employees_collection.find_by_first_name('Jane')
print(added_employee)

print('\n')

# Update many values
employees_collection.update_position('Designer')
updated_employees_list = employees_collection.find({})
for employee in updated_employees_list:
    print(employee)

print('\n')

# Sort list of employees using sorting from Base Mongo
sorted_employees = employees_collection.sorting('first_name', 'asc')
for employee in sorted_employees:
    print(employee)

# Delete all employees that meet criteria
employees_collection.delete_by_position('Designer')
list_after_delete = employees_collection.find_by_position('Designer')
print(list_after_delete)

products_collection.delete_many({})
employees_collection.delete_many({})
