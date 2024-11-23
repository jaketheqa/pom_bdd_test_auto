from selenium.common.exceptions import *

from base.BasePage import BasePage


class AppPage(BasePage):
    """
    구현 하려는 앱 페이지 상 컴포넌트 값, 동작 구현 클래스
    """

    # 컴포넌트 작성
    # button = (AppiumBy.ACCESSIBILITY_ID, "홈")

    # 동작 작성
    # def move_to_home(self):
    #     """
    #     홈페이지 이동
    #     :return:
    #     """
    #     try:
    #         self.click_element(self.button)
    #     except (NoSuchElementException, TimeoutException):
    #         # print_stack()
    #         print("Failed to move to home")
    #         assert False
