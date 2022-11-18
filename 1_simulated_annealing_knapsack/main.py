import methods_2

#Declaration of constants:
weights = [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120]
profits = [135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240]

capicity_maximun = 750


for i in range(10000):
    L = methods_2.getRandomList()
    is_solution = methods_2.is_solution(L, weights, profits, capicity_maximun)

    if is_solution == True:
        total_profits = methods_2.get_total_profits(L, profits)
    else:
        L = methods_2.get_corrected_solution(L, weights, profits, capicity_maximun)
        total_profits = methods_2.get_total_profits(L, profits)







