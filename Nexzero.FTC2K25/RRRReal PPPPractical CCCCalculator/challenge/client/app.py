from flask import Flask, request, render_template, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from utils.rpc_client import calculate

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

UNARY_OPS = {
    'abs', 'sqrt', 'inc', 'dec', 'sin', 'cos', 'tan',
    'log', 'exp', 'floor', 'ceil', 'rand', 'fact', 'fib',
    'cube', 'square', 'pow10', 'is_even', 'is_odd',
    'is_prime', 'is_perfect', 'sqrt2', 'cbrt',
    'sin_deg', 'cos_deg', 'tan_deg', 'log10'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
@limiter.limit("10 per minute")
def do_calc():
    data = request.json
    op = data.get('op')

    if op in UNARY_OPS:
        a = data.get('a')
        if a is None:
            return jsonify({'error': 'Missing operand a for unary operation'}), 400
        try:
            a = int(a)
        except ValueError:
            return jsonify({'error': 'Operand a must be a number'}), 400
        result, errno = calculate(op, a, 0)
    else:
        a = data.get('a')
        b = data.get('b')
        if a is None or b is None:
            return jsonify({'error': 'Missing operand(s) for binary operation'}), 400
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            return jsonify({'error': 'Operands a and b must be numbers'}), 400
        
        result, errno = calculate(op, a, b)

    if errno != 0:
        return jsonify({'error': f'ErrorMessage: {result} | ErrorCode {errno}'}), 400
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4444)
