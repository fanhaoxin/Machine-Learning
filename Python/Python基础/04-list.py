bicycles = ['trek', 'cannondale', 'redline', 'specialized']
for i in range(len(bicycles)):
    print(bicycles[i])

for i in bicycles:
    print(i)

# 4-3
for i in range(21):
    print(i)

# 4-4
a=[]
for i in range(101):
    a.append(i)
    print(i)
print(a)

# 4-5
print(min(a))
print(max(a))
print(sum(a))

# 4-6
b=[]
for i in range(1,20,2):
    print(i)
    b.append(i)
print(b)

# 4-7
c=[]
for i in range(3, 31):
    if i%3==0:
        c.append(i)
print(c)

# 4-9
d = [x**3 for x in range(1, 11)]
print(d)


car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# 5-3
alien_color = ['green', 'yellow', 'red']
for alien in alien_color:
    if alien == 'green':
        print('5 points.')
    elif alien == 'yellow':
        print('10 points.')
    else:
        print('15 points.')

# 5-11
nums=[]
for i in range(1,10):
    nums.append(i)
for num in nums:
    if num == 1:
        print(str(num)+'st')
    elif num == 2:
        print(str(num)+'nd')
    elif num == 3:
        print(str(num)+'rd')
    else:
        print(str(num)+'th')