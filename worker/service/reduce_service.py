from concurrent.futures import ThreadPoolExecutor, as_completed
from .word_count_reducer import WordCountReducer
from .distributed_grep_reducer import DistributedGrepReducer
from .reverse_web_link_reducer import ReverseWebLinkReducer
from util.file_operator import FileOperator

class ReduceService:

    def __init__(self, worker_no):
        self.worker_no = worker_no

    def word_count(self, reduce_obj):
        key_mapping = {}
        intermediate_files = reduce_obj['intermediateFiles']
        num_workers = len(intermediate_files)

        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            futures = [executor.submit(WordCountReducer(self.worker_no, file_path, num_workers).run) for file_path in intermediate_files]
            print(f"Starting to wait for the reducer futures...")

            for future in as_completed(futures):
                local_key_mapping = future.result()
                print(f"Local key mapping: {local_key_mapping}")
                for key, value in local_key_mapping.items():
                    if key in key_mapping:
                        key_mapping[key] += value
                    else:
                        key_mapping[key] = value

        print(f"Final key mapping: {key_mapping}")
        return FileOperator.write_hashmap_to_file(key_mapping)

    def distributed_grep(self, reduce_obj):
        key_mapping = {}
        intermediate_files = reduce_obj['intermediateFiles']
        num_workers = len(intermediate_files)

        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            futures = [executor.submit(DistributedGrepReducer(self.worker_no, file_path, num_workers).run) for file_path in intermediate_files]

            for future in as_completed(futures):
                local_key_mapping = future.result()
                for key, value in local_key_mapping.items():
                    if key in key_mapping:
                        key_mapping[key] += value
                    else:
                        key_mapping[key] = value

        return FileOperator.write_hashmap_to_file(key_mapping)

    def reverse_web_link(self, reduce_obj):
        key_mapping = {}
        intermediate_files = reduce_obj['intermediateFiles']
        num_workers = len(intermediate_files)

        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            futures = [executor.submit(ReverseWebLinkReducer(self.worker_no, file_path, num_workers).run) for file_path in intermediate_files]

            for future in as_completed(futures):
                local_key_mapping = future.result()
                for key, value in local_key_mapping.items():
                    if key in key_mapping:
                        key_mapping[key] += value
                    else:
                        key_mapping[key] = value

        return FileOperator.write_hashmap_to_file(key_mapping)
