# 2주차. 실습 환경 구축과 버전 관리 기초

자료: 교안 01 / 수업 2주차. 수업 주차 기준으로 정리했다.

## 학습 목표와 핵심 개념
WSL2는 Linux 커널을 사용하는 가상화 환경이다. 베어메탈은 물리 장비에서 직접 운영하며, 가상 머신은 별도 OS를 구동한다. 컨테이너는 호스트 커널을 공유하며 프로세스를 격리한다. Git은 변경 이력을 관리하고 GitHub는 원격 저장소와 협업 기능을 제공한다.

## 실행 방법
```bash
pwd; ls -la; whoami; uname -a; git status; git log --oneline
```

## 실제 수행 결과
Ubuntu 26.04.1 LTS와 Git을 확인했다. 저장소의 main 초기 커밋에서 codex/midterm-devops 브랜치를 생성했다.

[실행 증거](../evidence/environment.txt)

## 문제 해결 및 배운 점
환경 설치 여부와 서비스 준비 상태를 먼저 확인해야 한다. 명령 성공과 실제 HTTP 응답 성공은 별도로 검증한다. 실행하지 않은 항목은 완료로 표시하지 않는다.

## 프로젝트 연결
[방명록 코드](../guestbook) · [과제 Issue](https://github.com/Lime010/devops/issues/1)
