def settle(owed):
    debtors = []    # people who owe (positive)
    creditors = []  # people who are owed (negative)
    for i in range(len(owed)):
        if owed[i] > 0:
            debtors.append([i, owed[i]])
        elif owed[i] < 0:
            creditors.append([i, -owed[i]])

    d = 0
    c = 0
    while d < len(debtors) and c < len(creditors):
        amount = min(debtors[d][1], creditors[c][1])
        print("Person " + str(debtors[d][0] + 1) + " gives person "
              + str(creditors[c][0] + 1) + " " + str(round(amount, 2)))
        debtors[d][1] -= amount
        creditors[c][1] -= amount
        if debtors[d][1] < 0.01:
            d += 1
        if creditors[c][1] < 0.01:
            c += 1


def split(cost):
    k = len(cost)
    owed = [0]*k
    total = sum(cost)
    for i in range(k):
        owed[i] = (total / k) - cost[i]

    print(owed)
    settle(owed)




people = int(input("How many people do u wish to split in : "))
print(str(people)+" people. Okay")
cost = [0]*people
for i in range(people):
    cost[i] = int(input("how much did person " +str(i+1)+ " pay : " ))

print(cost)
split(cost)

