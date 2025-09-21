# PyTest String Validation

### **Introduction:**
Validate a string input using two specific tests: one to check the length and structure of the input string, and another to verify basic grammar rules. This will involve creating test cases using PyTest to ensure these checks are met.

### **Goal:**
Learn to create automated test cases using PyTest to validate code functionality based on predefined criteria.

<br>

### **Objectives:**
- Verify that string inputs meet specified length constraints (word and character limits).
- Ensure that string inputs adhere to basic structural rules, such as starting with an uppercase letter and ending with a period.

<br>

### **Instructions:**
<br>

#### **1. Setup**
- Open the `test_spellcheck.py` file in the **PROJECT** folder.

#### **2. Import Required Modules**
- Import the `pytest` module and the `spellcheck` module, which contains the functions you’ll be testing.

#### **3. Define Test String Variables**
- In `test_spellcheck.py`, two variables are already defined:
  - `alpha`: A string that should pass the tests.
  - `beta`: A string that should fail one of the tests (for the bonus step).
- Comment out the `beta` variable using the `#` symbol for now.

#### **4. Create PyTest Fixture**
- Create a fixture named `input_value()` that returns `alpha` as the default input string to be tested. This will allow you to test both functions with `alpha` by default.

#### **5. Write Test Functions**

- **Function `test_length()`**
   - This function should check the length of the string in terms of both words and characters.
   - **Step 5.1**: Add an `assert` statement to check that the `word_count()` function (from `spellcheck`) returns a value less than 10.
   - **Step 5.2**: Add an `assert` statement to check that the `char_count()` function (from `spellcheck`) returns a value less than 50.

- **Function `test_struc()`**
   - This function should check if the string adheres to basic grammar rules.
   - **Step 6.1**: Add an `assert` statement to call `first_char()` and check that the returned character is uppercase using `.isupper()`.
   - **Step 6.2**: Add an `assert` statement to call `last_char()` and check that it returns a period (`"."`).

#### **6. Save and Run Tests**
- After modifying the script, navigate to **File** > **Save** to save changes in the script. 
- In the **PROJECT** directory, navigate to **Terminal > New Terminal**.
- Run the test script using the following command:
  ```bash
  pytest test_spellcheck.py
- Both tests should pass if your code is implemented correctly.

### **Bonus Step:**
- Update the `input_value` fixture to return `beta` instead of `alpha`.  
- Rerun the tests. One of the tests should now fail, demonstrating that the tests can detect incorrect input based on the criteria defined.

<br>

### **Expected Results:**
- With `alpha` as the input, both tests should pass.
- With `beta` as the input (in the bonus step), one test should fail.

<br>
