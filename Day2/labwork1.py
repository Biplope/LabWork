#convert second to day, hour, minute and second

S=int(input("enter the value for second"))
Day=(((S/60)/60)/24)
print(f"Total day for given seconds: {Day}")
Hour=((S/60)/60)
print(f"Total hours for given seconds: {Hour}")
Minute=(S/60)
print(f"total minutes for given seconds:{Minute}")