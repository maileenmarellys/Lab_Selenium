
from selenium import webdriver
from login_page import LoginPage
import time

def test_ejecucion_pom():

    driver = webdriver.Chrome()

    try:
        # Abrir Sauce Demo
        print("Abriendo Sauce Demo...")
        driver.get("https://www.saucedemo.com/")

        time.sleep(3)

        # Instanciar la página
        print("Creando objeto LoginPage...")
        login = LoginPage(driver)

        # Ingresar credenciales del usuario bloqueado
        print("Ingresando credenciales...")
        login.ingresar_credenciales(
            "locked_out_user",
            "secret_sauce"
        )

        time.sleep(3)

        # Hacer clic en iniciar sesión
        print("Presionando botón Login...")
        login.click_login()

        # Obtener mensaje de error
        mensaje = login.obtener_error()

        print("--------------------------------")
        print("RESULTADO DE LA PRUEBA")
        print("--------------------------------")
        print("Mensaje:", mensaje)

        assert "locked out" in mensaje.lower()

        print("PRUEBA POM COMPLETADA CORRECTAMENTE")
        print("--------------------------------")
        print("El navegador permanecerá abierto")
        print("durante 30 segundos para tomar evidencias.")

        time.sleep(30)

    finally:
        driver.quit()


if __name__ == "__main__":
    test_ejecucion_pom()
