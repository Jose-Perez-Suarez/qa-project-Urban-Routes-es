from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



class UrbanRoutesPage:
    from_field = (By.ID,'from')
    to_field = (By.ID, 'to')
    pedir_taxi_button = (By.XPATH, "//button[@class='button round' and text()='Pedir un taxi']")
    comfort_button = (By.XPATH, "//div[contains(@class,'tcard-title') and text()='Comfort']")
    selected_tariff = (By.CSS_SELECTOR, ".tcard.active .tcard-title")
    phone_open_button = (By.XPATH, "//div[@class='np-text' and text()='Número de teléfono']")
    phone_input = (By.ID, "phone")
    button_siguiente = (By.XPATH, "//button[@class='button full' and text()='Siguiente']")
    phone_code_input = (By.ID, "code")
    confirm_button = (By.XPATH, "//button[@class='button full' and text()='Confirmar']")
    payment_open_button = (By.XPATH, "//div[@class='pp-text' and text()='Método de pago']")
    add_card_button = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    card_number_input = (By.ID, "number")
    card_code_input = (By.CSS_SELECTOR, "input#code.card-input")
    add_card_submit_button = (By.XPATH, "//button[@type='submit' and contains(@class,'button') and text()='Agregar']")
    payment_close_button = (By.XPATH, "//div[contains(@class,'payment-picker') and contains(@class,'open')]" "//button[contains(@class,'section-close')]")
    message_input = (By.ID, "comment")
    manta_switch = (By.XPATH, "//*[text()='Manta y pañuelos']/..//span[contains(@class,'slider')]")
    manta_checkbox = (By.XPATH, "//*[text()='Manta y pañuelos']/..//input[@type='checkbox']")
    icecream_plus_button = (By.XPATH, "//*[text()='Helado']/..//div[contains(@class,'counter-plus')]")
    icecream_counter_value = (By.XPATH, "//*[text()='Helado']/..//div[contains(@class,'counter-value')]")
    search_taxi_button = (By.XPATH, "//span[@class='smart-button-secondary']")



    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def set_from(self, from_address):
        self.wait.until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(EC.presence_of_element_located(self.to_field)).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_pedir_un_taxi_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.pedir_taxi_button))

    def click_on_pedir_un_taxi_button(self):
        self.get_pedir_un_taxi_button().click()

    def get_comfort_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.comfort_button))

    def click_comfort_button(self):
        self.get_comfort_button().click()

    def get_selected_tariff_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.selected_tariff)).text

    def get_phone_number(self):
        return self.wait.until(EC.element_to_be_clickable(self.phone_open_button))

    def click_phone_number(self):
        self.get_phone_number().click()

    def get_phone_input(self):
        return self.wait.until(EC.visibility_of_element_located(self.phone_input))

    def set_telefono(self, number):
        self.get_phone_input().send_keys(number)

    def get_button_siguiente(self):
        return self.wait.until(EC.element_to_be_clickable(self.button_siguiente))

    def click_button_siguiente(self):
        self.get_button_siguiente().click()

    def get_phone_code_input(self):
        return self.wait.until(EC.visibility_of_element_located(self.phone_code_input))

    def set_codigo_telefono(self, code):
        self.get_phone_code_input().send_keys(code)

    def get_confirm_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.confirm_button))

    def click_button_confirmar(self):
        self.get_confirm_button().click()

    def get_payment_open_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.payment_open_button))

    def click_payment_open_button(self):
        self.get_payment_open_button().click()

    def get_add_card_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_card_button))

    def click_add_card_button(self):
        self.get_add_card_button().click()

    def get_card_number_input(self):
        return self.wait.until(EC.visibility_of_element_located(self.card_number_input))

    def set_card_number(self, number):
        self.get_card_number_input().send_keys(number)

    def get_card_code_input(self):
        return self.wait.until(EC.visibility_of_element_located(self.card_code_input))

    def set_card_code(self, code):
        self.get_card_code_input().send_keys(code, Keys.TAB)

    def get_add_card_submit_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_card_submit_button))

    def click_add_card_submit_button(self):
        self.get_add_card_submit_button().click()

    def get_payment_close_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.payment_close_button))

    def click_payment_close_button(self):
        self.get_payment_close_button().click()

    def get_message_input(self):
        return self.wait.until(EC.visibility_of_element_located(self.message_input))

    def click_message_input(self):
        self.wait.until(EC.element_to_be_clickable(self.message_input)).click()

    def set_message(self, text):
        self.wait.until(EC.visibility_of_element_located(self.message_input)).send_keys(text)

    def get_message_value(self):
        return self.driver.find_element(*self.message_input).get_property('value')

    def get_manta_switch(self):
        return self.wait.until(EC.element_to_be_clickable(self.manta_switch))

    def click_manta_switch(self):
       self.get_manta_switch().click()

    def get_manta_checkbox(self):
        return self.wait.until(EC.presence_of_element_located(self.manta_checkbox))

    def is_manta_on(self):
        return self.get_manta_checkbox().is_selected()

    def get_icecream_plus_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.icecream_plus_button))

    def click_icecream_plus_button(self):
        self.get_icecream_plus_button().click()

    def get_icecream_counter_value(self):
        return self.wait.until(EC.visibility_of_element_located(self.icecream_counter_value)).text.strip()

    def get_search_taxi_button(self):
        return self.wait.until(EC.visibility_of_element_located(self.search_taxi_button))

    def click_search_taxi_button(self):
        self.get_search_taxi_button().click()

    def get_search_modal_text(self):
        return self.get_search_taxi_button().text

