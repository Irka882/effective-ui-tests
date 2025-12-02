from playwright.sync_api import Page

class MainPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://effective-mobile.ru"

        self.menu_links = {
            "О нас": "//a[contains(text(),'О нас')]",
            "Контакты": "//a[contains(text(),'Контакты')]",
            "Карьера": "//a[contains(text(),'Карьера')]",
            "Услуги": "//a[contains(text(),'Услуги')]",
        }

    def open(self):
        self.page.goto(self.url)

    def click_menu(self, name: str):
        locator = self.menu_links[name]
        self.page.locator(locator).click()

    def section_loaded(self, expected_url_part: str):
        return expected_url_part in self.page.url
