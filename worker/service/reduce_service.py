from concurrent.futures import ThreadPoolExecutor, as_completed
from .word_count_reducer import WordCountReducer
from .distributed_grep_reducer import DistributedGrepReducer
from .reverse_web_link_reducer import ReverseWebLinkReducer
from util.file_operator import write_hashmap_to_file

class ReduceService:

    def __init__(self, worker_no):
        self.worker_no = worker_no

    def word_count(self, reduce_obj):
        key_mapping = {}
        intermediate_files = reduce_obj['intermediateFiles']
        len_intermediate_files = len(intermediate_files)

        with ThreadPoolExecutor(max_workers=len_intermediate_files) as executor:
            futures = [executor.submit(WordCountReducer(self.worker_no, file_path, key_mapping).run) for file_path in intermediate_files]

            for future in as_completed(futures):
                future.result()

        return write_hashmap_to_file(key_mapping)

    def distributed_grep(self, reduce_obj):
        key_mapping = {}
        intermediate_files = reduce_obj['intermediateFiles']
        len_intermediate_files = len(intermediate_files)

        with ThreadPoolExecutor(max_workers=len_intermediate_files) as executor:
            futures = [executor.submit(DistributedGrepReducer(self.worker_no, file_path, key_mapping).run) for file_path in intermediate_files]

            for future in as_completed(futures):
                future.result()

        return write_hashmap_to_file(key_mapping)

    def reverse_web_link(self, reduce_obj):
        key_mapping = {}
        intermediate_files = reduce_obj['intermediateFiles']
        len_intermediate_files = len(intermediate_files)

        with ThreadPoolExecutor(max_workers=len_intermediate_files) as executor:
            futures = [executor.submit(ReverseWebLinkReducer(self.worker_no, file_path, key_mapping).run) for file_path in intermediate_files]

            for future in as_completed(futures):
                future.result()

        return write_hashmap_to_file(key_mapping)
