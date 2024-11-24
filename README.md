# Test Automation Template
Page Object Model + BDD 기반 APP 테스트 자동화 구현 템플릿 (Python Version.)

&nbsp;

## 구현
- MobileOS : Android
- Test Device : Real Device
- Language : Python
- Framework : Appium, Selenium, Behave, Cucumber
- IDE : PyCharm
- Design Pattern : Page Object Model

&nbsp;

## 필요 패키지 설치(pip)
- Appium-Python-Client
- selenium
- behave


```pip install -r requirements.txt```

&nbsp;

## 파일 구조
```
├── base : appium element 공통 동작 구현 page 파일 위치
│   └── BasePage.py
├── features : behave 관련 파일 위치
│   ├── test_scenario.feature : feature, scenario, given, when, then으로 TC 표현
│   ├── environment.py : behave, scenario, step hook 별 동작 구현
│   └── steps
│       └── step_definitions.py : scenario, step 구현 page 파일들 위치
├── pages : 페이지 별 동작, element 구현
├── reports : 테스트 결과 파일
├── utilities : 유틸 파일 위치
├── requirements.txt : python pip 패키지 설치용 파일
└── README.md
```

&nbsp;
