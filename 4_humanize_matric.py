import humanize

# # 4 METRIC

unit = humanize.metric(12000000,"W")
print(unit)  # 12.0 Mw  

unit = humanize.metric(12000000,"V")
print(unit)  # 12.0 Mv  

# unit = humanize.metric(12e-10,"V")
# print(unit)  # 1.20 nV

# unit = humanize.metric(12e-6,unit="V")
# print(unit)  # 12.0 μV

# unit = humanize.metric(12.4567e-6,unit="V")
# print(unit)  # 12.5 μV

# unit = humanize.metric(12.4567e-6,unit="V",precision=4)
# print(unit)  # 12.46 μV

unit = humanize.metric(12.4567e-3,unit="V",precision=4)
print(unit)  # 12.46 mV

# unit = humanize.metric(12000000,"V")
# print(unit)  # 12.0 Mw  




