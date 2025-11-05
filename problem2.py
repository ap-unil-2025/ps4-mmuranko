"""
Problem 2: Dictionary Operations and Nested Structures
Practice working with Python dictionaries - creating, accessing, modifying, and nesting them.
"""


def create_student_record(name, age, major, gpa):
    """
    Create a student record as a dictionary.

    Args:
        name (str): Student name
        age (int): Student age
        major (str): Student major
        gpa (float): Student GPA

    Returns:
        dict: Student record with keys 'name', 'age', 'major', 'gpa'

    Example:
        >>> create_student_record("Alice", 20, "Computer Science", 3.8)
        {'name': 'Alice', 'age': 20, 'major': 'Computer Science', 'gpa': 3.8}
    """
    # problem 2.1
    return {
        'name': name,
        'age': age,
        'major': major,
        'gpa': gpa
    }


def get_value_safely(dictionary, key, default=None):
    """
    Get a value from a dictionary safely, returning default if key doesn't exist.

    Args:
        dictionary (dict): The dictionary to search
        key: The key to look for
        default: Value to return if key not found

    Returns:
        The value if key exists, otherwise default

    Example:
        >>> d = {'a': 1, 'b': 2}
        >>> get_value_safely(d, 'a')
        1
        >>> get_value_safely(d, 'c', 'Not found')
        'Not found'
    """
    # problem 2.2
    # .get(key, default) tries to find the key.
    # If it finds it, it returns the value.
    # If it doesn't, it returns the default value
    return dictionary.get(key, default)


def merge_dictionaries(dict1, dict2):
    """
    Merge two dictionaries. If keys conflict, dict2's values take precedence.

    Args:
        dict1 (dict): First dictionary
        dict2 (dict): Second dictionary

    Returns:
        dict: Merged dictionary

    Example:
        >>> merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
        {'a': 1, 'b': 3, 'c': 4}
    """
    # problem 2.3
    # {**dict1} unpacks the first dict
    # {**dict2} unpacks the second and overwrites any matching keys from dict1
    return {**dict1, **dict2}


def count_word_frequency(text):
    """
    Count the frequency of each word in a text string.
    Convert to lowercase and ignore punctuation.

    Args:
        text (str): Input text

    Returns:
        dict: Dictionary mapping each word to its frequency

    Example:
        >>> count_word_frequency("hello world hello")
        {'hello': 2, 'world': 1}
    """
    # problem 2.4
    # Converts text to lowercase and removes simple punctuation
    cleaned_text = text.lower()
    cleaned_text = cleaned_text.replace('.', '').replace(',', '').replace('!', '').replace('?', '')

    # 3. Split into words
    words = cleaned_text.split()
    
    # 4. Count each word's frequency
    frequency = {}
    for word in words:
        # Get the current count (or 0 if it's not there) and add 1
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency


def invert_dictionary(dictionary):
    """
    Invert a dictionary (swap keys and values).
    Assume all values are unique.

    Args:
        dictionary (dict): Dictionary to invert

    Returns:
        dict: Inverted dictionary

    Example:
        >>> invert_dictionary({'a': 1, 'b': 2, 'c': 3})
        {1: 'a', 2: 'b', 3: 'c'}
    """
    # problem 2.5
    inverted = {}
    # .items() a list of (key, value) tuples
    # for each tuple, the key becomes the value and the value becomes the key in the inverted dict
    for key, value in dictionary.items():
        inverted[value] = key
    return inverted


def filter_dictionary(dictionary, keys_to_keep):
    """
    Create a new dictionary with only the specified keys.

    Args:
        dictionary (dict): Source dictionary
        keys_to_keep (list): List of keys to keep

    Returns:
        dict: Filtered dictionary

    Example:
        >>> filter_dictionary({'a': 1, 'b': 2, 'c': 3, 'd': 4}, ['a', 'c'])
        {'a': 1, 'c': 3}
    """
    # problem 2.6
    filtered_dict = {}
    # Check if key actually exists in the original dictionary
    # If it does, add the key and its value to the new dict
    for key in keys_to_keep:
        if key in dictionary:
            filtered_dict[key] = dictionary[key]
    return filtered_dict


def group_by_first_letter(words):
    """
    Group words by their first letter.

    Args:
        words (list): List of words

    Returns:
        dict: Dictionary where keys are first letters, values are lists of words

    Example:
        >>> group_by_first_letter(['apple', 'banana', 'apricot', 'blueberry'])
        {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}
    """
    # problem 2.7
    groups = {}
    for word in words:

        # Make sure the word is not empty
        if word: 
            first_letter = word[0]
            # Check if we have seen this letter before
            if first_letter in groups:
                # If yes, just append the word to the existing list
                groups[first_letter].append(word)
            else:
                # If no, this is the first time.
                # Create a new list for this letter, with the word in it.
                groups[first_letter] = [word]

    return groups


