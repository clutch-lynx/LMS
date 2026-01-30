import pytest
from math_utils import is_valid_password

def test_valid_password():
    assert is_valid_password("Password123") is True


def test_password_without_uppercase():
    assert is_valid_password("password123") is False


def test_password_without_lowercase():
    assert is_valid_password("PASSWORD123") is False


def test_password_without_digit():
    assert is_valid_password("Password") is False


def test_password_too_short():
    assert is_valid_password("Pass12") is False