from appium import webdriver
from appium.options.android import UiAutomator2Options

from utilities import Utilities as util

# appium_server_url -> variable
appium_server_url = "http://127.0.0.1:4723/wd/hub"
device_name = util.get_aos_device()
test_results = []
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName=device_name,
    appPackage='(App Package -> Optional)',
    appActivity='(App Activity -> Optional)',
    noReset='true'
)

"""
before_feature(context, feature) − Executes prior every feature.
before_scenario(context, scenario) − Executes prior every scenario.
before_step(context, step) − Executes prior every step.
before_tag(context, tag) − Executes prior every tag.
before_all(context) − Executes prior everything.

after_feature(context, feature) − Executes post every feature.
after_scenario(context, scenario) − Executes post every scenario.
after_step(context, step) − Executes post every step.
after_tag(context, tag) − Executes post every tag.
after_all(context) − Executes post everything.
"""

"""
앱 활동을 어디서 새로 시작할 것 인가(all, feature, scenario 등)에 따라 아래 코드 구문 추가
(ex)
def before_scenario(context, scenario):
    context.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
"""

"""
아래 함수 내용 테스트 자동화 상항에 맞춰 커스텀 개발 하면 됨.
"""


def before_all(context):
    print(context)


def before_feature(context, feature):
    print(context)
    print(feature)
    

def before_scenario(context, scenario):
    print(context)
    print(scenario)
    

def before_step(context, step):
    print(context)
    print(step)


def after_all(context):
    print(context)


def after_feature(context, feature):
    print(context)
    print(feature)


def after_scenario(context, scenario):
    print(context)
    print(scenario)
    

def after_step(context, step):
    print(context)
    print(step)
