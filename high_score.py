scores = [1, 5 ,8, 17, 3.5, 9.2, 10]
scores2 = [0, 1, 2, 3, 4, 5]

def latest(scores):
    return scores[-1]


def personal_best(scores):
    scores.sort()
    return scores[-1]


def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores[0:3]



print(latest(scores2))
print(personal_best(scores2))
print(personal_top_three(scores2))


