# Assignment 2 — Genetic Algorithm: Knapsack Problem
## Observation Report

**Student Name  :** Y Vignesh
**Student ID    :** 2310040087
**Date Submitted:** 2026-03-25  

---

## How to Submit

1. Run each experiment following the instructions below
2. Fill in every answer box — do not leave placeholders
3. Make sure the `plots/` folder contains all required images
4. Commit this README and the `plots/` folder to your GitHub repo

---

## Before You Begin — Read the Code

Open `ga_knapsack.py` and read through it. Then answer these questions.

**Q1. What does the `fitness()` function return? Why does an overweight solution score 0?**

```
The `fitness()` function returns the total value of all packed items in the knapsack. An overweight solution scores 0 because it violates the maximum weight constraint, making it an invalid solution, and a score of 0 ensures it is highly unlikely to be selected for reproduction.
```

**Q2. What does `tournament_select()` do? Why are higher-fitness individuals more likely to be chosen?**

```
`tournament_select()` randomly picks a small subset of individuals (k candidates) and returns the one with the highest fitness among them. Higher-fitness individuals are more likely to be chosen because they have a higher probability of being the best within any randomly selected subset, propelling the population towards better solutions.
```

**Q3. Look at the `run_ga()` loop. Find this line:**
```python
next_gen = [best_chromosome[:]]
```
**What is this doing? Why is it important to always keep the best solution?**

```
This line implements elitism by copying the absolute best chromosome from the current generation directly into the next generation. It is important to always keep the best solution so that the algorithm's performance monotonically improves (or stays the same) over generations, avoiding losing a great solution due to random mutation or crossover.
```

---

## Experiment 1 — Baseline Run

**Instructions:** Run the program without changing anything.
```bash
python ga_knapsack.py
```

**Fill in this table:**

| Metric | Your result |
|--------|-------------|
| Number of generations | 50 |
| Best value at generation 1 | 60 |
| Final best value | 77 |
| Total weight of best solution (kg) | 14.4 |
| Is solution valid (Yes / No) | Yes |

**Copy the printed packing list here:**
```
  Best Packing List
--------------------------------------
  + Water bottle
  + First aid kit
  + Sleeping bag
  + Torch
  + Energy bars (x6)
  + Rain jacket
  + Map & compass
  + Cooking stove
  + Rope (10 m)
  + Sunscreen
  + Power bank
--------------------------------------
  Weight : 14.4 / 15.0 kg
  Value  : 77
  Valid  : Yes
```

**Look at `plots/experiment_1.png` and describe what you see (2–3 sentences).**  
*Where does the biggest improvement happen? Does the curve flatten at some point?*
```
The biggest improvement happens in the early generations (roughly the first 10-20), where the algorithm rapidly discovers better items to pack. The curve then flattens out around the midway point, indicating that the population converged on a very strong regional optimum and stopped finding significantly better variations.
```

---

## Experiment 2 — Effect of Mutation Rate

**Instructions:** In `ga_knapsack.py`, find the `# EXPERIMENT 2` block in `__main__`.  
Copy it three times and run with `mutation_rate` = **0.01**, **0.05**, and **0.30**.  
Save plots as `experiment_2a.png`, `experiment_2b.png`, `experiment_2c.png`.

**Results table:**

| mutation_rate | Final best value | Weight (kg) | Valid? | Shape of curve |
|--------------|-----------------|-------------|--------|----------------|
| 0.01         | 75              | 14.9        | Yes    | Gradual steps, early flat plateau |
| 0.05         | 77              | 14.4        | Yes    | Steep initial climb, then plateau |
| 0.30         | 78              | 14.1        | Yes    | Climbing continuously with more small steps |

**Compare the three plots. What happens when mutation is too low? Too high? (3–4 sentences)**  
*Hint: Too low = no diversity, may get stuck. Too high = random search. What is the sweet spot?*
```
When mutation is too low (0.01), there is very little genetic diversity, causing the algorithm to get stuck in local optima early with a lower final score. When mutation is too high (0.30), the search becomes overly random, taking longer to converge smoothly. The sweet spot (0.05) balances exploration and exploitation, efficiently finding a robust high score without excessive randomness.
```

**Which mutation_rate gave the best result? Why do you think that is?**
```
The mutation_rate of 0.30 gave the absolute best final value (78) in this particular run. While 0.05 is generally safer and more efficient, the higher mutation rate injected enough random diversity to allow the algorithm to stumble upon a slightly better global optimum that the others missed.
```

---

## Summary

**Complete this table with your best result from each experiment:**

| Experiment | Key setting | Final value | Main finding in one sentence |
|------------|-------------|-------------|------------------------------|
| 1 — Baseline | mutation_rate = 0.05 | 77 | Balanced exploration yields a strong result quickly. |
| 2 — Mutation rate | mutation_rate = 0.30 | 78 | Higher mutation provides enough noise to reach a slightly better score here. |

**In your own words — what is the most important thing you learned about Genetic Algorithms from these experiments? (3–5 sentences)**
```
I learned that balancing exploration (mutation) and exploitation (crossover/selection) is crucial for a Genetic Algorithm to find high-quality solutions effectively. Too little mutation limits the algorithm to early, suboptimal solutions, while too much disrupts convergence, making it more like a random search. Additionally, retaining the best solution (elitism) is essential to ensure promising traits aren't entirely lost when high mutation or chaotic crossover occurs.
```

---

## Submission Checklist

- [x] Student name and ID filled in
- [x] Q1, Q2, Q3 answered
- [x] Experiment 1: table filled, packing list pasted, plot observation written
- [x] Experiment 2: results table filled (3 rows), observation and answer written
- [x] Summary table completed and reflection written
- [x] `plots/` contains: `experiment_1.png`, `experiment_2a.png`, `experiment_2b.png`, `experiment_2c.png`
