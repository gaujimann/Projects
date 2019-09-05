pop = 307357870

years_str = input("Years: ")
years_float = float(years_str) #convert string to float

x = (60**2 * 24 * 365) / 7      #births per year
y = (60**2 * 24 * 365) / 13     #deaths per year
z = (60**2 * 24 * 365) / 35     #immigrants per year

newpop = int((x - y + z) * years_float + pop)

if years_float < 0:
    print("Invalid output!")

elif years_float == 1:
    print("New population after", years_float, "year is",\
          newpop)

else:
    print("New population after", years_float, "years is",\
          newpop)
