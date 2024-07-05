import humanize


# # 3 Humanize file size


size  = humanize.naturalsize(5)
print(size)                      # 5 Bytes


# size  = humanize.naturalsize(500)
# print(size)                      # 500 Bytes


# size  = humanize.naturalsize(1500)
# print(size)                      # 1.5 kB


# size  = humanize.naturalsize(15000000)
# print(size)                      # 15.0 MB

# size  = humanize.naturalsize(150000000)
# print(size)                      # 150.0 MB

# size  = humanize.naturalsize(1500000000)
# print(size)                      # 1.5 GB

# size  = humanize.naturalsize(15000000000)
# print(size)                      # 15.0 GB

# size  = humanize.naturalsize(15000000000000)
# print(size)                      # 15.0 TB


# size  = humanize.naturalsize(15000000000000, binary=True) 
# # # it uses 2^10 base instead of 10^3 
# print(size)                              # 13.6 TiB


# size  = humanize.naturalsize(15000000000000, gnu=True)
# # # it gives output in linux like format
# print(size)                              # 13.6T


