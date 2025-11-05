from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import math
import time

class CalculatorTest:
    def __init__(self):
        # Initialize Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("file:///c:/my_drive/ip_project/index.html")
        time.sleep(1)  # Give the page a second to load

    def click_button(self, value):
        """Click a button based on its visible text."""
        button = self.driver.find_element(By.XPATH, f"//button[text()='{value}']")
        button.click()
        time.sleep(0.3)

    def clear(self):
        """Clear the calculator display."""
        self.click_button('C')

    def get_display_value(self):
        """Get the current calculator display value."""
        display = self.driver.find_element(By.ID, "display")
        return display.get_attribute("value")

    # ---- BASIC OPERATIONS ----
    def test_addition(self):
        self.clear()
        self.click_button('1')
        self.click_button('+')
        self.click_button('2')
        self.click_button('=')
        result = self.get_display_value()
        assert result == '3', f"Expected 3, got {result}"
        print("Addition test passed")

    def test_subtraction(self):
        self.clear()
        self.click_button('9')
        self.click_button('-')
        self.click_button('4')
        self.click_button('=')
        result = self.get_display_value()
        assert result == '5', f"Expected 5, got {result}"
        print("Subtraction test passed")

    def test_multiplication(self):
        self.clear()
        self.click_button('6')
        self.click_button('*')
        self.click_button('7')
        self.click_button('=')
        result = self.get_display_value()
        assert result == '42', f"Expected 42, got {result}"
        print("Multiplication test passed")

    def test_division(self):
        self.clear()
        self.click_button('8')
        self.click_button('/')
        self.click_button('2')
        self.click_button('=')
        result = self.get_display_value()
        assert result == '4', f"Expected 4, got {result}"
        print("Division test passed")

    def test_divide_by_zero(self):
        self.clear()
        self.click_button('5')
        self.click_button('/')
        self.click_button('0')
        self.click_button('=')
        result = self.get_display_value()
        assert result == 'Infinity', f"Expected Infinity, got {result}"
        print("Divide by zero test passed")

    # ---- SCIENTIFIC OPERATIONS ----
    def test_square(self):
        self.clear()
        self.click_button('5')
        self.click_button('x²')
        result = self.get_display_value()
        assert result == '25', f"Expected 25, got {result}"
        print("Square test passed")

    def test_square_root(self):
        self.clear()
        self.click_button('9')
        self.click_button('√')
        result = self.get_display_value()
        assert result == '3', f"Expected 3, got {result}"
        print("Square root test passed")

    def test_sin(self):
        self.clear()
        self.click_button('3')
        self.click_button('0')
        self.click_button('sin')
        result = float(self.get_display_value())
        expected = round(math.sin(math.radians(30)), 2)
        assert abs(result - expected) < 0.01, f"Expected {expected}, got {result}"
        print("Sine test passed")

    def test_cos(self):
        self.clear()
        self.click_button('6')
        self.click_button('0')
        self.click_button('cos')
        result = float(self.get_display_value())
        expected = round(math.cos(math.radians(60)), 2)
        assert abs(result - expected) < 0.01, f"Expected {expected}, got {result}"
        print("Cosine test passed")

    def test_tan(self):
        self.clear()
        self.click_button('4')
        self.click_button('5')
        self.click_button('tan')
        result = float(self.get_display_value())
        expected = round(math.tan(math.radians(45)), 2)
        assert abs(result - expected) < 0.01, f"Expected {expected}, got {result}"
        print("Tangent test passed")

    def test_log(self):
        self.clear()
        self.click_button('1')
        self.click_button('0')
        self.click_button('0')
        self.click_button('log')
        result = float(self.get_display_value())
        expected = round(math.log10(100), 2)
        assert abs(result - expected) < 0.01, f"Expected {expected}, got {result}"
        print("Log test passed")

    def test_ln(self):
        self.clear()
        self.click_button('2')
        self.click_button('ln')
        result = float(self.get_display_value())
        expected = round(math.log(2), 2)
        assert abs(result - expected) < 0.01, f"Expected {expected}, got {result}"
        print("Natural log test passed")

    def test_pi(self):
        self.clear()
        self.click_button('π')
        result = float(self.get_display_value())
        expected = round(math.pi, 2)
        assert abs(result - expected) < 0.01, f"Expected {expected}, got {result}"
        print("Pi constant test passed")

    # ---- TEST RUNNER ----
    def run_tests(self):
        try:
            self.test_addition()
            self.test_subtraction()
            self.test_multiplication()
            self.test_division()
            self.test_divide_by_zero()
            self.test_square()
            self.test_square_root()
            self.test_sin()
            self.test_cos()
            self.test_tan()
            self.test_log()
            self.test_ln()
            self.test_pi()
            print("\n✅ All calculator tests passed successfully!")
        except Exception as e:
            print(f"\n❌ Test failed: {e}")
        finally:
            self.driver.quit()


if __name__ == "__main__":
    test = CalculatorTest()
    test.run_tests()
