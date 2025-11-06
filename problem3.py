"""
Problem 3: Mini Contact Manager
Build a simple contact manager using lists and dictionaries.
Practice combining data structures and writing functions.
"""


def create_contact(name, phone, email=""):
    """
    Create a contact dictionary.

    Args:
        name (str): Contact name
        phone (str): Contact phone number
        email (str): Contact email (optional)

    Returns:
        dict: Contact dictionary with keys 'name', 'phone', 'email'

    Example:
        >>> create_contact("Alice", "555-0001", "alice@email.com")
        {'name': 'Alice', 'phone': '555-0001', 'email': 'alice@email.com'}
    """
    # problem 3.1
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    return contact


def add_contact(contacts, name, phone, email=""):
    """
    Add a new contact to the contacts list.

    Args:
        contacts (list): List of contact dictionaries
        name (str): Contact name
        phone (str): Contact phone
        email (str): Contact email (optional)

    Returns:
        dict: The newly created contact

    Example:
        >>> contacts = []
        >>> add_contact(contacts, "Alice", "555-0001")
        {'name': 'Alice', 'phone': '555-0001', 'email': ''}
        >>> len(contacts)
        1
    """
    # problem 3.2
    contact = create_contact(name, phone, email="")
    contacts.append(contact)
    return contact


def find_contact_by_name(contacts, name):
    """
    Find a contact by name (case-insensitive).

    Args:
        contacts (list): List of contact dictionaries
        name (str): Name to search for

    Returns:
        dict or None: The contact if found, None otherwise

    Example:
        >>> contacts = [{'name': 'Alice', 'phone': '555-0001', 'email': ''}]
        >>> find_contact_by_name(contacts, 'alice')
        {'name': 'Alice', 'phone': '555-0001', 'email': ''}
    """
    # problem 3.3
    # loops through the entire list of contact dicts until it finds a "name" key that is identical to the searched name
    # if no corresponding name is found, None is returned
    for contact in contacts:

        if contact["name"].lower() == name.lower():
            return contact
        
    return None


def search_contacts(contacts, search_term):
    """
    Search for contacts by name or phone (partial match).

    Args:
        contacts (list): List of contact dictionaries
        search_term (str): Term to search for

    Returns:
        list: List of matching contacts

    Example:
        >>> contacts = [
        ...     {'name': 'Alice Smith', 'phone': '555-0001', 'email': ''},
        ...     {'name': 'Bob Jones', 'phone': '555-0002', 'email': ''}
        ... ]
        >>> search_contacts(contacts, 'alice')
        [{'name': 'Alice Smith', 'phone': '555-0001', 'email': ''}]
    """
    # problem 3.4
    # matches is going to be the list of all contact dicts that match the search term (which is turned lower case)
    matches = []
    search_term = search_term.lower()
    # each entry for the keys "name" and "phone" of all contact dicts is compared to the search term
    for contact in contacts:
        name_matches = search_term in contact['name'].lower()
        phone_matches = search_term in contact['phone']
        
        # if name_matches or phone_matches return TRUE, the corresponding contact dict gets added to the matches list
        if name_matches or phone_matches:
            matches.append(contact)
            
    return matches


def delete_contact(contacts, name):
    """
    Delete a contact by name.

    Args:
        contacts (list): List of contact dictionaries
        name (str): Name of contact to delete

    Returns:
        bool: True if contact was deleted, False if not found

    Example:
        >>> contacts = [{'name': 'Alice', 'phone': '555-0001', 'email': ''}]
        >>> delete_contact(contacts, 'Alice')
        True
        >>> len(contacts)
        0
    """
    # problem 3.5
    search_name = name.lower()

    # .pop() uses the contact dict's list index
    # enumerate() creates index, contact pairs
    for index, contact in enumerate(contacts):
        if contact['name'].lower() == search_name:
            contacts.pop(index)
            return True
            
    # If the loop finishes without finding the name, FALSE is returned
    return False


def count_contacts_with_email(contacts):
    """
    Count how many contacts have an email address.

    Args:
        contacts (list): List of contact dictionaries

    Returns:
        int: Number of contacts with non-empty email

    Example:
        >>> contacts = [
        ...     {'name': 'Alice', 'phone': '555-0001', 'email': 'alice@email.com'},
        ...     {'name': 'Bob', 'phone': '555-0002', 'email': ''}
        ... ]
        >>> count_contacts_with_email(contacts)
        1
    """
    # problem 3.6
    counter = 0
    for contact in contacts:
        if contact["email"] != "":
            counter += 1
    return counter


