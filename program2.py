s=(['hi','hai','hello','guys'])
s[1]='friends'
print(s)

s[0:2]=['do','did']
print(s)

s.remove('do')
print(s)

s.pop(2)
print(s)

del s[0]
print(s)

s.sort()
print(s)

s.sort(reverse=True)
print(s)

s.reverse()
print(s)

s.clear()
print(s)

m=[99,98,97,94,90]
print("the minimum number is: ",min(m))
print("the maximum number is: ",max(m))
