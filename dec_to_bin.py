def decimalToBinary(n):
    if(n==0):
        return "0"
    elif(n==1):
        return "1"
    else:
        return decimalToBinary(n//2) + "" +  decimalToBinary(n%2)

# *** Test Cases *** #
"""
print(decimalToBinary(1394))
print(decimalToBinary(9))
print(decimalToBinary(0))
print(decimalToBinary(-9))
"""
