# Usage: python .

from numpy import array, mean, ndarray, std
from pandas import DataFrame
from scipy.optimize import fsolve
from typing import Any


def main():
    print("Hello World !")

    array_: ndarray[int] = get_numpy_array()
    print(f"Array Mean: {mean(array_)}")
    print(f"Array Standard Deviation: {std(array_)}")
    
    data_frame: DataFrame = get_pandas_data_frame()    
    print(f"Average Age: {data_frame["Age"].mean()}")

    print("SciPy Roots of x^2 - 4 = 0:")
    result: Any = get_scipy_result(2, 4)
    print(result)


def get_numpy_array() -> ndarray[int]:
    # Create a NumPy array
    array_: ndarray[int] = array([1, 2, 3, 4, 5])
    
    return array_


def get_pandas_data_frame() -> DataFrame:
    # Create a pandas DataFrame
    data: dict[str, Any] = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
    data_frame: DataFrame = DataFrame(data)
    
    return data_frame


def get_scipy_result(t1: int, t2: int) -> Any: 
    # Define a quadratic function: x^2 - 4 = 0
    def func(x) -> Any:
        return x ** t1 - t2

    # Solve for roots
    # Initial guesses: 1 and -1
    return fsolve(func, [1, -1])


if __name__ == "__main__":
    main()
