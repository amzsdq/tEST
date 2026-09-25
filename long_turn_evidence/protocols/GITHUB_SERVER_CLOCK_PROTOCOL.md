# GitHub 서버 시각 기반 작업시간 측정 규칙

## 목적

모델이 직접 `START / END / WORKED` 시간을 기록하는 방식을 폐기하고, GitHub 서버의 `created_at` 타임스탬프를 외부 시계로 사용합니다.

목표는 다음과 같습니다.

* 모델의 시간 착각 제거
* 작업시간 계산 오류 제거
* 사후 검증 가능한 객관적 기록 확보
* 작업 지속/핸드오프 판정을 실제 서버 기록에 기반하도록 변경

## 핵심 원칙

모델이 작업 시작·종료 시각을 직접 작성하지 않습니다.

실제 작업 시작 직전에 GitHub에 `START_MARKER`를 생성하고, 작업 종료 직후 `END_MARKER`를 생성합니다.

작업시간은 두 마커의 GitHub `created_at` 차이로 계산합니다.

```text
WORKED =
END_MARKER.created_at
-
START_MARKER.created_at
```

## 실행 절차

```text
1. SESSION_ID 생성
2. 실제 작업 시작 직전 START_MARKER 생성
3. START_MARKER 생성 성공 확인
4. 실질 작업 수행
5. 작업 종료 직후 END_MARKER 생성
6. 동일 SESSION_ID의 START/END created_at 조회
7. 두 시각의 차이로 WORKED 계산
8. WORKED를 기준으로 다음 상태 결정
```

## Marker 형식

START:
```text
[WORK_MARKER]
session=<SESSION_ID>
phase=START
```

END:
```text
[WORK_MARKER]
session=<SESSION_ID>
phase=END
```

START_MARKER 생성 성공 전에는 실질 작업을 시작하지 않는다.

## 중복 및 오류 처리

```text
START 여러 개 → 가장 이른 valid START 사용
END 여러 개 → START 이후 가장 이른 valid END 사용

START 없음 → INVALID_SESSION
END 없음 → OPEN_SESSION
END < START → INVALID_SESSION
```

## 작업 지속 판정

모델이 작업시간을 자가 추정하지 않는다.

```text
GitHub 서버 기록 확인
→ elapsed 계산
→ 규칙에 따라 상태 전이
```

## 역할 분리

```text
모델 = 작업 수행
GitHub = 외부 시계 + 증거 저장소
프로토콜 = 상태 판정 규칙
```

## 폐기할 기존 방식

모델 자가신고 START/END/WORKED는 공식 기록으로 인정하지 않는다.

## 최종 불변식

```text
WORK_DURATION의 Source of Truth는
모델 출력이 아니라 GitHub 서버 timestamp이다.

WORKED =
END_MARKER.created_at
-
START_MARKER.created_at
```

## tEST 구현 주석

Issue-comment mutation이 OpenAI safety layer에서 반복 차단된 것이 검증되었으므로, tEST의 canonical 구현은 START/END marker를 고유 파일로 생성하고 그 생성 commit의 GitHub `created_at`을 사용한다. 이는 위 원칙의 구현 primitive만 바꾸며 Source of Truth는 그대로 GitHub server timestamp이다.
