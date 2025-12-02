import allure
from pages.main_page import MainPage

@allure.feature("Main page navigation")
class TestMainPageNavigation:

    @allure.story("Verify menu navigation")
    @allure.title("Проверка переходов по меню главной страницы")
    def test_navigation_menu(self, page):

        main = MainPage(page)
        main.open()

        test_data = {
            "О нас": "/about",
            "Контакты": "/contacts",
            "Карьера": "/career",
            "Услуги": "/services"
        }

        for name, url_part in test_data.items():
            with allure.step(f"Кликаю по разделу '{name}'"):
                main.click_menu(name)

            with allure.step(f"Проверяю, что открылся раздел '{name}'"):
                assert main.section_loaded(url_part), f"URL не содержит {url_part}"

            page.goto(main.url)

