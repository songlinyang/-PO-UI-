from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
class Page(object):
    """
    页面基础类，用于所有页面的继承
    """
    BASE_URL = ""

    def __init__(self,selenium_driver,base_url=BASE_URL,parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout=30
        self.parent = parent

    def _open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3) #隐式等待
        assert self.on_page(),"Did not land on %s" % url

    def open(self):
        self._open(self.url)


    def on_page(self):
        return self.driver.current_url == (self.base_url+self.url)

    def find_element(self,*loc):
        try:
            return self.driver.find_element(*loc)
        except Exception as e:
            raise e

    def find_elements(self,*loc):
        try:
            return self.driver.find_elements(*loc)
        except Exception as e:
            raise e

    def script(self,src):
        try:
            return self.driver.execute_script(src)
        except Exception as e:
            raise e

    def find_element_wait(self,*loc):
        print(*loc)
        try:
            return WebDriverWait(self.driver,60,0.5).until(EC.element_to_be_clickable((loc[0],loc[1])))
        except Exception as e:
            raise e


