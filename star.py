def star(n):
    if n==0 :
        return n
    elif n==1:
        print(' '*3+''+'*')
        print('*'*(2*n+1)+' '*1+'*'*(2*n+1))
        print(' '+'*'+' '*3+'*')
        print('*'*(2*n+1)+' '*1+'*'*(2*n+1))
        print(' '*3+''+'*')
    else:
        for i in range(n):
            if i==0:
                print(' '*(3*n-1)+'*')
            else:
                print(' '*(2*n+(n-i-1))+'*'+' '*(2*(i-1)+1)+'*')
        print('*'*(2*(n)+1)+' '*(2*(n-1)-1)+'*'*(2*(n)+1))
        for i in range(n):
            print(' '*(i+1)+'*'+' '*(6*n-1-2*(i+2))+'*')
        for i in range(n-2,-1,-1):
            print(' '*(i+1)+'*'+' '*(6*n-1-2*(i+2))+'*')
        print('*'*(2*(n)+1)+' '*(2*(n-1)-1)+'*'*(2*(n)+1))
        for i in range(n-1,-1,-1):
             if i==0:
                print(' '*(3*n-1)+'*')
             else:
                print(' '*(2*n+(n-i-1))+'*'+' '*(2*(i-1)+1)+'*')
            

print(star(1))
print(star(5))
