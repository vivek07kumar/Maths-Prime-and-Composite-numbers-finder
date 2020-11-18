done = True
print()
print('      >>>>>>>>>>>>>>>>> PRIME and COMPOSITE NUMBERS FINDER <<<<<<<<<<<<<<<<<')
print()
while done :
    done2 = True
    done3 = True
    while done3 :
        choice = input('>> Press P for Prime number or Press Co for Composite number : ')
        if choice == 'p' or choice == 'P' :
            done3 = False
            show = 'Prime'
            print()
        elif choice == 'co' or choice == 'CO' or choice == 'Co' or choice == 'cO' :
            done3 = False
            show = 'Composite'
            print()
        else :
            print()
            print('                                  Wrong Input !')
            print()
    print('>> Display',show,'numbers up to what value ? : ',end='')
    number = int(input())
    if number <= 1 :
        print()
        print('                    ERROR ! Number must be greater than 1.')
        print()
    else :
        print()
        print('------------------------------------------------------------------------------')
        print('* ASWER : All',show,'numbers up to',number,'--> ',end='')
        for prime in range(2,number + 1,1) :
            factors = 0
            for divider in range(1,prime + 1,1) :
                if prime % divider == 0 :
                    factors = factors + 1
            if factors == 2 and ( choice == 'p' or choice == 'P' ) :
                if prime == 2 :
                    print(prime,end='')
                else :
                    print(',',prime,sep='',end='')
            if factors > 2 and ( choice == 'co' or choice == 'CO' or choice == 'Co' or choice == 'cO' ) :
                if prime == 4 :
                    print(prime,end='')
                else :
                    print(',',prime,sep='',end='')
        print()
        print('------------------------------------------------------------------------------')
        print()
        while done2 :
            userinput = input('>> Press C to Continue or Pres E to Exit : ')
            if userinput == 'c' or userinput == 'C' :
                done2 = False
                print()
            elif userinput == 'e' or userinput == 'E' :
                done2 = False
                done = False
            else :
                print()
                print('                                  Wrong Input !')
                print()
