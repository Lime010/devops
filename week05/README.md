# 05. Docker

자료: 교안 05 / 수업 5주차. 폴더는 수업 주차 기준이다.

## 학습 목표와 핵심 개념
이미지는 실행 환경의 템플릿이고 컨테이너는 실행 인스턴스다. 컨테이너의 쓰기 계층은 삭제 시 사라진다. docker run -p는 호스트 포트를 게시하며 exec는 실행 중인 컨테이너 안에서 명령을 실행한다.

## 실행 방법
```bash
docker version; docker run --rm hello-world; docker ps
```

## 실제 수행 결과
Docker 29.1.3을 설치하고 hello-world를 실행했다. Nginx와 Redis 이미지를 내려받고 Compose 실습에 사용했다.

[실행 증거](../evidence/hello-world.txt)

## 문제 해결 및 배운 점
환경 설치 여부와 서비스 준비 상태를 먼저 확인해야 한다. 명령 성공과 실제 HTTP 응답 성공은 별도로 검증한다. 실행하지 않은 항목은 완료로 표시하지 않는다.

## 프로젝트 연결
[방명록 코드](../guestbook) · [과제 Issue](https://github.com/Lime010/devops/issues/1)
