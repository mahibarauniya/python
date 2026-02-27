import sys

def add_numbers(a, b):
    """Add two numbers and return the result"""
    return a + b

if __name__ == "__main__":
    # Get arguments from command line
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    
    # Calculate result
    result = add_numbers(num1, num2)
    
    # Print result
    print(f"{num1} + {num2} = {result}")
