from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



START_URL = "https://www.youtube.com/channel/UCx28xnLUUyQcnHizvvUq1FQ"

# Webdriver
#browser = webdriver.Chrome("D:/Area de Trabalho/whitehatjr/Pro Versão 2 - Python/c127")
#browser.get(START_URL)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(START_URL)