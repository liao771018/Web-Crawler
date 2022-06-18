from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
driver = Chrome('./chromedriver')
driver.get('https://studio.youtube.com/channel/UCWW86D059MQpOCalMl6bFYw/playlists')

driver.find_element(By.ID, 'identifierId').send_keys('123456@gmail.com')
driver.find_element(By.ID, 'identifierNext').click()

# youtube 阻擋