num =int(input("Enter a number up to 5 digit:"))
if num>=0 and num<=9:
    print("It is single digit number",num)
elif num>=10 and num<=99:
    print("It is double digit number",num)
elif num>=100 and num<=999:
    print("It is triple digit number",num)
elif num>=1000 and num<=9999:
    print("It is quad digit number",num)
elif num>=10000 and num<=99999:
    print("It is pent digit number",num)
else:
    print("Invalid input")







