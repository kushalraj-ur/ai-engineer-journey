# 🐍 Python – Day 02 Notes

**AI Engineer Journey | Day 02**

---

# 01. Lists

A list is an ordered and changeable collection of elements. It allows duplicate values and can store different data types.

### Characteristics of Lists

- **Ordered:** Elements maintain their insertion order.
- **Changeable (Mutable):** Elements can be modified after creation.
- **Allows Duplicates:** Duplicate values are permitted.
- **Different Data Types:** Can store multiple data types.

### 1. Creating a List

**Syntax:**

```python
variable_name = [element1, element2, element3]
```

**Example:**

```python
nums = [10, 20, 30, 40, 50]
print(nums)
```

**Output:**

```text
[10, 20, 30, 40, 50]
```

A list can also contain different data types.

```python
data = [10, "Kushal", 3.5, True]
print(data)
```

### 2. Indexing

Indexing is used to access individual elements from a list.

Python uses zero-based indexing.

**Example:**

```python
nums = [10, 20, 30, 40, 50]

print(nums[0])
print(nums[2])
print(nums[4])
```

**Output:**

```text
10
30
50
```

### 3. Negative Indexing

Negative indexing is used to access elements from the end of a list.

- `-1` → Last element
- `-2` → Second-last element
- `-3` → Third-last element

**Example:**

```python
nums = [10, 20, 30, 40, 50]

print(nums[-1])
print(nums[-2])
```

**Output:**

```text
50
40
```

### 4. Slicing

Slicing is used to access a specific portion of a list.

**Syntax:**

```python
list_name[start : stop : step]
```

- `start`: Starting index (inclusive).
- `stop`: Ending index (exclusive).
- `step`: Number of positions to skip.

**Example 1:**

```python
nums = [10, 20, 30, 40, 50]

print(nums[1:4])
```

**Output:**

```text
[20, 30, 40]
```

**Example 2: Reverse a List**

```python
nums = [10, 20, 30, 40, 50]

print(nums[::-1])
```

**Output:**

```text
[50, 40, 30, 20, 10]
```

### 5. List Methods and Functions

| Method / Function | Description                                   |
| ----------------- | --------------------------------------------- |
| `append()`        | Adds an element at the end of the list.       |
| `insert()`        | Adds an element at a specified index.         |
| `remove()`        | Removes the first matching element.           |
| `pop()`           | Removes and returns an element.               |
| `sort()`          | Sorts the list in ascending order by default. |
| `len()`           | Returns the number of elements in a list.     |

**A. append()**

Adds an element at the end of the list.

```python
nums = [10, 20, 30]

nums.append(40)

print(nums)
```

Output:

```text
[10, 20, 30, 40]
```

**B. insert()**

Adds an element at a specified index.

Syntax:

```python
list_name.insert(index, element)
```

Example:

```python
nums = [10, 20, 40]

nums.insert(2, 30)

print(nums)
```

Output:

```text
[10, 20, 30, 40]
```

**C. remove()**

Removes the first occurrence of a specified value.

```python
nums = [10, 20, 30, 20]

nums.remove(20)

print(nums)
```

Output:

```text
[10, 30, 20]
```

**D. pop()**

Removes and returns an element using its index. If no index is provided, it removes the last element.

```python
nums = [10, 20, 30, 40]

nums.pop()

print(nums)
```

Output:

```text
[10, 20, 30]
```

**E. sort()**

Sorts the list in ascending order by default.

```python
nums = [40, 10, 30, 20]

nums.sort()

print(nums)
```

Output:

```text
[10, 20, 30, 40]
```

For descending order:

```python
nums.sort(reverse=True)

print(nums)
```

Output:

```text
[40, 30, 20, 10]
```

**F. len()**

Returns the total number of elements in a list.

```python
nums = [10, 20, 30, 40, 50]

print(len(nums))
```

Output:

```text
5
```

### 6. Looping Through Lists

**A. Using for loop**

Used to access elements directly.

```python
nums = [10, 20, 30, 40]

for x in nums:
    print(x)
```

Output:

```text
10
20
30
40
```

**B. Using enumerate()**

Used to access both the index and the element during iteration.

```python
nums = [10, 20, 30, 40]

for i, x in enumerate(nums):
    print(i, x)
```

Output:

```text
0 10
1 20
2 30
3 40
```

---

# 02. Dictionaries

A dictionary is an ordered and changeable collection that stores data in key-value pairs.

### Characteristics of Dictionaries

- **Ordered:** Maintains insertion order.
- **Changeable (Mutable):** Values can be modified.
- **Unique Keys:** Duplicate keys are not allowed.
- **Key-Value Pair:** Each value is associated with a key.

### 1. Creating a Dictionary

**Syntax:**

```python
variable_name = {
    "key1": "value1",
    "key2": "value2"
}
```

**Example:**

```python
student = {
    "name": "Kushal",
    "age": 22,
    "course": "Python"
}

print(student)
```

