# leetcode
Solutions to LeetCode problems in Python. Tracking progress and approaches!

[![LeetCode](https://img.shields.io/badge/LeetCode-alessiottavo-FFA116?logo=leetcode&logoColor=white)](https://leetcode.com/alessiottavo)

## Adding a new exercise

1. Create the solution file in the relevant category package, e.g.:
   ```
   top_interview_150/two_sum.py
   ```
   Use underscores (no hyphens) so Python can import it.

2. Implement the `Solution` class with the LeetCode method signature.

3. Create a test file alongside it:
   ```
   top_interview_150/test_two_sum.py
   ```
   Import pattern:
   ```python
   import pytest
   from top_interview_150.two_sum import Solution

   @pytest.fixture
   def s():
       return Solution()

   def test_example(s):
       assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
   ```

4. Run the tests locally:
   ```bash
   python3 -m pytest --tb=short -v
   ```
### Lessons Learned
* read instructions carefully
* problem constraints often point to solution
* consider the advantages sorting gives (ignore first element in duplicates, no need for maps etc etc)