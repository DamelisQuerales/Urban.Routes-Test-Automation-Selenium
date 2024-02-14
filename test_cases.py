import time

import data
from main import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):  # Configuración inicial de la clase de prueba
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    # Prueba 1 - Configura la dirección
    def test_set_route(self):
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    # Prueba 2- Selecciona la tarifa comfort y pide un taxi
    def test_select_comfort_tariff(self):
        self.routes_page.click_on_request_taxi()
        self.routes_page.click_on_comfort_tariff()

    # Prueba 3- Rellena el número de teléfono
    def test_set_phone(self):
        self.routes_page.click_on_phone_number_button()
        self.routes_page.set_phone_number(data.phone_number)
        self.routes_page.get_phone_number()
        assert self.routes_page.get_phone_number() == data.phone_number
        self.routes_page.click_phone_number_next_button()

        self.routes_page.set_phone_code()
        time.sleep(3)
        phone_code = self.routes_page.get_phone_code()

        WebDriverWait(self.driver, timeout=10).until(
            EC.text_to_be_present_in_element_value(self.routes_page.phone_number_code_field, phone_code)
        )
        assert phone_code is not None
        assert phone_code != 'None'
        self.routes_page.click_on_confirmation_phone_code()
        time.sleep(2)

    # Prueba 4 - Agregar una tarjeta de crédito
    def test_set_modal_pay_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_modal_pay_button()
        routes_page.click_modal_add_card()
        time.sleep(3)
        card_number = data.card_number
        card_code = data.card_code
        self.routes_page.set_modal_pay_card(card_number, card_code)
        assert routes_page.get_card() == card_number
        assert routes_page.get_code() == card_code
        time.sleep(2)

    # Prueba 5 - Escribir un mensaje para el conductor
    def test_set_message_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        message_for_driver = data.message_for_driver
        self.routes_page.set_message_for_driver_field(message_for_driver)
        assert routes_page.get_message_field() == message_for_driver

    # Prueba 6 - Pedir manta y pañuelos
    def test_click_blanket_and_scarf_selector(self):
        routes_page = UrbanRoutesPage(self.driver)
        self.routes_page.click_order_requirements_dropdown()
        routes_page.click_order_requirements_dropdown()
        self.routes_page.click_blanket_and_scarf_selector()

    # Prueba 7 - Pedir 2 helados
    def test_click_ice_cream_counter_plus(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_ice_cream_counter_plus()

    # Prueba 8 - Aparece el modal para buscar un taxi
    def test_click_order_taxi_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_order_taxi_button()

        time.sleep(40)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
