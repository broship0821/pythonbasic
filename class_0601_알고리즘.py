## 선택정렬 알고리즘
# arr = [8, 4, 7, 3, 2]
# print(arr)
# if arr[0] > arr[1]:
#     arr[0], arr[1] = arr[1], arr[0]
# else:
#     if arr[0] > arr[2]:
#         arr[0], arr[2] = arr[2], arr[0]
#     else:
#         if arr[0] > arr[3]:
#             arr[0], arr[3] = arr[3], arr[0]
#         else:
#             if arr[0] > arr[4]:
#                 arr[0], arr[4] = arr[4], arr[0]
# print(arr)
# if arr[1] > arr[2]:
#     arr[1], arr[2] = arr[2], arr[1]
# else:
#     if arr[1] > arr[3]:
#         arr[1], arr[3] = arr[3], arr[1]
#     else:
#         if arr[1] > arr[4]:
#             arr[1], arr[4] = arr[4], arr[1]
# print(arr)
# if arr[2] > arr[3]:
#     arr[2], arr[3] = arr[3], arr[2]
# else:
#     if arr[2] > arr[4]:
#         arr[2], arr[4] = arr[4], arr[2]
# print(arr)
# if arr[3] > arr[4]:
#     arr[3], arr[4] = arr[4], arr[3]
# print(arr)

# arr = [3, 4, 7, 8, 2]
# print(arr)
# i=0
# if arr[i] > arr[i+1]:
#     arr[i], arr[i+1] = arr[i+1], arr[i]
# else:
#     if arr[i] > arr[i+2]:
#         arr[i], arr[i+2] = arr[i+2], arr[i]
#     else:
#         if arr[i] > arr[i+3]:
#             arr[i], arr[i+3] = arr[i+3], arr[i]
#         else:
#             if arr[i] > arr[i+4]:
#                 arr[i], arr[i+4] = arr[i+4], arr[i]
# print(arr)
# if arr[i+1] > arr[i+2]:
#     arr[i+1], arr[i+2] = arr[i+2], arr[i+1]
# else:
#     if arr[i+1] > arr[i+3]:
#         arr[i+1], arr[i+3] = arr[i+3], arr[i+1]
#     else:
#         if arr[i+1] > arr[i+4]:
#             arr[i+1], arr[i+4] = arr[i+4], arr[i+1]
# print(arr)
# if arr[i+2] > arr[i+3]:
#     arr[i+2], arr[i+3] = arr[i+3], arr[i+2]
# else:
#     if arr[i+2] > arr[i+4]:
#         arr[i+2], arr[i+4] = arr[i+4], arr[i+2]
# print(arr)
# if arr[i+3] > arr[i+4]:
#     arr[i+3], arr[i+4] = arr[i+4], arr[i+3]
# print(arr)

# arr = [3, 4, 7, 8, 2]
# print(arr)
# for i in range(1, len(arr)):
#     if arr[0] > arr[i]:
#         arr[0], arr[i] = arr[i], arr[0]
# print(arr)
# for i in range(2, len(arr)):
#     if arr[1] > arr[i]:
#         arr[1], arr[i] = arr[i], arr[1]
# print(arr)
# for i in range(3, len(arr)):
#     if arr[2] > arr[i]:
#         arr[2], arr[i] = arr[i], arr[2]
# print(arr)
# for i in range(4, len(arr)):
#     if arr[3] > arr[i]:
#         arr[3], arr[i] = arr[i], arr[3]
# print(arr)

#최종
# arr = [3, 4, 7, 8, 2, 9, 1, 6, 5]
# print(arr)
# for j in range(len(arr)):
#     for i in range(j+1, len(arr)):
#         if arr[j] > arr[i]:
#             arr[j], arr[i] = arr[i], arr[j]
#     print(arr)
