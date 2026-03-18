# Assignment 2 — Genetic Algorithm: Knapsack Problem
## Observation Report

**Student Name  :** D Guru Yeswanth  
**Student ID    :** 2310040085  
**Date Submitted:** 18/03/2026  

---

## How to Submit

1. Run each experiment following the instructions below
2. Fill in every answer box — do not leave placeholders
3. Make sure the plots/ folder contains all required images
4. Commit this README and the plots/ folder to your GitHub repo

---

## Before You Begin — Read the Code

Open ga_knapsack.py and read through it. Then answer these questions.

Q1. What does the fitness() function return? Why does an overweight solution score 0?

The fitness() function returns the total value of the packed items.
If the total weight exceeds the maximum limit, the function returns 0.
This prevents invalid overweight solutions from being selected.

Q2. What does tournament_select() do? Why are higher-fitness individuals more likely to be chosen?

tournament_select() randomly selects a few individuals and picks the one with the highest fitness.
Higher fitness individuals are more likely to win the tournament.
This helps the algorithm keep better solutions.

Q3. Look at the run_ga() loop. Find this line:

next_gen = [best_chromosome[:]]

What is this doing? Why is it important to always keep the best solution?

This copies the best chromosome into the next generation.
It prevents losing the best solution during mutation or crossover.
This method is called elitism and helps convergence.

---

## Experiment 1 — Baseline Run

python ga_knapsack.py

| Metric | Your result |
|--------|-------------|
| Number of generations | 50 |
| Best value at generation 1 | 33 |
| Final best value | 46 |
| Total weight of best solution (kg) | 14.8 |
| Is solution valid (Yes / No) | Yes |

Best Packing List

First aid kit  
Tent  
Sleeping bag  
Torch  
Energy bars (x6)  
Rain jacket  
Map & compass  
Power bank  

Weight : 14.8 / 15.0 kg  
Value  : 46  
Valid  : Yes  

Observation

The value increases quickly in early generations.
After generation 15 the improvement slows.
The curve becomes flat at the end.

---

## Experiment 2 — Effect of Mutation Rate

Results table

| mutation_rate | Final best value | Weight (kg) | Valid? | Shape of curve |
|--------------|-----------------|-------------|--------|----------------|
| 0.01 | 41 | 14.5 | Yes | slow |
| 0.05 | 46 | 14.8 | Yes | smooth |
| 0.30 | 38 | 13.9 | Yes | noisy |

Observation

When mutation is too low the algorithm gets stuck.
When mutation is too high the search becomes random.
0.05 gives the best balance.

Which mutation_rate gave the best result? Why?

0.05 gave the best result because it balances exploration and stability.

---

## Summary

| Experiment | Key setting | Final value | Main finding in one sentence |
|------------|-------------|-------------|------------------------------|
| 1 — Baseline | mutation_rate = 0.05 | 46 | balanced mutation works best |
| 2 — Mutation rate | mutation_rate = 0.05 | 46 | best performance |

Reflection

Genetic algorithms depend on mutation rate.
Too low causes early convergence.
Too high makes search random.
Balanced mutation gives best result.

---

## Submission Checklist

Student name and ID filled in  
Q1, Q2, Q3 answered  
Experiment 1 completed  
Experiment 2 completed  
Summary completed  
plots/ contains experiment_1.png experiment_2a.png experiment_2b.png experiment_2c.png