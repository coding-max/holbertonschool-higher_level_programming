>>> lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

#TypeError

    ### m_a and m_b must be a list

    >>> lazy_matrix_mul("Holberton", [1, 2, 3])
    Traceback (most recent call last):
    TypeError: m_a must be a list

    >>> lazy_matrix_mul("Holberton", [[1, 2], [3, 4]])
    Traceback (most recent call last):
    TypeError: m_a must be a list

    >>> lazy_matrix_mul([1, 2, 3], "School")
    Traceback (most recent call last):
    TypeError: m_b must be a list

    >>> lazy_matrix_mul([[1, 2], [3, 4]], "School")
    Traceback (most recent call last):
    TypeError: m_b must be a list

    >>> lazy_matrix_mul("Holberton", "School")
    Traceback (most recent call last):
    TypeError: m_a must be a list

    ### m_a and m_b must be a list of lists

    >>> lazy_matrix_mul([2, 4], [[1, 2], [3, 4]])
    Traceback (most recent call last):
    TypeError: m_a must be a list of lists

    >>> lazy_matrix_mul([[1, 2], [3, 4]], [2, 4])
    Traceback (most recent call last):
    TypeError: m_b must be a list of lists

    >>> lazy_matrix_mul([1, 2], [3, 4])
    Traceback (most recent call last):
    TypeError: m_a must be a list of lists

    ### all elements in m_a and m_b must be integers or floats

    >>> lazy_matrix_mul([[1, 2], [3, '4']], [[1, 2], [3, 4]])
    Traceback (most recent call last):
    TypeError: m_a should contain only integers or floats

    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, '4']])
    Traceback (most recent call last):
    TypeError: m_b should contain only integers or floats

    ### each row of m_a and m_b must be of the same size

    >>> lazy_matrix_mul([[1, 2], [3, 4, 5]], [[1, 2], [3, 4]])
    Traceback (most recent call last):
    TypeError: each row of m_a must be of the same size

    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4, 5]])
    Traceback (most recent call last):
    TypeError: each row of m_b must be of the same size

    ### other cases

    >>> lazy_matrix_mul()
    Traceback (most recent call last):
    TypeError: lazy_matrix_mul() missing 2 required positional arguments: 'm_a' and 'm_b'

    >>> lazy_matrix_mul(None)
    Traceback (most recent call last):
    TypeError: lazy_matrix_mul() missing 1 required positional argument: 'm_b'

    >>> lazy_matrix_mul([[1, 2], [3, 4]])
    Traceback (most recent call last):
    TypeError: lazy_matrix_mul() missing 1 required positional argument: 'm_b'



#ValueError

    ### m_a and m_b must be not empty

    >>> lazy_matrix_mul([], [[1, 2], [3, 4]])
    Traceback (most recent call last):
    ValueError: m_a can't be empty

    >>> lazy_matrix_mul([[]], [[1, 2], [3, 4]])
    Traceback (most recent call last):
    ValueError: m_a can't be empty

    >>> lazy_matrix_mul([[1, 2], [3, 4]], [])
    Traceback (most recent call last):
    ValueError: m_b can't be empty

    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[]])
    Traceback (most recent call last):
    ValueError: m_b can't be empty

    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[5, 6]])
    Traceback (most recent call last):
    ValueError: m_a and m_b can't be multiplied



#General Case

    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]

    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[5.5, 6.6], [7.7, 8.8]])
    [[20.9, 24.200000000000003], [47.3, 55.0]]

    >>> lazy_matrix_mul([[1.1, 2.2], [3.3, 4.4]], [[5.5, 6.6], [7.7, 8.8]])
    [[22.990000000000002, 26.620000000000005], [52.03, 60.5]]
