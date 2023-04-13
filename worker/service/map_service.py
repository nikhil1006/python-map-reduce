import os
import re
import random

class MapService:

    def __init__(self, worker_no):
        self.worker_no = worker_no

    def word_count(self, map_obj):
        input_file = map_obj['fileName']
        start_line_no = map_obj['startNo']
        end_line_no = map_obj['endNo']
        file_path_intermediate = f"intermediateFile-{self.worker_no}.txt"

        with open(input_file, 'r') as file, open(file_path_intermediate, 'w') as intermediate_file_writer:
            for _ in range(start_line_no):
                next(file)

            count = start_line_no
            for line in file:
                if count >= end_line_no:
                    break
                line = re.sub(r'\p{Punct}', '', line)
                line = re.sub(r'\s+', ' ', line)

                words = line.split()

                for word in words:
                    intermediate_file_writer.write(f"{word.lower()},1\n")
                count += 1

        return file_path_intermediate

    def distributed_grep(self, map_obj):
        input_file = map_obj['fileName']
        start_line_no = map_obj['startNo']
        end_line_no = map_obj['endNo']
        pattern = map_obj['misc']
        file_path_intermediate = f"intermediateFile-{self.worker_no}.txt"

        with open(input_file, 'r') as file, open(file_path_intermediate, 'w') as intermediate_file_writer:
            for _ in range(start_line_no):
                next(file)

            count = start_line_no
            for line in file:
                if count >= end_line_no:
                    break
                if pattern in line:
                    intermediate_file_writer.write(f"{count + 1},{line.strip()}\n")
                count += 1

        return file_path_intermediate

    def reverse_web_link(self, map_obj):
        input_file = map_obj['fileName']
        start_line_no = map_obj['startNo']
        end_line_no = map_obj['endNo']
        file_path_intermediate = f"intermediateFile-{self.worker_no}.txt"

        with open(input_file, 'r') as file, open(file_path_intermediate, 'w') as intermediate_file_writer:
            for _ in range(start_line_no):
                next(file)

            count = start_line_no
            for line in file:
                if count >= end_line_no:
                    break
                words = line.strip().split('->')
                intermediate_file_writer.write(f"{words[1]},{words[0]}\n")
                count += 1

        return file_path_intermediate
