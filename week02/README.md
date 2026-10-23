# 02. 셸 스크립팅

자료: 교안 02 / 수업 3주차. 폴더 번호는 교안 번호 기준이다.

## 학습 목표와 핵심 개념
셔뱅은 스크립트를 실행할 인터프리터를 지정한다. $1은 첫 인자, $#은 인자 수, $?는 직전 종료 코드다. 경로와 변수는 따옴표로 감싸 공백을 안전하게 다룬다. 조건문과 반복문으로 반복 작업을 자동화한다.

## 실행 방법
```bash
bash -n ../guestbook/reconcile.sh; bash ../guestbook/reconcile.sh
```

## 실제 수행 결과
복구 스크립트에 변수, 명령 치환, 조건문, 종료 코드를 적용했다. Ollama 컨테이너에 qwen3:0.6b를 내려받아 실제 응답 "안녕하세요!"를 확인했다. 직접 구현한 chat.py와 start.sh를 실행하고 GET 및 질문 POST 응답을 검증했다. 교안의 Ubuntu 직접 설치 대신 Ubuntu 내 Docker로 Ollama를 실행했다.

[실행 증거](../evidence/recovery.json)

## 문제 해결 및 배운 점
환경 설치 여부와 서비스 준비 상태를 먼저 확인해야 한다. 명령 성공과 실제 HTTP 응답 성공은 별도로 검증한다. 실행하지 않은 항목은 완료로 표시하지 않는다.

## 프로젝트 연결
[방명록 코드](../guestbook) · [과제 Issue](https://github.com/Lime010/devops/issues/1)

[Qwen API 결과](../evidence/qwen.json) · [웹 결과](../evidence/qwen-web.txt)
