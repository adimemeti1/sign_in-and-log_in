def Sign_Up_Log_in():
    email=input('Sheno emailin')
    paswordi=input('Sheno paswordin')
    DTFW=input('Deshiron te futesh ne web')
    while DTFW == 'Jo':
        break
    else:
        email2=input('Sheno emailin')
        while email2 != email:
            print('Incorrect')
            break
        else:
            print('Correct')
            paswordi2=input('Sheno paswordin')
            while paswordi2 != paswordi:
                print('Incorrect')
                break
            else:
                print('Correct','\n','Tani do te fus ne web')
Sign_Up_Log_in()
