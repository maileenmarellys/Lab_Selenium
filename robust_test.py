
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # CASO 1: Login exitoso
    print("Ejecutando Login...")

    driver.get("https://www.saucedemo.com/")

    usuario = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    usuario.send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory.html" in driver.current_url

    print("Login exitoso.")

    # CASO 2: Agregar producto
    boton = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    )
    boton.click()

    carrito = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert carrito.text == "1"

    print("Producto agregado correctamente.")

    # CASO 3: Login fallido
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    error = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "h3[data-test='error']")
        )
    )

    assert "locked out" in error.text.lower()

    print("Error de usuario bloqueado validado.")

finally:
    driver.quit()
