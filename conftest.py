from pytest import  fixture
from playwright.sync_api import Playwright, sync_playwright
from page_objects.application import App


@fixture()
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright

@fixture()
def desktop_app(get_playwright):
    app = App(get_playwright)
    yield app
    app.close()
    

# @fixture()
# def ultimate_answer():
#     return 42
#
# @fixture()
# def new_answer(ultimate_answer):
#     return ultimate_answer+1
