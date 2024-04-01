import os
import random
from typing import Any, Self, Tuple

import numpy as np
from numpy.typing import ArrayLike

from copy import copy


def seed_everything(seed: int):
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)


class HashMixin:
    def __hash__(self):
        """
        the hash sum is the sum of the hashes of each number in the matrix, shifted by 100, multiplied
        by the row and column indices (to encode position), and the result is modulo 10001
        """
        return sum(
            hash((self.value[i][j] + 100) * (i + j + 1) * (j + 1) % 10001)
            for i in range(self.rows)
            for j in range(self.cols)
        )


class Matrix(HashMixin):
    def __init__(self, value: ArrayLike):
        self.value = value

    matmul_cache = dict()

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

    def _matmul_no_cache(self, other: Any) -> Self:
        self.check_is_matrix(other)

        if self.cols != other.rows:
            raise ValueError("Incompatible matrix dimensions")

        new_value = np.zeros((self.cols, other.rows), dtype=self.value.dtype)
        for i in range(self.cols):
            for j in range(self.rows):
                for k in range(self.rows):
                    new_value[i][j] += self.value[i][k] * other.value[k][j]

        return Matrix(new_value)

    def __matmul__(self, other: Any) -> Self:
        hash_key = hash((hash(self), hash(other)))
        if hash_key in Matrix.matmul_cache:
            return Matrix.matmul_cache[hash_key]

        Matrix.matmul_cache[hash_key] = self._matmul_no_cache(other)
        return Matrix.matmul_cache[hash_key]

    def __copy__(self):
        return Matrix(self.value.copy())


def find_collision(rows: int, cols: int) -> Tuple[Matrix, Matrix]:
    i = 0
    while True:
        if i % 1000 == 0:
            print(f"Trying to find a collision, the attempt №{i}", flush=True)

        a = Matrix.generate_random_matrix(rows, cols)
        c = Matrix.generate_random_matrix(rows, cols)

        if hash(a) == hash(c) and any(
            a.value[i][j] != c.value[i][j] for i in range(rows) for j in range(cols)
        ):
            break
        i += 1
    return a, c


if __name__ == "__main__":
    seed_everything(0)
    rows = 10
    cols = 10

    a, c = find_collision(rows, cols)

    b = Matrix.generate_random_matrix(rows, cols)
    d = copy(b)

    artifacts_dir = os.path.join(os.getcwd(), "hw_3", "artifacts", "3.3")
    a.save_to_file(os.path.join(artifacts_dir, "A.txt"))
    b.save_to_file(os.path.join(artifacts_dir, "B.txt"))
    c.save_to_file(os.path.join(artifacts_dir, "C.txt"))
    d.save_to_file(os.path.join(artifacts_dir, "D.txt"))
    (a @ b).save_to_file(os.path.join(artifacts_dir, "AB.txt"))
    c @ d
    (c._matmul_no_cache(d)).save_to_file(os.path.join(artifacts_dir, "CD.txt"))

    with open(os.path.join(artifacts_dir, "hash.txt"), "w") as f:
        f.write(str([key for key in Matrix.matmul_cache]))
