import pytest
from src.output_manager import OutputManager
from src.generator import MarchingDoubler
from main import main


def test_writer(tmp_path):
    # Arrange
    md = MarchingDoubler()
    md.terms_length = 4
    md.run_length = 4
    pattern = md.generate_pattern()
    output_file = tmp_path / "output.txt"
    
    # Act
    OutputManager.write_to_file(pattern, output_file, md.terms_length, md.run_length)
    
    # Assert
    assert output_file.read_text() == "1,1,2,3,"


def test_write_file_term_len(tmp_path):
    # Arrange
    md = MarchingDoubler()
    md.terms_length = 1048576//2  # 1 MB
    md.run_length = 4
    pattern = md.generate_pattern() 
    output_file = tmp_path / "output.txt"
    
    # Act
    OutputManager.write_to_file(pattern, output_file, md.terms_length, md.run_length)
    
    # Assert
    # -1 an ending comma
    assert len(output_file.read_text().split(','))-1 == md.terms_length


# # Edge case tests   

def test_large_terms(tmp_path):
    # Arrange
    run_length = 4
    total_terms = 1048576   # terms * 2 => 2 MB 
    max_file_size = 1   # Suppose to write 1MB file
    
    assert main(run_length, total_terms, 'output_file', max_file_size) == -1