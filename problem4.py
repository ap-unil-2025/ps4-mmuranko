"""
Problem 4: Data Persistence with JSON
Learn to use Python modules (imports) and save data to files using JSON.
"""

import json
# Note: json is a built-in Python module for working with JSON data


def save_to_json(data, filename):
    """
    Save data to a JSON file.

    Args:
        data: Python data structure (list, dict, etc.)
        filename (str): Name of file to save to

    Returns:
        bool: True if successful, False if error occurred

    Example:
        >>> data = {'name': 'Alice', 'age': 25}
        >>> save_to_json(data, 'test.json')
        True
    """
    # problem 4.1
    try:
        # "w" mode means "write" and overwrites the file
        # json.dump writes the data object "data" to the file "f"
        # indent=2 makes the file human-readable
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        return True
    except (IOError, TypeError):
        # permission denied (IOError)
        # data can't be serialized (TypeError)
        return False
    


def load_from_json(filename):
    """
    Load data from a JSON file.

    Args:
        filename (str): Name of file to load from

    Returns:
        Data from file if successful, None if error occurred

    Example:
        >>> data = load_from_json('test.json')
        >>> data
        {'name': 'Alice', 'age': 25}
    """
    # problem 4.2
    try:
        # "r" mode means "read"
        with open(filename, "r") as f:
            # json.load reads the file "f" and returns the python data
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file is not found etc., None is returned
        return None


def save_contacts_to_file(contacts, filename="contacts.json"):
    """
    Save a list of contacts to a JSON file.

    Args:
        contacts (list): List of contact dictionaries
        filename (str): File to save to (default: contacts.json)

    Returns:
        bool: True if successful, False otherwise
    """
    # problem 4.3
    # Uses the previous function save_to_json()
    return save_to_json(contacts, filename)


def load_contacts_from_file(filename="contacts.json"):
    """
    Load contacts from a JSON file.

    Args:
        filename (str): File to load from (default: contacts.json)

    Returns:
        list: List of contacts, or empty list if file doesn't exist
    """
    # problem 4.4
    contacts = load_from_json(filename)
    
    if contacts is None:
        # If the file does not exist or was empty, return a new empty list.
        return []
    else:
        # Otherwise, return the loaded contacts
        return contacts


def append_contact_to_file(contact, filename="contacts.json"):
    """
    Load existing contacts, add a new contact, and save back to file.

    Args:
        contact (dict): Contact dictionary to add
        filename (str): File to use

    Returns:
        bool: True if successful
    """
    # problem 4.5
    # load existing contacts via the previous function (which gives an empty list if the file does not exist)
    contacts = load_contacts_from_file(filename)
    
    # add new contact to list
    contacts.append(contact)
    
    # save updated list back to file
    return save_contacts_to_file(contacts, filename)


def backup_file(source_filename, backup_filename):
    """
    Create a backup copy of a file.

    Args:
        source_filename (str): Original file
        backup_filename (str): Backup file name

    Returns:
        bool: True if successful
    """
    # problem 4.6
    # load the data from the source via previous function
    data = load_from_json(source_filename)
    
    # check if loading failed
    if data is None:
        return False
    
    # save the data to the new backup file
    return save_to_json(data, backup_filename)


def get_file_stats(filename):
    """
    Get statistics about a JSON file.

    Args:
        filename (str): File to analyze

    Returns:
        dict or None: Dictionary with keys:
            - 'exists': bool
            - 'type': 'list' or 'dict' or 'other'
            - 'count': number of items (if list) or keys (if dict)
            - 'size_bytes': file size in bytes

    Example:
        >>> get_file_stats('contacts.json')
        {'exists': True, 'type': 'list', 'count': 5, 'size_bytes': 1234}
    """
    # problem 4.7
    import os

    stats = {}
    
    # check if file exists
    stats["exists"] = os.path.exists(filename)
    
    if not stats["exists"]:
        # if the file does not exist, this sets the other stats
        stats["type"] = None
        stats["count"] = 0
        stats["size_bytes"] = 0
    else:
        # if the file exists, os.path.getsize() gives the file size
        stats["size_bytes"] = os.path.getsize(filename)
        
        # load the file via older function to get "internal" stats
        data = load_from_json(filename)
        
        if data is None:
            # file exists, but is not a valid JSON
            stats["type"] = "corrupt_or_empty"
            stats["count"] = 0
        # find the number of items or keys
        elif isinstance(data, list):
            stats["type"] = "list"
            stats["count"] = len(data)
        elif isinstance(data, dict):
            stats["type"] = "dict"
            stats["count"] = len(data) # Number of keys
        else:
            stats["type"] = "other" # e.g., a single string or number
            stats["count"] = 1
    
    return stats

