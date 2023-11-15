'''
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.'''

def make_shirt(size="Large", message="I love python"):
    print(f"Creating a {size} shirt with the message: '{message}'")

# Print Default message 
make_shirt()

# Creating a medium size with the default message
make_shirt(size="medium")

# Creating a small size with a differnt message 
make_shirt(size="small", message="Python is not easy")
