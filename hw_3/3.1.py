import os
import random
from typing import List, Optional, Any, Self

import numpy as np
from numpy.typing import ArrayLike


def seed_everything(seed: int):
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)


class Matrix:
    def __init__(self, value: ArrayLike):
        self.value = value

    @property
    def value(self) -> ArrayLike:
        return self._value

    @value.setter
    def value(self, value: ArrayLike) -> None:
        self._value = value

    @property
    def cols(self) -> int:
        return len(self.value)

    @property
    def rows(self) -> int:
        return len(self.value[0])

    def generate_random_matrix(rows: int, cols: int) -> Self:
        return Matrix(np.random.randint(0, 10, (rows, cols)))

    def check_is_matrix(self, a: Any) -> None:
        if not isinstance(a, Matrix):
            raise ValueError("Invalid operand type")
        
    def save_to_file(self, path: str):
        with open(path, "w") as f:
            f.write(str(self))

    def __str__(self) -> str:
        return str(self.value)

    def __add__(self, other: Any) -> Self:
        self.check_is_matrix(other)
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Incompatible matrix dimensions")

        new_value = self.value.copy()
        for i in range(self.cols):
            for j in range(self.rows):
                new_value[i][j] += other.value[i][j]
        return Matrix(new_value)

    def __mul__(self, other: Any) -> Self:
        self.check_is_matrix(other)
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Incompatible matrix dimensions")

        new_value = self.value.copy()
        for i in range(self.cols):
            for j in range(self.rows):
                new_value[i][j] *= other.value[i][j]
        return Matrix(new_value)

    def __matmul__(self, other: Any) -> Self:
        self.check_is_matrix(other)
        if self.cols != other.rows:
            raise ValueError("Incompatible matrix dimensions")

        new_value = np.zeros((self.cols, other.rows), dtype=self.value.dtype)
        for i in range(self.cols):
            for j in range(self.rows):
                for k in range(self.rows):
                    new_value[i][j] += self.value[i][k] * other.value[k][j]
        return Matrix(new_value)


if __name__ == "__main__":
    seed_everything(0)

    m1 = Matrix.generate_random_matrix(10, 10)
    m2 = Matrix.generate_random_matrix(10, 10)

    artifacts_dir = os.path.join(os.getcwd(), "hw_3", "artifacts", "3.1")
    (m1 + m2).save_to_file(os.path.join(artifacts_dir, "matrix+.txt"))
    (m1 * m2).save_to_file(os.path.join(artifacts_dir, "matrix_star.txt"))
    (m1 @ m2).save_to_file(os.path.join(artifacts_dir, "matrix@.txt"))
