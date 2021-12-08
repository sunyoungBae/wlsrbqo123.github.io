from flask import Flask

app = Flask(__name__)  # Flask 인스턴스 객체 생성(현재 실행되는 애플리케이션 모듈명)


# 호출되는 URI을 처리하는 함수를 연결하는 방법 제공(연결될 URL 지정)
@app.route('/')
def hello():
    # view 함수 : 브라우저 상에서 특정 URI를 호출했을 때 실행되는 함수 정의
    return 'Hello Flask'


# URI에 사용되는 동적 변수 지정(name) : 타입을 지정하지 않을 때는 기본적으로 문자열 데이터 타입으로 인식
@app.route('/info/<name>')
def get_name(name):
    return "hello {}".format(name)


# 데이터 타입 지정 : URI 변수(id)의 데이터타입으로 int 설정.(문자열이 오는 경우, 해당 URL을 찾을 수 없다는 오류 페이지 출력)
@app.route('/user/<int:id>')
def get_user(id):
    return "user id is {}".format(id)


# 하나의 뷰 함수에 여러 개의 URI 지정 가능
@app.route('/json/<int:dest_id>/<message>')
@app.route('/JSON/<int:dest_id>/<message>')
def send_message(dest_id, message):
    json = {
        "bot_id": dest_id,
        "message": message
    }  # 딕셔너리를 이용해 JSON 데이터 표현
    return json


if __name__ == '__main__':
    app.run()  # (host='127.0.0.1', port='5000') : 서버의 주소와 포트를 인자로 설정 가능
