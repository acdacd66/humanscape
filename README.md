# ๐ด [์์ฝ๋ x ์ํฐ๋] humanscape ๊ธฐ์ ํ์ ๊ณผ์ 

## ๐ก ๊ตฌํ ๊ธฐ์  ์คํ
- Language  : Python

- Framework :  Django Rest Framework

- Postman

- DB  : sqlite3

- ๋ฐฐํฌ :AWS EC2 with Nginx, Gunicorn

## ๐ก Contributors
|์ด๋ฆ |๋ด๋น ๊ธฐ๋ฅ| GitHub ์ฃผ์|
|------|---|---|
|์ด์ ์ฐ|๋ชจ๋ธ๋ง ๋ฐ API ์ ์ฒด ๊ตฌํ| [acdacd66](http://github.com/acdacd66)|
|์ฑ์ฐ์ง|๋ฐฐํฌ | [jinatra](http://github.com/jinatra)|
|๊น๋๋ด|README.md, postman api ์์ฑ| [damdream](http://github.com/damdream)|

## ๐ก ๋น๋ ๋ฐ ์คํ ๋ฐฉ๋ฒ
- repo ํด๋์์ requirements.text ํ์ผ์ install ํ๋ค.
pip install -r requirements.txt

- secret.json ํ์ผ์ ํตํด secret key์ api key๋ฅผ ๋ถ๋ฆฌํ์ฌ ๊ธฐ์ํ์์ต๋๋ค.
<img width="470" alt="แแณแแณแแตแซแแฃแบ 2021-11-17 แแฉแแฅแซ 12 04 26" src="https://user-images.githubusercontent.com/81546305/142010149-8bcaf47d-44eb-409c-acee-863677aee5df.png">
- manage.py์ ๊ฐ์ ๊ฒฝ๋ก์์ secret.json ํ์ผ์ ์์ฑํด์ฃผ์์ต๋๋ค.
<img width="470" alt="แแณแแณแแตแซแแฃแบ 1 2021-11-17 แแฉแแฅแซ 12 04 26" src="https://user-images.githubusercontent.com/39540606/142033855-8440379c-a29a-472f-8e3b-3bde11f826d8.png"> 
<br>
- python manage.py runserver๋ฅผ ํตํด ์๋ฒ๋ฅผ ์คํํ๋ค.
<br>
- [POSTMAN API ๋ฌธ์](https://documenter.getpostman.com/view/16843875/UVCB94M1) ๋ฅผ ํตํด ํ์ธ ๊ฐ๋ฅํฉ๋๋ค.
<br>


## ๐ก ๊ธฐ๋ณธ ์ค๊ณ
<img width="866" alt="แแณแแณแแตแซแแฃแบ 2021-11-16 แแฉแแฎ 11 11 51" src="https://user-images.githubusercontent.com/81546305/142001113-adb11c1e-1e34-4e51-8e24-21c81e45b46f.png">


- clinic data ๋จ์ผ ํ์ด๋ธ๋ก ๊ตฌ์ฑํ์์ต๋๋ค. ์์์ ๋ณด ํฌํจ ํญ๋ชฉ๋ค์ ๋ชจ๋ธ์ ๋ฐ์ํ์์ต๋๋ค.


## ๐ก ๊ตฌํ ๋ด์ฉ
- Batch POST API
- ์์์ ๋ณด ๋ฆฌ์คํธ API
- ์์์ ๋ณด ๊ฒ์ API

## ๐ก ๊ตฌํ ๊ธฐ๋ฅ/๊ตฌํ ๋ฐฉ๋ฒ
๐ต  BATCH API
 
 - ๊ณต๊ณต๋ฐ์ดํฐ ํฌํธ๋ก๋ถํฐ ๋ฐ์ดํฐ๋ฅผ ์์งํ๋ api์๋๋ค. 1์๊ฐ๋ง๋ค ์ฃผ๊ธฐ์ ์ผ๋ก ๋ฐฑ๊ทธ๋ผ์ด๋์์์ api๊ฐ ํธ์ถ์ด ๋์ ๋ฐ์ดํฐ๋ฒ ์ด์ค๋ฅผ ์๋ฐ์ดํธํฉ๋๋ค.. 

๐ต ์์์ ๋ณด ๋ฆฌ์คํธ API

- ์์์ ๋ณด ๋ฆฌ์คํธ๋ฅผ ๋ถ๋ฌ์ต๋๋ค. limit,offset์ ํตํด Pagination์ ํ์์ต๋๋ค. (์ค๋ - 7) ~ ์ค๋ ๋ฒ์์์ update ์ด๋ ฅ์ด ์๋ ์์ ์ ๋ณด ๋ฐ์ดํฐ๋ค์ ๋ถ๋ฌ์ต๋๋ค. ์ฆ ์ต๊ทผ ์ผ์ฃผ์ผ ์ด๋ด์ update ์ด๋ ฅ์ด ์๋ ์์ ์ ๋ณด๋ค์ ์ถ์ถํฉ๋๋ค.

๐ต ์์์ ๋ณด ๊ฒ์ API

- ์์์ ๋ณด๋ฅผ ๊ฒ์ํ๋ API์๋๋ค. taskCode(๊ณผ์  ๋ฒํธ)๋ฅผ ํตํด ๊ฒ์ํ  ์ ์์ต๋๋ค.



## ๐ก ๋ฐฐํฌ ์๋ฒ
- ์๋ OPEN API ๋งํฌ๋ฅผ ํตํด ์๋ํฌ์ธํธ ๋ฐ API TEST๋ฅผ ์งํํ  ์ ์์ต๋๋ค.
- http://3.20.204.233:8000/


## ๐ก ์๋ํฌ์ธํธ ์ค๋ช
|METHOD| ENDPOINT| QueryParams | ์ํ๋ชฉ์  |
|------|---|---|----|
| POST	| /clinical/batch	|| batch ์์ฑ |
| GET | /clinical/search  | ?taskCode=C140006  | ๊ฒ์ |
| POST | /clinical/list  | ?offset=0&limit=2 | ์์์ ๋ณด ๋ฆฌ์คํธ |



## ๐ก ํ๋ก์ ํธ ํ๊ณ 

- ์ด์ ์ฐ: [๋ธ๋ก๊ทธ](https://mytech123.tistory.com/)
- ์ฑ์ฐ์ง: [๋ธ๋ก๊ทธ](https://velog.io/@jinatra)
- ๊น๋๋ด: [๋ธ๋ก๊ทธ](http://velog.io/@damdreammm)
