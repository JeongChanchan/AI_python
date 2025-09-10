def solution(k, d):
    answer = 0
    limit = (d // k) ** 2  

    for a in range(d // k + 1):     
        max_b = int((limit - a**2) ** 0.5)  
        answer += max_b + 1  

    return answer

print(solution(1,5))