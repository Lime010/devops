# 07. Docker Compose

자료: 교안 07 / 수업 7주차. 폴더 번호는 교안 번호 기준이다.

## 학습 목표와 핵심 개념
Compose는 여러 서비스를 하나의 YAML로 정의한다. 같은 네트워크에서 서비스 이름을 DNS로 사용한다. healthcheck와 depends_on의 service_healthy로 준비 상태를 확인한다. .env는 비밀값을 분리하지만 암호화하지 않으므로 Git에서 제외한다. 볼륨은 컨테이너와 별도로 데이터를 보존한다.

## 실행 방법
```bash
cd ../guestbook; docker compose up -d --scale web=3 --wait; docker compose ps
```

## 실제 수행 결과
웹 3개, Redis, Nginx를 실행했다. 웹 1개를 stop한 뒤 20회 요청 모두 200이었고 웹은 2개로 남았다. 복구 스크립트 실행부터 준비 완료까지 5.31초가 걸렸다. 이는 단일 실험 결과이며 무중단 보장은 아니다.

[실행 증거](../evidence/recovery.json)

## 문제 해결 및 배운 점
환경 설치 여부와 서비스 준비 상태를 먼저 확인해야 한다. 명령 성공과 실제 HTTP 응답 성공은 별도로 검증한다. 실행하지 않은 항목은 완료로 표시하지 않는다.

## 프로젝트 연결
[방명록 코드](../guestbook) · [과제 Issue](https://github.com/Lime010/devops/issues/1)
