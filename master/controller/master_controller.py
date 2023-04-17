from flask import Flask, request, jsonify
from service.master_service import MasterService
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
service = MasterService()


@app.route('/wordCount', methods=['POST'])
def word_count():
    payload = request.json
    print(payload)
    intermediate_files = service.word_count_map_phase(payload)
    output_files = service.reduce_phase(intermediate_files, payload, "WordCount")
    return jsonify(output_files), 200


@app.route('/distributedGrep', methods=['POST'])
def distributed_grep():
    payload = request.json
    intermediate_files = service.distributed_grep_map_phase(payload)
    output_files = service.reduce_phase(intermediate_files, payload, "DistributedGrep")
    return jsonify(output_files), 200


@app.route('/reverseWebLink', methods=['POST'])
def reverse_web_link():
    payload = request.json
    intermediate_files = service.reverse_weblink_map_phase(payload)
    output_files = service.reduce_phase(intermediate_files, payload, "ReverseWeblink")
    return jsonify(output_files), 200


if __name__ == "__main__":
    app.run()
