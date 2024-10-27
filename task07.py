import numpy as np
import matplotlib.pyplot as plt

num_simulations = 1000000
possible_sums = list(range(2, 13))
sum_counts = {sum_: 0 for sum_ in possible_sums}

for _ in range(num_simulations):
    dice1 = np.random.randint(1, 7)  
    dice2 = np.random.randint(1, 7)  
    dice_sum = dice1 + dice2
    sum_counts[dice_sum] += 1

sum_probabilities = {sum_: count / num_simulations for sum_, count in sum_counts.items()}

print("Сума | Імовірність (Монте-Карло)")
for sum_, prob in sum_probabilities.items():
    print(f"{sum_:>4} | {prob:.2%}")

analytical_probabilities = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]
monte_carlo_probs = [sum_probabilities[sum_] for sum_ in possible_sums]

plt.figure(figsize=(10, 6))
plt.plot(possible_sums, analytical_probabilities, label="Аналітична ймовірність", marker='o')
plt.plot(possible_sums, monte_carlo_probs, label="Ймовірність (Монте-Карло)", marker='x')
plt.xlabel("Сума")
plt.ylabel("Ймовірність")
plt.title("Ймовірності сум при киданні двох кубиків")
plt.legend()
plt.grid(True)
plt.show()

plt.savefig("monte_carlo_plot.png")