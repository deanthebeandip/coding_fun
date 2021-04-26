from random import seed
from random import randint

seed(1)

#give me base, I give you earning
def roulette_payout(base):
    if(randint(0,2)):
        return (2/3)*base
    else:
        return -base

#returns how much is in pocket
def roulette_simulator(start, rolls, reroll_ratio, pullout_ratio):
    no_losing = 1
    pocket = start
    for r in range(rolls):
        pocket += roulette_payout(pocket * reroll_ratio)
        if no_losing: #cut your losses if you fall below a certain amount
            if pocket < (start *pullout_ratio):
                return pocket

    return int(pocket)


#Start the simulation here...
visit = 10 #visit the casino 10 times0
lifetime_earnings = 0
for i in range(visit):
    total_earning = 0
    starting_money = 1000
    roll_again = 100
    reroll_ratio_main = 1/3
    pullout_ratio_main = .2
    earning = roulette_simulator(starting_money, roll_again, reroll_ratio_main, pullout_ratio_main) - starting_money
    lifetime_earnings += earning

    print("Total earning for visit #", i ," is:", earning)

print("Lifetime earning: ", lifetime_earnings)
