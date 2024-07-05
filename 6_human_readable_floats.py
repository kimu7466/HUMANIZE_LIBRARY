import humanize 

unit = humanize.fractional(0.5)
print(unit)             # 1/2

unit = humanize.fractional(0.75)
print(unit)             # 3/4

unit = humanize.fractional(0.25)
print(unit)             # 1/4

unit = humanize.fractional(1.25)
print(unit)             # 1 1/4

unit = humanize.fractional(0.33)
print(unit)             # 33/100
