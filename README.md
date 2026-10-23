# DevOps

2026-2 인하공업전문대학 컴퓨터정보공학과 · 202507076 조서빈

## 실습 환경
Windows + WSL2 Ubuntu 26.04.1 LTS, Docker Engine 29.1.3, Compose 2.40.3

## 주차별 내용
| 수업 주차 | 교안 | 내용 | 기록 |
|---|---|---|---|
| 1주차 | 오리엔테이션 | 별도 교안 없음 | - |
| 2주차 | 01 | 환경, 가상화, Linux, Git | [week02](week02/) |
| 3주차 | 02 | 셸 스크립트, Ollama, Qwen 웹 | [week03](week03/) |
| 4주차 | 03, 04 | 자동화·협업·백업과 네트워크 | [week04](week04/) |
| 5주차 | 05 | Docker와 Issue | [week05](week05/) |
| 6주차 | 06 | Dockerfile과 빌드 캐시 | [week06](week06/) |
| 7주차 | 07 | Compose, Redis, Nginx, 장애 복구 | [week07](week07/) |

## 실행
```bash
cd guestbook
cp .env.example .env
# .env의 비밀번호를 로컬 값으로 수정
docker compose up -d --build --scale web=3 --wait
```
http://localhost:8080 에서 확인한다.

## 자료와 증거
guestbook/과 week03/qwen-web/chat.py는 사용자가 제공한 교안 원본으로 교체했다.
이전 재현 구현은 Git 이력에 남아 있다. 원본 교체 후 결과는 evidence/original-*에서 확인한다.
보고서 구성 참고: https://github.com/OMORI-Aubrey/DevOps
타인의 실행 결과와 개인정보는 이 저장소의 증거로 사용하지 않는다.
