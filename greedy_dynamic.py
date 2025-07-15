
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True
    )
    selected = []
    total_cost = 0
    total_calories = 0

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            selected.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return selected, total_cost, total_calories


def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, data = item_list[i - 1]
        cost, calories = data["cost"], data["calories"]
        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]

    
    selected = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name, data = item_list[i - 1]
            selected.append(name)
            b -= data["cost"]

    total_calories = dp[n][budget]
    total_cost = sum(items[i]["cost"] for i in selected)

    return selected[::-1], total_cost, total_calories

#  Тестування
def compare_algorithms(items, budget):
    print(f" Бюджет: {budget}₴\n")

    print("🔹 Жадібний алгоритм:")
    g_items, g_cost, g_cal = greedy_algorithm(items, budget)
    print("  Страви:", g_items)
    print("  Вартість:", g_cost)
    print(" Калорійність:", g_cal)

    print("\n🔹 Динамічне програмування:")
    dp_items, dp_cost, dp_cal = dynamic_programming(items, budget)
    print("   Страви:", dp_items)
    print("  Вартість:", dp_cost)
    print("   Калорійність:", dp_cal)

compare_algorithms(items, budget=100)