# DevOps 중간고사 대체과제

컴퓨터정보공학과 202507076 조서빈

## 교안별 학습 기록

- [교안 01 / 수업 2주차: 실습 환경 구축과 버전 관리 기초](week01/README.md)
- [교안 02 / 수업 3주차: 셸 스크립팅](week02/README.md)
- [교안 03 / 수업 4주차: 자동화와 협업](week03/README.md)
- [교안 04 / 수업 4주차: 네트워크](week04/README.md)
- [교안 05 / 수업 5주차: Docker](week05/README.md)
- [교안 06 / 수업 6주차: Dockerfile](week06/README.md)
- [교안 07 / 수업 7주차: Docker Compose](week07/README.md)

폴더는 교안 01~07 기준이며 실제 수업 주차는 각 문서에 별도 표기한다.

## 실행

```bash
cd guestbook
cp .env.example .env
# .env에 로컬 실습 비밀번호 설정
docker compose up -d --build --scale web=3 --wait
```

http://localhost:8080 에 접속한다. 배포용 서버가 아닌 학습용 Flask 서버다.

## 출처와 재현 범위

제공된 교안 01~07을 바탕으로 작성했다. 방명록은 원본 ZIP을 확보하지 못한 상태에서 기능을 재현한 코드다. 실제 실행 증거는 evidence/에 보관한다.
