import grpc
from concurrent import futures
import math
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import challenge.common.calculator_pb2 as calculator_pb2
import challenge.common.calculator_pb2_grpc as calculator_pb2_grpc


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    def x10(self, request, context):  # Addition
        result = request.arg1 + request.arg2
        return calculator_pb2.Response(somme=result, errno=0)

    def x11(self, request, context):  # Subtraction
        result = request.arg1 - request.arg2
        return calculator_pb2.Response(somme=result, errno=0)

    def x12(self, request, context):  # Multiplication
        result = request.arg1 * request.arg2
        return calculator_pb2.Response(somme=result, errno=0)

    def x13(self, request, context):  # Division
        if request.arg2 == 0:
            return calculator_pb2.Response(somme=0, errno=1)
        result = request.arg1 // request.arg2
        return calculator_pb2.Response(somme=result, errno=0)

    def x14(self, request, context):  # Modulo
        if request.arg2 == 0:
            return calculator_pb2.Response(somme=0, errno=1)
        result = request.arg1 % request.arg2
        return calculator_pb2.Response(somme=result, errno=0)

    def x15(self, request, context):  # Power
        result = request.arg1 ** request.arg2
        return calculator_pb2.Response(somme=result, errno=0)

    def x16(self, request, context):  # Max
        result = max(request.arg1, request.arg2)
        return calculator_pb2.Response(somme=result, errno=0)

    def x17(self, request, context):  # Min
        result = min(request.arg1, request.arg2)
        return calculator_pb2.Response(somme=result, errno=0)

    def x18(self, request, context):  # Average
        result = (request.arg1 + request.arg2) / 2
        return calculator_pb2.Response(somme=result, errno=0)

    def x19(self, request, context):  # Multiply by Two
        result = request.arg1 * 2
        return calculator_pb2.Response(somme=result, errno=0)

    def x20(self, request, context):  # Divide by Two
        result = request.arg1 / 2
        return calculator_pb2.Response(somme=result, errno=0)

    def x21(self, request, context):  # Increment
        result = request.arg1 + 1
        return calculator_pb2.Response(somme=result, errno=0)

    def x22(self, request, context):  # Decrement
        result = request.arg1 - 1
        return calculator_pb2.Response(somme=result, errno=0)

    def x23(self, request, context):  # Abs
        result = abs(request.arg1)
        return calculator_pb2.Response(somme=result, errno=0)

    def x24(self, request, context):  # Sqrt
        if request.arg1 < 0:
            return calculator_pb2.Response(somme=0, errno=1)
        result = request.arg1 ** 0.5
        return calculator_pb2.Response(somme=result, errno=0)

    def x25(self, request, context):  # Sin
        result = math.sin(request.arg1)
        return calculator_pb2.Response(somme=result, errno=0)

    def x26(self, request, context):  # Cos
        result = math.cos(request.arg1)
        return calculator_pb2.Response(somme=result, errno=0)

    def x27(self, request, context):  # Tan
        result = math.tan(request.arg1)
        return calculator_pb2.Response(somme=result, errno=0)

    def x28(self, request, context):  # Log (Base)
        if request.arg1 <= 0 or request.arg2 <= 0 or request.arg2 == 1:
            return calculator_pb2.Response(somme=0, errno=1)
        result = math.log(request.arg1, request.arg2)
        return calculator_pb2.Response(somme=result, errno=0)

    def x29(self, request, context):  # Exp
        result = math.exp(request.arg1)
        return calculator_pb2.Response(somme=result, errno=0)

    def x30(self, request, context):  # Floor
        result = math.floor(request.arg1)
        return calculator_pb2.Response(somme=result, errno=0)

    def x31(self, request, context):  # Ceil
        result = math.ceil(request.arg1)
        return calculator_pb2.Response(somme=result, errno=0)

    def x33(self, request, context):  # GCD
        result = self.gcd(request.arg1, request.arg2)
        return calculator_pb2.Response(somme=result, errno=0)

    def x34(self, request, context):  # LCM
        result = self.lcm(request.arg1, request.arg2)
        return calculator_pb2.Response(somme=result, errno=0)

    def x35(self, request, context):  # Factorial
        result = self.factorial(request.arg1)
        return calculator_pb2.Response(somme=result, errno=0)

    def x36(self, request, context):  # Fibonacci
        result = self.fibonacci(request.arg1)
        return calculator_pb2.Response(somme=result, errno=0)

    def x37(self, request, context):  # Cube
        result = request.arg1 ** 3
        return calculator_pb2.Response(somme=result, errno=0)

    def x38(self, request, context):  # Square
        result = request.arg1 ** 2
        return calculator_pb2.Response(somme=result, errno=0)

    def x39(self, request, context):  # PowTen
        result = 10 ** request.arg1
        return calculator_pb2.Response(somme=result, errno=0)

    def x40(self, request, context):  # IsEven
        result = 1 if request.arg1 % 2 == 0 else 0
        return calculator_pb2.Response(somme=result, errno=0)

    def x41(self, request, context):  # IsOdd
        result = 1 if request.arg1 % 2 != 0 else 0
        return calculator_pb2.Response(somme=result, errno=0)

    def x42(self, request, context):  # IsPrime
        result = self.is_prime(request.arg1)
        return calculator_pb2.Response(somme=result, errno=0)

    def x43(self, request, context):  # IsPerfect
        result = self.is_perfect(request.arg1)
        return calculator_pb2.Response(somme=result, errno=0)

    def x44(self, request, context):  # SquareRoot
        if request.arg1 < 0:
            return calculator_pb2.Response(somme=0, errno=1)
        result = math.sqrt(request.arg1)
        return calculator_pb2.Response(somme=result, errno=0)

    def x9(self, request, context):  # File reader
        try:
            with open(request.path, 'r') as f:
                content = f.read()
            return calculator_pb2.FileResponse(content=content, errno=0)
        except FileNotFoundError:
            return calculator_pb2.FileResponse(content="", errno=1)

    # Helper functions
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return abs(a * b) // self.gcd(a, b)

    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n - 1)

    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def is_prime(self, n):
        if n <= 1:
            return 0
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return 0
        return 1

    def is_perfect(self, n):
        return 1 if n == sum(i for i in range(1, n) if n % i == 0) else 0

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:8888')
    server.start()
    print("Server started on port 8888.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
