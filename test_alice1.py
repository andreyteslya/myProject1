def test_new_alice1(desktop_app):
    desktop_app.login()
    desktop_app.create_test()
    desktop_app.open_test()
    assert desktop_app.check_test_created()
    desktop_app.delete_test()
    desktop_app.close()


