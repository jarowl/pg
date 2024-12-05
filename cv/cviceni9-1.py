def nejvetsi(seznam_cisel):
    return max(seznam_cisel)


def test_nejvetsi():
    assert nejvetsi([1,2,3,4]) == 4
    assert nejvetsi([1000,2000,3000,4000]) == 4000
    assert nejvetsi([-4,-3,-2,-1,0]) == 0