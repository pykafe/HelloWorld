from behave import then, when


@when(u'I visit the website root url')
def impl(context):
    context.browser.visit(context.config.server_url)


@then(u"some text is visible")  # noqa
def impl(context):
    for row in context.table:
        assert context.browser.find_by_text(row['text'])
