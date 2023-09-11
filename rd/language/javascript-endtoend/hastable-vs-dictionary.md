# Hashtable vs Dictionary

The terms "hash table" and "dictionary" are often used interchangeably.

But there are some nuanced differences, mainly depending on the programming language or context in which you are working.

### Hash Table

1. **Definition**: A hash table is a low-level data structure that stores key-value pairs and uses a hash function to map keys to indices in an array.
2. **Collisions**: Handles collisions using techniques like open addressing or chaining.
3. **Language**: More commonly referred to as a hash table in languages like Java (`HashMap`) and C++ (`unordered_map`).
4. **Order**: Does not maintain the order of insertion.
5. **Performance**: Generally offers constant time complexity for add, delete, and search operations, but this can degrade depending on the load factor and the quality of the hashing function.

### Dictionary

1. **Definition**: A dictionary is a higher-level, abstract data structure that maps keys to values. It can be implemented using a hash table but could also use other means, like a balanced search tree.
2. **Collisions**: The user doesn't have to worry about collisions; the underlying implementation takes care of it.
3. **Language**: Referred to as a dictionary in languages like Python (`dict`) and .NET (`Dictionary`).
4. **Order**: Some dictionary implementations maintain the order of insertion (e.g., Python 3.7+).
5. **Performance**: Time complexity varies depending on the underlying implementation but often closely resembles that of a hash table.

### Summary Table

| Aspect      | Hash Table     | Dictionary           |
| ----------- | -------------- | -------------------- |
| Level       | Low-level      | High-level           |
| Collisions  | User-handled   | Internally handled   |
| Order       | Not maintained | Sometimes maintained |
| Language    | Java, C++      | Python, .NET         |
| Performance | O(1) typical   | Varies, often O(1)   |
