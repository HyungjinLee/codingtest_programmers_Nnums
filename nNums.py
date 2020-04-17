import copy 
# copy를 이용 안하는 법은 없을까? 고민중
def solution(N, number):  
    candidates = [set() for _ in range (8)]
    for i in range (8) :
        candidates[i].add(int(str(N) * (i+1)))
    def search(count) :
        global answer
        
        if count >= 8 :
            answer = -1
            return False
            
        for i in range (count) :
            j = count-i-1
            for x in copy.deepcopy(candidates[i]) :
                for y in copy.deepcopy(candidates[j]) :
                    candidates[count].add(x+y)
                    candidates[count].add(x-y)                   
                    candidates[count].add(x*y) 
                    if x != 0 :
                        candidates[count].add(y//x)
        
        if number in candidates[count] :
            answer = count+1
            return True      
        search(count+1)
    
    search(1)
    return answer