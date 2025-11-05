"""
Problem 1: List Operations and Comprehensions
Practice working with Python lists - creating, modifying, filtering, and transforming them.
"""


def create_number_list(start, end):
    """
    Create a list of numbers from start to end (inclusive).

    Args:
        start (int): Starting number
        end (int): Ending number

    Returns:
        list: List of numbers from start to end

    Example:
        >>> create_number_list(1, 5)
        [1, 2, 3, 4, 5]
    """
    # problem 1.1
    # range(start, end+1) creates the numbers from start to end, including end
    # list() converts that into a list
    return list(range(start, end + 1))


def filter_even_numbers(numbers):
    """
    Return a new list containing only the even numbers.

    Args:
        numbers (list): List of integers

    Returns:
        list: List of even numbers only

    Example:
        >>> filter_even_numbers([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
    """
    # problem 1.2
    # every element of numbers is checked for its divisibility by 2
    # if it is divisible by 2, it gets added to the list even_numbers
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers


def square_numbers(numbers):
    """
    Return a new list with each number squared.

    Args:
        numbers (list): List of numbers

    Returns:
        list: List where each element is squared

    Example:
        >>> square_numbers([1, 2, 3, 4])
        [1, 4, 9, 16]
    """
    # problem 1.3
    # all elements in numbers are squared and then added to the list squares
    squares=[]
    for n in numbers:
        squares.append(n**2)
    return squares


def find_max_min(numbers):
    """
    Find the maximum and minimum values in a list.

    Args:
        numbers (list): List of numbers

    Returns:
        tuple: (max_value, min_value)

    Example:
        >>> find_max_min([3, 1, 4, 1, 5, 9, 2, 6])
        (9, 1)
    """
    # problem 1.4
    # max and min values are initially set to 0
    max_number=[0]
    min_number=[0]
    # each number in numbers is compared to current max and min
    for n in numbers:
        if n>max_number[0]:
            max_number[0]=n
        if n<min_number[0] or min_number[0]==0:
            min_number[0]=n
    return (max_number[0], min_number[0])


def remove_duplicates(items):
    """
    Remove duplicate items from a list while preserving order.

    Args:
        items (list): List that may contain duplicates

    Returns:
        list: List with duplicates removed

    Example:
        >>> remove_duplicates([1, 2, 2, 3, 4, 3, 5])
        [1, 2, 3, 4, 5]
    """
    # problem 1.5
    # every element of items is checked if it is already in unique_items
    # if not, it gets added to unique_items
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items


def merge_lists(list1, list2):
    """
    Merge two lists, alternating elements from each.
    If one list is longer, append remaining elements.

    Args:
        list1 (list): First list
        list2 (list): Second list

    Returns:
        list: Merged list with alternating elements

    Example:
        >>> merge_lists([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
        >>> merge_lists([1, 2], [10, 20, 30, 40])
        [1, 10, 2, 20, 30, 40]
    """
    # problem 1.6
    # the shorter length of the two lists is determined
    combined_list = []
    short_len = min(len(list1), len(list2))
    # elements from both lists are added alternately to combined_list until the end of the shorter list is reached
    for i in range(short_len):
        combined_list.append(list1[i])
        combined_list.append(list2[i])
    # remaining elements from the longer list are added to combined_list
    if list1[short_len:] == [] and list2[short_len:] != []:
        combined_list.extend(list2[short_len:])
    elif list1[short_len:] != [] and list2[short_len:] == []:
        combined_list.extend(list1[short_len:])
    return combined_list


def list_statistics(numbers):
    """
    Calculate statistics for a list of numbers.

    Args:
        numbers (list): List of numbers

    Returns:
        dict: Dictionary with keys 'sum', 'average', 'count', 'max', 'min'

    Example:
        >>> list_statistics([1, 2, 3, 4, 5])
        {'sum': 15, 'average': 3.0, 'count': 5, 'max': 5, 'min': 1}
    """
    # problem 1.7
    # if the list is empty, return None
    if not numbers:
        return None
    
    # calculate sum, average, count, max, and min
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    maximum = max(numbers)
    minimum = min(numbers)
    return {
        'sum': total,
        'average': average,
        'count': count,
        'max': maximum,
        'min': minimum
    }


def chunk_list(items, chunk_size):
    """
    Split a list into chunks of specified size.

    Args:
        items (list): List to split
        chunk_size (int): Size of each chunk

    Returns:
        list: List of lists (chunks)

    Example:
        >>> chunk_list([1, 2, 3, 4, 5, 6, 7], 3)
        [[1, 2, 3], [4, 5, 6], [7]]
    """
    # problem 1.8
    chunks = []
    # range(0, len(items), chunk_size) generates starting indices for each chunk
    # slices of items from i to i + chunk_size are created and added to chunks
    for i in range(0, len(items), chunk_size):
        chunks.append(items[i:i + chunk_size])
    return chunks


# Test cases
if __name__ == "__main__":
    print("Testing List Operations...")
    print("-" * 50)

    # Test create_number_list
    print("Test 1: create_number_list(1, 5)")
    result = create_number_list(1, 5)
    print(f"Result: {result}")
    assert result == [1, 2, 3, 4, 5], "Failed!"
    print("✓ Passed\n")

    # Test filter_even_numbers
    print("Test 2: filter_even_numbers([1, 2, 3, 4, 5, 6])")
    result = filter_even_numbers([1, 2, 3, 4, 5, 6])
    print(f"Result: {result}")
    assert result == [2, 4, 6], "Failed!"
    print("✓ Passed\n")

    # Test square_numbers
    print("Test 3: square_numbers([1, 2, 3, 4])")
    result = square_numbers([1, 2, 3, 4])
    print(f"Result: {result}")
    assert result == [1, 4, 9, 16], "Failed!"
    print("✓ Passed\n")

    # Test find_max_min
    print("Test 4: find_max_min([3, 1, 4, 1, 5, 9, 2, 6])")
    result = find_max_min([3, 1, 4, 1, 5, 9, 2, 6])
    print(f"Result: {result}")
    assert result == (9, 1), "Failed!"
    print("✓ Passed\n")

    # Test remove_duplicates
    print("Test 5: remove_duplicates([1, 2, 2, 3, 4, 3, 5])")
    result = remove_duplicates([1, 2, 2, 3, 4, 3, 5])
    print(f"Result: {result}")
    assert result == [1, 2, 3, 4, 5], "Failed!"
    print("✓ Passed\n")

    # Test merge_lists
    print("Test 6: merge_lists([1, 3, 5], [2, 4, 6])")
    result = merge_lists([1, 3, 5], [2, 4, 6])
    print(f"Result: {result}")
    assert result == [1, 2, 3, 4, 5, 6], "Failed!"
    print("✓ Passed\n")

    # Test list_statistics
    print("Test 7: list_statistics([1, 2, 3, 4, 5])")
    result = list_statistics([1, 2, 3, 4, 5])
    print(f"Result: {result}")
    expected = {'sum': 15, 'average': 3.0, 'count': 5, 'max': 5, 'min': 1}
    assert result == expected, "Failed!"
    print("✓ Passed\n")

    # Test chunk_list
    print("Test 8: chunk_list([1, 2, 3, 4, 5, 6, 7], 3)")
    result = chunk_list([1, 2, 3, 4, 5, 6, 7], 3)
    print(f"Result: {result}")
    assert result == [[1, 2, 3], [4, 5, 6], [7]], "Failed!"
    print("✓ Passed\n")

    print("=" * 50)
    print("All tests passed! Great work!")
