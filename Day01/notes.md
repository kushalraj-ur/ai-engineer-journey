# 🐍 Python – Day 01 Notes

**AI Engineer Journey | Day 01**

---

## 01. Introduction to Python

Python is a high-level, object-oriented, dynamically typed, interpreted scripting language, as well as a programming language.

### Characteristics of Python

1. **High-level language:** It is a human-readable language.
2. **Object-oriented language:** It supports classes and objects.
3. **Dynamically typed language:** The type of a variable is decided during runtime.
4. **Interpreted scripting language:** Code is executed through an interpreter. Execution stops when an unhandled error occurs.
5. **Programming language:** Used to develop different types of applications.

### Runtime vs Compile Time

| Concept | Definition |
|---|---|
| Runtime | The time taken by the machine to execute the program. |
| Compile Time | The time taken by the compiler to compile the program. |

---

## 02. Python Fundamentals

### 1. Variables
A variable is a name given to a memory location.

### 2. Identifiers
Names used in a program to identify classes, functions, variables, objects, etc.

### 3. Keywords
Predefined reserved words that have their own meaning in Python.

---

## 03. Rules of Identifiers

1. **Identifiers are alphanumeric.**

   Example:
   ```python
   num1 = 1
   ```

2. **Keywords are not allowed as identifiers.**

   Examples: `random`, `def`, `class`, etc.

3. **Special characters are not allowed except underscore (`_`).**

   Example:
   ```python
   class_name = "Python"
   ```

4. **Identifiers should not start with numbers.**

   Invalid examples:
   ```python
   1num
   2age
   ```

---

## 04. Output Statement

- `print()` is known as the output statement.

### Syntax

```python
print(*values, sep=' ', end='\n')
```

- `values`: Values to be printed.
- `sep`: Separator between multiple values. Default is a space.
- `end`: Character/string printed at the end. Default is a newline.

### Example

```python
print(10, 20, 30, 40, 50, 60, sep='-')
```

**Output:**
```text
10-20-30-40-50-60
```

---

## 05. Input Statement

- Used to take dynamic/user input from the user.

### Syntax

```python
input(msg)
```

### Example

```python
input('Enter number:')
```

**Example interaction:**
```text
Enter number: 10
```

### Important Note

The `input()` statement is designed in such a way that it takes input in the form of a string.

To overcome this, we perform **typecasting**, also called type conversion.

---

## 06. type() Function

`type()` is a built-in function that returns the data type of the value stored in a variable.

### Syntax

```python
type(variable)
```

### Example

```python
a = 10
print(a, type(a))
```

**Output:**
```text
10 <class 'int'>
```

---

## 07. Type Casting / Type Conversion

Type casting is the process of converting one data type into another data type.

### Types of Type Casting

#### 1. Implicit Type Casting

It is a process where the Python interpreter automatically converts one data type into another data type.

**Example:**

```python
a = 10
b = 2.5

c = a + b

print(c, type(c))
```

**Output:**
```text
12.5 <class 'float'>
```

#### 2. Explicit Type Casting

It is a process where the user manually converts one data type into another data type.

**Syntax:**

```python
variable_name = data_type(input(msg))
```

**Example:**

```python
a = int(input('Enter number:'))
```

---

## 08. Data Types

**Data:** Data is information that is collected and stored in a structured manner.

There are two types of data types:

### 1. Primitive / Primary Data Types

#### A. Numeric

| Type | Description | Examples |
|---|---|---|
| Integer (`int`) | Whole numbers | `3`, `4`, `5` |
| Float (`float`) | Decimal numbers | `3.4`, `34.5` |
| Complex (`complex`) | Complex numbers | `3j + 5j` |

#### B. String (`str`)

A character or sequence of characters enclosed within single, double or triple quotes.

Examples:

```python
a = 'q'
b = "q"
c = '''q'''
```

#### C. Boolean (`bool`)

Represents two values:

```python
True
False
```

### 2. Non-Primitive / Secondary Data Types

- List
- Tuple
- Dictionary
- Set

---

## 09. Operators

**Operators:** Symbols that perform specific operations.

**Operands:** Values on which operations take place.

### Types of Operators

#### I. Based on Number of Operands

| Type | Description |
|---|---|
| Unary | Operates on one operand (`NOT`, as covered in your notes) |
| Binary | Operates on two operands (`AND`, `OR`, as covered in your notes) |
| Ternary | Involves three operands |

