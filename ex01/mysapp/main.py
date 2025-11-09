from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world!'

if __name__ == '__main__':
    # 외부 접속 허용 + 8001 포트에서 실행
    app.run(host='0.0.0.0', port=8001)
