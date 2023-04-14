# Map Reduce Implementation

# Folder structure

```markdown
├── master
│   ├── controller
│   ├── service
│   └── util
└── worker
    ├── controller
    ├── service
    └── util
```

# components of the application:

The application consists of two main components: the master and the worker. The master is responsible for receiving requests and distributing tasks among workers, while the workers are responsible for executing the tasks (mapping and reducing) and returning the results to the master. Each of these components has its own directory in the project, containing their respective services, controllers, and utilities.

The **`master`** directory contains the following subdirectories:

- **`controller`**: This contains the **`master_controller.py`** file, which holds the route handlers for the master's REST API.
- **`service`**: This holds the service classes responsible for handling different features and coordinating with the workers.
- **`util`**: This contains utility classes and functions that assist with file handling and payload processing.

The **`worker`** directory has a similar structure, with a **`controller`**, **`service`**, and **`util`** subdirectory, as well as text files that serve as sample inputs for the various tasks (word count, distributed grep, reverse web link).

## The master node:

The master node is implemented as a Flask application that exposes a REST API for clients to interact with. It accepts incoming requests and manages the distribution of tasks among the workers. The master node's functionality is defined in the **`master_main.py`**, **`master_controller.py`**, and the service files located in the **`service`** subdirectory.

When a client sends a request to the master node's API, the **`master_controller`** processes the request and calls the appropriate service function based on the feature specified in the payload. The service function is responsible for dividing the input data into smaller chunks and sending them to the workers for processing. The master node then waits for the results from the workers, combines them, and sends the final output back to the client.

## The worker node:

The worker node is also implemented as a Flask application with a REST API. It listens for incoming requests from the master node to perform map and reduce operations. The worker node's functionality is defined in the **`worker_main.py`**, **`worker_controller.py`**, and the service files in the **`service`** subdirectory.

When a worker node receives a request from the master node, the **`worker_controller`** processes the request and calls the appropriate map or reduce service function based on the feature specified in the payload. The worker node then processes the data it received and sends the results back to the master node.

# Execution flow of the application:

To help understand how the entire application works together, we can take overview of the execution flow using the "WordCount" feature as an example.

1. Client sends a request to the master node with the following payload:
    
    ```json
    {
      "feature": "WordCount",
      "input_files": ["file1.txt", "file2.txt"]
    }
    ```
    
2. Master node receives the request in **`master_controller.py`**. Based on the "feature" key in the payload, the corresponding service method (in this case, **`word_count()`**) is called.
3. The **`word_count()`** method in the **`map_service.py`** of the master node reads the input files, divides them into chunks, and sends each chunk to a different worker node for mapping. It sends the following payload to each worker node:
    
    ```json
    {
      "feature": "WordCount",
      "data": "chunk_of_text_here"
    }
    ```
    
4. Each worker node receives the request in **`worker_controller.py`**. Based on the "feature" key in the payload, the corresponding service method (**`word_count()`** in this case) is called.
5. The **`word_count()`** method in the **`map_service.py`** of the worker node processes the data (counts the words in the given chunk) and sends the intermediate results (a list of key-value pairs where the key is a word and the value is the count) back to the master node.
6. The master node collects the intermediate results from all worker nodes and sends them to the reduce service (**`word_count()`** method in **`reduce_service.py`**). The reduce service combines the intermediate results to produce the final output.
7. The master node sends the final output (a list of key-value pairs with the total word count for each word in the input files) back to the client.

The execution flow for other features, such as "DistributedGrep" and "ReverseWebLink", is similar. The primary differences are in the processing steps for mapping and reducing.

## Running the application locally:

To run the application locally, first, you need to start the master and worker nodes. In separate terminal windows, navigate to the master and worker directories, respectively. Start the master node by running **`python master_main.py`** and start each worker node by running **`python worker_main.py [worker_number]`** (e.g., **`python worker_main.py 1`**). Replace **`[worker_number]`** with the desired worker number.

Once the master and worker nodes are running, you can send HTTP requests to the master node's API using tools like curl, Postman, or a custom client. The master node's API will be available at **`http://localhost:5000`** and each worker node's API will be available at **`http://localhost:[5000 + worker_number]`** (e.g., **`http://localhost:5001`** for worker 1).
