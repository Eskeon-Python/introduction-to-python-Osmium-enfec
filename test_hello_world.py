"""
Unit tests for hello_world.py with detailed feedback and scoring
"""

import unittest
from hello_world import hello_world


class TestHelloWorld(unittest.TestCase):
    """Test cases for the hello_world function"""

    def test_hello_world_returns_string(self):
        """Test that hello_world returns a string"""
        result = hello_world()
        self.assertIsInstance(
            result, str, "Error: Function should return a string, not other data types")

    def test_hello_world_exact_output(self):
        """Test that hello_world returns exactly 'Hello World'"""
        result = hello_world()
        self.assertEqual(result, "Hello World",
                         f"Error: Expected 'Hello World' but got '{result}'")

    def test_hello_world_not_empty(self):
        """Test that hello_world does not return an empty string"""
        result = hello_world()
        self.assertNotEqual(
            result, "", "Error: Function should not return an empty string")


class TestReportGenerator(unittest.TestCase):
    """Generate comprehensive test report with scoring"""

    def test_generate_report(self):
        """Generate a detailed report of test results"""
        print("\n" + "="*70)
        print("STUDENT ASSIGNMENT TEST REPORT - HELLO WORLD PROGRAM")
        print("="*70)

        # Initialize tracking
        tests_passed = 0
        tests_failed = 0
        errors = []

        # Test 1: Check if function returns a string
        try:
            result = hello_world()
            if isinstance(result, str):
                tests_passed += 1
                print("✓ Test 1 PASSED: Function returns a string")
            else:
                tests_failed += 1
                error_msg = f"Function returns {type(result).__name__} instead of string"
                errors.append(error_msg)
                print(f"✗ Test 1 FAILED: {error_msg}")
        except Exception as e:
            tests_failed += 1
            error_msg = f"Exception in function: {str(e)}"
            errors.append(error_msg)
            print(f"✗ Test 1 FAILED: {error_msg}")

        # Test 2: Check if function returns exactly "Hello World"
        try:
            result = hello_world()
            if result == "Hello World":
                tests_passed += 1
                print("✓ Test 2 PASSED: Function returns exactly 'Hello World'")
            else:
                tests_failed += 1
                error_msg = f"Function returns '{result}' instead of 'Hello World'"
                errors.append(error_msg)
                print(f"✗ Test 2 FAILED: {error_msg}")
        except Exception as e:
            tests_failed += 1
            error_msg = f"Exception in function: {str(e)}"
            errors.append(error_msg)
            print(f"✗ Test 2 FAILED: {error_msg}")

        # Test 3: Check if function does not return empty string
        try:
            result = hello_world()
            if result != "":
                tests_passed += 1
                print("✓ Test 3 PASSED: Function does not return empty string")
            else:
                tests_failed += 1
                error_msg = "Function returns empty string"
                errors.append(error_msg)
                print(f"✗ Test 3 FAILED: {error_msg}")
        except Exception as e:
            tests_failed += 1
            error_msg = f"Exception in function: {str(e)}"
            errors.append(error_msg)
            print(f"✗ Test 3 FAILED: {error_msg}")

        # Calculate score
        total_tests = 3
        score = (tests_passed / total_tests) * 10

        # Print summary
        print("\n" + "-"*70)
        print("SUMMARY")
        print("-"*70)
        print(f"Tests Passed: {tests_passed}/{total_tests}")
        print(f"Tests Failed: {tests_failed}/{total_tests}")

        if errors:
            print("\nERRORS FOUND:")
            for i, error in enumerate(errors, 1):
                print(f"  {i}. {error}")
        else:
            print("\n✓ NO ERRORS FOUND - Code is correct!")

        print("\n" + "-"*70)
        print(f"FINAL SCORE: {score:.1f}/10")
        print("-"*70)

        if score == 10:
            print("★ EXCELLENT WORK! Perfect implementation! ★")
        elif score >= 7:
            print("★ GOOD WORK! Your code is mostly correct. ★")
        elif score >= 5:
            print("★ FAIR - Some issues to fix. ★")
        else:
            print("★ NEEDS IMPROVEMENT - Please review the errors above. ★")

        print("="*70 + "\n")


if __name__ == "__main__":
    unittest.main(verbosity=2)
