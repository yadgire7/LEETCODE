original = [1,2,3,4]
m = 2
n = 2
two_d_array =[]
for i in range(m):
    two_d_array.append(original[i*n:(i+1)*n])
print(two_d_array)


