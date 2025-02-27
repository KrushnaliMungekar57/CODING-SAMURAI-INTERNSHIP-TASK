import numpy as np
import matplotlib.pyplot as plt

def generate_one_digit_numbers(num_samples=100):
    return np.random.randint(0, 10, num_samples)

def count_zero_or_one(numbers):
    return np.sum((numbers == 0) | (numbers == 1))

# User input for number of trials
num_trials = int(input("Enter the number of trials: "))
trial_counts = []

for _ in range(num_trials):
    numbers = generate_one_digit_numbers(100)
    trial_counts.append(count_zero_or_one(numbers))

# Plot Count vs Frequency for user-defined trials
plt.figure(figsize=(8, 5))
plt.hist(trial_counts, bins=range(min(trial_counts), max(trial_counts) + 1), color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Count of 0s or 1s')
plt.ylabel('Frequency')
plt.title(f'Count of 0s or 1s vs Frequency for {num_trials} Trials')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
