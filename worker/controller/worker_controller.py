import os
from flask import Blueprint, request, jsonify
from service.map_service import MapService
from service.reduce_service import ReduceService

os.getenv("workerNo")

worker_no = int(os.getenv("workerNo", 0))

def create_worker_controller(worker_no):
    worker_controller = Blueprint("worker_controller", __name__)
    map_service = MapService(worker_no)
    reduce_service = ReduceService(worker_no)

    @worker_controller.route("/mapProcess", methods=["POST"])
    def map_process():
        payload = request.json
        print(payload)

        feature = payload["feature"]
        intermediate_files = "Null"

        try:

            if feature == "WordCount":
                intermediate_files = map_service.word_count(payload)
            elif feature == "DistributedGrep":
                intermediate_files = map_service.distributed_grep(payload)
            else:
                intermediate_files = map_service.reverse_web_link(payload)

        except Exception as e:
            print(e)
            return jsonify({"error": str(e)}), 500
            
        return jsonify({"fileName":intermediate_files}), 200


    @worker_controller.route("/reduceProcess", methods=["POST"])
    def reduce_process():
        payload = request.json
        print(payload)

        feature = payload["feature"]
        output_files = "Null"

        try:
            if feature == "WordCount":
                output_files = reduce_service.word_count(payload)
            elif feature == "DistributedGrep":
                output_files = reduce_service.distributed_grep(payload)
            else:
                output_files = reduce_service.reverse_web_link(payload)
        except Exception as e:
            print(e)
            return jsonify({"error": str(e)}), 500

        return jsonify(output_files), 200
    
    return worker_controller