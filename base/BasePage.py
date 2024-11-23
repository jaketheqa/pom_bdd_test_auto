from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Page 별 반복되는 동작(Click, Send_Keys, ...etc) 커스텀 작성 Class
    pages/... 내 위치한 page 파일들은 모두 이 클래스를 상속.
    """
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator_tuple):
        """
        최대 10초 이내 element 로딩 대기 후 element 클릭
        :param locator_tuple: element 조회 목적 (AppiumBy 값, locator) 튜플
        :return:
        """
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator_tuple)).click()

    def send_keys_element(self, locator_tuple, text):
        """
        최대 10초 이내 element 로딩 대기 후 텍스트 필드 등에 텍스트 값 입력
        :param locator_tuple:  element 조회 목적 (AppiumBy 값, locator) 튜플
        :param text: 텍스트 필드 등에 입력할 텍스트 인자
        :return:
        """
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator_tuple)).send_keys(text)
