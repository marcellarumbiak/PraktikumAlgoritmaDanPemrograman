dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print(f"{'key':<10}{'value':<10}{'item':<10}")


for key, value in dict.items():
    print(f"{key:<10}{value:<10}{key:<10}")
