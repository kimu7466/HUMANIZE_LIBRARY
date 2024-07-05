import humanize

from datetime import datetime, date, time, timedelta


# # 2 humanize date time and time deltas


# # 2.1 Natural Date

time = datetime(1998,9,1)
print(time)                         # 1998-09-01 00:00:00

time = humanize.naturaldate(time)
print(time)                         # Sep 01 1998


# time = date(1998,9,1)
# print(time)                         # 1998-09-01

# time = humanize.naturaldate(time)
# print(time)                         # Sep 01 1998

##############################################################################################
##############################################################################################
# # 2.2 Natural Day 

# time = datetime(1998,9,1)
# print(time)                         # 1998-09-01 00:00:00

# time = humanize.naturalday(time)
# print(time)                         # Sep 01


# time = datetime.now()
# print(time)                         # 2024-07-04 18:06:30.837528

# time = humanize.naturalday(time)
# print(time)                         # today


# time = datetime.now() - timedelta(days=1)
# print(time)                         # 2024-07-04 18:06:30.837528

# time = humanize.naturalday(time)
# print(time)                         # yesterday


# time = datetime.now() + timedelta(days=1)
# print(time)                         # 2024-07-04 18:06:30.837528

# time = humanize.naturalday(time)
# print(time)                         # tomorrow


# time = datetime.now() - timedelta(days=5)
# print(time)                         # 2024-07-04 18:06:30.837528

# time = humanize.naturalday(time)
# print(time)                         # Jun 29


# time = datetime.now() + timedelta(days=5)
# print(time)                         # 2024-07-04 18:06:30.837528

# time = humanize.naturalday(time)
# print(time)                         # Jul 09





##############################################################################################
##############################################################################################
# # 2.3 Natural time 

# time = datetime(1998,9,1)
# print(time)                         # 1998-09-01 00:00:00

# time = humanize.naturaltime(time)
# print(time)                         # 25 years ago


# time = datetime.now()
# print(time)                         # 2024-07-04 18:06:30.837528

# time = humanize.naturaltime(time)
# print(time)                         # now


# time = datetime.now() - timedelta(days=1)
# print(time)                         # 2024-07-04 18:06:30.837528

# time = humanize.naturaltime(time)
# print(time)                         # a day ago



# time = datetime.now() + timedelta(days=1)
# print(time)                         # 2024-07-04 18:06:30.837528

# time = humanize.naturaltime(time)
# print(time)                         # a day from now


# time = datetime.now() - timedelta(days=5)
# print(time)                         # 2024-07-04 18:06:30.837528

# time = humanize.naturaltime(time)
# print(time)                         # 5 days ago


# time = datetime.now() + timedelta(days=5)
# print(time)                         # 2024-07-04 18:06:30.837528

# time = humanize.naturaltime(time)
# print(time)                         # 5 days from now



# time =  timedelta(hours=5,minutes=5,seconds=5)
# print(time)                            # 5:05:05

# time = humanize.naturaltime(time)
# print(time)                            # 5 hours ago


# time =  - timedelta(hours=5,minutes=5,seconds=5)
# print(time)                            # 5:05:05

# time = humanize.naturaltime(time)
# print(time)                            # 5 hours from now



# time = datetime.now() - timedelta(days=5)
# time = humanize.naturaltime(time)
# print(time)                             # 5 days ago

# time = datetime.now() - timedelta(hours=5)
# time = humanize.naturaltime(time)
# print(time)                             # 5 hours ago

# time = datetime.now() - timedelta(minutes=5)
# time = humanize.naturaltime(time)
# print(time)                             # 5 minutes ago


# time = datetime.now() - timedelta(seconds=5)
# time = humanize.naturaltime(time)
# print(time)                             # 5 seconds ago

# time = datetime.now() - timedelta(seconds=60)
# time = humanize.naturaltime(time)
# print(time)                             # minute

##########################################################################
##########################################################################

# # 2.4 Natural delta

## a). humanize.naturaldelta 
## b). humanize.precisedelta

# time  = humanize.naturaldelta(timedelta(days=5))
# print(time)                                         # 5 days


# time  = humanize.naturaldelta(timedelta(days=5, hours=5))
# print(time)                                         # 5 days




# time  = humanize.precisedelta(timedelta(days=5, hours=5))
# print(time)                                         # 5 days and 5 hours


# time  = humanize.precisedelta(timedelta(days=5, hours=5, seconds=15))
# print(time)                                         # 5 days, 5 hours and 15 seconds

# time  = humanize.precisedelta(timedelta(days=5, hours=5, minutes=45, seconds=12, milliseconds=300))
# print(time)                                         # 5 days, 5 hours, 45 minutes and 12.30 seconds


# time  = humanize.precisedelta(timedelta( seconds=1001))
# print(time)                                         # 16 minutes and 41 seconds
