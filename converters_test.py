"""Unit tests for the units converter library functions"""
# pylint: disable=unused-variable

# import the functions to be tested
from converters import psi2kpa, kpa2psi, mpg2lp100k, lp100k2mpg

def describe_a_library_of_units_converters():
    """Test suite for units conversion functions"""
    def blows_smoke():
        assert True

    def can_convert_psi_to_kpa():
        assert psi2kpa(32) == 220.631712 # 32 PSI == 220.631712 KPa; average car tire pressure
        assert psi2kpa(8.5) == 58.6052985 # 8.5 PSI == 58.6052985 KPa; basketball pressure

    def can_convert_kpa_to_psi():
        assert kpa2psi(101.325) == 14.695952495133 # KPa => PSI; average air pressure at sea level
        assert kpa2psi(220.631712) == 31.999932479367043 # KPa => PSI; average car tire pressure

    def can_convert_mpg_to_lp100k():
        assert mpg2lp100k(40) == 5.8803694563 # miles-per-gallon => liters per 100km
        assert mpg2lp100k(25) == 9.408591130080001 # miles-per-gallon => liters per 100km

    def can_convert_lp100k_to_mpg():
        assert lp100k2mpg(9.4) == 25.022895167663442 # liters per 100km => mpg
        assert lp100k2mpg(5.1) == 46.12063030902673 # liters per 100km => mpg
