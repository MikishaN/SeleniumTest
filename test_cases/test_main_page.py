def test_check_title(open_main_page):
    """
    @test description: Test verifies that page title is correct
    @test steps:
        1. Open main Page.
        2. Verify page title.
    @expected: main page title >>>
    """
    home_page = open_main_page
    home_page_title = home_page.get_page_title()
    assert home_page_title == 'Лайфстайл', f'Expected: Лайфстайл \n Actual: {home_page_title}'


