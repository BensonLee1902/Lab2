import Lab2
import mock

def test_user_input():
    result = []
    test_result = [1,5,8,10,13,19]
    with mock.patch('builtins.input', return_value="1,5,8,10,13,19"):
        assert (Lab2.get_user_input() == test_result)

def test_calc_average():
    result = 0
    input_array = [1,4,7,8,10]

    result = Lab2.calc_average(input_array)

    assert (result == 6)