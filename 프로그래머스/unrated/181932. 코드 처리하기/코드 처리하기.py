def solution(code):
    ret = ""
    mode = True
    for i,v in enumerate(code):
        if mode == True:
            if v != "1" and i%2 == 0:
                ret += v
            elif v == "1":
                mode = False
        elif mode == False:
            if v != "1" and i%2 == 1:
                ret += v
            elif v == "1":
                mode = True
    if ret == "":
        return "EMPTY"
    return ret
    
    