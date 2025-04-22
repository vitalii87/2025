from playwright.sync_api import Page
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators

class HomePage(BasePage):
    def go_to_homepage(self):
        self.page.goto("https://automationexercise.com/")

    def is_logo_visible(self):
        return self.page.locator(HomePageLocators.LOGO).is_visible()
