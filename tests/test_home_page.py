from pages.home_page import HomePage

def test_homepage_logo_visible(page):
    home = HomePage(page)
    home.go_to_homepage()
    assert home.is_logo_visible(), "Логотип не відображається"
