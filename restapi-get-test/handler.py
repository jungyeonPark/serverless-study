'''
sls deploy할 때 뒤에다가 리전 붙여주기!!!!
sls deploy --stage dev --region ap-northeast-2

'''
import json
import random
import boto3       # dynamodb 쓰려구(그 외 aws서비스도 쓸 수 있음)

# dynamodb를 쓰겠다.(client도 있고 resource도 있는데 비슷함)
dynamodb = boto3.client('dynamodb')     



def make_random_ary():
    ary = []
    # 단순히 반복만 할 때 _사용 (i, v(value), idx는 의미가 있는것들)
    for _ in range(5):  
        ary.append(random.randint(1, 100))
    return ary

# 핸들러 함수
def hello(event, context):  # event는 프론트에서 받은거(POST같은거로) context는 뭐더라..
    body = {
        "message" : "this is test",
        "numbers" : make_random_ary()
    }

    # 다시 프론트에 보내는거
    response = {
        # 에러 없이 정상적으로 보내면 200
        "statusCode" : 200,
        # 헤더
        "headers" : {
            # 실제 요청에 사용할 수 있는 HTTP 헤더의 목록을 나열
            'Access-Control-Allow-Headers': 'Content-Type',

            # 이 응답이 주어진 origin으로부터의 요청 코드와 공유될 수 있는지
            # 나중에 여기에 프론트 주소를 적어줘야 한다!
            # *은 보안에 취약
            'Access-Control-Allow-Origin': '*',

            # 리소스에 엑세스 할 때 허용되는 메서드 지정
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        # 바디
        "body": json.dumps(body)    # json형식의 body를 디코딩(문자열로 바꿈)
    }

    return response

if __name__ == "__main__":
    # scan은 다 출력하는거(filter할수도 있긴 함) get_item은 조건에 맞는거만 출력
    data = dynamodb.scan(
        # 데이터를 가져올 dynamodb테이블 이름
        TableName = 'postTable'
    )

    print(data)