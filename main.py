import sys
from src.generator import MarchingDoubler


def run(run_length: int, total_terms: int, output_file: str):
    """Executer

    Args:
        run_length (int): length of the Run
        total_terms (int): total no of term(each no is called term) in the series
        output_file (str): where you want to write the generated pattern
    """
    try:
        
        marching_doubler = MarchingDoubler()
        marching_doubler.run_length = run_length
        marching_doubler.terms_length = total_terms
        
        pattern = marching_doubler.generate_pattern()

        # Space Complexity is O(1) as holder holds 2 items max at anytime of execution
        # This also reduces the no.of.writes to file // 2 resulting in O(log n)
        holder = []
        length = 0

        # File Context manager to load or append file one at a time in memory efficiently
        with open(output_file, 'a+') as file:
            for prev, term in pattern:
                # print(term)
                if length == total_terms:
                    # print(', '.join(holder), end='')
                    content = f"{','.join(holder)},"
                    file.write(content)
                    break
                if prev and len(holder) == 1:
                    holder[-1] = str(prev)
                holder.append(str(term))
                if len(holder) == 2:
                    # here you will be writing to the file
                    # print(','.join(holder), end=',')
                    content = f"{','.join(holder)},"
                    file.write(content)
                    holder.clear()
                length += 1
            content = f"{','.join(holder)}"
            file.write(content)
    except Exception as e:
        print(f'Exception while generating pattern {e}')

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python main.py <run_length> <total_terms> <output_file>")
        sys.exit(1)

    run_length = int(sys.argv[1])
    total_terms = int(sys.argv[2])
    output_file = sys.argv[3]

    max_output_file_size = 100 * 1024 * 1024  # 100MB
    # storing 1 term == number<str><,> so totally 2 char
    # 52428800 terms (numbers) makes 100 MB file
    if total_terms*2 > max_output_file_size:
        print("Total terms exceed the maximum output file size constraint.")
        sys.exit(1)

    run(run_length, total_terms, output_file)
    print(f"Marching doubler series generated and saved to {output_file}")