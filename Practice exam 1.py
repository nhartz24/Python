def pyramid(n):
    print((n+2) * '*')
    x=1
    while x <= n:
        print(((n//2-x//2)+1)*'*' + x*'-' + ((n//2-x//2)+1)*'*')
        x+=2


    x -= 4
    while x > 0:
        print(((n//2- x//2)+1)*'*' + x*'-' + ((n//2-x//2)+1)*'*')
        x -= 2

    print((n+2) * '*')

def for_loop(s):
    print('f')
    A='' #empty string
    B='' #empty string
    i = 0
    while i < len(s):
        if s[i].isupper():
            A += s[i]
            
        elif s[i].isdigit():
            B += s[i]

        i+=1

    return B + ' ' + A #quotes contain space

print(for_loop('mOV1EuRs8iT1UcR2E'))




'''
    for x in s:
        if x.isupper():
            A += x
        elif x.isdigit():
            B += x
    return B + ' ' + A #quotes contain space
'''

