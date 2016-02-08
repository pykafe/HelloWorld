from behave import *


@when(u'I visit the website root url')
def impl(context):
    context.browser.visit(context.config.server_url)


@then(u"the text 'Hello World!' is visible")
def impl(context):
    assert context.browser.find_by_text('Hello World!')
