import sys
import os
from flask import Flask
from controller.worker_controller import create_worker_controller


def main():
    print("Please enter the worker number")
    if len(sys.argv) < 2:
        sys.exit(0)

    worker_no = sys.argv[1]
    os.environ["workerNo"] = worker_no
    print(f"Worker no : {worker_no}")

    app = Flask(__name__)
    app.register_blueprint(create_worker_controller(int(worker_no)))

    app.run(port=int(worker_no)+5000)


if __name__ == "__main__":
    main()
