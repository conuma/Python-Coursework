import random
roll3 = random.choices(range(1, 7), k=3)
roll4 = random.choices(range(1, 7), k=4)
roll5 = random.choices(range(1, 7), k=5)
scc = [6, 5, 4]
sc = [6, 5]
cc = [5, 4]
crew = [4]
captain = [5]
ship = [6]
n = 0
while n <= 2:
    roll5 = random.choices(range(1, 7), k=5)
    print(roll5)
    if set(scc).issubset(roll5):
        result = [i for i in roll5 if not i in scc or scc.remove(i)]
        total = sum(result)
        print("Total: " + str(total))
        break
    if set(sc).issubset(roll5):
        m = 0
        while m <= 1:
            roll3 = random.choices(range(1, 7), k=3)
            print(roll3)
            if set(crew).issubset(roll3):
                result4 = [i for i in roll3 if not i in crew or crew.remove(i)]
                total4 = sum(result4)
                print("Total: " +str(total4))
                break
            else:
                m = m + 1
        break
    if 6 in roll5 and 5 not in roll5:
        q = 0
        while q <= 1:
            roll4 = random.choices(range(1, 7), k=4)
            print(roll4)
            if set(cc).issubset(roll4):
                result2 = [i for i in roll4 if not i in cc or cc.remove(i)]
                total2 = sum(result2)
                print("Total: " + str(total2))
                break
            if set(captain).issubset(roll4) and n < 2:
                roll3 = random.choices(range(1, 7), k=3)
                print(roll3)
                if set(crew).issubset(roll3):
                  result3 = [i for i in roll3 if not i in crew or crew.remove(i)]
                  total3 = sum(result3)
                  print("Total: " + str(total3))
                  break
                else:
                    break
            else:
                q = q + 1
                if q > 1 and n < 2:
                    break
        break
        if n >= 2:
            break
    else:
        n = n + 1
# Problem: when only 6 is rolled in 2nd round, it continues rolling for 2 more rounds,\n
# when it should ony be 1 more round.
