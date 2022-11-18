import random

#F1
def getRandomList():   
    L = [] 
    val = None
    for i in range(15):
        val = random.randrange(0,2)
        L.append(val)
    return L
    

# def isSolution(L, weights, profits, capicity_maximun):
#     total_weights = 0
#     total_benifits = 0
#     solutions_indices = []
#     for i in range(len(L)):
#         if L[i] == 0: continue

#         total_weights = total_weights + weights[i]
#         total_benifits = total_benifits + profits[i]

#     if total_weights < capicity_maximun: return total_benifits
#     else: return reparer_solution(solutions_indices, weights, profits, capicity_maximun) 

#F2
def is_solution(L, weights, profits, capicity_maximun):
    weights_solutions = []
    profits_solutions = []

    for i in range(len(L)):
        if L[i] == 0: continue

        weights_solutions.append(weights[i])
        profits_solutions.append(profits[i])



    if sum(weights_solutions) > capicity_maximun: return False
    else: 
        # if(sum(profits_solutions) > 1100):
        #     print(sum(profits_solutions))
        return True

#F3 
def get_total_profits(L, profits):
    total = 0
    for i in range(len(L)):
        if L[i] == 0: continue
        total = total + profits[i]
    return total
    
#F4
def get_corrected_solution(L, weights, profits, capicity_maximun):
    while True:
        L_correc = L
        r = random.randint(0, 14)
        if L_correc[r] == 0: continue
        L_correc[r] = 0
        if not is_solution(L_correc, weights, profits, capicity_maximun): continue
        return L_correc

    

#F5
def get_next_solution(L, weights,weights_solution, profits, profits_solution,capicity_maximun, first_solution):
    print("first solution is: "+str(first_solution))
    flag = False
    for i in range(len(L)):
        if L[i] == 1: continue
        if(weights[i]+sum(weights_solution) < capicity_maximun): 
            flag = True
            return f"new solution is {str(first_solution+profits[i])}"
        

    if flag == False:
        return f"The first solution {first_solution} is optimum"



    
def get_solution_with_heuristic(weights, profits, max_capacity):
    profits_per_w_list = [profits[i]/weights[i] for i in range(len(profits))]
    print(profits_per_w_list)

    profits_per_w_dic = {}
    for val in range(len(profits_per_w_list)):
        profits_per_w_dic[val] = profits_per_w_list[val]

    #sorted_profits_per_w_dic = sorted(profits_per_w_list)
    sorted_profits_per_w_dic = {k: v for k, v in sorted(profits_per_w_dic.items(), key=lambda item: item[1], reverse=True)}
    print(sorted_profits_per_w_dic)
    
    acc_weights = 0
    idx_weigts = []
    solutions = []

    for i in sorted_profits_per_w_dic.keys():
        if(acc_weights + weights[i] > max_capacity): 
            continue
        acc_weights = acc_weights + weights[i]
        idx_weigts.append(i)

    for v in range(len(weights)):
        if v in idx_weigts:
            solutions.append(1)
        else: solutions.append(0)
    print(acc_weights)
    return solutions


