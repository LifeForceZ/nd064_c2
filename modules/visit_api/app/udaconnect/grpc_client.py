import grpc
import visit_pb2
import visit_pb2_grpc


channel = grpc.insecure_channel("localhost:5005")
stub = visit_pb2_grpc.VisitServiceStub(channel)

# Update this with desired payload
visit = visit_pb2.VisitMessage(
    person_id=1,
    coordinate='010100000097FDBAD39D925EC0D00A0C59DDC64240',
    creation_time='2020-07-07 10:37:06.000000',
)

response = stub.Create(visit)