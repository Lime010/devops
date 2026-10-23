# 06. Dockerfile

자료: 교안 06 / 수업 6주차. 폴더는 수업 주차 기준이다.

## 학습 목표와 핵심 개념
FROM은 기반 이미지, WORKDIR은 작업 경로, COPY는 파일 복사, RUN은 빌드 단계 실행이다. ENV는 기본 환경변수, EXPOSE는 사용 포트의 문서화, CMD는 시작 명령이다. requirements를 먼저 복사하면 코드만 바뀔 때 의존성 설치 캐시를 재사용할 수 있다.

## 실행 방법
```bash
cd ../guestbook; docker compose build --progress plain
```

## 실제 수행 결과
Python 3.12 기반 방명록을 빌드했다. 재빌드 로그에서 CACHED를 확인할 수 있다. 교안의 공개 이미지는 manifest not found로 실패했으나, 이후 제공받은 guestbook-week07.zip 원본으로 교체하고 다시 빌드했다. GHCR 배포와 외부 이미지 실습은 추가 검증 대상이다.

[실행 증거](../evidence/build-cache.txt)

## 문제 해결 및 배운 점
환경 설치 여부와 서비스 준비 상태를 먼저 확인해야 한다. 명령 성공과 실제 HTTP 응답 성공은 별도로 검증한다. 실행하지 않은 항목은 완료로 표시하지 않는다.

## 프로젝트 연결
[방명록 코드](../guestbook) · [과제 Issue](https://github.com/Lime010/devops/issues/1)