Output:

```text
{'name': 'Kushal', 'age': 22, 'course': 'Python'}
```

### 2. Reading Dictionary Values

Values can be accessed using their respective keys.

```python
student = {
    "name": "Kushal",
    "age": 22
}

print(student["name"])
print(student["age"])
```

Output:

```text
Kushal
22
```

### 3. Adding and Updating Values

The same assignment syntax is used to add a new key or update an existing key.

```python
student = {
    "name": "Kushal",
    "age": 22
}

# Adding a new key
student["city"] = "Bengaluru"

# Updating an existing key
student["age"] = 23

print(student)
```

Output:

```text
{'name': 'Kushal', 'age': 23, 'city': 'Bengaluru'}
```

### 4. Safe Reading Using get()

The `get()` method is used to retrieve a value without raising a KeyError when the key is missing.

**Syntax:**

```python
dictionary.get(key, default_value)
```

**Example:**

```python
student = {
    "name": "Kushal",
    "age": 22
}

print(student.get("name"))
print(student.get("marks", 0))
```

Output:

```text
Kushal
0
```

### 5. Dictionary Methods

| Method     | Description               |
| ---------- | ------------------------- |
| `keys()`   | Returns all keys.         |
| `values()` | Returns all values.       |
| `items()`  | Returns key-value pairs.  |
| `get()`    | Retrieves a value safely. |

**A. keys()**

```python
student = {"name": "Kushal", "age": 22}

print(student.keys())
```

Output:

```text
dict_keys(['name', 'age'])
```

**B. values()**

```python
print(student.values())
```

Output:

```text
dict_values(['Kushal', 22])
```

**C. items()**

```python
print(student.items())
```

Output:

```text
dict_items([('name', 'Kushal'), ('age', 22)])
```

### 6. Looping Through Dictionaries

**A. Using items()**

Used to access both keys and values.

```python
student = {
    "name": "Kushal",
    "age": 22,
    "course": "Python"
}

for key, value in student.items():
    print(key, value)
```

Output:

```text
name Kushal
age 22
course Python
```

**B. Using keys()**

```python
for key in student.keys():
    print(key)
```

**C. Using values()**

```python
for value in student.values():
    print(value)
```

### 7. Membership Operator

Used to check whether a particular key exists in a dictionary.

```python
student = {
    "name": "Kushal",
    "age": 22
}

print("name" in student)
print("marks" in student)
```

Output:

```text
True
False
```

**Note:** Membership checks dictionary keys by default, not values.

---

# 03. Sets

A set is an unordered collection of unique elements.

### Characteristics of Sets

- **Unordered:** Elements do not have fixed positions.
- **Mutable:** Elements can be added or removed.
- **Unique Elements:** Duplicate elements are automatically removed.
- **No Indexing:** Elements cannot be accessed using indexes.

### 1. Creating a Set

**Syntax:**

```python
variable_name = {element1, element2, element3}
```

**Example:**

```python
nums = {10, 20, 30, 40}

print(nums)
```

### 2. Removing Duplicates

Sets automatically remove duplicate elements.

```python
nums = set([1, 2, 2, 3])

print(nums)
```

Output:

```text
{1, 2, 3}
```

### 3. Set Methods

| Method           | Description                            |
| ---------------- | -------------------------------------- |
| `add()`          | Adds an element to the set.            |
| `remove()`       | Removes a specified element.           |
| `union()`        | Combines elements from two sets.       |
| `intersection()` | Returns common elements from two sets. |

**A. add()**

```python
nums = {10, 20, 30}

nums.add(40)

print(nums)
```

Output:

```text
{10, 20, 30, 40}
```

**B. remove()**

```python
nums = {10, 20, 30}

nums.remove(20)

print(nums)
```

Output:

```text
{10, 30}
```

Note: `remove()` raises a KeyError if the specified element does not exist.

### 4. Set Operations

Consider two sets:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

**A. Union (`|`)**

Combines all unique elements from both sets.

```python
print(a | b)
```

Output:

```text
{1, 2, 3, 4, 5, 6}
```

**B. Intersection (`&`)**

Returns only the common elements.

```python
print(a & b)
```

Output:

```text
{3, 4}
```

### 5. Membership Checking

Sets are useful for checking whether an element exists in a collection.

```python
nums = {10, 20, 30, 40}

print(20 in nums)
print(50 in nums)
```

Output:

```text
True
False
```

### 6. Main Uses of Sets

1. Removing duplicate elements.
2. Finding common elements between collections.
3. Combining unique elements.
4. Performing fast membership checks on average.

---

# 04. Tuples

A tuple is an ordered and unchangeable (immutable) collection of elements.

### Characteristics of Tuples

- **Ordered:** Maintains insertion order.
- **Immutable:** Elements cannot be modified after creation.
- **Allows Duplicates:** Duplicate elements are permitted.
- **Different Data Types:** Can store multiple data types.

