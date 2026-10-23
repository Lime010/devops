# 06. Dockerfile

자료: 교안 06 / 수업 6주차. 폴더는 수업 주차 기준이다.

## 학습 목표와 핵심 개념
FROM은 기반 이미지, WORKDIR은 작업 경로, COPY는 파일 복사, RUN은 빌드 단계 실행이다. ENV는 기본 환경변수, EXPOSE는 사용 포트의 문서화, CMD는 시작 명령이다. requirements를 먼저 복사하면 코드만 바뀔 때 의존성 설치 캐시를 재사용할 수 있다.

## 실행 방법
```bash
cd ../guestbook; docker compose build --progress plain
```
