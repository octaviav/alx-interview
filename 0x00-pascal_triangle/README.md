# Pascal's Triangle

A Python function to generate Pascal's triangle up to `n` rows.

## Function

```python
def pascal_triangle(n):
    """
    Returns list of lists representing Pascal's triangle of n rows.
    Returns empty list if n <= 0.
    """
```

 Usage

```python
triangle = pascal_triangle(5)
# Output:
# [1]
# [1,1]
# [1,2,1]
# [1,3,3,1]
# [1,4,6,4,1]
```

# Algorithm

- Return empty list if n <= 0
- Start with first row [1]
- For each new row:
- Start with 1
- Middle values = sum of two numbers above
- End with 1
  
Files
- 0-pascal_triangle.py: Main function
- 0-main.py: Test script
