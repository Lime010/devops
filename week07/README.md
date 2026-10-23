# 07. Docker Compose

자료: 교안 07 / 수업 7주차. 폴더는 수업 주차 기준이다.

## 학습 목표와 핵심 개념
Compose는 여러 서비스를 하나의 YAML로 정의한다. 같은 네트워크에서 서비스 이름을 DNS로 사용한다. healthcheck와 depends_on의 service_healthy로 준비 상태를 확인한다. .env는 비밀값을 분리하지만 암호화하지 않으므로 Git에서 제외한다. 볼륨은 컨테이너와 별도로 데이터를 보존한다.

## 실행 방법
```bash
cd ../guestbook; docker compose up -d --scale web=3 --wait; docker compose ps
```