def merge_json_files(file1, file2, output_file):
    """
    Merge two JSON files containing lists.

    Args:
        file1 (str): First file
        file2 (str): Second file
        output_file (str): Output file

    Returns:
        bool: True if successful

    Example:
        If file1.json has [1, 2, 3] and file2.json has [4, 5],
        output_file.json will have [1, 2, 3, 4, 5]
    """
    # problem 4.8
    # load the data with previous function (will be [] if the file does not exist).
    list1 = load_contacts_from_file(file1)
    list2 = load_contacts_from_file(file2)

    # combine them
    combined_list = list1 + list2
    
    # save combined list
    return save_to_json(combined_list, output_file)


def search_json_file(filename, key, value):
    """
    Search a JSON file (containing a list of dicts) for items matching a key-value pair.

    Args:
        filename (str): JSON file to search
        key (str): Key to search for
        value: Value to match

    Returns:
        list: List of matching items

    Example:
        If file has [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
        search_json_file('data.json', 'name', 'Alice')
        returns [{'name': 'Alice', 'age': 25}]
    """
    # problem 4.9
    # load the data with previous function (will be [] if the file does not exist).
    data = load_contacts_from_file(filename)
    
    results = []
    for item in data:
        # .get(key) to prevent a crash if key does not exist (returns None)
        if item.get(key) == value:
            results.append(item)
            
    return results


# Test cases
if __name__ == "__main__":
    print("Testing JSON File Operations...")
    print("-" * 50)

    # Test 1: save_to_json and load_from_json
    print("Test 1: save_to_json and load_from_json")
    test_data = {'name': 'Alice', 'age': 25, 'city': 'Paris'}
    save_to_json(test_data, 'test_data.json')
    loaded_data = load_from_json('test_data.json')
    print(f"Saved and loaded: {loaded_data}")
    assert loaded_data == test_data
    print("✓ Passed\n")

    # Test 2: save_contacts_to_file and load_contacts_from_file
    print("Test 2: save and load contacts")
    contacts = [
        {'name': 'Alice', 'phone': '555-0001', 'email': 'alice@email.com'},
        {'name': 'Bob', 'phone': '555-0002', 'email': 'bob@email.com'}
    ]
    save_contacts_to_file(contacts, 'test_contacts.json')
    loaded_contacts = load_contacts_from_file('test_contacts.json')
    print(f"Loaded {len(loaded_contacts)} contacts")
    assert len(loaded_contacts) == 2
    assert loaded_contacts[0]['name'] == 'Alice'
    print("✓ Passed\n")

    # Test 3: append_contact_to_file
    print("Test 3: append_contact_to_file")
    new_contact = {'name': 'Charlie', 'phone': '555-0003', 'email': 'charlie@email.com'}
    append_contact_to_file(new_contact, 'test_contacts.json')
    contacts = load_contacts_from_file('test_contacts.json')
    print(f"After append: {len(contacts)} contacts")
    assert len(contacts) == 3
    print("✓ Passed\n")

    # Test 4: backup_file
    print("Test 4: backup_file")
    backup_file('test_contacts.json', 'test_contacts_backup.json')
    backup_data = load_from_json('test_contacts_backup.json')
    print(f"Backup created with {len(backup_data)} items")
    assert len(backup_data) == 3
    print("✓ Passed\n")

    # Test 5: get_file_stats
    print("Test 5: get_file_stats")
    stats = get_file_stats('test_contacts.json')
    print(f"File stats: {stats}")
    assert stats is not None
    assert stats['exists'] == True
    assert stats['type'] == 'list'
    assert stats['count'] == 3
    print("✓ Passed\n")

    # Test 6: merge_json_files
    print("Test 6: merge_json_files")
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    save_to_json(list1, 'list1.json')
    save_to_json(list2, 'list2.json')
    merge_json_files('list1.json', 'list2.json', 'merged.json')
    merged = load_from_json('merged.json')
    print(f"Merged list: {merged}")
    assert merged == [1, 2, 3, 4, 5, 6]
    print("✓ Passed\n")

    # Test 7: search_json_file
    print("Test 7: search_json_file")
    results = search_json_file('test_contacts.json', 'name', 'Alice')
    print(f"Search results: {results}")
    assert len(results) == 1
    assert results[0]['name'] == 'Alice'
    print("✓ Passed\n")

    # Cleanup
    print("Cleaning up test files...")
    import os
    for file in ['test_data.json', 'test_contacts.json', 'test_contacts_backup.json',
                 'list1.json', 'list2.json', 'merged.json']:
        if os.path.exists(file):
            os.remove(file)
    print("✓ Cleaned up\n")

    print("=" * 50)
    print("All tests passed! You've mastered JSON file operations!")