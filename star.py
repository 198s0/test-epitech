def star(n):
    if n==0 :
        return n
    else:
        for i in range(n):
            if i==0:
                print(' '*(3*n-i-2),'*')
            elif i==1:
                print(' '*(3*n-i-2),'*','*')
            else:
                print(' '*(3*n-i-2),'*',' '*(2*(i-1)-1),'*')
        print('*'*(2*n+1),' '*(2*n-5),'*'*(2*n+1))
        for i in range(1,n):
            print(' '*(i-1),'*',' '*(6*n-3-2*(i+1)),'*')
        for i in range(n,0,-1):
            print(' '*(i-1),'*',' '*(6*n-3-2*(i+1)),'*')
        print('*'*(2*n+1),' '*(2*n-5),'*'*(2*n+1))
        for i in range(n-1,-1,-1):
            if i==0:
                print(' '*(3*n-i-2),'*')
            elif i==1:
                print(' '*(3*n-i-2),'*','*')
            else:
                print(' '*(3*n-i-2),'*',' '*(2*(i-1)-1),'*')
        
        

print(star(5))
