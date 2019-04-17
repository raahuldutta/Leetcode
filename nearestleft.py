def leftSmaleer(arr, n, SE):
    stack = []
    for i in range(n):
        while stack!=[] and stack[len(stack) - 1] >= arr[i]:
            stack.pop()
        if stack!= []:
            SE[i] = stack[len(stack) - 1]
        else:
            SE[i] = 0
        stack.append(arr[i])




arr = [2, 4, 8, 7, 7, 9, 3] 
ls = [0] * len(arr)
rs = [0] * len(arr)
leftSmaleer(arr, len(arr), ls)
leftSmaleer(arr[::-1], len(arr), rs)
rs = rs[::-1]
ans = -1
for i in range(len(arr)):
    ans = max(ans, abs(ls[i] - rs[i]))
print(ans)

