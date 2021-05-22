>>> matrix_divided = __import__('2-matrix_divided').matrix_divided


#TypeError

    ### matrix must be a list of lists of integers or floats

    >>> matrix = [[True, False], [1.1 , 2.2]]
    >>> matrix_divided(matrix, 2)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix = [[]]
    >>> matrix_divided(matrix, 2)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix = []
    >>> matrix_divided(matrix, 2)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix = [1, 2, 3]
    >>> matrix_divided(matrix, 2)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix = "Holberton School"
    >>> matrix_divided(matrix, 2)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix = None
    >>> matrix_divided(matrix, 2)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    ### Each row of the matrix must be of the same size

    >>> matrix = [[1, 2, 3], [0], [0]]
    >>> matrix_divided(matrix, 2)
    Traceback (most recent call last):
    TypeError: Each row of the matrix must have the same size

    >>> matrix = [[1, 2], [1, 2, 3]]
    >>> matrix_divided(matrix, 2)
    Traceback (most recent call last):
    TypeError: Each row of the matrix must have the same size

    ### div must be a number (integer or float)

    >>> matrix = [[1.2, 2.4, 3.6], [4.8, 5.0, 6.2]]
    >>> matrix_divided(matrix, True)
    Traceback (most recent call last):
    TypeError: div must be a number

    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, "ups")
    Traceback (most recent call last):
    TypeError: div must be a number

    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> print(matrix_divided(matrix))
    Traceback (most recent call last):
    TypeError: matrix_divided() missing 1 required positional argument: 'div'

    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> print(matrix_divided())
    Traceback (most recent call last):
    TypeError: matrix_divided() missing 2 required positional arguments: 'matrix' and 'div'

    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> print(matrix_divided(None))
    Traceback (most recent call last):
    TypeError: matrix_divided() missing 1 required positional argument: 'div'


#ZeroDivisionError

    ### div can’t be equal to 0

    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero

    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, 0.9)
    [[1.11, 2.22, 3.33], [4.44, 5.56, 6.67]]



#General Case

    ### All elements of the matrix should be divided by div, rounded to 2 decimal places

    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> print(matrix_divided(matrix, 3))
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> print(matrix_divided(matrix, float('inf')))
    [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
