'''Write a function called make_shirt() that accepts a size and the text of a message that should be printed on 
the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the function a second time using keyword 
arguments.'''

def make_shirt(size, message):
    print(f"Creating a {size} shirt with the message: '{message}'")

#Call the function using posotional arguments
make_shirt("medium size", "Hello, World!")

#Call the function using keyboard arguments
make_shirt(size="Large size", message="Life is easy")