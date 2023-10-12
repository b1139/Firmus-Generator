from typing import Generator

class OutputManager:
    
    @staticmethod
    def write_to_file(pattern: Generator, output_file: str, total_terms: int) -> None:
        """Writes a generated marching doubler pattern to an output file.
        Focused solely on writing the pattern to file.
            Flow:
            . Takes in the pattern generator, output file path and total terms.
            . Writes terms to the file in batches of 2 using a holder list.
            . Prints a completion message.
        Args:
            pattern (MarchingDoubler): Matching doubler generator
            output_file (str): _description_
        
        Performance:
            . Looping through the pattern will take O(n) time
            . Writing batches(holder) will take O(n/b) time, since we write n/b batches
            . Time Complexity => O(n) + O(n/b) = O(n)
            . Space Complexity is O(1) as holder holds 2 items max at anytime of execution
        """
        
        holder = []
        length = 0
        # File Context manager to append series one at a time in memory efficiently
        with open(output_file, 'a+') as file:
            for prev, term in pattern:
                if length == total_terms:
                    file.write(f"{','.join(holder)},")
                    break
                if prev and len(holder) == 1:
                    holder[-1] = str(prev)
                holder.append(str(term))
                if len(holder) == 2:
                    file.write(f"{','.join(holder)},")
                    holder.clear()
                length += 1
            file.write(f"{','.join(holder)}")
        print(f"Marching doubler series generated and saved to -> {output_file}")
    
    
    @staticmethod
    def write_to_db(conn, pattern: Generator, total_terms: int) -> None:
        # Writing to DB
        ...
    
    @staticmethod
    def write_to_cloud(bucket_object, pattern: Generator, total_terms: int) -> None:
        # Writing to Cloud bucket, gdrive, azure drive
        ...