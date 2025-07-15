import random
import matplotlib.pyplot as plt


trials = 100000


analytical_probs = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}


counter = {total: 0 for total in range(2, 13)}

for _ in range(trials):
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    total = roll1 + roll2
    counter[total] += 1


monte_probs = {k: v / trials for k, v in counter.items()}


print("Сума | Монте-Карло | Аналітична | Відхилення")
print("--------------------------------------------")
for value in range(2, 13):
    m = monte_probs[value]
    a = analytical_probs[value]
    diff = abs(m - a)
    print(f" {value:>3} |   {m:.4f}    |   {a:.4f}   |   {diff:.4f}")


sums = list(range(2, 13))
monte_vals = [monte_probs[s] for s in sums]
analytical_vals = [analytical_probs[s] for s in sums]

plt.figure(figsize=(10, 5))
plt.bar(sums, monte_vals, color='skyblue', label='Монте-Карло')
plt.plot(sums, analytical_vals, color='orange', marker='o', linewidth=2, label='Аналітична')
plt.xlabel("Сума кубиків")
plt.ylabel("Ймовірність")
plt.title("Порівняння ймовірностей: Монте-Карло vs Аналітична")
plt.legend()
plt.grid(True)
plt.show()