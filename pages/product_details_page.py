from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep
from pages.base_page import BasePage


class ProductDetails(BasePage):

    COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
    SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")
    SELECT_SHOE_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent']:nth-of-type(2)")

    def open_target(self, product_id):
        self.open_url(f'https://www.target.com/p/{product_id}')
        sleep(10)


    def click_and_verify_colors(self):
        expected_colors = ['Blue Tint', 'Denim Blue', 'Raven', 'Marine']
        actual_colors = []

        colors = self.driver.find_elements(*self.COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
        for color in colors:
            color.click()

            selected_color = self.driver.find_element(*self.SELECTED_COLOR).text  # 'Color\nBlack'
            print('Current color', selected_color)

            selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
            actual_colors.append(selected_color)
            print(actual_colors)

        assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'


    def click_and_verify_shoes_colors(self):
        expected_colors = ['grey', 'navy/tan', 'white/sand/tan', 'black/gum - Out of Stock', 'dark khaki - Out of Stock', 'white/navy/red - Out of Stock']
        actual_colors = []

        colors = self.driver.find_elements(*self.COLOR_OPTIONS)  # color_elem1, color_elem2, ...
        for color in colors:
            color.click()

            selected_color = self.driver.find_element(*self.SELECT_SHOE_COLOR).text  # RED\n
            print('Current color', selected_color)

            selected_color = selected_color.split('\n')[1]  # ['RED', '\n']
            actual_colors.append(selected_color)
            print(actual_colors)

        assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

