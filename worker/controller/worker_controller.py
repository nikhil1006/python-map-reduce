from flask import Blueprint, request, jsonify
from service.map_service import MapService
from service.reduce_service import ReduceService

worker_controller = Blueprint("worker_controller", __name__)

map_service = MapService()
reduce_service = ReduceService()


@worker_controller.route("/mapProcess", methods=["POST"])
def map_process():
    payload = request.json
    print(payload)

    feature = payload["feature"]
    intermediate_files = "Null"

    if feature == "WordCount":
        intermediate_files = map_service.word_count(payload)
    elif feature == "DistributedGrep":
        intermediate_files = map_service.distributed_grep(payload)
    else:
        intermediate_files = map_service.reverse_web_link(payload)

    return jsonify(intermediate_files), 200


@worker_controller.route("/reduceProcess", methods=["POST"])
def reduce_process():
    payload = request.json
    print(payload)

    feature = payload["feature"]
    output_files = "Null"

    if feature == "WordCount":
        output_files = reduce_service.word_count(payload)
    elif feature == "DistributedGrep":
        output_files = reduce_service.distributed_grep(payload)
    else:
        output_files = reduce_service.reverse_web_link(payload)

    return jsonify(output_files), 200
