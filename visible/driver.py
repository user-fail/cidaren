import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def visible(token: str):
    print('开启可视化')
    user_agent = [
        'Mozilla/5.0 (Linux; Android 8.1.2; LIO-AN00 Build/LIO-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Safari/537.36 MMWEBID/4462 MicroMessenger/8.0.20.2100(0x28001438) Process/toolsmp WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64',
        'Mozilla/5.0 (Linux; Android 10; HLK-AL00 Build/HONORHLK-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4313 MMWEBSDK/20220805 Mobile Safari/537.36 MMWEBID/2095 MicroMessenger/8.0.27.2220(0x28001B3F) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64']
    driver_option = webdriver.ChromeOptions()
    driver_option.add_experimental_option("detach", True)
    driver_option.add_argument(
        f"user-agent={random.choice(user_agent)}")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=driver_option)

    driver.get(
        "https://app.vocabgo.com/student/api/Student/Main?timestamp=1704182548197&version=2.6.1.231204&app_type=1")
    driver.execute_script(f"let token = JSON.stringify('{token}');window.localStorage.setItem('USER_TOKEN',token);")
    driver.get("https://app.vocabgo.com/student/#/student/home")


if __name__ == '__main__':
    visible('test')
