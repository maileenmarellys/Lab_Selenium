
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    opciones = webdriver.ChromeOptions()
    opciones.add_argument("--start-maximized")

    navegador = webdriver.Chrome(options=opciones)

    yield navegador

    navegador.quit()


def test_login_exitoso(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory")
    )

    assert "ERROR" in driver.current_url

    time.sleep(15)


def test_agregar_producto(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    )
    boton.click()

    carrito = driver.find_element(
        By.CLASS_NAME, "shopping_cart_badge"
    )

    assert carrito.text == "1"

    time.sleep(15)


def test_usuario_bloqueado(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    mensaje = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "h3[data-test='error']")
        )
    )

    assert "locked out" in mensaje.text.lower()

    time.sleep(15)
