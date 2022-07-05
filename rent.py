from rent_service import Service

if __name__ == '__main__':
    service = Service()
    flag = False
    while(not flag):
        cmd = 'Z'
        while(cmd != 'A' and cmd != 'L' and cmd != 'R' and cmd != 'D' and cmd != 'X'):
            print("A)dd an order L)ist R)evenue D)elete E)xit")
            keyInfo = input("")
            cmd = keyInfo.upper()
            if(cmd == 'X'):
                flag = True
            elif(cmd == 'L'):
                service.List()
            elif(cmd == 'A'):
                service.addOrder()
            elif(cmd == 'D'):
                service.delete()
            elif(cmd == 'R'):
                service.computeRevenue()


