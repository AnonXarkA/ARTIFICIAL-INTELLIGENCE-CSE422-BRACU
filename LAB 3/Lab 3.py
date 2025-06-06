import numpy as num_py
import random

def genetic_algo(money):
    population = num_py.random.randint(2, size=(4,c))
    for x in range(100):
        new_list = []
        for y in range(len(population)):
            root = selection(population,money)
            child = cross_func(root)
            child = mutation(child)
            if sum(child) == 0:
                genetic_algo(money)
                return
            if fitness_func(child,money) == 0:
                for x in child:
                    print(x,end="")
                # print(child)
                return
            new_list.append(child)
        population = new_list
    print(-1)
    return


def selection(population,money):
    array = []
    min_val = 999999
    population = num_py.array(population)
    for i in range(len(population)):
        v = fitness_func(population[i,:],money)
        if min_val < v:
            min_val = min_val
        if min_val > v :
            min_val = v
            array = population[i,:]
    return array

def cross_func(root):
    x = random.randint(0,len(root)-1)
    for i in range(x):
        y = random.randint(0,len(root)-1)
        z = random.randint(0,len(root)-1)
        root[y],root[z] = root[z],root[y]
    return root

def fitness_func(a,money):
    f = 0
    for i in range(len(money)):
        x =(money[i]*a[i])
        f = x + f
    f = abs(f)
    return f

def mutation(child):
    if random.uniform(0,1)< 0.6:
        num_py = random.randint(0,len(child)-1)
        if child[num_py] == 1:
            child[num_py] = child[num_py] - 1
            return child
        elif child[num_py] == 0:
            child[num_py] = child[num_py] +1
            return child
    return child


money = []

with open("input.txt","r") as input_file:
    for x in input_file:
        i = x.split()
        if i[0] == "l":
            money.append(int(i[1])*-1)
        elif i[0] == "d":
            money.append(int(i[1])*1)
        else:
            c = int(i[0])


genetic_algo(money)                 