transaction={}
bal=0
damount=0
wamount=0
for i in range(4):
    print("Enter D for deposit and W for withdrawal")
    str=input()
    if str=='D':
        damount=int(input("Enter amount"))
        transaction['D'] =damount
        bal=bal+damount
    if str=='W':
        wamount=int(input("Enter amount"))
        transaction['W'] =wamount
        bal=bal-wamount
    
print(transaction)    
print("Balanace amount:{}".format(bal))