### 1. Creating a Tuple

**Syntax:**

```python
variable_name = (element1, element2, element3)
```

**Example:**

```python
nums = (10, 20, 30, 40)

print(nums)
```

Output:

```text
(10, 20, 30, 40)
```

### 2. Indexing and Slicing

Tuples support both positive and negative indexing and slicing.

```python
nums = (10, 20, 30, 40, 50)

print(nums[0])
print(nums[-1])
print(nums[1:4])
```

Output:

```text
10
50
(20, 30, 40)
```

### 3. Tuple Immutability

Once a tuple is created, its elements cannot be changed.

```python
nums = (10, 20, 30)

# This will raise TypeError
nums[0] = 100
```

### 4. Tuple Unpacking

Tuple unpacking is used to assign tuple elements to individual variables.

**Example:**

```python
point = (3, 4)

x, y = point

print(x)
print(y)
```

Output:

```text
3
4
```

### 5. Single-Element Tuple

To create a tuple with one element, a trailing comma is required.

```python
a = (10,)

print(type(a))
```

Output:

```text
<class 'tuple'>
```

Without the comma, `(10)` is just an integer expression.

### 6. Tuple Methods

| Method    | Description                                      |
| --------- | ------------------------------------------------ |
| `count()` | Returns the number of occurrences of an element. |
| `index()` | Returns the index of the first occurrence.       |

**Example:**

```python
nums = (10, 20, 30, 20, 40)

print(nums.count(20))
print(nums.index(30))
```

Output:

```text
2
2
```

### 7. Uses of Tuples

1. Storing fixed data.
2. Representing coordinates and records.
3. Returning multiple values from functions.
4. Protecting collections from accidental modification.

---

# 05. Comprehensions

Comprehensions provide a concise way to create collections using an existing iterable.

They allow us to write shorter and cleaner code compared to traditional loops.

### Types of Comprehensions

1. List Comprehension
2. Dictionary Comprehension
3. Set Comprehension

### 1. List Comprehension

Used to create a new list from an existing iterable.

**Syntax:**

```python
new_list = [expression for item in iterable]
```

**Example:**

Using a traditional for loop:

```python
nums = [1, 2, 3, 4, 5]

squares = []

for x in nums:
    squares.append(x ** 2)

print(squares)
```

Using list comprehension:

```python
nums = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in nums]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

### 2. List Comprehension with Conditions

Used to filter elements based on a condition.

**Syntax:**

```python
new_list = [expression for item in iterable if condition]
```

**Example:**

Create a list containing only even numbers.

```python
nums = [1, 2, 3, 4, 5, 6]

even_nums = [x for x in nums if x % 2 == 0]

print(even_nums)
```

Output:

```text
[2, 4, 6]
```

### 3. Dictionary Comprehension

Used to create a dictionary in a concise way.

**Syntax:**

```python
new_dict = {key: value for item in iterable}
```

**Example:**

```python
nums = [1, 2, 3, 4]

squares = {x: x ** 2 for x in nums}

print(squares)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16}
```

### 4. Set Comprehension

Used to create a set from an iterable.

**Syntax:**

```python
new_set = {expression for item in iterable}
```

**Example:**

```python
nums = [1, 2, 2, 3, 3, 4]

unique_nums = {x for x in nums}

print(unique_nums)
```

Output:

```text
{1, 2, 3, 4}
```

### 5. Comprehension vs Traditional Loop

| Traditional Loop                                | Comprehension                                    |
| ----------------------------------------------- | ------------------------------------------------ |
| Requires multiple lines.                        | Usually requires fewer lines.                    |
| Creates collections using append or assignment. | Creates collections directly.                    |
| Can be easier for complex logic.                | Useful for simple transformations and filtering. |

---

# 06. Quick Comparison of Collections

| Feature      | List                   | Dictionary        | Set             | Tuple            |
| ------------ | ---------------------- | ----------------- | --------------- | ---------------- |
| Syntax       | `[]`                   | `{key: value}`    | `{}`            | `()`             |
| Ordered      | Yes                    | Yes               | No              | Yes              |
| Mutable      | Yes                    | Yes               | Yes             | No               |
| Duplicates   | Yes                    | Keys: No          | No              | Yes              |
| Indexing     | Yes                    | By key            | No              | Yes              |
| Main purpose | Collection of elements | Key-value storage | Unique elements | Fixed collection |

**Important:** An empty set is created using `set()`, not `{}`. Empty `{}` creates a dictionary.

---
### Concepts Covered

- Lists and list methods
- Positive and negative indexing
- Slicing
- enumerate()
- Dictionaries and key-value pairs
- Dictionary methods
- Sets and set operations
- Tuples and unpacking
- List comprehension
- Dictionary comprehension
- Set comprehension

---

**End of Day 02 – Python Collections & Comprehensions**

*Learn the logic, practise the implementation, and build something every day.* 🚀
