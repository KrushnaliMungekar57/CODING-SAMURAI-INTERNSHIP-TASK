import numpy as np
import matplotlib.pyplot as plt

def generate_one_digit_numbers(num_samples=100):
    return np.random.randint(0, 10, num_samples)

def count_zero_or_one(numbers):
    return np.sum((numbers == 0) | (numbers == 1))

# Step 1: Generate 100 one-digit numbers and plot the frequency distribution
numbers_100 = generate_one_digit_numbers(100)
freq_100 = [np.sum(numbers_100 == i) for i in range(10)]

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(range(10), freq_100, color='skyblue')
plt.xlabel('Digit')
plt.ylabel('Frequency')
plt.title('Frequency Distribution of Digits (100 Numbers)')

# Step 2: Perform trials of generating 100 one-digit numbers
num_trials = [10, 20, 30, 40, 50, 100, 200, 500, 1000]
trial_counts = []

for trials in num_trials:
    count_per_trial = [count_zero_or_one(generate_one_digit_numbers(100)) for _ in range(trials)]
    trial_counts.append(count_per_trial)

# Plot Count vs Frequency for all trials
plt.subplot(1, 2, 2)
for i, trials in enumerate(num_trials):
    plt.hist(trial_counts[i], bins=range(min(trial_counts[i]), max(trial_counts[i]) + 1), alpha=0.5, label=f'{trials} trials')

plt.xlabel('Count of 0s or 1s')
plt.ylabel('Frequency')
plt.title('Count of 0s or 1s vs Frequency for Multiple Trials')
plt.legend()
plt.tight_layout()
plt.show()
