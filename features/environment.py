from behave import fixture, use_fixture
from selenium import webdriver


@fixture
def selenium_browser_chrome(context):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    context.browser = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
    yield context.browser


def before_all(context):
    use_fixture(selenium_browser_chrome, context)


def after_all(context):
    context.browser.quit()
