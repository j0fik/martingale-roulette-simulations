import random
a = int(input("Entry budget: "))
b = int(input("Number of simulations: "))
c = int(input("Color you want to bet on (1 for black; 2 for red): "))
p = int(input("Expected return(%): "))
print()
def roulette(budget, reps, color, p):
    ruleta = [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2,
              1, 2]
    data = []
    return_x = 1 + p/100
    old_budget = budget
    for i in range(reps):
        streak = []
        old_bets = []
        x = 0
        condition = budget < return_x*old_budget
        budget = old_budget
        while budget > 0 and condition:
            if x == 0:
                bet = 1
            else:
                if streak[x - 1] == 0:
                    bet = 2 * old_bets[x - 1]
                elif streak[x - 1] == 1:
                    bet = 1
            if budget < bet or budget > return_x*old_budget:
                break
            else:
                budget = budget - bet
            old_bets.append(bet)

            c = random.randint(0, len(ruleta) - 1)
            if ruleta[c] == color:
                bet = 2 * bet
                budget += bet
                streak.append(1)

            elif ruleta[c] != color:
                streak.append(0)
            x = x + 1
        if old_bets:
            big_bet = max(old_bets)
        else:
            big_bet = 0

        if budget >= return_x*old_budget:
            data.append([x, budget, big_bet, 1])
        else:
            data.append([x, budget, big_bet, 0])
    return data

d = roulette(a, b, c, p)
round_info = 0
round_info_w = 0
round_info_l = 0
no_w = 0
no_l = 0
for i in range(len(d)):
    #print(f"Number of rounds: {d[i][0]}")
    #print(f"Ending budget: {d[i][1]}")
    #print(f"Highiest bet: {d[i][2]}")
    round_info += d[i][0]
    if d[i][3] == 1:
        round_info_w += d[i][0]
        no_w += 1
    elif d[i][3] == 0:
        round_info_l += d[i][0]
        no_l += 1
    #print()

print(f"Average number of rounds per roulette game: {round_info/b}")
print()
if no_w != 0:
    print(f"Average number of rounds achieving the goal/return: {round_info_w/no_w}")
else:
    print(f"Average number of rounds achieving the goal/return: 0")
if no_l != 0:
    print(f"Average number of rounds of failed games: {round_info_l / no_l}")
else:
    print(f"Average number of rounds of failed games: 0")
print(f"Succes rate: {(no_w/b)*100} %")
print()


#for rows in d:
#    print(rows)
