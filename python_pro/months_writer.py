# jerry inyang
# 9.14.23
# implement write and read fxs and open and close fxs
#seek(0) takes u back to the beginning of file



months = open('months.txt')

print(months)
print(months.mode)
print(months.readable())
#months.close()


months = open('months.txt')

print(months.read())
print(months.readline()) #reads one line
print(months.readline()) #reads next line
print(months.readlines()) #prints an array
print(months.readlines()) #prints an empty array because we already read it
months.seek(0)
print(months.readlines()) #prints an array again

months.seek(0)
for month in months:
	print(month)
	
months.seek(0)
for month in months:
	print(month.strip())	

months.close()

	
days = open("days.txt", "w")
days.write("Monday")
days.close()

days = open("days.txt", "w")
days.write("\nTuesday") # overwrites
days.close()

days = open("days.txt", "a")
days.write("\nWednesday") # appends
days.close()