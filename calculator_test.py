from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import math
import time


class CalculatorTestV2:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("file:///c:/my_drive/ip_project/index.html")
        time.sleep(1)  # Allow load time

    def click_button(self, value):
        btn = self.driver.find_element(By.XPATH, f"//button[text()='{value}']")
        btn.click()
        time.sleep(0.2)

    def clear(self):
        self.click_button("C")

    def get_display(self):
        return self.driver.find_element(By.ID, "display").get_attribute("value")

   

    def test_basic_operations(self):
        print("\n---- BASIC TESTS ----")

        # Addition
        self.clear()
        self.click_button("1"); self.click_button("+"); self.click_button("2"); self.click_button("=")
        assert self.get_display() == "3"

        # Subtraction
        self.clear()
        self.click_button("9"); self.click_button("-"); self.click_button("4"); self.click_button("=")
        assert self.get_display() == "5"

        # Multiplication
        self.clear()
        self.click_button("6"); self.click_button("*"); self.click_button("7"); self.click_button("=")
        assert self.get_display() == "42"

        # Division
        self.clear()
        self.click_button("8"); self.click_button("/"); self.click_button("2"); self.click_button("=")
        assert self.get_display() == "4"

        # Division by zero
        self.clear()
        self.click_button("5"); self.click_button("/"); self.click_button("0"); self.click_button("=")
        assert self.get_display() == "Infinity"

        print("Basic operations passed")

    # ==================================
    # SCIENTIFIC TESTS
    # ==================================

    def test_scientific(self):
        print("\n---- SCIENTIFIC TESTS ----")

        # Square
        self.clear()
        self.click_button("5"); self.click_button("x²")
        assert self.get_display() == "25"

        # Square root
        self.clear()
        self.click_button("9"); self.click_button("√")
        assert self.get_display() == "3"

        # Sin
        self.clear()
        self.click_button("3"); self.click_button("0"); self.click_button("sin")
        assert abs(float(self.get_display()) - round(math.sin(math.radians(30)), 2)) < 0.01

        # Cos
        self.clear()
        self.click_button("6"); self.click_button("0"); self.click_button("cos")
        assert abs(float(self.get_display()) - round(math.cos(math.radians(60)), 2)) < 0.01

        # Tan
        self.clear()
        self.click_button("4"); self.click_button("5"); self.click_button("tan")
        assert abs(float(self.get_display()) - round(math.tan(math.radians(45)), 2)) < 0.01

        # Log
        self.clear()
        self.click_button("1"); self.click_button("0"); self.click_button("0"); self.click_button("log")
        assert abs(float(self.get_display()) - round(math.log10(100), 2)) < 0.01

        # Ln
        self.clear()
        self.click_button("2"); self.click_button("ln")
        assert abs(float(self.get_display()) - round(math.log(2), 2)) < 0.01

        # Pi
        self.clear()
        self.click_button("π")
        self.click_button("=")
        assert abs(float(self.get_display()) - round(math.pi, 2)) < 0.01

        print("Scientific operations passed")

    # ==================================
    # EXPRESSION TESTS (New)
    # ==================================

    def test_expressions(self):
        print("\n---- EXPRESSION HANDLING TESTS ----")

        # 2 + 3 * 4 = 14
        self.clear()
        for c in "2+3*4=":
            self.click_button(c)
        assert self.get_display() == "14"

        # (5 + 3) * 2 = 16
        self.clear()
        for c in "(5+3)*2=":
            self.click_button(c)
        assert self.get_display() == "16"

        # Nested: 2*(3+(4-1)) = 12
        self.clear()
        for c in "2*(3+(4-1))=":
            self.click_button(c)
        assert self.get_display() == "12"

        # Mixed: 7 + (6/2) - 1 = 9
        self.clear()
        for c in "7+(6/2)-1=":
            self.click_button(c)
        assert self.get_display() == "9"

        print("Expression tests passed")

    # ==================================
    # MIXED SCIENTIFIC + EXPRESSION TESTS
    # ==================================

    def test_mixed_expressions(self):
        print("\n---- MIXED SCIENTIFIC + EXPRESSION TESTS ----")

        # sin(30) + 5 ≈ 5.5
        self.clear()
        self.click_button("3"); self.click_button("0"); self.click_button("sin")
        self.click_button("+"); self.click_button("5"); self.click_button("=")
        assert abs(float(self.get_display()) - (round(math.sin(math.radians(30)), 2) + 5)) < 0.1

        # √9 + 2 = 5
        self.clear()
        self.click_button("9"); self.click_button("√")
        self.click_button("+"); self.click_button("2"); self.click_button("=")
        assert self.get_display() == "5"

        # 3 + π
        self.clear()
        self.click_button("3"); self.click_button("+"); self.click_button("π"); self.click_button("=")
        assert abs(float(self.get_display()) - (3 + round(math.pi, 2))) < 0.01

        print("Mixed expression tests passed")

    # ==================================
    # RUN ALL TESTS
    # ==================================

    def run_tests(self):
        try:
            self.test_basic_operations()
            self.test_scientific()
            self.test_expressions()
            self.test_mixed_expressions()
            print("\n✅ ALLcalcu TESTS PASSED SUCCESSFULLY!")
        except Exception as e:
            print(f"\n❌ Test failed: {e}")
        finally:
            self.driver.quit()


if __name__ == "__main__":
    test = CalculatorTestV2()
    test.run_tests()
