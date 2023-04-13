import sys
from flask import Flask
from controller.worker_controller import worker_controller

app = Flask(__name__)
app.register_blueprint(worker_controller)

def main():
    if len(sys.argv) < 2:
        print("Please enter the port number")
        sys.exit(0)

    worker_no = sys.argv[1]
    print(f"Worker no : {worker_no}")

    app.run(port=int(worker_no))

if __name__ == "__main__":
    main()
