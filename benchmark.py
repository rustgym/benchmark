import benchmark_pb2_grpc
import benchmark_pb2
import grpc
import time
import os
from dotenv import load_dotenv

load_dotenv()


class Benchmark:
    def __init__(
        self,
        program,
        machine=os.environ.get("MACHINE", "machine"),
        target="backend.rustgym.com",
    ):
        channel = grpc.secure_channel(target, grpc.ssl_channel_credentials())
        self.stub = benchmark_pb2_grpc.BenchmarkServiceStub(channel)
        self.machine = machine
        self.program = program
        self.start_time = int(time.time())

    def SetEpochTime(self, epoch_id):
        end_time = int(time.time())
        seconds = end_time - self.start_time
        self.stub.SetEpochTime(
            benchmark_pb2.SetEpochTimeRequest(
                machine=self.machine,
                program=self.program,
                epoch_id=epoch_id,
                seconds=seconds,
            )
        )
        self.start_time = end_time


if __name__ == "__main__":
    print("Benchmarking...")
