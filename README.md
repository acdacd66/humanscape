# 🔴 [위코드 x 원티드] humanscape 기업 협업 과제

## 🟡 구현 기술 스택
- Language  : Python

- Framework :  Django Rest Framework

- Postman

- DB  : sqlite3

- 배포 :AWS EC2 with Nginx, Gunicorn

## 🟡 Contributors
|이름 |담당 기능| GitHub 주소|
|------|---|---|
|이정우|모델링 및 API 전체 구현| [acdacd66](http://github.com/acdacd66)|
|성우진|배포 | [jinatra](http://github.com/jinatra)|
|김도담|README.md, postman api 작성| [damdream](http://github.com/damdream)|

## 🟡 빌드 및 실행 방법
- repo 폴더안의 requirements.text 파일을 install 한다.
pip install -r requirements.txt
- python manage.py runserver를 통해 서버를 실행한다.
<br>
- [POSTMAN API 문서](https://documenter.getpostman.com/view/16843875/UVC8CR6j) 를 통해 확인 가능합니다.
<br>

## 🟡 기본 설계
![image](https://user-images.githubusercontent.com/81546305/141465168-efdb4b70-05ed-42a2-8bec-d525d2451037.png)


- User, Account, Transaction 총 세개의 테이블로 구성하였습니다.
- User는 기본적인 가입, 로그인/회원가입, 데코레이터를 구현했고, Account는 User와 연결된 계좌의 잔고와 기본적인 입금/출금 기능을 구행하는 테이블입니다.
- Transaction은 거래내역을 담은 테이블로 거래 시간, 잔고, 적요, 등을 담았습니다.


## 🟡 구현 내용
- Batch POST API
- 임상정보 리스트 API
- 임상정보 검색 API

## 🟡 구현 기능/구현 방법
🔵  BATCH API
 
- 검색 시작 날짜(`start_date`), 검색 종료 날짜(`end_date`), 입/출금 타입(`type`) 및 pagination data(`offset`, `limit`)을 쿼리 스트링으로 전달받습니다.
- 각각의 쿼리스트링이 전달되지 않으 경우, 기존에 지정해두 default value를 통해 filtering하게 됩니다.
- filtering method로는 q객체를 사용하였습니다.
- 인증되지 않은 유저(다른 유저)의 접근을 제한하기 위해 토큰을 이용하여 사용자르 식별합니다.
- Key Error, Value Error(잘못된 type 형식 등), Validation Error(잘못된 날짜 형식 등)에 대한 예외처리를 주었습니다.

🔵 임상정보 리스트 API

- json을 통해 입금할 금액, account_id, 적요를 받아온 후, account_id가 존재하는지 확인합니다. id가 없다면 계좌 없음 에러를 반환합니다.
- 그 후 계좌 잔액과 입금 금액을 더해 전체 금액을 저장해주고, account_id와 account_balance, brief를 결과값으로 받아옵니다.

🔵 임상정보 검색 API

- json을 통해 출금할 금액, account_id, 적요를 받아온 후, account_id가 존재하는지 확인합니다. id가 없다면 계좌 없음 에러를 반환합니다.
- 그 후 계좌 잔액과 출금 금액을 빼 전체 금액을 저장해주고, 뺀 금액이 0보다 큰지 확인합니다. 0보다 작다면 잔고 부족으로 에러를 반환합니다.
- account_id와 account_balance, brief를 결과값으로 받아옵니다.



## 🟡 배포 서버
- 아래 OPEN API 링크를 통해 엔드포인트 및 API TEST를 진행할 수 있습니다.
- http://3.20.204.233:8000/


## 🟡 엔드포인트 설명
|METHOD| ENDPOINT| body | 수행목적 |
|------|---|---|----|
| POST	| /batch	| 	| batch 생성 |
| GET | /search  |  | 검색 |
| POST | /list  |  | 임상정보 리스트 |



## 🟡 프로젝트 회고

- 이정우: [블로그](https://mytech123.tistory.com/)
- 성우진: [블로그](https://velog.io/@jinatra)
- 김도담: [블로그](http://velog.io/@damdreammm)
