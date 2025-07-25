import numpy

numpy.set_printoptions(legacy='1.13')
arr = numpy.array([
    [2,2],
    [1,2],
    [3,4]
])

# N,M = map(int, input().split())

# arr = numpy.array([list(map(float, input().split())) for _ in range(N)])

print(numpy.mean(arr,axis=1))
print(numpy.var(arr,axis=0))
print(numpy.std(arr,axis=None))
# print(mean_Arr)
# print(var_arr)
# print(std_Arr)
