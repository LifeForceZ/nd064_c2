# UdaConnect
## Commands to run the project

**0. Introduction**

For the purpose of this submission, the monolith application for UdaConnect has been refactored into 3 
microservices (i.e. `Person`, `Location`, `Connection`). The `Connection` microservice has been further
modified to call a REST API to the `Person` microservice to return a list of connections. `gRPC` and `Kafka` 
are used to show how the different message passing techniques can be implemented for the application,
although they are not eventually integrated with the application. An overview of the as-is and to-be 
architectural design can be found respectively in `docs/architecture_design_as_is.png` and 
`docs/architecture_design_to_be.png`.

**1. Deploy `kubectl`**

Assuming kubebernetes is already operationalized, then run the following commands:
- `cd ~/nd064_c2` - to navigate to the project folder.
- `kubectl apply -f deployment/db-configmap.yaml` - to set environment variables.
- `kubectl apply -f deployment/db-secret.yaml` - to set secrets.
- `kubectl apply -f deployment/postgres.yaml` - to set up Postgres database.
- `kubectl apply -f deployment/udaconnect-app.yaml` - to deploy webapp UI (localhost:30000).
- `kubectl apply -f deployment/udaconnect-person-api.yaml` - to deploy Person API (localhost:30001).
- `kubectl apply -f deployment/udaconnect-location-api.yaml` - to deploy Location API (localhost:30002).
- `kubectl apply -f deployment/udaconnect-connection-api.yaml` - to deploy Connection API (localhost:30003).
- `kubectl get pods` - to get the `<POD_NAME>` of the Postgres database.
- `sh scripts/run_db_command.sh <POD_NAME>` - to initialize the database.

**2. Verify deployment**

Successful deployment can be verified using `kubectl get pods` and `kubectl get services`. The output screenshots 
can be found in `docs/pods_screenshot.png` and `docs/services_screenshot.png` respectively.

**3. Kafka**

Calls to the `Location` microservice would potentially be the most computationally expensive. The Kafka distributed 
queue system can be implemented to manage traffic from the `Connection` microservice to the `Location` microservice 
to enable scalability. This can be implemented via a `Visit` microservice that is envisioned to sit between the 
frontend App UI and the `Connection` microservice. Note that the `Visit` microservice has not been integrated for
the purpose of this demonstration.

Assuming that `Kafka` is already installed, then run the following commands in separate terminals from the `Kafka` 
directory (this is not part of the project folder):
- `bin/zookeeper-server-start.sh config/zookeeper.properties` - to initialize the `ZooKeeper` service.
- `bin/kafka-server-start.sh config/server.properties` - to initialize the `Kafka` broker service.

Next, navigate to the `visit_api` project folder and run the `kafka_consumer.py` and `kafka_producer.py` scripts:
- `cd ~/nd064_c2/modules/visit_api/app/udaconnect` - to navigate to the project folder.
- `python3 kafka_consumer.py` - to initialize `Kafka` consumer service to receive message from producer service.
- `python3 kafka_producer.py` - to generate message from `Kafka` producer service.

The output screenshots can be found in `docs/kafka_screenshot.png`. For this demonstration, consider a case that a
user visited a new location and would like to find possible connections via UdaConnect. When the `Visit` API endpoint
is called, it will send the user's `id` and current `coordinates` to the `Kafka` queue via REST API, and the request 
will be consumed by the `Connection` microservice to retrieve and return the connections. 

**4. gRPC**

gRPC can be used to improve performance within the backend microservices since it is a more efficient alternative
to the RESTFUL solution. To demonstrate the `gRPC` message passing technique, navigate to the `visit_api` project 
folder and run the `grpc_server.py` and `grpc_client.py` scripts:
- `cd ~/nd064_c2/modules/visit_api/app/udaconnect` - to navigate to the project folder.
- `python3 grpc_server.py` - to initialize `gRPC` server to receive message.
- `python3 grpc_client.py` - to generate message to the `gRPC` server.

The output screenshots can be found in `docs/grpc_screenshot.png`. For this demonstration, consider a case that a
request has been received via `Kafka`. The request can be converted into a `gRPC` format to call the `Location` and
`Person` microservices to return the list of possible connections, which can subsequently be returned to the App UI
via a RESTFUL solution.