def get_all_phone_numbers(contacts):
    """
    Extract all phone numbers from contacts.

    Args:
        contacts (list): List of contact dictionaries

    Returns:
        list: List of phone numbers

    Example:
        >>> contacts = [
        ...     {'name': 'Alice', 'phone': '555-0001', 'email': ''},
        ...     {'name': 'Bob', 'phone': '555-0002', 'email': ''}
        ... ]
        >>> get_all_phone_numbers(contacts)
        ['555-0001', '555-0002']
    """
    # problem 3.7
    phone_numbers = []
    for contact in contacts:
        phone_numbers.append(contact['phone'])
        
    return phone_numbers

def sort_contacts_by_name(contacts):
    """
    Return a new list of contacts sorted alphabetically by name.

    Args:
        contacts (list): List of contact dictionaries

    Returns:
        list: New list sorted by name

    Example:
        >>> contacts = [
        ...     {'name': 'Charlie', 'phone': '555-0003', 'email': ''},
        ...     {'name': 'Alice', 'phone': '555-0001', 'email': ''}
        ... ]
        >>> sorted_contacts = sort_contacts_by_name(contacts)
        >>> [c['name'] for c in sorted_contacts]
        ['Alice', 'Charlie']
    """
    # problem 3.8
    # "key" tells sorted() to look at each contact's "name" when comparing items
    # lambda c: c["name"] is a function that does the following:
    # for any contact c, get me c["name"]
    sorted_list = sorted(contacts, key=lambda c: c['name'])
    
    return sorted_list


def contact_exists(contacts, name):
    """
    Check if a contact with the given name exists.

    Args:
        contacts (list): List of contact dictionaries
        name (str): Name to check

    Returns:
        bool: True if contact exists, False otherwise
    """
    # problem 3.9
    # Use previous function:
    contact = find_contact_by_name(contacts, name)
    
    # find_contact_by_name returns a dict (found) or None (not found)
    if contact is not None:
        return True
    else:
        return False


# Test cases
if __name__ == "__main__":
    print("Testing Mini Contact Manager...")
    print("-" * 50)

    # Create test contacts list
    contacts = []

    # Test 1: create_contact
    print("Test 1: create_contact")
    contact = create_contact("Alice", "555-0001", "alice@email.com")
    print(f"Created: {contact}")
    assert contact == {'name': 'Alice', 'phone': '555-0001', 'email': 'alice@email.com'}
    print("✓ Passed\n")

    # Test 2: add_contact
    print("Test 2: add_contact")
    add_contact(contacts, "Alice", "555-0001", "alice@email.com")
    add_contact(contacts, "Bob", "555-0002")
    add_contact(contacts, "Charlie", "555-0003", "charlie@email.com")
    print(f"Added 3 contacts. Total: {len(contacts)}")
    assert len(contacts) == 3
    print("✓ Passed\n")

    # Test 3: find_contact_by_name
    print("Test 3: find_contact_by_name")
    found = find_contact_by_name(contacts, "alice")  # Case-insensitive
    print(f"Found: {found}")
    assert found is not None and found['name'] == 'Alice'
    print("✓ Passed\n")

    # Test 4: search_contacts
    print("Test 4: search_contacts")
    results = search_contacts(contacts, "555-000")
    print(f"Search '555-000' found {len(results)} contacts")
    assert len(results) == 3  # All have 555-000 in phone
    print("✓ Passed\n")

    # Test 5: count_contacts_with_email
    print("Test 5: count_contacts_with_email")
    count = count_contacts_with_email(contacts)
    print(f"Contacts with email: {count}")
    assert count == 2  # Alice and Charlie have emails
    print("✓ Passed\n")

    # Test 6: get_all_phone_numbers
    print("Test 6: get_all_phone_numbers")
    phones = get_all_phone_numbers(contacts)
    print(f"Phone numbers: {phones}")
    assert phones == ['555-0001', '555-0002', '555-0003']
    print("✓ Passed\n")

    # Test 7: sort_contacts_by_name
    print("Test 7: sort_contacts_by_name")
    sorted_contacts = sort_contacts_by_name(contacts)
    names = [c['name'] for c in sorted_contacts]
    print(f"Sorted names: {names}")
    assert names == ['Alice', 'Bob', 'Charlie']
    print("✓ Passed\n")

    # Test 8: contact_exists
    print("Test 8: contact_exists")
    assert contact_exists(contacts, "Alice") == True
    assert contact_exists(contacts, "David") == False
    print("✓ Passed\n")

    # Test 9: delete_contact
    print("Test 9: delete_contact")
    deleted = delete_contact(contacts, "Bob")
    print(f"Deleted Bob: {deleted}, Remaining: {len(contacts)}")
    assert deleted == True and len(contacts) == 2
    print("✓ Passed\n")

    print("=" * 50)
    print("All tests passed! Great work on the contact manager!")
