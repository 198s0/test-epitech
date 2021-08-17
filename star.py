def star(n):
    if n==0 :
        return n
    elif n==1:
        print(' '*5,'*')
        print('*'*(2*n+1),' '*4,'*'*(2*n+1))
        print('','*',' '*4,' ','*')
        print('*'*(2*n+1),' '*4,'*'*(2*n+1))
        print(' '*5,'*') 
    else:
        for i in range(n):
            if i==0:
                print(' '*(3*n-i-3),'*')
            elif i==1:
                print(' '*(3*n-i-3),'*','*')
            else:
                print(' '*(3*n-i-3),'*',' '*(2*(i-1)-1),'*')
        print('*'*(2*n),' '*(2*n-5),'*'*(2*n))
        for i in range(1,n):
            print(' '*(i-1),'*',' '*(6*n-5-2*(i+1)),'*')
        for i in range(n,0,-1):
            print(' '*(i-1),'*',' '*(6*n-5-2*(i+1)),'*')
        print('*'*(2*n),' '*(2*n-5),'*'*(2*n))
        for i in range(n-1,-1,-1):
            if i==0:
                print(' '*(3*n-i-3),'*')
            elif i==1:
                print(' '*(3*n-i-3),'*','*')
            else:
                print(' '*(3*n-i-3),'*',' '*(2*(i-1)-1),'*')
        
        

print(star(1))
print(star(5))