#### II. Based on Operation

**A. Arithmetic Operators**

Used to perform arithmetic operations.

| Operator | Operation |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Modulus |
| `**` | Exponentiation |

**B. Relational Operators**

Used to compare two values.

```python
==  !=  <  >  <=  >=
```

**C. Logical Operators**

Used to evaluate multiple conditions and return Boolean values.

```python
and
or
not
```

**D. Bitwise Operators**

- Bitwise AND (`&`)
- Bitwise OR (`|`)
- XOR (`^`)
- Right Shift (`>>`)
- Left Shift (`<<`)
- Bitwise NOT / Tilde (`~`)

**E. Assignment Operator**

Used to assign a value to a variable.

```python
=
```

**F. Shorthand Assignment Operators**

Combination of arithmetic and assignment operators.

```python
+=
-=
/=
*=
```

#### III. Special Operators

- Membership operator
- Identity operator
- Dot operator
- Decorators
- Slicing

**A. Membership Operators**

Used to check whether an element is a member of a collection.

```python
in
not in
```

**B. Identity Operators**

Used to compare the identity of two objects.

```python
is
is not
```

---

## 10. Control Statements

Used to control the flow of programs.

### Types of Control Statements

1. **If Statement:** Executes a respective block of code if the condition is true.

2. **If-Else Statement:** Executes the `if` block when the condition is true; otherwise, executes the `else` block.

3. **Elif Statement:** A form of else-if statement used to check multiple conditions.

4. **Nested If Statement:** Contains multiple `if` statements inside another `if` statement.

5. **Match Case:** Used for pattern matching and selecting a block based on a matching case.

6. **Break:** Used to terminate a loop forcefully.

7. **Continue:** Used to skip the current iteration of a loop.

8. **Pass:** Used to create an empty block without executing any operation.

---

## 11. Looping Statements

Used to perform a task for a specific number of times or until a condition becomes false.

### I. For Loop

Executes a block of code for a specific number of iterations or over a collection.

**A. range()**

Used to iterate a specific number of times.

**B. Variable Iteration**

Used to iterate through a collection or non-primitive data types.

### II. While Loop

Executes a block of code until the condition becomes false.

---

## 12. Functions

A function is a block of code written for reusability and modularity. It executes when it is called.

### Types of Functions

#### 1. Built-in Functions

Predefined functions available in Python.

Examples:

- `print()`
- `input()`
- `type()`
- `len()`
- `id()`

#### 2. User-Defined Functions (UDF)

A function defined by the user is called a user-defined function.

**Syntax:**

```python
def function_name():
    # Statements

function_name()
```

### Types of User-Defined Functions

#### I. No Arguments, No Return Value

The function performs a fixed task and prints or updates something directly without sending data back.

```python
def greet():
    print("Hello, World!")

greet()
```

#### II. With Arguments, No Return Value

The function accepts input data to process, but does not return a result to the caller.

```python
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")
```

#### III. No Arguments, With Return Value

The function takes no inputs, generates or fetches a value internally, and sends it back using `return`.

```python
def get_pi():
    return 3.14159

pi_val = get_pi()
```

#### IV. With Arguments, With Return Value

The function takes input values, processes them, and returns the final result.

```python
def add(a, b):
    return a + b

total = add(5, 3)
```

### 3. Miscellaneous Function

Storing the reference of a function in a variable and accessing the function through that variable.

**Example:**

```python
def banana():
    print("Hello")

apple = banana

apple()
```

### 4. Anonymous Function

To be covered in upcoming lessons.

---

## 13. Strings

A string is a character or sequence of characters enclosed within single, double or triple quotes.

### Example

```python
name = 'kushal'
```

### F-Strings (Formatted String Literals)

F-strings are a modern and convenient way to format strings in Python.

They allow variables and expressions to be embedded directly inside strings using `{}`.

**Example:**

```python
a = 10
b = 20

print(f"a is {a} and b is {b}")
```

**Output:**
```text
a is 10 and b is 20
```

---

## 14. Day 01 Practice

### Programs Completed

- [x] FizzBuzz
- [x] Number Guessing Game

### Concepts Practised

- Variables and data types
- Input and output statements
- Type conversion
- Conditional statements
- Random number generation
- While loops
- Comparison operators
- Incrementing counters
- F-strings

---

**End of Day 01 – Python Fundamentals**

*Consistency is the key to mastering programming. Keep practising!* 🚀