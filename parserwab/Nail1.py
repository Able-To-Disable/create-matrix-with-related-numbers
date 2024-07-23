import random
import pickle
import data dataclass from dataclasses


@dataclass
class MatrixManager:
    _defolt_file_name = 'matrix_data.pkl'

    def __init__(self, rows=3, cols=5):
        self._rows = rows
        self._cols = cols

    def get_new_matrix(self) -> list[list[int]]:
        """создаём и заполняем матрицу"""
        target_sum = 300
        new_matrix = []
        for i in range(self._rows):
            row = []
            for j in range(self._cols):
                if j == self._cols - 1:
                    item = target_sum - sum(row)
                else:
                    max_val = min(150, target_sum - sum(row) - (self._cols - j - 1))
                    item = random.randint(1, max_val)
                row.append(item)
            new_matrix.append(row)
        return new_matrix

    @staticmethod
    def display_matrix(matrix_to_display):
        """выводим матрицу"""
        for row in matrix_to_display:
            print(row)
        total_sum = sum([sum(row) for row in matrix_to_display])
        print("Сумма всех значений в матрице:", total_sum)

    @classmethod
    def write_matrix(cls, matrix_to_write, file_name=None):
        """записываем значения в файл"""
        with open(file_name or cls._defolt_file_name, 'wb') as f:
            pickle.dump(matrix_to_write, f)


if __name__ == "__main__":
    matrix_manager = MatrixManager()
    matrix = matrix_manager.get_new_matrix()
    matrix_manager.display_matrix(matrix)
    matrix_manager.write_matrix(matrix)
    print(matrix_manager.get_new_matrix.__doc__)
    print(matrix_manager.display_matrix.__doc__)
    print(matrix_manager.write_matrix.__doc__)
