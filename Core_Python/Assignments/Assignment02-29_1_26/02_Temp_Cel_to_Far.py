# 2. Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

# Formula
# F = (C × 9/5) + 32
# Or F = (C × 1.8) + 32 


temp = int(input('Enter the temperature in Celcius: '))

Faranite = temp * (9 /5) + 32

Celcius = ((Faranite - 32) / 9) * 5

print('Conversion of temp(Celcius) into Faranite: ',Faranite)

print('Conversion of temp(faranite) into Celcius: ',Celcius)



'''
NOTE:
This program converts temperature from Celsius to Fahrenheit using a 
mathematical formula and also converts it back to Celsius.
'''