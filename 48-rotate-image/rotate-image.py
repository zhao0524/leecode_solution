class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        c = copy.deepcopy(matrix)
        # ij
        # 11 => 14
        # 12 => 24
        # 13 => 34 
        # 14 => 44
        # 22 => 23
        # 12 => 24
        # 22 => 23
        # 32 => 22
        # 42 => 21
        # new i = old j
        # new j = len(matrix)+1 - i

        for i in range(len(c)):
            for j in range(len(c)):
                matrix[j][len(matrix)-i-1] = c[i][j]
        return matrix
