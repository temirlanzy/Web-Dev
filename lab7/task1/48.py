n = int(input())
records = {}

for _ in range(n):
    data = input().split()
    name, scores = data[0], list(map(float, data[1:]))
    records[name] = scores

query_name = input()
average_score = sum(records[query_name]) / len(records[query_name])
print(f"{average_score:.2f}")
