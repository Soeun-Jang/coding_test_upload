def solution(id_pw, db):
    _id = []
    for i in db:
        for j in range(2):
            if id_pw[0] == i[j]:
                _id.append(i[j])
                _id.append(i[j+1])

    if id_pw[0] not in _id:
        return "fail"
    elif id_pw != _id:
        return "wrong pw"
    else:
        return "login"