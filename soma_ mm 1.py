vetor = [int(i) for i in input().split()]
if len(vetor) > 5:
    exit()
print(max(vetor) + min(vetor))
