from flask import Flask, request, jsonify

# request : 클라이언트로부터 HTTP 요청을 받을 때 요청 정보를 확인할 수 있는 모듈
# jsonify : 데이터 객체를 JSON 응답으로 변환해주는 Flask 유틸리티
app = Flask(__name__)

# 서버 리소스
resource = []


# 사용자 정보 조회 : 리소스를 탐색해 user_id 값으로 저장된 데이터가 있으면 해당 객체를 JSON으로 응답한다.
# GET 메서드의 경우 라우트 데커레이터 인자에서 methods를 생략할 수 있다.
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in resource:
        if user['user_id'] is user_id:
            return jsonify(user)

    return jsonify(None)


# 사용자 추가 : HTTP 요청시 Body에 포함된 JSON 데이터를 서버 리소스에 추가한 후 현재 저장된 전체 리소스 데이터를 JSON으로 변환해 응답한다.
@app.route('/user', methods=['POST'])
def add_user():
    user = request.get_json()  # HTTP 요청의 body에서 json 데이터를 딕셔너리 형태로 가져옴 불러옴
    resource.append(user)  # 리소스 리스트에 추가
    return jsonify(resource)


if __name__ == '__main__':
    app.run()
