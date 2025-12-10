[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/p5ZVvAv1)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=22013351&assignment_repo_type=AssignmentRepo)
# Hello World Assignment

A simple Python assignment for students to implement a "Hello World" function with unit tests and automated grading.

## Overview

This is a **GitHub Template Repository** designed for educational purposes. Students can use this as a starting point to complete the hello world assignment.

## Contents

- **`hello_world.py`** - Student assignment file with a function stub to implement
- **`test_hello_world.py`** - Comprehensive unit tests with automatic grading and feedback
- **`.gitignore`** - Git configuration file

## Assignment Instructions

### Task
Implement the `hello_world()` function in `hello_world.py` that returns the string `"Hello World"`.

### Requirements
1. The function must return a string (not print it)
2. The returned string must be exactly `"Hello World"` (case-sensitive)
3. The string cannot be empty

### How to Complete

1. Open `hello_world.py`
2. Replace the `pass` statement with your implementation
3. Make sure your function returns `"Hello World"`

Example:
```python
def hello_world():
    return "Hello World"
```

## Testing

To run the unit tests and get your grade:

```bash
python test_hello_world.py
```

or

```bash
python -m unittest test_hello_world.py -v
```

### Test Report

The test file provides:
- ✓/✗ indicators for each test
- Detailed error messages if tests fail
- A comprehensive score out of 10
- Performance feedback

### Scoring Breakdown
- **10/10** - All tests passed (Perfect implementation)
- **6.7/10** - 2 out of 3 tests passed
- **3.3/10** - 1 out of 3 tests passed
- **0/10** - No tests passed

## Using This as a Template

To create your own copy of this repository:

1. Go to [test-demo repository](https://github.com/Osmium-enfec/test-demo)
2. Click the **"Use this template"** button (green button in the top right)
3. Create a new repository from this template
4. Start working on the assignment!

## What Gets Tested

The `test_hello_world.py` file tests:

1. **Type Check** - Ensures the function returns a string
2. **Exact Output** - Verifies it returns exactly `"Hello World"`
3. **Non-Empty** - Confirms the string is not empty

## Example Output

When you run the tests, you'll see output like:

```
======================================================================
STUDENT ASSIGNMENT TEST REPORT - HELLO WORLD PROGRAM
======================================================================
✓ Test 1 PASSED: Function returns a string
✓ Test 2 PASSED: Function returns exactly 'Hello World'
✓ Test 3 PASSED: Function does not return empty string

----------------------------------------------------------------------
SUMMARY
----------------------------------------------------------------------
Tests Passed: 3/3
Tests Failed: 0/3

✓ NO ERRORS FOUND - Code is correct!

----------------------------------------------------------------------
FINAL SCORE: 10.0/10
----------------------------------------------------------------------
★ EXCELLENT WORK! Perfect implementation! ★
======================================================================
```

## Troubleshooting

If your tests fail, check:
- Did you return a string? (not print it)
- Is the string exactly `"Hello World"` with correct capitalization?
- Did you remove the `pass` statement?
- Are there any syntax errors?

## Questions?

If you have questions about the assignment, ask your instructor!

---

Happy coding! 🚀
