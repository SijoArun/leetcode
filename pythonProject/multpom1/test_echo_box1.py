

def test_echo_box(home):

    echo=home.nav_to_echobox()
    message="Hello"
    echo.sendmessage(message)
    assert echo.getsavemessage() == message
    home = echo.nav_back()
    echo = home.nav_to_echobox()
    assert echo.getsavemessage() == message

def test_echo_box2(home):
    echo = home.nav_to_echobox()
    assert echo.getsavemessage() is None