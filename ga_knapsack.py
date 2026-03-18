"""
ga_knapsack.py  —  Genetic Algorithm: 0/1 Knapsack Problem
===========================================================
This program is COMPLETE and works as-is. DO NOT rewrite it.

Your task:
  1. Read the code and understand how it works
  2. Run the 2 experiments described in README.md
  3. Save the plots and fill in your observations in README.md

HOW TO RUN
----------
    python ga_knapsack.py

PROBLEM
-------
A trekker is packing a 15 kg backpack. There are 15 items to choose from,
each with a weight and a value score. Pick items that maximise total value
without exceeding the weight limit.
"""

import random
import matplotlib.pyplot as plt
import os

# ================================
# PROBLEM DATA
# ================================

ITEMS = [
    ("Water bottle",2.0,9),
    ("First aid kit",1.5,10),
    ("Tent",4.0,10),
    ("Sleeping bag",3.0,9),
    ("Torch",0.5,6),
    ("Energy bars (x6)",1.0,7),
    ("Rain jacket",1.0,8),
    ("Map & compass",0.3,7),
    ("Camera",1.2,5),
    ("Extra clothes",2.0,4),
    ("Cooking stove",1.5,6),
    ("Rope (10 m)",2.5,5),
    ("Sunscreen",0.3,4),
    ("Trekking poles",1.5,5),
    ("Power bank",0.8,6),
]

NUM_ITEMS=len(ITEMS)
MAX_WEIGHT=15.0

WEIGHTS=[i[1] for i in ITEMS]
VALUES=[i[2] for i in ITEMS]
NAMES=[i[0] for i in ITEMS]


# ================================
# FITNESS
# ================================

def fitness(chromosome):

    w=sum(WEIGHTS[i] for i in range(NUM_ITEMS) if chromosome[i]==1)
    v=sum(VALUES[i] for i in range(NUM_ITEMS) if chromosome[i]==1)

    if w>MAX_WEIGHT:
        return 0

    return v


# ================================
# OPERATORS
# ================================

def tournament_select(population,fitnesses,k=3):

    c=random.sample(range(len(population)),k)
    w=max(c,key=lambda i:fitnesses[i])

    return population[w][:]


def crossover(p1,p2,rate=0.8):

    if random.random()>rate:
        return p1[:]

    cut=random.randint(1,NUM_ITEMS-1)

    return p1[:cut]+p2[cut:]


def mutate(chromosome,rate):

    r=chromosome[:]

    for i in range(NUM_ITEMS):

        if random.random()<rate:
            r[i]=1-r[i]

    return r


# ================================
# GA
# ================================

def run_ga(
    population_size=20,
    generations=50,
    crossover_rate=0.8,
    mutation_rate=0.05,
    tournament_size=3,
    seed=42,
):

    random.seed(seed)

    population=[
        [random.randint(0,1) for _ in range(NUM_ITEMS)]
        for _ in range(population_size)
    ]

    best=None
    best_val=-1
    log=[]

    for _ in range(generations):

        fitnesses=[fitness(c) for c in population]

        g=max(range(population_size),key=lambda i:fitnesses[i])

        if fitnesses[g]>best_val:
            best_val=fitnesses[g]
            best=population[g][:]

        log.append(best_val)

        next_gen=[best[:]]

        while len(next_gen)<population_size:

            p1=tournament_select(population,fitnesses)
            p2=tournament_select(population,fitnesses)

            child=crossover(p1,p2)
            child=mutate(child,mutation_rate)

            next_gen.append(child)

        population=next_gen

    return best,best_val,log


# ================================
# PRINT
# ================================

def print_solution(ch):

    w=sum(WEIGHTS[i] for i in range(NUM_ITEMS) if ch[i]==1)
    v=sum(VALUES[i] for i in range(NUM_ITEMS) if ch[i]==1)

    print("\nBest Packing List")

    for i in range(NUM_ITEMS):
        if ch[i]==1:
            print("+",NAMES[i])

    print("Weight:",w,"/",MAX_WEIGHT)
    print("Value:",v)


# ================================
# PLOT (COLAB FIX)
# ================================

def save_plot(log,name,title):

    os.makedirs("plots",exist_ok=True)

    plt.figure(figsize=(6,4))
    plt.plot(log,marker="o")
    plt.title(title)
    plt.xlabel("Generation")
    plt.ylabel("Value")

    plt.savefig(name)
    plt.show()   # important for colab
    plt.close()


# ================================
# RUN
# ================================

# EXP 1
best,val,log=run_ga()

print_solution(best)
print("Final:",val)

save_plot(log,"plots/experiment_1.png","baseline")


# EXP 2

c2,v2,l2=run_ga(mutation_rate=0.01)
print_solution(c2)
print("Final:",v2)
save_plot(l2,"plots/experiment_2a.png","0.01")


c3,v3,l3=run_ga(mutation_rate=0.05)
print_solution(c3)
print("Final:",v3)
save_plot(l3,"plots/experiment_2b.png","0.05")


c4,v4,l4=run_ga(mutation_rate=0.30)
print_solution(c4)
print("Final:",v4)
save_plot(l4,"plots/experiment_2c.png","0.30")


# show files
print(os.listdir("plots"))
