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

## 데이터 보존 실험
| 동작 | 테스트 글 유지 |
|---|---|
| web 재시작 | 유지 |
| down 후 up | 유지 |
| down -v 후 up | 삭제 |

[실험 원본](../evidence/volume.json). 사용자 승인 후 과제용 테스트 볼륨만 삭제했다.

## 48페이지 호기심 문제 해결
`docker stop`한 컨테이너는 unless-stopped로 자동 복구되지 않았다. 요청 처리와 원하는 개수 유지는 서로 다른 문제다.
`reconcile.sh`는 실행 중인 web 개수가 3이 아니면 compose up으로 다시 맞춘다. flock으로 중복 실행을 막고 .maintenance가 있으면 건너뛴다.
주기 실행은 systemd timer 또는 cron에 등록할 수 있다. 현재 5.31초는 단발 실행 측정이며 주기 감시가 설치된 상태는 아니다.

장점: 수업의 셸과 Compose만으로 구현 가능하고 원하는 개수를 쉽게 확인한다.
단점: 감시 주기만큼 복구가 늦어질 수 있고 의도적인 축소도 되돌릴 수 있다.
한계: running이지만 unhealthy인 상태를 이 스크립트는 복구하지 않는다. 호스트·Docker 데몬이 고장나면 작동하지 않는다. Redis와 Nginx도 단일 장애점이며 데이터 백업·다중 서버 복구는 별도 설계가 필요하다.
대안: 여러 노드의 오케스트레이터로 원하는 복제 수를 관리하되 DB 복제, 영속 스토리지, 외부 진입점의 고가용성까지 구성해야 한다. 단일 PC 실습만으로 서버 장애 복구를 입증할 수 없다.
