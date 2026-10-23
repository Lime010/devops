# 05. Docker

자료: 교안 05 / 수업 5주차. 폴더는 수업 주차 기준이다.

## 학습 목표와 핵심 개념
이미지는 실행 환경의 템플릿이고 컨테이너는 실행 인스턴스다. 컨테이너의 쓰기 계층은 삭제 시 사라진다. docker run -p는 호스트 포트를 게시하며 exec는 실행 중인 컨테이너 안에서 명령을 실행한다.

## 실행 방법
```bash
docker version; docker run --rm hello-world; docker ps
```
