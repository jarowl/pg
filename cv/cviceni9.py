def sudy_lichy(cislo):
    if int(cislo) % 2 == 0:
        return "sudy"
    else:
        return "lichy"
    
def test_sudy_lichy():
    assert sudy_lichy("1") == "lichy"
    assert sudy_lichy(2) == "sudy"
    assert sudy_lichy("3") == "lichy"
    assert sudy_lichy(4) == "sudy"
    assert sudy_lichy("5") == "lichy"