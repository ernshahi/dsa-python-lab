from typing import Any, Callable, Dict

class TestCaseRunner:
    def __init__(self):
        print("Test validator initialized")

    def run(self, tests: list[Dict[str, Any]], func: Callable) -> None:
        for test in tests:
            try:
                test_input = test["input"]
                expected_output = test["output"]
                result = func(test_input)
                if result == expected_output:
                    print(f"\033[92m✅ Test case passed: {test_input} -> {result} == {expected_output}\033[0m")
                else:
                    print(f"\033[91m❌ Test case failed: {test_input} -> {result} != {expected_output}\033[0m")
            except Exception as e:
                print(f"\033[91m❌ Test case failed: {test_input} -> {e}\033[0m")
            