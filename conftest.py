
import pytest
import os
from selenium import webdriver


@pytest.fixture
def driver(request):
    opciones = webdriver.ChromeOptions()
    opciones.add_argument("--start-maximized")

    navegador = webdriver.Chrome(options=opciones)

    yield navegador

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        carpeta = os.path.join(os.path.dirname(__file__), "capturas")
        os.makedirs(carpeta, exist_ok=True)

        nombre = request.node.name + ".png"
        ruta = os.path.join(carpeta, nombre)

        resultado = navegador.save_screenshot(ruta)

        print(f"Captura guardada: {ruta}")
        print(f"Resultado: {resultado}")

    navegador.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    reporte = resultado.get_result()

    if reporte.when == "call":
        item.rep_call = reporte
