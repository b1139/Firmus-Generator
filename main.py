import typer
from src.generator import MarchingDoubler
from src.output_manager import OutputManager

def main(run_length: int, total_terms: int, output_file: str, max_file_size: int = 100):
    """Main function to generate and save a marching doubler pattern series.
    Flow:
        . Validates inputs.
        . Initializes MarchingDoubler with params.
        . Gets pattern generator.
        . Calls write_to_file() to save pattern.
        . Handles exceptions.
    Args:
        run_length (int): Length of the Run
        total_terms (int): Total no of term(each no is called term) in the series
        output_file (str): File path to save series
        max_file_size (int): Maximum file size. Default to 100MB. Sizes in MB
    """
    try:
        max_output_file_size = max_file_size * 1024 * 1024  # MB
        # storing 1 term == number<str><,> so totally 2 char
        # 52428800 terms (numbers) makes 100 MB file
        if total_terms*2 > max_output_file_size:
            print("Total terms exceeds the maximum output file size constraint.")
            return -1

        marching_doubler = MarchingDoubler()
        marching_doubler.run_length = run_length
        marching_doubler.terms_length = total_terms
        
        pattern = marching_doubler.generate_pattern()

        OutputManager.write_to_file(pattern, output_file, marching_doubler.terms_length) 
    except Exception as e:
        print(f'Exception while generating pattern {e}')

if __name__ == '__main__':
    typer.run(main)