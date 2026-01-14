start_sum = float(input())
target_sum = float(input())
percent = float(input())
month = 0
current_sum = start_sum
while current_sum < target_sum:
    month += 1
    month_percent =(current_sum * percent) / 100 / 12
    current_sum += month_percent
    print(f'{month}-{current_sum:.2f}')