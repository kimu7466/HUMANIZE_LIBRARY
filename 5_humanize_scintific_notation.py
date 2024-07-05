import humanize 

unit = humanize.scientific(0.3)
print(unit)             # 3.00 x 10⁻¹

unit = humanize.scientific("200000")
print(unit)             # 2.00 x 10⁵

unit = humanize.scientific(200000)
print(unit)             # 2.00 x 10⁵

unit = humanize.scientific(0.00005)
print(unit)             # 5.00 x 10⁻⁵
