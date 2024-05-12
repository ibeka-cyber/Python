def to_number(roman):
    num={
        "I": 1,
        "V": 5,
        "X": 10,
        "L":  50,
        "C": 100,
        "D":500,
        "M":1000 
                }
    
    total=0
    total+=num[roman[-1]]
    temp=0
    for i in range(len(roman)-1):
            if num[roman[i+1]]<=num[roman[i]]:
                total+=num[roman[i]]
            else:
                total-=num[roman[i]]
    return total

print(to_number("MCMVII")) #1907
print(to_number("MMXI")) #2011
print(to_number("XC")) #90
print(to_number("MCMXC")) #1990

    
    