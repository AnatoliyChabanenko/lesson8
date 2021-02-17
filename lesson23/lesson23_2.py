s = input()
stack = []
good = True
for i in s :
    if i in '{[(':
        stack.append(i)
    elif i in ')]}':
        if stack == []:
            good = False
            break
        ydalit = stack.pop()
        if ydalit == '(' and i == ')':
            continue
        if ydalit == '[' and i == ']':
            continue
        if ydalit == '{' and i == '}':
            continue
        good = False
        break

if good and stack == []:
    print('Yes')
else:
    print('NO')