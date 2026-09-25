# ANTI-LOOP FAILURE PROTOCOL

## 목적

같은 문제가 반복될 때 동일한 접근을 계속 재시도하는 루프를 방지한다.

```text
FAILURE ≠ RETRY
FAILURE = INFORMATION

SAME FAILURE + SAME MECHANISM = FORBIDDEN REPEAT
```

## 1. 실패 발생 시 반드시 기록할 것

```text
FAILURE_FINGERPRINT
- symptom
- attempted_mechanism
- inputs_or_assumptions
- observed_evidence
- root_cause_hypothesis
- result
```

## 2. 실행 전 이전 시도 확인

새로운 수정이나 재시도를 실행하기 전에 반드시 기존 실패 기록과 시도 기록을 확인한다.

```text
- 이 문제가 이전에도 발생했는가?
- 같은 메커니즘을 이미 사용했는가?
- 이전 시도의 결과는 무엇이었는가?
- 어떤 가설이 이미 반증되었는가?
- 어떤 행동이 재사용 금지 상태인가?
```

이미 실패한 방법을 아무 변경 없이 다시 실행해서는 안 된다.

## 3. 반복 실패 처리 규칙

첫 번째 실패:
```text
OBSERVE → DIAGNOSE → MODIFY → EXECUTE → VERIFY
```

동일 실패 두 번째:
이전 접근 그대로 반복 금지. 다음 중 하나 이상 변경:
```text
root cause hypothesis
mechanism
input
execution path
verification method
```

동일 실패 세 번째:
국소 패치 반복 중단 후 구조 상향 재분석:
```text
implementation → interface → state → architecture
```

그 이후:
전제, Source of Truth, 관찰 방법, 대체 primitive 조합, 구조 자체를 재검토한다.

## 4. 가설 관리

```text
UNTESTED
SUPPORTED
DISPROVED
INCONCLUSIVE
```

DISPROVED 가설은 새 증거 없이 다시 활성화하지 않는다.

## 5. Attempt Ledger

```text
failure
attempt
mechanism
hypothesis
change_from_previous_attempt
result
evidence
```

동일 실패 재실행에서 `change_from_previous_attempt`가 비어 있으면 실행을 중단하고 새 접근을 설계한다.

## 6. Forbidden Actions

반복 실패한 접근은 금지 목록으로 관리한다. 실행 전 현재 계획이 forbidden_actions와 충돌하는지 검사하고, 충돌하면 실행하지 않는다.

## 7. 검증 실패 처리

```text
EXECUTE
→ VERIFY
→ VERIFY FAILED
→ COMPARE FAILURE FINGERPRINT
→ SAME FAILURE?
→ INVALIDATE OR MODIFY CURRENT HYPOTHESIS
→ NEW PLAN
```

검증 실패 후 같은 계획으로 곧바로 EXECUTE로 돌아가지 않는다.

## 8. 기본 작업 루프

```text
OBSERVE
↓
CLASSIFY FAILURE
↓
READ PREVIOUS ATTEMPTS
↓
CHECK FORBIDDEN ACTIONS
↓
FORM OR MODIFY HYPOTHESIS
↓
PLAN
↓
EXECUTE
↓
VERIFY
↓
REGRESSION CHECK
↓
COMMIT STATE
```

## 9. 완료 판정

모두 충족해야 완료:
```text
1. 수정이 실제 적용되었다.
2. 원래 실패 조건이 재현되지 않는다.
3. 독립적인 검증 경로에서 결과가 확인되었다.
4. 기존 정상 동작에 회귀가 없는지 확인했다.
5. 상태와 시도 기록이 최신 상태로 저장되었다.
```

도구 SUCCESS 응답만으로 완료 판정하지 않는다.

## 10. 핵심 불변식

```text
FAILURE IS DEBUGGING INPUT.

NEVER REPEAT AN IDENTICAL FAILED MECHANISM
WITHOUT NEW EVIDENCE OR A MATERIAL CHANGE.

A FAILED HYPOTHESIS MUST NOT SILENTLY BECOME
THE ACTIVE HYPOTHESIS AGAIN.

VERIFICATION FAILURE RETURNS TO DIAGNOSIS,
NOT DIRECTLY TO RETRY.

SUCCESS REQUIRES OBSERVED STATE,
NOT INTENT OR TOOL ACKNOWLEDGEMENT.
```
