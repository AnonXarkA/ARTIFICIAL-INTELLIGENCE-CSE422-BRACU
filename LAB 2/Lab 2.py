import random
class alphabeta:   #creating alphabeta class
    def __init__(self,bracu_id,minmax_range):
        self.bracu_id = bracu_id
        self.minmax_range = minmax_range

    def alpha_beta_game(self): #alphabeta game

        bracu_id = self.bracu_id                #bracu id and min_max range which is in input
        minmax_range = self.minmax_range
        min_max = minmax_range.split(" ")

        min_val = int(min_max[0])
        max_val = int(min_max[1])
        num_turn = int(bracu_id[0])
        def_hp = (bracu_id[-1] + bracu_id[-2])
        initial_hp = int(def_hp)
        branch = int(bracu_id[2])
        depth = num_turn * 2
        list_tables = [[]]
        table_rows = int(num_turn * 2 + 1)

        for x in range(table_rows):        #this list creates table with coloumn value of 0
            for y in range(branch ** x):
                list_tables[x].append(0)
            if table_rows - 1 > x:
                list_tables.append([])   #removes extra rows from table

        table_lastrow_len = int(len(list_tables[len(list_tables) - 1]))    #taking tables last row lenght

        for x in range(table_lastrow_len):
            list_tables[len(list_tables) - 1][x] = random.randint(min_val, max_val)   # placing random value from random module in the last row

        last_row = int(len(list_tables) - 1)

        count = last_row
        for x in range(num_turn * 2):
            s = 0
            even = (x + 1) % 2
            if even != 0:  #checks even or odd
                for y in range(int((branch ** count) / branch)):
                    e = s + branch - 1

                    t = list_tables[count][s:e + 1]
                    list_tables[count - 1][y] = min(t)  #if it is odd number then it finds minimum
                    s = e + 1
                                                                                         #checking minimum or maximum
            else:
                for y in range(int((branch ** count) / branch)):
                    e = s + branch - 1

                    t = list_tables[count][s:e + 1]
                    list_tables[count - 1][y] = max(t) # #if it is not odd number then it finds maximum

                    s = e + 1

            count -= 1

        leaf = list_tables[last_row]

        aplha = min(leaf[:branch])
        compare = branch
        indx = branch

        for x in range(int((len(leaf) / branch) - 1)):     #compares leaf nodes
            c = 0
            while branch > c:
                if leaf[indx] < aplha:
                    compare += 1
                    indx = indx + branch - c
                    break
                else:
                    compare += 1

                indx += 1
                c += 1
            if branch == c:
                s = (x + 1) * branch
                aplha = min(leaf[s:indx])
        max_neg_HP = list_tables[0][0]
        life_left = initial_hp - max_neg_HP


        print1 = (f"Depth and Branches ratio is {depth} : {branch}\n")
        print2 = (f"Terminal States (leaf node values) are {list_tables[last_row]}\n")
        print3 = (f"Left life(HP) of the defender after maximum damage caused by the attacker is {life_left}\n")
        print4 = (f"After Alpha-Beta Pruning Leaf Node Comparisons {compare}")
        main_print = print1+print2+print3+print4
        return main_print



bracu_id = input("Enter BRACU ID: ")
minmax_range = input("ENter Minimum and Maximum value for the range of negative HP: ")

game = alphabeta(bracu_id,minmax_range)
print(game.alpha_beta_game())