def calculate_grades_average(students):
    """
    Calculate the average grade for each student.

    Args:
        students (dict): Dictionary where keys are student names,
                        values are lists of grades

    Returns:
        dict: Dictionary where keys are student names,
              values are average grades (rounded to 2 decimals)

    Example:
        >>> calculate_grades_average({
        ...     'Alice': [90, 85, 88],
        ...     'Bob': [75, 80, 78]
        ... })
        {'Alice': 87.67, 'Bob': 77.67}
    """
    # problem 2.8
    average_grades = {}
    # Loop through each student (key) and their list of grades (value)
    for student, grades in students.items():
        
        # Make sure the grades list is not empty to avoid dividing by zero
        if grades:
            # Calculate the sum and count
            total_sum = sum(grades)
            count = len(grades)
            
            # Calculate the average
            average = total_sum / count
            
            # Store the rounded average in the new dictionary
            average_grades[student] = round(average, 2)
        else:
            # If a student has no grades, set their average to 0.0
            average_grades[student] = 0.0

    return average_grades


def nested_dict_access(data, keys):
    """
    Access a nested dictionary using a list of keys.
    Return None if any key doesn't exist.

    Args:
        data (dict): Nested dictionary
        keys (list): List of keys to traverse

    Returns:
        Value at the nested location, or None if not found

    Example:
        >>> data = {'a': {'b': {'c': 123}}}
        >>> nested_dict_access(data, ['a', 'b', 'c'])
        123
        >>> nested_dict_access(data, ['a', 'x'])
        None
    """
    # problem 2.9
    # Start with the top-level dictionary
    current_level = data
    
    try:
        # Loop through the list of keys to "dig" down
        for key in keys:
            current_level = current_level[key]
            
        # If the loop finishes, 'current_level' holds the final value
        return current_level
        
    except (KeyError, TypeError):
        # A KeyError happens if a key in the list doesn't exist.
        # A TypeError happens if we try to do [key] on something
        # that isn't a dictionary (like the number 123).
        # In either case, we stop and return None.
        return None


# Test cases
if __name__ == "__main__":
    print("Testing Dictionary Operations...")
    print("-" * 50)

    # Test create_student_record
    print("Test 1: create_student_record")
    result = create_student_record("Alice", 20, "CS", 3.8)
    print(f"Result: {result}")
    assert result == {'name': 'Alice', 'age': 20, 'major': 'CS', 'gpa': 3.8}
    print("✓ Passed\n")

    # Test get_value_safely
    print("Test 2: get_value_safely")
    d = {'a': 1, 'b': 2}
    assert get_value_safely(d, 'a') == 1
    assert get_value_safely(d, 'c', 'Not found') == 'Not found'
    print("✓ Passed\n")

    # Test merge_dictionaries
    print("Test 3: merge_dictionaries")
    result = merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
    print(f"Result: {result}")
    assert result == {'a': 1, 'b': 3, 'c': 4}
    print("✓ Passed\n")

    # Test count_word_frequency
    print("Test 4: count_word_frequency")
    result = count_word_frequency("hello world hello")
    print(f"Result: {result}")
    assert result == {'hello': 2, 'world': 1}
    print("✓ Passed\n")

    # Test invert_dictionary
    print("Test 5: invert_dictionary")
    result = invert_dictionary({'a': 1, 'b': 2, 'c': 3})
    print(f"Result: {result}")
    assert result == {1: 'a', 2: 'b', 3: 'c'}
    print("✓ Passed\n")

    # Test filter_dictionary
    print("Test 6: filter_dictionary")
    result = filter_dictionary({'a': 1, 'b': 2, 'c': 3, 'd': 4}, ['a', 'c'])
    print(f"Result: {result}")
    assert result == {'a': 1, 'c': 3}
    print("✓ Passed\n")

    # Test group_by_first_letter
    print("Test 7: group_by_first_letter")
    result = group_by_first_letter(['apple', 'banana', 'apricot', 'blueberry'])
    print(f"Result: {result}")
    assert result == {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}
    print("✓ Passed\n")

    # Test calculate_grades_average
    print("Test 8: calculate_grades_average")
    result = calculate_grades_average({
        'Alice': [90, 85, 88],
        'Bob': [75, 80, 78]
    })
    print(f"Result: {result}")
    assert result == {'Alice': 87.67, 'Bob': 77.67}
    print("✓ Passed\n")

    # Test nested_dict_access
    print("Test 9: nested_dict_access")
    data = {'a': {'b': {'c': 123}}}
    assert nested_dict_access(data, ['a', 'b', 'c']) == 123
    assert nested_dict_access(data, ['a', 'x']) is None
    print("✓ Passed\n")

    print("=" * 50)
    print("All tests passed! Excellent work!")
