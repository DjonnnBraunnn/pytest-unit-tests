import pytest
from simple_math import SimpleMath


@pytest.fixture
def math():
    """Фикстура: создаёт объект SimpleMath для тестов."""
    return SimpleMath()


# -------- ТЕСТЫ ДЛЯ square --------

def test_square_positive(math):
    # square(2) → 4
    assert math.square(2) == 4


def test_square_negative(math):
    # square(-5) → 25
    assert math.square(-5) == 25


def test_square_zero(math):
    # square(0) → 0
    assert math.square(0) == 0


# -------- ТЕСТЫ ДЛЯ cube --------

def test_cube_positive(math):
    # cube(3) → 27
    assert math.cube(3) == 27


def test_cube_negative(math):
    # cube(-3) → -27 (как в примере в ДЗ)
    assert math.cube(-3) == -27


def test_cube_zero(math):
    # cube(0) → 0
    assert math.cube(0) == 0
