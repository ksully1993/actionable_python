# Simple script to divide two positive integers and print the floor result and remainder
import sys

def main():
  if validate(sys.argv[1:]): # Validating arguments before dividing. If error, print message
    print(validate(sys.argv[1:]))
    return
  result = divide_with_remainder(sys.argv[1], sys.argv[2])
  print(sys.argv[1] + " divided by " + sys.argv[2] + " equals " + str(result[0]) + " with a remainder of " + str(result[1]))
  return
  

def divide_with_remainder(num, den):
  result = int(num) // int(den) # floor operation gives the result with no remainder
  remainder = int(num) % int(den) # modulo operator gives the remainder
  return result, remainder # returns both values as an array
    
#Input validation
def validate(args):
  error = 0         # default of 0 for non-error status

  # ceck to see if there was too many arguments
  if len(args) > 2: 
    error = "Only two values allowed. Type 'divide.py -h' for help"
    return error
  
  if '-h' in args:
    error = "Please pass the numerator followed by the denominator as cmd line arguments. \nBoth values must be positive. Denominator must be a non-zero value. \nExample: divide.py 12 4 \nResult: '12 divided by 4 equals 3 with a remainder of 0'"
    return error
    
  if len(args) < 2:
    error = "Invalid arguments. Type 'divide.py -h' for help"
    return error
  
  for arg in args:
    try:
      integer = int(arg)
      if integer < 0:
        error = "Cannot use negative values. Please try again!"
    except ValueError:
      error = "Only integers allowed. No decimals please"
      return error

  if int(args[1]) == 0:
    error = "Error: Cannot divide by zero. Please try again!"
    return error
  
  
  return error # return default non-error status of 0 or error message
  
main()
