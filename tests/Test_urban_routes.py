from data import data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages import Urban_routes_page as urp
from utils.retrive_code import retrieve_phone_code


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = urp.UrbanRoutesPage(cls.driver)

    # direcciones
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = urp.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    # tarifa comfort
    def test_select_comfort(self):
        self.routes_page.click_on_pedir_un_taxi_button()
        self.routes_page.click_comfort_button()
        assert self.routes_page.get_selected_tariff_text() == "Comfort"

    # telefono
    def test_phone_number(self):
        self.routes_page.click_phone_number()
        self.routes_page.set_telefono(data.phone_number)
        assert self.routes_page.get_phone_input().get_property('value') == data.phone_number
        self.routes_page.click_button_siguiente()
        code = retrieve_phone_code(self.driver)
        self.routes_page.set_codigo_telefono(code)
        self.routes_page.click_button_confirmar()

    # metodo de pago
    def test_add_card(self):
        self.routes_page.click_payment_open_button()
        self.routes_page.click_add_card_button()
        self.routes_page.set_card_number(data.card_number)
        self.routes_page.set_card_code(data.card_code)
        self.routes_page.click_add_card_submit_button()
        self.routes_page.get_payment_close_button()
        self.routes_page.click_payment_close_button()
        assert self.routes_page.get_payment_open_button().is_enabled()

    # mensaje al conductor
    def test_set_message(self):
        self.routes_page.set_message(data.message_for_driver)
        assert self.routes_page.get_message_value() == data.message_for_driver

    # mantas y pañuelos
    def test_blanket_and_tissues(self):
        self.routes_page.get_manta_switch()
        self.routes_page.click_manta_switch()
        assert self.routes_page.is_manta_on()

    # helados
    def test_two_icecreams(self):
        self.routes_page.click_icecream_plus_button()
        self.routes_page.click_icecream_plus_button()
        assert self.routes_page.get_icecream_counter_value() == "2"

    # buscar un taxi
    def test_search_taxi_modal(self):
        self.routes_page.click_search_taxi_button()
        assert "El recorrido será de" in self.routes_page.get_search_modal_text()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()