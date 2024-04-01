import os
import random
from typing import List, Optional, Any, Self

import numpy as np
from numpy.typing import ArrayLike
from numpy.lib.mixins import NDArrayOperatorsMixin
import numbers


def seed_everything(seed: int):
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)


class SaveToFileMixin:
    def save_to_file(self, path: str):
        with open(path, "w") as f:
            f.write(str(self))


class StrMixin:
    def __str__(self) -> str:
        return str(self.value)


class ValueMixin:
    def __init__(self, value: ArrayLike):
        super().__init__()
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


class Matrix(NDArrayOperatorsMixin, StrMixin, ValueMixin, SaveToFileMixin):
    def generate_random_matrix(rows: int, cols: int) -> Self:
        return Matrix(np.random.randint(0, 10, (rows, cols)))

    _HANDLED_TYPES = (np.ndarray, numbers.Number)

    # the implementation from offical doc
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get("out", ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (Matrix,)):
                return NotImplemented

        inputs = tuple(x.value if isinstance(x, Matrix) else x for x in inputs)
        if out:
            kwargs["out"] = tuple(x.value if isinstance(x, Matrix) else x for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            # multiple return values
            return tuple(type(self)(x) for x in result)
        elif method == "at":
            # no return value
            return None
        else:
            # one return value
            return type(self)(result)


if __name__ == "__main__":
    seed_everything(0)

    m1 = Matrix.generate_random_matrix(10, 10)
    m2 = Matrix.generate_random_matrix(10, 10)

    artifacts_dir = os.path.join(os.getcwd(), "hw_3", "artifacts", "3.2")
    (m1 + m2).save_to_file(os.path.join(artifacts_dir, "matrix+.txt"))
    (m1 * m2).save_to_file(os.path.join(artifacts_dir, "matrix_star.txt"))
    (m1 @ m2).save_to_file(os.path.join(artifacts_dir, "matrix@.txt"))
