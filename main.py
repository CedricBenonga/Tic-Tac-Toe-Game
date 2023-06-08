from prettytable import PrettyTable, ALL

# Create table
table = PrettyTable()

# Create borderline between rows
table.hrules = ALL

# create column
columns = ['', '', '']

# Add rows
a = ['a', 'b', 'c']
b = ['d', 'e', 'f']
c = ['g', 'h', 'i']

table.add_column(columns[0], a)
table.add_column(columns[1], b)
table.add_column(columns[2], c)

# remove the table header
table.header = False

# set players
player1 = []
player2 = []
winner = []

# Welcome message
print('******* Welcome to the Tic Tac Toe Game! *******')

# Set up and play game
while not winner:
    print("\n")
    print(f"""a | d | g
--+---+---
b | e | h
--+---+---
c | f | i""")

    location_codes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    player1_select = input("Please select your location code from the above table:\n").lower()

    # player selection checking
    if player1_select in location_codes:

        player1.append(player1_select)
        location_codes.remove(player1_select)
        print(player1)

        # show progressive table

        A = "a"
        B = "b"
        C = "c"
        D = "d"
        E = "e"
        F = "f"
        G = "g"
        H = "h"
        I = "i"

        if A in player1 and A != "x" and A != "o":
            A = "x"
            if B != "x" and B != "o":
                B = "o"
                if "b" not in player2:
                    player2.append("b")
            elif D != "x" and D != "o":
                D = "o"
                if "d" not in player2:
                    player2.append("d")
            elif I != "x" and I != "o":
                I = "o"
                if "i" not in player2:
                    player2.append("i")
            elif C != "x" and C != "0":
                C = "o"
                if "c" not in player2:
                    player2.append("c")
            else:
                if G != "x" and G != "o":
                    G = "o"
                    if "g" not in player2:
                        player2.append("g")
        else:
            if A != "X" and A != "o":
                A = " "

        if B in player1 and B != "x" and B != "o":
            B = "x"
            if H != "x" and H != "o":
                H = "o"
                if "h" not in player2:
                    player2.append("h")
            elif E != "x" and E != "o":
                E = "o"
                if "e" not in player2:
                    player2.append("i")
            elif H != "x" and H != "e":
                H = "o"
                if "h" not in player2:
                    player2.append("h")
            else:
                if C != "x" and C != "o":
                    C = "o"
                    if "c" not in player2:
                        player2.append("c")
        else:
            if B != "x" and B != "o":
                B = " "

        if C in player1 and C != "x" and C != "o":
            C = "x"
            if E != "x" and E != "o":
                E = "o"
                if "e" not in player2:
                    player2.append("e")
            elif F != "x" and F != "o":
                F = "o"
                if "f" not in player2:
                    player2.append("f")
            elif I != "x" and I != "o":
                I = "o"
                if "i" not in player2:
                    player2.append("i")
            elif E != "x" and E != "o":
                E = "o"
                if "e" not in player2:
                    player2.append("e")
            elif A != "x" and A != "o":
                A = "o"
                if "a" not in player2:
                    player2.append("a")
            elif G != "x" and G != "o":
                G = "o"
                if "g" not in player2:
                    player2.append("g")
            else:
                if I != "x" and I != "o":
                    I = "o"
                    if "i" not in player2:
                        player2.append("i")
        else:
            if C != "x" and C != "o":
                C = " "

        if D in player1 and D != "x" and D != "o":
            D = "x"
            if G != "x" and G != "o":
                G = "o"
                if "g" not in player2:
                    player2.append("g")
            elif A != "x" and A != "o":
                A = "o"
                if "a" not in player2:
                    player2.append("a")
            elif E != "x" and E != "o":
                E = "o"
                if "e" not in player2:
                    player2.append("e")
            else:
                if F != "x" and F != "o":
                    F = "o"
                    if "f" not in player2:
                        player2.append("f")
        else:
            if D != "x" and D != "o":
                D = " "

        if E in player1 and E != "x" and E != "o":
            E = "x"
            if C != "x" and C != "o":
                C = "o"
                if "c" not in player2:
                    player2.append("c")
            elif G != "x" and G != "o":
                G = "o"
                if "g" not in player2:
                    player2.append("g")
            elif I != "x" and I != "o":
                I = "o"
                if "i" not in player2:
                    player2.append("i")
            else:
                if A != "x" and A != "o":
                    A = "o"
                    if "a" not in player2:
                        player2.append("a")
        else:
            if E != "x" and E != "o":
                E = " "

        if F in player1 and F != "x" and F != "o":
            F = "x"
            if D == "x" and E == " ":
                E = "o"
                if "e" not in player2:
                    player2.append("e")
            elif I != "x" and I != "o":
                I = "o"
                if "i" not in player2:
                    player2.append("i")
            elif C != "x" and C != "o":
                C = "o"
                if "c" not in player2:
                    player2.append("c")
            elif E != "x" and E != "o":
                E = "o"
                if "e" not in player2:
                    player2.append("e")
            else:
                if D != "x" and D != "o":
                    D = "o"
                    if "d" not in player2:
                        player2.append("d")
        else:
            if F != "x" and F != "o":
                F = " "

        if G in player1 and G != "x" and G != "o":
            G = "x"
            if A == "x" and D != "x" and D != "o":
                D = "o"
                if "d" not in player2:
                    player2.append("d")
            elif H != "x" and H != "o":
                H = "o"
                if "h" not in player2:
                    player2.append("h")
            elif A != "x" and A != "o":
                A = "o"
                if "a" not in player2:
                    player2.append("a")
            elif I != "x" and I != "o":
                I = "o"
                if "i" not in player2:
                    player2.append("i")
            elif D != "x" and D != "o":
                D = "o"
                if "d" not in player2:
                    player2.append("d")
            elif C != "x" and C != "o":
                    C = "o"
                    if "c" not in player2:
                        player2.append("c")
            else:
                if E != "x" and E != "o":
                    E = "o"
                    if "e" not in player2:
                        player2.append("e")
        else:
            if G != "x" and G != "o":
                G = " "

        if H in player1 and H != "x" and H != "o":
            H = "x"
            if B != "x" and B != "o":
                B = "o"
                if "b" not in player2:
                    player2.append("b")
            elif I != "x" and I != "o":
                I = "o"
                if "i" not in player2:
                    player2.append("i")
            elif G != "x" and G != "o":
                G = "o"
                if "g" not in player2:
                    player2.append("g")
            else:
                if E != "x" and E != "o":
                    E = "o"
                    if "e" not in player2:
                        player2.append("e")
        else:
            if H != "x" and H != "o":
                H = " "

        if I in player1 and I != "x" and I != "o":
            I = "x"
            if E == "x" and A == " ":
                A = "o"
                if "a" not in player2:
                    player2.append("a")
            elif A == "x" and E == " ":
                E = "o"
                if "e" not in player2:
                    player2.append("e")
            elif C != "x" and C != "o":
                C = "o"
                if "c" not in player2:
                    player2.append("c")
            elif E != "x" and E != "o":
                E = "o"
                if "e" not in player2:
                    player2.append("e")
            elif F != "x" and F != "o":
                F = "o"
                if "f" not in player2:
                    player2.append("f")
            elif A != "x" and A != "o":
                A = "o"
                if "a" not in player2:
                    player2.append("a")
            elif G != "x" and G != "o":
                G = "o"
                if "g" not in player2:
                    player2.append("g")
            else:
                if H != "x" and H != "o":
                    H = "o"
                    if "h" not in player2:
                        player2.append("h")
        else:
            if I != "x" and I != "o":
                I = " "

        progressive_table = f"""{A} | {D} | {G}
--+---+---
{B} | {E} | {H}
--+---+---
{C} | {F} | {I}"""
        print(progressive_table)

        # Check draw
        draw_check = [A, B, C, D, E, F, G, H, I]
        if " " not in draw_check and not winner:
            print("It's a draw!")
            rester = input("Would you like to play again?\n").lower()
            if rester == "yes" or rester == "y":
                # clear()
                player1 = []
                print("Let's do it!")
            else:
                print("Goodbye!")
                winner = True

        # Winning rule
        win_rules = [a, b, c, [a[0], b[0], c[0]], [a[1], b[1], c[1]], [a[2], b[2], c[2]], [c[0], b[1], a[2]],
                     [a[0], b[1], c[2]]]
        for rule in win_rules:
            if rule in player1 and not winner:
                winner = player1
                print("Congratulations! You are the winner😀")
            if rule in player2:
                winner = player2
                print("Sorry, you lost!😔\n"
                      "The computer is the winner!")

        # checking winner
        for rule in win_rules:
            if rule[0] in player1 and rule[1] in player1 and rule[2] in player1 and not winner:
                print(rule)
                print("Congratulations! You are the winner😀")
                rester = input("Would you like to play again?\n").lower()
                if rester == "yes" or rester == "y":
                    # clear()
                    player1 = []
                    print("Let's do it!")
                else:
                    print("Goodbye!")
                    winner = True

            if rule[0] in player2 and rule[1] in player2 and rule[2] in player2 and not winner:
                print(rule)
                print("Sorry, you lost!😔\n"
                      "The computer is the winner!")
                rester = input("Would you like to play again?\n").lower()
                if rester == "yes" or rester == "y":
                    # clear()
                    player1 = []
                    print("Let's do it!")
                else:
                    print("Goodbye!")
                    winner = True
    else:
        print("Incorrect code!")
        player1_select = input("Please select a correct location code from the above table:\n").lower()




