def decimalToBinary(n):
    # base cases
    if(n==0):
        return "0"
    elif(n==1):
        return "1"
    #increment throught the number by dividing by integer 2, and return it's parity (n%2) as 1 or 0
    else:
        return decimalToBinary(n//2) + "" +  decimalToBinary(n%2)

# *** Test Cases *** #
"""
print(decimalToBinary(1394))
print(decimalToBinary(9))
print(decimalToBinary(0))
print(decimalToBinary(-9))
"""
