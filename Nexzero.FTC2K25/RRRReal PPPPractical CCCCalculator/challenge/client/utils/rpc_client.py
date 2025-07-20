# grpc_client.py
import grpc
import sys
import os
from dotenv import load_dotenv
load_dotenv()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
import challenge.common.calculator_pb2 as calculator_pb2
import challenge.common.calculator_pb2_grpc as calculator_pb2_grpc

HOST=os.getenv("SERVER_HOST", "127.0.0.1")
PORT=os.getenv("SERVER_PORT", "8888")
PROGRAM=int(os.getenv("PROGRAM", "0x20000001"), 16)

class GRPCCalculatorClient:
    def __init__(self, host=HOST, port=int(PORT)):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = calculator_pb2_grpc.CalculatorStub(self.channel)
        self.program = PROGRAM

        # Mapping operation names to stub methods
        self.operations = {
            'add': self.stub.x10,
            'sub': self.stub.x11,
            'mul': self.stub.x12,
            'div': self.stub.x13,
            'mod': self.stub.x14,
            'pow': self.stub.x15,
            'gcd': self.stub.x33,
            'lcm': self.stub.x34,
            'fact': self.stub.x35,
            'fib': self.stub.x36,
            'max': self.stub.x16,
            'min': self.stub.x17,
            'avg': self.stub.x18,
            'sqrt': self.stub.x24,
            'abs': self.stub.x23,
            'floor': self.stub.x30,
            'ceil': self.stub.x31,
            'exp': self.stub.x29,
            'log': self.stub.x28,
            'log10': self.stub.x52,
            'sin': self.stub.x25,
            'cos': self.stub.x26,
            'tan': self.stub.x27,
            'sin_deg': self.stub.x49,
            'cos_deg': self.stub.x50,
            'tan_deg': self.stub.x51,
            'square': self.stub.x38,
            'cube': self.stub.x37,
            'pow10': self.stub.x39,
            'is_even': self.stub.x40,
            'is_odd': self.stub.x41,
            'is_prime': self.stub.x42,
            'is_perfect': self.stub.x43,
            'floor_div': self.stub.x48,
            'square_diff': self.stub.x53,
            'triangle_area': self.stub.x54,
            'rectangle_area': self.stub.x55,
            'circle_area': self.stub.x56,
            'perimeter_rect': self.stub.x57,
            'perimeter_circle': self.stub.x58
        }

    def calculate(self, op_name, a, b=0):
        if op_name not in self.operations:
            return "Weird 'non existing' operation!", -999
        try:
            request = calculator_pb2.Data(arg1=a, arg2=b)
            response = self.operations[op_name](request)
            return response.somme, response.errno
        except grpc.RpcError as e:
            return e, -1

    def file_request(self, path):
        try:
            request = calculator_pb2.FileRequest(path=path)
            response = self.stub.FileRead(request)
            return response.content, response.errno
        except grpc.RpcError as e:
            print(f"RPC failed: {e}")
            return None, -1


def calculate(op, a=None, b=None):
    client = GRPCCalculatorClient()

    result, errno = client.calculate(op_name=op, a=a, b=b)
    return result, errno
