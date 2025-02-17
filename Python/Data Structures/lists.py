"""
LinkedIn (connect with me): https://linkedin.com/in/alex-t-reed
TikTok (follow): https://tiktok.com/@ar.codes
GitHub (for source code): https://github.com/alex-t-reed
YouTube (subscribe): https://www.youtube.com/@alex_t_reed
"""

"""
# Lists in Python
# I'm referencing: https://docs.python.org/3/tutorial/datastructures.html
# Add me (Alex Reed) on LinkedIn: https://www.linkedin.com/in/alextreed/
"""

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# Count: returns the number of times x is in a list 
print(f"The string 'apple' is found {fruits.count('apple')} time(s).")
# Prints 2 since that's how many instances of 'apple' are in fruits

# Index: list.index(x[, start[, end]])
print(fruits.index('banana')) # Returns 3, since 'banana' is 4th in list
# Let's say we wanted to know where the next instance of banana is, we could just set the start as the last index found for banana plus one
last_index_banana = fruits.index('banana')
print(fruits.index('banana', last_index_banana + 1))

current_length = len(fruits)
print(f'fruits list contains {len(fruits)} items')
# Current length of list: 7

# Append: list.append(x) - adds an item to the end of a list
fruits.append('banana')
print(f'fruits list now contains {len(fruits) - current_length} more items')

# Let's write a function that looks for all instances of banana and returns those indices as a list

def find_all_instances(search_list, find):
    """Returns all instances of a string in a list as indices."""
    return_list = []
    try:
        first_index = search_list.index(find)
        return_list.append(first_index)
        search_list_len = len(search_list)
        next_index = first_index + 1
        while next_index < search_list_len:  # Fix: changed != to <
            try:
                next_instance = search_list.index(find, next_index)
                return_list.append(next_instance)
                next_index = next_instance + 1  # Cange to the found index to continue search
            except ValueError:  # Catch ValueError specifically when no further match is found
                break  # Exit loop if no further match
    except ValueError as error:  # Catch ValueError for the first index search
        print(error)
        return return_list  # Return whatever has been found so far (if any)
    
    return return_list
    
# find_all_instances(fruits, 'Alex') - Returns a ValueError: 'Alex' is not in list
print(find_all_instances(fruits, 'banana')) # Returns [3, 6, 7]
