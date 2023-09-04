fruits = [
    {"fruit": "kiwi", "quantity": 2},
    {"fruit":"banana", "quantity": 3},
    {"fruit": "apple", "quantity": 1}
]

# def f(fruits):
#     return fruits["quantity"]



# fruits.sort(key = f)

# alternate way of doing the same- lambda function

fruits.sort( key = lambda fruits: fruits["fruit"])

print(fruits)