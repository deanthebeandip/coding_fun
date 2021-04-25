#Trying to map out the exact numbers, such as pi, phi, and e
print("Convert Bin to Dec and etc...")

def d2b(input):
    bin = 0
    while input >= 1:
        tt = 1
        tlvl = 0
        while input >= tt :
            tt *= 2
            tlvl += 1
        input -= tt/2
        bin += 10**(tlvl-1)

    return bin


def b2d(input):
    dec = 0
    step = 0
    while input > 0:
        if input % 10:#if the digit is 1, then add that 2 power
            dec += 2**step
        step += 1
        input = int(input/10) #reduce it by 1 digit
        #print(input)
    return dec

#zebra to horse to zebra, confirm it works
for i in range(2**4):
    print(i, d2b(i),d2b(i), b2d(d2b(i)))
