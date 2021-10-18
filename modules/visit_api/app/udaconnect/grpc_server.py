import time
from concurrent import futures

import grpc
import visit_pb2
import visit_pb2_grpc


class VisitServicer(visit_pb2_grpc.VisitServiceServicer):

    def Create(self, request, context):

        request_value = {
            "person_id": int(request.person_id),
            "coordinate": request.coordinate,
            "creation_time": request.creation_time,
        }

        print(request_value)

        return visit_pb2.VisitMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
visit_pb2_grpc.add_VisitServiceServicer_to_server(VisitServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()


# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)