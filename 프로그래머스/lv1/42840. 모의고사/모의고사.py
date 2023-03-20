def solution(answers):
    scores = [0, 0, 0] 
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]  # 수포자3 패턴
    
    for i, ans in enumerate(answers):
        for j in range(3):
            if ans == patterns[j][i % len(patterns[j])]:
                scores[j] += 1
    
    
    max_score = max(scores)
    return [i+1 for i, score in enumerate(scores) if score == max_score]
