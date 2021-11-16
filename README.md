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

- secret.json 파일을 통해 secret key와 api key를 분리하여 기입하였습니다.
<img width="470" alt="스크린샷 2021-11-17 오전 12 04 26" src="https://user-images.githubusercontent.com/81546305/142010149-8bcaf47d-44eb-409c-acee-863677aee5df.png">
- manage.py와 같은 경로에서 secret.json 파일을 생성해주었습니다.
<img width="470" alt="스크린샷 1 2021-11-17 오전 12 04 26" src="https://user-images.githubusercontent.com/39540606/142033855-8440379c-a29a-472f-8e3b-3bde11f826d8.png"> 
<br>
- python manage.py runserver를 통해 서버를 실행한다.
<br>
- [POSTMAN API 문서](https://documenter.getpostman.com/view/16843875/UVCB94M1) 를 통해 확인 가능합니다.
<br>


## 🟡 기본 설계
<img width="866" alt="스크린샷 2021-11-16 오후 11 11 51" src="https://user-images.githubusercontent.com/81546305/142001113-adb11c1e-1e34-4e51-8e24-21c81e45b46f.png">


- clinic data 단일 테이블로 구성하였습니다. 임상정보 포함 항목들을 모델에 반영하였습니다.


## 🟡 구현 내용
- Batch POST API
- 임상정보 리스트 API
- 임상정보 검색 API

## 🟡 구현 기능/구현 방법
🔵  BATCH API
 
 - 공공데이터 포털로부터 데이터를 수집하는 api입니다. 1시간마다 주기적으로 백그라운드상에서 api가 호출이 되서 데이터베이스를 업데이트합니다.. 

🔵 임상정보 리스트 API

- 임상정보 리스트를 불러옵니다. limit,offset을 통해 Pagination을 하였습니다. (오늘 - 7) ~ 오늘 범위에서 update 이력이 있는 임상 정보 데이터들을 불러옵니다. 즉 최근 일주일 이내의 update 이력이 있는 임상 정보들을 추출합니다.

🔵 임상정보 검색 API

- 임상정보를 검색하는 API입니다. taskCode(과제 번호)를 통해 검색할 수 있습니다.



## 🟡 배포 서버
- 아래 OPEN API 링크를 통해 엔드포인트 및 API TEST를 진행할 수 있습니다.
- http://3.20.204.233:8000/


## 🟡 엔드포인트 설명
|METHOD| ENDPOINT| body | 수행목적 |
|------|---|---|----|
| POST	| /clinical/batch	|공공데이터 포털로부터 데이터를 수집하는 api입니다. 1시간마다 주기적으로 백그라운드상에서 호출이 됩니다.  	| batch 생성 |
| GET | /clinical/search  | ?taskCode=C140006  | 검색 |
| POST | /clinical/list  | ?offset=0&limit=2 | 임상정보 리스트 |



## 🟡 프로젝트 회고

- 이정우: [블로그](https://mytech123.tistory.com/)
- 성우진: [블로그](https://velog.io/@jinatra)
- 김도담: [블로그](http://velog.io/@damdreammm)
