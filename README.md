# Assignment 2 — Genetic Algorithm: Knapsack Problem
## Observation Report

Student Name : D Guru Yeswanth  
Student ID : 2310040085  
Date Submitted: 18/03/2026  

---

## How to Submit

Run each experiment following the instructions below  
Fill in every answer box — do not leave placeholders  
Make sure the plots/ folder contains all required images  
Commit this README and the plots/ folder to your GitHub repo  

---

## Before You Begin — Read the Code

Open ga_knapsack.py and read through it. Then answer these questions.

### Q1. What does the fitness() function return? Why does an overweight solution score 0?

The fitness() function returns the total value of selected items.  
If the total weight exceeds the maximum allowed weight, the function returns 0.  
This prevents invalid overweight solutions from being selected.

### Q2. What does tournament_select() do? Why are higher-fitness individuals more likely to be chosen?

tournament_select() randomly selects a few individuals and picks the one with highest fitness.  
Higher fitness individuals win more often because they have better scores.  
This helps the algorithm keep good solutions in the population.

### Q3. Look at the run_ga() loop. Find this line:

next_gen = [best_chromosome[:]]

What is this doing? Why is it important to always keep the best solution?

This copies the best chromosome into the next generation.  
It prevents losing the best solution during crossover or mutation.  
This is called elitism and helps the algorithm converge faster.

---

## Experiment 1 — Baseline Run

Instructions: Run the program without changing anything.

python ga_knapsack.py

### Results Table

| Metric | Your result |
|--------|------------|
| Number of generations | 50 |
| Best value at generation 1 | 33 |
| Final best value | 46 |
| Total weight of best solution (kg) | 14.8 |
| Is solution valid (Yes / No) | Yes |

### Packing list

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
Value : 46  
Valid : Yes  

### Observation

The value increases quickly in early generations.  
After around generation 15 the improvement slows.  
The curve becomes flat near the end showing convergence.

---

## Experiment 2 — Effect of Mutation Rate

### Results table

| mutation_rate | Final best value | Weight (kg) | Valid? | Shape of curve |
|-------------|-----------------|------------|--------|---------------|
| 0.01 | 41 | 14.5 | Yes | Slow, gets stuck early |
| 0.05 | 46 | 14.8 | Yes | Smooth convergence |
| 0.30 | 38 | 13.9 | Yes | Noisy, unstable |

### Observation

When mutation is too low the population loses diversity and gets stuck early.  
When mutation is too high the search becomes random.  
Balanced mutation gives best result.  
0.05 is the best value.

### Best mutation rate

0.05 gave the best result because it balances exploration and stability.

---

## Summary

| Experiment | Key setting | Final value | Main finding in one sentence |
|-----------|------------|------------|------------------------------|
| 1 — Baseline | mutation_rate = 0.05 | 46 | Balanced mutation works best |
| 2 — Mutation rate | mutation_rate = 0.05 | 46 | Too low or too high mutation reduces performance |

### Reflection

Genetic algorithms depend strongly on mutation rate.  
Too low mutation causes early convergence.  
Too high mutation makes the search random.  
Keeping best solution every generation improves performance.  
Balanced parameters give best results.

---

## Submission Checklist

Student name and ID filled in  
Q1, Q2, Q3 answered  
Experiment 1: table filled, packing list pasted, plot observation written  
Experiment 2: results table filled (3 rows), observation and answer written  
Summary table completed and reflection written  
plots/ contains: experiment_1.png, experiment_2a.png, experiment_2b.png, experiment_2c.png