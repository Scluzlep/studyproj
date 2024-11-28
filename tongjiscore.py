score = []
max_score = []
with open("score.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().split(" ")
        scores = [int(x) for x in line[1:]]
        score.append(scores)
        max_score.append(max(scores))
    print(max_score)
