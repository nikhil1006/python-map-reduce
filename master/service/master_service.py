from concurrent.futures import ThreadPoolExecutor
from requests_futures.sessions import FuturesSession
from util.file_functions import get_total_no_of_lines
from service.word_count_map_tracker import WordCountMapTracker
from service.distributed_grep_map_tracker import DistributedGrepMapTracker
from service.reverse_web_link_map_tracker import ReverseWebLinkMapTracker
from service.reduce_tracker import ReduceTracker

class MasterService:
    base_port = 5000

    def get_worker_port(self, worker_no):
        return self.base_port + worker_no

    def word_count_map_phase(self, payload):
        total_no_of_lines = get_total_no_of_lines(payload["fileName"])
        print(f"Total No Of Lines : {total_no_of_lines}")

        trackers = [
            WordCountMapTracker(self.get_worker_port(i), payload["fileName"], "WordCount",
                                self.get_start_line_no(i, total_no_of_lines), self.get_end_line_no(i, total_no_of_lines))
            for i in range(3)
        ]

        with ThreadPoolExecutor(max_workers=3) as executor:
            results = [executor.submit(tracker.run) for tracker in trackers]
            intermediate_files = [result.result() for result in results]

        return intermediate_files

    # ... other map phase methods for distributed_grep_map_phase and reverse_weblink_map_phase

    def distributed_grep_map_phase(self, payload):
        total_no_of_lines = get_total_no_of_lines(payload["fileName"])
        print(f"Total No Of Lines : {total_no_of_lines}")

        trackers = [
            DistributedGrepMapTracker(self.get_worker_port(i), payload["fileName"], "DistributedGrep",
                                      self.get_start_line_no(i, total_no_of_lines), self.get_end_line_no(i, total_no_of_lines),
                                      payload["misc"])
            for i in range(3)
        ]

        with ThreadPoolExecutor(max_workers=3) as executor:
            results = [executor.submit(tracker.run) for tracker in trackers]
            intermediate_files = [result.result() for result in results]

        return intermediate_files

    def reverse_weblink_map_phase(self, payload):
        total_no_of_lines = get_total_no_of_lines(payload["fileName"])
        print(f"Total No Of Lines : {total_no_of_lines}")

        trackers = [
            ReverseWebLinkMapTracker(self.get_worker_port(i), self.get_start_line_no(i, total_no_of_lines),
                                     self.get_end_line_no(i, total_no_of_lines), payload["fileName"], "ReverseWebLink")
            for i in range(3)
        ]

        with ThreadPoolExecutor(max_workers=3) as executor:
            results = [executor.submit(tracker.run) for tracker in trackers]
            intermediate_files = [result.result() for result in results]

        return intermediate_files

    def reduce_phase(self, intermediate_files, payload, feature):
        trackers = [
            ReduceTracker(self.get_worker_port(i), feature, intermediate_files, payload.get("misc", None))
            for i in range(3)
        ]

        with ThreadPoolExecutor(max_workers=3) as executor:
            results = [executor.submit(tracker.run) for tracker in trackers]
            output_files = [result.result() for result in results]

        return ','.join([file for file in output_files if file is not None])

    def get_end_line_no(self, worker_no, total_no_of_lines):
        if total_no_of_lines < 3 and worker_no > 1:
            return 0
        elif worker_no == 3:
            return total_no_of_lines
        else:
            return (total_no_of_lines // 3) * worker_no

    def get_start_line_no(self, worker_no, total_no_of_lines):
        return (total_no_of_lines // 3) * (worker_no - 1)
