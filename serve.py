from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def handle_requests():
    if request.method == 'POST':
        subprocess.Popen(["python3", "stress_cpu.py"])
        return "Stressing CPU started."
    elif request.method == 'GET':
        private_ip = socket.gethostbyname(socket.gethostname())
        return f"Private IP Address: {private_ip}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

