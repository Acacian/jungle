#3회차





















# import sys
# input = sys.stdin.readline

# N = input().strip()
# M = input().strip()
# # strip없으면 값달라짐

# LCS = [[0] * (len(N)+1) for _ in range(len(M)+1)]
# #LCS.insert(0, 0)

# for i in range(1, len(N)+1):
#     for j in range(1, len(M)+1):
#         if N[j-1] == M[i-1]:
#             LCS[i][j] = LCS[i-1][j-1] + 1
#         else:
#             LCS[i][j] = max(LCS[i][j-1], LCS[i-1][j])
# print(LCS[-1][-1])
