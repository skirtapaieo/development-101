def deep_merge(dict1, dict2):
    result = dict1.copy()  # Start with dict1's keys and values

    for key, value in dict2.items():
        # If key is not in dict1, add it to the result
        if key not in result:
            result[key] = value
        else:
            # If key is in dict1 and both dict1 and dict2 have a dictionary for this key, then deep merge
            if isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = deep_merge(result[key], value)
            else:
                # Otherwise, update the value from dict2
                result[key] = value

    return result

# Example usage
dict1 = {'a': 1, 'b': {'x': 10, 'y': 20}}
dict2 = {'a': 2, 'b': {'y': 25, 'z': 30}, 'c': 3}

merged_dict = deep_merge(dict1, dict2)
print("Merged Dictionary:", merged_dict)
