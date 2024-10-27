items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']
    
    return selected_items, total_calories

def dynamic_programming(budget):
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    item_list = list(items.keys())

    for i in range(1, n + 1):
        for w in range(budget + 1):
            cost = items[item_list[i - 1]]['cost']
            calories = items[item_list[i - 1]]['calories']
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_list[i - 1])
            w -= items[item_list[i - 1]]['cost']

    selected_items.reverse() 
    return selected_items, dp[n][budget]

budget = 100
greedy_result = greedy_algorithm(budget)
dp_result = dynamic_programming(budget)

print("Жадібний алгоритм:")
print("Вибрані страви:", greedy_result[0], "з загальною калорійністю:", greedy_result[1])
print("\nАлгоритм динамічного програмування:")
print("Вибрані страви:", dp_result[0], "з загальною калорійністю:", dp_result[1])