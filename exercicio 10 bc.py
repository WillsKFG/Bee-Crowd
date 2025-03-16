name = str(input())
salary = float(input())
sellsformonth = float(input())

total = (sellsformonth * .15) + salary
print(f"TOTAL = R$ {total:.2f}")