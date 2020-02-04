# problem -> https://bit.ly/2v8CGt1

def print_rangoli(size):
    if 0< size <=26: 
        d={x:chr(97+x) for x in range(size+1)}
        for i in range(-(size-1),size):
            for j in range(-(size-1),size):
                if abs(i)+abs(j) <= size-1: 
                    if size%2==0:
                        if (abs(i)+abs(j)) %2 ==0:
                            print('-'+d[abs(i)+abs(j)]+'-',end='')
                        else:
                            print(d[abs(i)+abs(j)],end='')
                    elif size%2 !=0:
                        if (abs(i)+abs(j)) %2 !=0:
                            print('-'+d[abs(i)+abs(j)]+'-',end='')
                        else:
                            print(d[abs(i)+abs(j)],end='')
                else:
                    print('--',end='')
            print()

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
