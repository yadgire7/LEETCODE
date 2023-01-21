class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        two_d_array = []
        if m*n != len(original):
            return two_d_array
        else:
            for i in range(m):
                two_d_array.append(original[i*n:(i+1)*n])
            return (two_d_array)
