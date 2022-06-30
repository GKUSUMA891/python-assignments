def leap_year(year):
    leap=False
    year=int(input())   
if year%4==0:
    print("leap year")
elif year%100==0:
    print("NOT a leap year")
elif year%400==0:
    print("leap year")
else:
        print("NOT a leap year")
    return year
leap_year()
