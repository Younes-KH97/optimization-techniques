import random


def getRandomList():   #F1
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
def isSolution(L, weights, profits, capicity_maximun):
    weights_solutions = []
    profits_solutions = []

    for i in range(len(L)):
        if L[i] == 0: continue

        weights_solutions.append(weights[i])
        profits_solutions.append(profits[i])

    if sum(weights_solutions) < capicity_maximun: return get_next_solution(L,
                                                            weights,
                                                            weights_solutions,
                                                            profits ,
                                                            profits_solutions,
                                                            capicity_maximun,
                                                            first_solution=sum(profits_solutions))
    else: return get_corrected_solution(weights_solutions, profits_solutions, capicity_maximun) 

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

#F4
def get_corrected_solution(weights, profits, capicity_maximun):
    new_weights_solutions = []
    new_profits_solutions = []

    weights_dic = {}
    for i in range(len(weights)):
        weights_dic[i] = weights[i]

    sorted_weights_dic = {k: v for k, v in sorted(weights_dic.items(), key=lambda item: item[1])}
    sorted_weights_list = sorted(weights)

    if(sorted_weights_list[0] > capicity_maximun):
        return "Cannot fix this solution"

    for k in sorted_weights_dic.keys():
        new_weights_solutions.append(weights[k])
        new_profits_solutions.append(profits[k])

        if(sum(new_weights_solutions)<capicity_maximun): continue
        else: return "new corrected solution is: "+str(sum(new_profits_solutions))

    
def get_solution(weights, profits, max_capacity):
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


