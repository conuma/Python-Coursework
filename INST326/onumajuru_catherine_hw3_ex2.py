import random
scc = [6, 5, 4]
sc = [6, 5]
cc = [5, 4]
crew = [4]
captain = [5]
ship = [6]
n = 0

while n <= 2:
    inp = input("Hit enter to roll")
    if inp == "":
        roll5 = random.choices(range(1, 7), k=5)
        print(roll5)
        if set(scc).issubset(roll5):
            result_scc = [i for i in roll5 if not i in scc or scc.remove(i)]
            total_scc = sum(result_scc)
            inp_scc = input("Do you wish to keep one, both, or neither of the remaining dice? ")
            if inp_scc == "both":
                print("Total score: " + str(total_scc) + ".")
            if inp_scc == "neither":
                roll2_scc = random.choices(range(1, 7), k=2)
                print(roll2_scc)
                inp_scc_none = input("Do you wish to keep one, both, or neither of the remaining dice? ")
                if inp_scc_none == "both":
                    total_scc_none = sum(roll2_scc)
                    print("Total score: " + str(total_scc_none) + ".")
                if inp_scc_none == "neither":
                    roll2_scc_none = random.choices(range(1, 7), k=2)
                    total_scc_none2 = sum(roll2_scc_none)
                    print(roll2_scc_none)
                    print("Your total score is: " + str(total_scc_none2) + ".")
                if inp_scc_none == "one":
                    inp_scc_none_one = input("Which die do you want to keep? ")
                    roll1_scc_none_one = random.randint(1,6)
                    total_scc_none_one = roll1_scc_none_one + int(inp_scc_none_one)
                    print(roll1_scc_none_one)
                    print("Your total score is: " + str(total_scc_none_one) + ".")
            if inp_scc == "one":
                inp_scc_one = input("Which die do you want to keep? ")
                roll1_scc_one = random.randint(1,6)
                print(roll1_scc_one)
                total_scc_one = roll1_scc_one + int(inp_scc_one)
                inp_scc_one2 = input("Hit enter to roll again or type 'pass' to keep your score ")
                if inp_scc_one2 == "pass":
                    print("Your total score is: " + str(total_scc_one) + ".")
                if inp_scc_one2 == "":
                    roll1_scc_one2 = random.randint(1,6)
                    print(roll1_scc_one2)
                    total_scc_one2 = roll1_scc_one2 + int(inp_scc_one)
                    print("Your total score is: " + str(total_scc_one2) + ".")
        if set(sc).issubset(roll5):
            inp_sc = input("Now you need a 4(the Crew). Hit enter to roll the remaining dice")
            if inp_sc == "":
                roll3 = random.choices(range(1, 7), k=3)
                print(roll3)
                if set(crew).issubset(roll3):
                    result_crew = [i for i in roll3 if not i in crew or crew.remove(i)]
                    total_crew = sum(result_crew)
                    inp_crew = input("Do you wish to keep one, both, or neither of the remaining dice? ")
                    if inp_crew == "both":
                        print("Total score: " + str(total_crew) + ".")
                    if inp_crew == "neither":
                        roll2_crew = random.choices(range(1, 7), k=2)
                        print(roll2_crew)
                        total_crew_none = sum(roll2_crew)
                        print("Your total score is: " + str(total_crew_none) + ".")
                    if inp_crew == "one":
                        inp_crew_one = input("Which die do you want to keep? ")
                        roll1_crew_one = random.randint(1, 6)
                        print(roll1_crew_one)
                        total_crew_one = roll1_crew_one + int(inp_crew_one)
                        print("Your total score is: " + str(total_crew_one) + ".")
                else:
                    inp_sc3 = input("Still no 4. Hit enter to roll again")
                    if inp_sc3 == "":
                        roll3_sc3 = random.choices(range(1, 7), k=3)
                        print(roll3_sc3)
                        if set(crew).issubset(roll3_sc3):
                            result_crew_sc3 = [i for i in roll3_sc3 if not i in crew or crew.remove(i)]
                            total_crew_sc3 = sum(result_crew_sc3)
                            print("Your total score is: " + str(total_crew_sc3) + ".")
                        else:
                            print("Sorry, you get no points because the Ship, Captain, and Crew wasn't completed.")
        if set(ship).issubset(roll5) and 5 not in roll5 and n < 2:
            inp_ship = input("Now you need a 5(the Captain) and a 4(the Crew). Hit enter to roll the remaining dice ")
            if inp_ship == "":
                roll4_ship = random.choices(range(1, 7), k=4)
                print(roll4_ship)
                if set(cc).issubset(roll4_ship):
                    result_ship_cc = [i for i in roll4_ship if not i in cc or cc.remove(i)]
                    total_ship_cc = sum(result_ship_cc)
                    inp_ship_cc = input("Do you wish to keep one, both, or neither of the remaining dice? ")
                    if inp_ship_cc == "both":
                        print("Your total is: " + str(total_ship_cc) + ".")
                    if inp_ship_cc == "neither":
                        roll2_cc = random.choices(range(1, 7), k=2)
                        print(roll2_cc)
                        total_ship_cc_none = sum(roll2_cc)
                        print("Your total score is: " + str(total_ship_cc_none) + ".")
                    if inp_ship_cc == "one":
                        inp_ship_cc_one = input("Which die do you want to keep? ")
                        roll1_ship_cc_one = random.randint(1,6)
                        print(roll1_ship_cc_one)
                        total_ship_cc_one = roll1_ship_cc_one + int(inp_ship_cc_one)
                        print("Your total score is: " + str(total_ship_cc_one) + ".")
                if set(captain).issubset(roll4_ship):
                    roll3_captain = random.choices(range(1, 7), k=3)
                    print(roll3_captain)
                    if set(crew).issubset(roll3_captain):
                        result_ship_captain = [i for i in roll3_captain if not i in crew or crew.remove(i)]
                        total_ship_captain = sum(result_ship_captain)
                        print("Your total score is: " + str(total_ship_captain) + ".")
                    else:
                        print("Sorry, you get no points because the Ship, Captain, and Crew wasn't completed.")
        else:
            n = n + 1