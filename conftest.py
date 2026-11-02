
import pytest
import os
from selenium import webdriver

@pytest.fixture
def driver(request):
    opciones = webdriver.ChromeOptions()
    opciones.add_argument("--start-maximized")

    if os.getenv("GITHUB_ACTIONS") == "true":
        opciones.add_argument("--headless=new")
        opciones.add_argument("--no-sandbox")
        opciones.add_argument("--disable-dev-shm-usage")

    navegador = webdriver.Chrome(options=opciones)
    yield navegador

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        carpeta = os.path.join(os.path.dirname(__file__), "capturas")
        os.makedirs(carpeta, exist_ok=True)
        ruta = os.path.join(carpeta, request.node.name + ".png")
        navegador.save_screenshot(ruta)
        print(f"\nCaptura guardada: {ruta}")

    navegador.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    reporte = resultado.get_result()

    if reporte.when == "call":
        item.rep_call = reporte

