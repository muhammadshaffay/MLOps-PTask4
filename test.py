from main import Bulb

# Test Case : 1
bulb = Bulb()
def test_bulb_isOff():
    assert bulb.getStatus() == "Bulb is not glowing"

# Test Case : 2
def test_bulb_isOn():
    bulb.isOn()
    assert bulb.getStatus() == "Bulb is glowing"
