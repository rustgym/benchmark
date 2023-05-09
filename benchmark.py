import benchmark_pb2_grpc
import benchmark_pb2
import grpc
import time


class Benchmark:
    def __init__(self, machine, program, target):
        channel = grpc.insecure_channel(target)
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
