# function that takes function as a input
# funcitonal programming

def announce(f):
    def wrapper():
        print("About to run th function...")
        f()
        print("Done with the function.")
    return wrapper()

@announce
def hello():
    print("Hello World")

# use case - suppose you want to check something in web app only when thee user is logged in, 
# you can add condition in the decorator before running the specific function.