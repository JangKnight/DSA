from ipaddress import ip_address

def ips_between(start, end):
    return int(ip_address(end)) - int(ip_address(start))

=====================================OLD CODE: DO NOT USE OR DELETE

# def ips_between(start, end):
#     a = sum([int(e)*256**(3-i) for i, e in enumerate(start.split('.'))])
#     b = sum([int(e)*256**(3-i) for i, e in enumerate(end.split('.'))])
#     return abs(a-b)

======================================
# def ips_between(start, end):
#     start = start.split('.')
#     end = end.split('.')
#     dist = 0
#     if int(end[0]) > int(start[0]):
#         dist += abs(int(end[0]) - int(start[0])) * 16777216
#     if int(end[1]) > int(start[1]):
#         dist += abs(int(end[1]) - int(start[1])) * 65536
#     if int(end[2]) > int(start[2]):
#         dist += abs(int(end[2]) - int(start[2])) * 256
#     if int(end[3]) > int(start[3]):
#         dist += abs(int(end[3]) - int(start[3]))
#     if int(end[0]) < int(start[0]):
#         dist -= abs(int(end[0]) - int(start[0])) * 16777216
#     if int(end[1]) < int(start[1]):
#         dist -= abs(int(end[1]) - int(start[1])) * 65536
#     if int(end[2]) < int(start[2]):
#         dist -= abs(int(end[2]) - int(start[2])) * 256
#     if int(end[3]) < int(start[3]):
#         dist -= abs(int(end[3]) - int(start[3]))
        
#     return int(dist)