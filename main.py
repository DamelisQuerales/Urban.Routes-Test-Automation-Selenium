import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import data

# no modificar


def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time

    from selenium.common import WebDriverException
    code = None
    for i in range(30):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación")
        return code


class TestUrbanRoutes:

    driver = None
    routes_page = None

    @classmethod
    def setup_class(cls):
        # no modificar, se necesita un registro adicional habilitado para recuperar el código de confirmación del telf
        chrome_options = webdriver.ChromeOptions()
        cls.driver = webdriver.Chrome()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)


# Clase para el inicio de la página
class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    # Localiza el botón "Pedir un taxi"
    request_taxi_button = (By.XPATH, "//button[@class='button round' and text()='Pedir un taxi']")

    # El constructor de clase
    def __init__(self, driver):
        self.driver = driver

# Para la prueba 1
    # Comprueba que el elemento "Desde" contiene los datos de entrada pasados
    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    # Comprueba que el elemento "Hasta" contiene los datos de entrada pasados
    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    # El método introduce dirección de partida
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    # El método introduce dirección destino
    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def set_route(self, from_address, to_address):
        time.sleep(5)
        self.set_from(from_address)
        self.set_to(to_address)

    # Método hace click en "pedir un taxi"
    def click_on_request_taxi(self):
        time.sleep(2)
        self.driver.find_element(*self.request_taxi_button).click()

# Para la prueba 2

    # localizador del botón de la tarifa "Comfort"
    comfort_button = (By.XPATH, "//img[@src='/static/media/kids.27f92282.svg' and @alt='Comfort']")

    # El método hace click en la tarifa "comfort
    def click_on_comfort_tariff(self):
        time.sleep(1)
        self.driver.find_element(*self.comfort_button).click()
        time.sleep(3)

    # El método comprueba que la tarifa Comfort esta seleccionada
    def comfort_tariff_selected(self):
        self.driver.find_element(*self.comfort_button)

