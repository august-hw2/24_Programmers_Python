def solution(rsp):
    
    win = {"2":"0", "0":"5", "5":"2"}
    res = ""
    
    for i in rsp:
        res += win.get(i)
        
    return res