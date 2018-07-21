from behave import given, when, then


@given(u'I visit "{url}" page')
def step_impl(context, url):
    print('url = ' + url)
    context.browser.get(url=url)


@then(u'I am on "{title}" Page')
def step_impl(context, title):
    assert title in context.browser.title


@when(u'I click on "{link}" link on page')
def step_impl(context, link):
    link_element = context.browser.find_element_by_link_text(link_text=link)
    link_element.click()
