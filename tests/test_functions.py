import pytest
from project_template.functions import calc


class TestCalc:

    # test if addition works correct
    @pytest.mark.parametrize(
        "x,y,operation,expected", [(1, 1, "add", 2), (1, 3, "add", 4), (2, 5, "add", 7)]
    )
    def test_calc_add_with_param(self, x, y, operation, expected):
        assert calc(x, y, operation) == expected

    # test if division works correct
    @pytest.mark.parametrize(
        "a,b,operation,expected",
        [(1, 2, "div", 0.5), (6, 3, "div", 2), (2, 5, "div", 0.4)],
    )
    def test_calc_div_with_param(self, a, b, operation, expected):
        assert calc(a, b, operation) == expected

    # check if exception is raised when dividing by zero
    def test_calc_zero_div(self):
        a = 1
        b = 0
        operation = "div"

        with pytest.raises(ZeroDivisionError):
            assert calc(a, b, operation)

    # check if exception is raised when doperation is not supprted
    def test_UnsupportedOperation(self):
        a = 1
        b = 2
        operation = "unknown"

        with pytest.raises(ValueError):
            assert calc(a, b, operation)
