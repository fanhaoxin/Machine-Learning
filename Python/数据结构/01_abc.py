# 如果a+b+c=1000, 且a^2+b^2=c^2,求出所有abc可能组合

# 1  时间复杂度T =1000*1000*1000*2
# import time

# start_time = time.time()
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a+b+c==1000 and a**2+b**2==c**2:
#                 print("a, b, c:%d, %d, %d" % (a, b, c))
# end_time = time.time()
# print("times:%d" % (end_time-start_time))
# print("finished")

# 2
import time

start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000 - a - b
        if a**2+b**2==c**2:
            print("a, b, c:%d, %d, %d" % (a, b, c))
end_time = time.time()
print("times:%d" % (end_time-start_time))
print("finished")