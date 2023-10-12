import pytest
from src.generator import MarchingDoubler


def test_generate_pattern():
    # Arrange
    md = MarchingDoubler()
    md.run_length = 4
    md.terms_length = 1
    # Act
    pattern = md.generate_pattern()
    # Assert
    assert [term for _, term in pattern] == [1,1,2,3]


@pytest.mark.parametrize("run_length, terms_length", [(4, 16), (5, 25)]) 
def test_generate_pattern_len(run_length, terms_length):
    # Arrange
    md = MarchingDoubler()
    md.run_length = run_length
    md.terms_length = terms_length

    # Act
    pattern = list(md.generate_pattern())

    # Assert
    assert len(pattern) == terms_length


# # Edge case tests

def test_generate_pattern_one_term():
    # Arrange
    md = MarchingDoubler()
    md.terms_length = 1
    md.run_length = 1

    # Act
    pattern = list(md.generate_pattern())
    
    # Assert
    assert [(prev, term) for prev, term in pattern] == [(None, 1)]


# Error case tests   

def test_generate_pattern_invalid_run_length():
    # Arrange
    md = MarchingDoubler()

    # Act & Assert
    with pytest.raises(ValueError):
        md.run_length = "invalid"


def test_generate_pattern_invalid_terms_length():
    # Arrange
    md = MarchingDoubler()
    
    # Act & Assert
    with pytest.raises(ValueError):
        md.terms_length = -1
