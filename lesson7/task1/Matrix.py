from random import randrange


class Matrix:
    def __init__(self, i=0, j=0, is_random_fill=False, matrix_from_list=None):
        self.__is_random_fill = is_random_fill
        if matrix_from_list is not None:
            try:
                self.__i = len(matrix_from_list)
                self.__j = len(matrix_from_list[0])
                self.__matrix = matrix_from_list
            except:
                self.__i = i
                self.__j = j
                self.__matrix = []
        else:
            self.__i = int(input('Enter i: ')) if i == 0 else i
            self.__j = int(input('Enter j: ')) if j == 0 else j
            self.__matrix = []
            self.__fill()

    def __str__(self):
        result = ''
        for i in range(0, self.__i):
            result += f'{self.__matrix[i]}\n'
        return result

    def __random_fill(self):
        for i in range(0, self.__i):
            row = []
            for j in range(0, self.__i):
                row.append(randrange(0, 10))
            self.__matrix.append(row)

    def __fill_manually(self):
        for i in range(0, self.__i):
            row = []
            for j in range(0, self.__i):
                row.append(int(input(f'Enter element {i}, {j}: ')))
            self.__matrix.append(row)

    def __fill(self):
        if self.__is_random_fill:
            self.__random_fill()
        else:
            self.__fill_manually()

    def get_matrix(self):
        return self.__matrix

    def get_size(self):
        return {
            'i': self.__i,
            'j': self.__j
        }

    def multiply_matrix(self, target_matrix_obj):
        target_matrix_size = target_matrix_obj.get_size()
        if target_matrix_size.get('i') == self.__i and target_matrix_size.get('j') == self.__j:
            result_matrix = []
            target_matrix = target_matrix_obj.get_matrix()
            for i in range(0, self.__i):
                row = []
                for j in range(0, self.__i):
                    row.append(self.__matrix[i][j] + target_matrix[i][j])
                result_matrix.append(row)
            return Matrix(matrix_from_list=result_matrix)
