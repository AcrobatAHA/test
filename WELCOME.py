class welcome:
    a = int(input("Enter a number=>"))
    def pattern(n):
        print(n,end='')
        for i in range(2,n+1):
            if n<=2:
                print("      ",end='')
        print(n)
    pattern(a)
