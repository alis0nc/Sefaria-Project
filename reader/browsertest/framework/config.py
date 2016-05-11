from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from creds import BS_USER, BS_KEY, SAUCE_ACCESS_KEY, SAUCE_USERNAME
BS_MAX_THREADS = 2
SAUCE_MAX_THREADS = 5

REMOTE_URL = "http://test.sefaria.org"
LOCAL_URL = "http://localhost:8000"

# According to http://gs.statcounter.com/#browser_version-ww-monthly-201602-201604-bar
# According to https://www.browserstack.com/test-on-the-right-mobile-devices

BS_CAPS = [
    {'browser': 'Chrome', 'browser_version': '49.0', 'os': 'Windows', 'os_version': '8', 'resolution': '1920x1080',
        'sefaria_mode': 'multi_panel', 'sefaria_short_name': 'Chr/Win8'},

    {'browser': 'IE', 'browser_version': '11.0', 'os': 'Windows', 'os_version': '10', 'resolution': '1024x768',
        'sefaria_mode': 'multi_panel', 'sefaria_short_name': 'IE/Win10'},

    {'browser': 'Firefox', 'browser_version': '45.0', 'os': 'OS X', 'os_version': 'Yosemite', 'resolution': '1920x1080',
        'sefaria_mode': 'multi_panel', 'sefaria_short_name': 'FF/OSX'},

    {'browser': 'Safari', 'browser_version': '9.0', 'os': 'OS X', 'os_version': 'El Capitan', 'resolution': '1600x1200',
        'sefaria_mode': 'multi_panel', 'sefaria_short_name': 'Saf/OSX'},

    {'browserName': 'iPhone', 'platform': 'MAC', 'device': 'iPhone 5S',
        'sefaria_mode': 'single_panel', 'sefaria_short_name': 'iPhone5s'},

    {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Samsung Galaxy S5',
        'sefaria_mode': 'single_panel', 'sefaria_short_name': 'Galaxy S5'},

    {'browserName': 'iPad', 'platform': 'MAC', 'device': 'iPad Air 2',
        'sefaria_mode': 'multi_panel', 'sefaria_short_name': 'iPadAir2'}
]
SAUCE_CAPS = [
    {'browserName': "chrome", 'platform': "Windows 8", 'version': "48.0", 
        'sefaria_mode': 'multi_panel', 'sefaria_short_name': 'Chr/Win8'},

    {'browserName': "internet explorer", 'platform': "Windows 10", 'version': "11.103",
        'sefaria_mode': 'multi_panel', 'sefaria_short_name': 'IE/Win10'},

    {'browserName': "firefox", 'platform': "OS X 10.10", 'version': "44.0",
        'sefaria_mode': 'multi_panel', 'sefaria_short_name': 'FF/OSX10.10'},

    {'browserName': "safari", 'platform': "OS X 10.11", 'version': "9.0",
        'sefaria_mode': 'multi_panel', 'sefaria_short_name': 'Saf/OSX10.11'},

    {'browserName': "iPhone", 'platform': "OS X 10.10", 'version': "9.2", 'deviceName': "iPhone 5s", 'deviceOrientation':"portrait",
        'sefaria_mode': 'single_panel', 'sefaria_short_name': 'iPhone5s'},

    {'browserName': "iPhone", 'platform': "OS X 10.10", 'version': "9.2", 'deviceName': "iPad Air", 'deviceOrientation': "portrait",
        'sefaria_mode': 'single_panel', 'sefaria_short_name': 'iPadAir'},

    {'browserName': "iPhone", 'platform': "OS X 10.10", 'version': "9.2", 'deviceName': "iPad Air", 'deviceOrientation': "landscape",
        'sefaria_mode': 'multi_panel', 'sefaria_short_name': 'iPadAir'},

    {'browserName': 'android', 'platform': 'Linux', 'version': '4.4', 'deviceName': "Google Nexus 7 HD Emulator", 'deviceOrientation': "portrait",
        'sefaria_mode': 'single_panel', 'sefaria_short_name': 'Nexus7/4.4'},

    {'browserName': 'android', 'platform': 'Linux', 'version': '5.1', 'deviceName': "Android Emulator", 'deviceType': 'phone', 'deviceOrientation': "portrait",
        'sefaria_mode': 'single_panel', 'sefaria_short_name': 'GalaxyS4'},
]


"""
    {'browser': 'IE', 'browser_version': '10.0', 'os': 'Windows', 'os_version': '8', 'resolution': '1024x768'},
    {'browser': 'Chrome', 'browser_version': '48.0', 'os': 'OS X', 'os_version': 'Yosemite', 'resolution': '1024x768'},
    {'browser': 'Firefox', 'browser_version': '44.0', 'os': 'Windows', 'os_version': '10', 'resolution': '1920x1080'},
    {'browser': 'Firefox', 'browser_version': '43.0', 'os': 'Windows', 'os_version': '10', 'resolution': '1024x768'},
    {'browser': 'Chrome', 'browser_version': '47.0', 'os': 'OS X', 'os_version': 'Yosemite', 'resolution': '1024x768'},
    {'browser': 'Safari', 'browser_version': '9.0', 'os': 'OS X', 'os_version': 'El Capitan', 'resolution': '1024x768'},
"""

"""
    {'browserName': "android", 'deviceName': "Samsung Galaxy S4 Emulator", 'deviceOrientation': "portrait",
        'sefaria_mode': 'single_panel', 'sefaria_short_name': 'GalaxyS4'}

    {'browserName': 'iPhone', 'platform': 'MAC', 'device': 'iPhone 6S'},
    {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Google Nexus 7'},
    {'browserName': 'iPhone', 'platform': 'MAC', 'device': 'iPhone 6 Plus'},
    {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Samsung Galaxy Note 3'},
    {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Google Nexus 5'},
    {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Samsung Galaxy S5'},
    {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Amazon Kindle Fire HD 8.9'},
    {'browserName': 'iPad', 'platform': 'MAC', 'device': 'iPad Mini 2'}
"""