# Para la prueba 3
    phone_field = (By.ID, 'phone')
    # localiza el botón del número de teléfono
    phone_number_button = (By.CSS_SELECTOR, '.np-text')
    # localiza el campo para introducir el número de teléfono
    # localiza el botón para continuar
    phone_number_next_button = (By.XPATH, './/div[@class="buttons"]//button[@type="submit"]')
    # localiza el campo para añadir el código de verificación del número de teléfono
    phone_number_code_field = (By.ID, 'code')
    # localiza el botón para confirmar el código de verificación del teléfono
    phone_code_confirm_button = (By.XPATH, '//button[@type="submit" and @class="button full"][text()="Confirmar"]')

    # El método hace click en el botón número de teléfono
    def click_on_phone_number_button(self):
        self.driver.find_element(*self.phone_number_button).click()
        time.sleep(3)

    def get_phone_number(self):
        time.sleep(1)
        return self.driver.find_element(*self.phone_field).get_property('value')

    # Método para rellenar el número de teléfono
    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_field).send_keys(phone_number)

    # Método para hacer click en el botón "siguiente"
    def click_phone_number_next_button(self):
        self.driver.find_element(*self.phone_number_next_button).click()
        time.sleep(3)

    def get_phone_code(self) -> str:
        return self.driver.find_element(*self.phone_number_code_field).get_property('value')

    # Método para rellenar el código de verificación del número de teléfono
    def set_phone_code(self):
        time.sleep(2)
        phone_code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.phone_number_code_field).send_keys(str(phone_code))

    # Método para confirmar el código del número de teléfono
    def click_on_confirmation_phone_code(self):
        time.sleep(3)
        self.driver.find_element(*self.phone_code_confirm_button).click()
        time.sleep(3)

    # Función para hacer scroll para que selenium localice el resto de campos
    def scroll_into_fresa_text(self, fresa_text_locator):
        fresa_element = self.driver.find_element(*fresa_text_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", fresa_element)
        time.sleep(3)

# Para la prueba 4
    card_field = (By.CLASS_NAME, 'card-input')
    code_field = (By.CSS_SELECTOR, "[name='code']")
    # localiza el campo de "forma de pago"
    modal_pay_button = (By.CLASS_NAME, "pp-value-text")
    # localiza el campo para "Agregar una tarjeta"
    modal_add_card = (By.CSS_SELECTOR, "img.pp-plus")
    # localiza el botón de enlace de la tarjeta
    modal_pay_code_next_button = (By.CLASS_NAME, "pp-buttons")
    modal_pay_link_button = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/form/div[3]/button[1]")
    # localiza el botón de cerrar ventana de pago
    modal_pay_card_close_button = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/button")

    def click_modal_pay_button(self):
        self.driver.find_element(*self.modal_pay_button).click()

    def click_modal_add_card(self):
        self.driver.find_element(*self.modal_add_card).click()

    # Obtiene el nro de la tarjeta
    def get_card(self):
        return self.driver.find_element(*self.card_field).get_property('value')

    # Obtiene el código de la tarjeta
    def get_code(self):
        return self.driver.find_element(*self.code_field).get_property('value')

    # Ingresa el nro de la tarjeta en el campo
    def set_modal_card_number_field(self, card_number):
        self.driver.find_element(*self.card_field).send_keys(card_number)

    # Ingresa el código de la tarjeta en el campo
    def set_modal_card_code_field(self, card_code):
        self.driver.find_element(*self.code_field).send_keys(card_code)

    # Hace click fuera de los campos nro y código de tarjeta para que se habilite el botón de "enlace"
    def click_modal_pay_code_next_button(self):
        time.sleep(3)
        self.driver.find_element(*self.modal_pay_code_next_button).click()
        time.sleep(2)

    # Hace click en el botón "enlace" dentro del modal de pago
    def click_modal_pay_link_button(self):
        time.sleep(3)
        self.driver.find_element(*self.modal_pay_link_button).click()
        time.sleep(3)

    # Cierra el modal de pago
    def click_modal_pay_card_close_button(self):
        time.sleep(3)
        self.driver.find_element(*self.modal_pay_card_close_button).click()
        time.sleep(3)

    def set_modal_pay_card(self, card_field, code_field):
        self.set_modal_card_number_field(card_field)
        self.set_modal_card_code_field(code_field)
        self.click_modal_pay_code_next_button()
        self.click_modal_pay_link_button()
        self.click_modal_pay_card_close_button()

# Para la prueba 5

    # localiza el campo para escribir un mensaje para el conductor
    message_field = (By.ID, "comment")

    # Obtiene el mensaje para el conductor
    def get_message_field(self):
        return self.driver.find_element(*self.message_field).get_property('value')

    # Ingresa el mensaje para el conductor en el campo
    def set_message_for_driver_field(self, message_for_driver):
        self.driver.find_element(*self.message_field).send_keys(message_for_driver)

# Para la prueba 6

    # localiza el desplegable de Requisitos del pedido
    order_requirements_dropdown = (By.CSS_SELECTOR, "div.reqs-head")
    # localiza el selector para pedir manta y pañuelos
    blanket_and_scarf_selector = (By.XPATH, "//span[@class='slider round']")

    # Hace click para desplegar el menú de requisitos del pedido
    def click_order_requirements_dropdown(self):
        self.driver.find_element(*self.order_requirements_dropdown).click()
        time.sleep(3)

    # Marca seleccionar manta y pañuelos
    def click_blanket_and_scarf_selector(self):
        time.sleep(3)
        self.driver.find_element(*self.blanket_and_scarf_selector).click()
        time.sleep(3)

# Para la prueba 7

    # localiza el contador para agregar 2 helados
    ice_cream_counter_plus = (By.CSS_SELECTOR, 'div.counter-plus')

    # Hace click en el contador de helados 2 veces
    def click_ice_cream_counter_plus(self):
        for _ in range(2):
            self.driver.find_element(*self.ice_cream_counter_plus).click()
            time.sleep(1)

    # Para la prueba 8 y 9

    # localiza el botón para pedir un taxi
    order_taxi_button = (By.CLASS_NAME, "smart-button-main")
    # localiza la ventana de confirmación de taxi
    modal_order_body = (By.CLASS_NAME, "order-body")
    modal_order_confirmation = (By.CLASS_NAME, "order-header-title")

    # Hace click en el botón para confirmar pedido
    def click_order_taxi_button(self):
        self.driver.find_element(*self.order_taxi_button).click()
        time.sleep(5)
