"""Unit tests for the units converter library functions"""

# import the functions to be tested
from converters import psi2kpa, kpa2psi

def describe_a_library_of_units_converters():
    """Test suite for units conversion functions"""
    # pylint: disable=unused-variable
    def blows_smoke():
        assert True

    def can_convert_psi_to_kpa():
        assert psi2kpa(32) == 220.631712 # 32 PSI == 220.631712 KPa; average car tire pressure
        assert psi2kpa(8.5) == 58.6052985 # 8.5 PSI == 58.6052985 KPa; basketball pressure

    def can_convert_kpa_psi():
        assert kpa2psi(101.325) == 14.695952495133 # KPa => PSI; average air pressure at sea level
        assert kpa2psi(220.631712) == 31.999932479367043 # KPa => PSI; average car tire pressure
