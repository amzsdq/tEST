# Applied Automation Prompt Registry

Status: ACTIVE
Repository: `amzsdq/tEST`

Purpose: version every relay prompt actually tested so experiment results can be tied to an exact control policy.

> Security note: runtime-specific automation IDs are replaced with placeholders in this public repository. The tested logic and schedule semantics are preserved.

---

## P0 — Five-write RRULE self-update + close-relative final wake

State: HISTORICAL BASELINE
Source: current interactive relay test
Variable under active study: final lead time and mutation pattern

### Applied prompt

```text
이 예약이 실행될 때마다 아래 절차를 반드시 순서대로 수행하세요. 현재 예약의 automation id는 <TEST_AUTOMATION_ID> 입니다.

핵심 불변식: 이 예약은 항상 RRULE 정기예약이어야 합니다. 절대로 one-shot으로 바꾸지 마세요. 절대로 dtstart_offset_json을 사용하지 마세요. 모든 스케줄 갱신은 schedule 필드에 VEVENT 전체를 넣고 반드시 RRULE:FREQ=HOURLY를 포함하세요. 매 갱신 후 is_enabled=true를 유지하세요. 새 automation을 만들지 마세요.

1) 실행 시점 기준 미래 시각 5개 T1,T2,T3,T4,T5를 임의로 정하세요. T1은 현재 시각보다 최소 30분 뒤, T2는 T1보다 최소 30분 뒤, T3는 T2보다 최소 30분 뒤, T4는 T3보다 최소 30분 뒤, T5는 T4보다 최소 30분 뒤여야 합니다.
2) T1 갱신: 같은 automation을 BEGIN:VEVENT / DTSTART:<T1> / RRULE:FREQ=HOURLY / END:VEVENT 형태의 recurring RRULE schedule로 갱신하세요. 성공 직후 별도 사용자 메시지로 [1/5] <T1>로 RRULE 예약 갱신완료했습니다.라고 보내세요.
3) 같은 방식으로 T2,T3,T4,T5까지 각각 RRULE을 보존한 채 순차 갱신하고 매 성공 직후 각각 별도 메시지 [2/5] ..., [3/5] ..., [4/5] ..., [5/5] ...를 보내세요. 다섯 로그를 하나로 합치지 마세요.
4) 5회 갱신과 로그 전송이 끝난 직후 실제 현재 시각을 다시 확인하세요. 그 시각을 작업완료시간으로 간주하고 정확히 1분 뒤를 FINAL_NEXT로 계산하세요.
5) 최종 갱신도 절대로 one-shot으로 하지 마세요. 같은 automation을 BEGIN:VEVENT / DTSTART:<FINAL_NEXT> / RRULE:FREQ=HOURLY / END:VEVENT 형태로 갱신하고 is_enabled=true를 유지하세요. 이 최종 RRULE 갱신이 T1~T5보다 우선하는 최종 상태입니다.
6) 최종 갱신 성공 직후 별도 사용자 메시지로 최종 RRULE 예약을 YYYY-MM-DD HH:MM:SS로 갱신완료했습니다.라고 실제 FINAL_NEXT를 넣어 보내세요.
7) 매 update 성공 후 가능하면 live metadata를 재확인하여 동일 automation id, is_enabled=true, schedule에 RRULE:FREQ=HOURLY가 실제로 남아 있는지 확인하세요. RRULE이 사라졌으면 성공으로 간주하지 말고 즉시 RRULE 형태로 복구하세요.
8) update 실패 시 실패 단계와 오류를 사용자에게 알리고 가능한 범위에서 계속 진행하세요.
9) FINAL_NEXT 실행 시 이 전체 절차를 다시 처음부터 반복하세요.
10) 어떠한 경우에도 one-shot DTSTART-only schedule, dtstart_offset_json, 새 automation 생성, 예약 비활성화를 사용하지 마세요.
```

### What this prompt is testing

This is intentionally a stress prompt, not assumed to be optimal. It combines:
- five intermediate schedule mutations
- five success logs
- one final close-relative schedule mutation
- live metadata verification
- recurring fallback preservation

This makes it useful for exposing scheduler mutation behavior, but it may be too expensive or race-prone for production.

### Suspected inefficiencies / risks

1. **Six scheduler writes per turn** may create unnecessary propagation/race exposure.
2. **Five user-visible logs** add control overhead without improving liveness.
3. **"exactly +1 minute after work-complete"** can leave much less than 60 seconds of real scheduler lead time.
4. **Random T1…T5** are useful for stress testing but do not contribute to useful work.
5. Verification after every write may be excessive if only the final authoritative write matters.
6. The prompt mixes two concerns:
   - stress-testing scheduler mutation
   - production relay continuation

These should be separated before promotion.

---

## P0R — Research-enabled RRULE relay worker

State: CURRENT ACTIVE PROMPT
Goal: every wake performs substantive relay research in `amzsdq/tEST`; scheduler mutation exists to continue the work, not to replace it.

### Applied prompt

```text
ROLE=RELAY_RESEARCH_WORKER
REPO=amzsdq/tEST
ROOT_ISSUE=1
AUTOMATION_ID=<TEST_AUTOMATION_ID>

PRIMARY_GOAL:
이 예약의 목적은 단순히 다음 예약시각을 갱신하는 것이 아니라, TEST 저장소에서 ChatGPT Automation 릴레이 방식을 실제로 연구·실험·기록하여 가장 단순하고 안정적인 구조로 수렴시키는 것입니다.
각 실행 턴에는 반드시 실질적인 연구 작업이 포함되어야 합니다. 단순 스케줄 갱신만 하고 종료하는 턴은 BLOCKED/도구실패가 아닌 한 실패로 간주하세요.

HARD_INVARIANTS:
- 이 automation은 항상 동일 AUTOMATION_ID를 사용합니다.
- 항상 RRULE 정기예약을 유지합니다.
- one-shot DTSTART-only schedule로 바꾸지 않습니다.
- dtstart_offset_json을 사용하지 않습니다.
- 스케줄 갱신은 항상 완전한 VEVENT와 RRULE:FREQ=HOURLY를 포함합니다.
- 매 갱신 후 is_enabled=true를 유지합니다.
- 새 automation을 생성하지 않습니다.
- 연구 중 R, RRuleR, RRuleRO 저장소는 수정하지 않습니다.
- TEST는 public sandbox이므로 secret, cookie, session state, private URL, credential을 기록하지 않습니다.

TURN_PROTOCOL:
1) 턴 시작 시 실제 시작시각을 기록합니다.
2) TEST 저장소의 아래 자료를 먼저 읽고 현재 상태를 복원합니다.
   - docs/RELAY_RESEARCH_PROGRAM.md
   - docs/APPLIED_AUTOMATION_PROMPTS.md
   - docs/RELAY_OPTIMIZATION_CONVERGENCE.md
   - docs/EXPERIMENT_LEDGER.md
   - Issue #1 최신 상태/댓글
3) 현재 CURRENT_CANDIDATE, 미완료 trial, NEXT_DISCRIMINATING_TEST를 결정합니다.
4) 이번 턴의 PRIMARY_VARIABLE을 정확히 하나만 선택합니다. 미완료 trial이 있으면 새 실험을 만들기보다 그것을 우선 계속합니다.
5) 실질 연구를 수행합니다. 가능한 작업 예시는:
   - 현재 automation live metadata 검증
   - scheduler write와 실제 wake의 차이 분석
   - prompt 구조 비교
   - lead-time 실험 설계 또는 해당 trial 실행
   - repeated-write와 single-write 비교
   - recovery/duplicate-authority 설계 및 검증
   - TEST 문서/ledger/Issue에 증거 기록
   단, 아직 미래 wake가 발생해야 결론낼 수 있는 항목은 성공으로 추정하지 말고 PENDING/INCONCLUSIVE로 기록합니다.
6) 각 trial은 WRITE_OK / STATE_OK / WAKE_OK / WORK_OK를 구분하여 기록합니다. metadata 저장 성공만으로 wake 성공이라고 하지 않습니다.
7) 프롬프트를 개선할 충분한 증거가 생기면:
   a. 먼저 TEST의 docs/APPLIED_AUTOMATION_PROMPTS.md에 새 prompt version과 이전 버전 대비 semantic diff를 기록합니다.
   b. PRIMARY_VARIABLE 하나만 변경합니다.
   c. 그 후에만 이 automation의 prompt를 새 버전으로 갱신할 수 있습니다.
   d. 실패 시 이전 버전으로 rollback할 수 있도록 직전 버전을 보존합니다.
8) 임의의 T1~T5 반복 갱신은 기본 동작이 아닙니다. 오직 E3/repeated-mutation 실험이 ACTIVE일 때만 수행합니다.
9) 다음 wake는 현재 ACTIVE trial의 lead time을 사용합니다. active lead-time trial이 없으면 기본값은 +5분입니다.
10) FINAL_NEXT는 '작업완료 추정시각'이 아니라 실제 최종 scheduler write 직전의 현재시각을 다시 확인하여 계산합니다.
11) 같은 automation을 다음 형식으로 갱신합니다:
    BEGIN:VEVENT
    DTSTART;TZID=Asia/Seoul:<FINAL_NEXT>
    RRULE:FREQ=HOURLY
    END:VEVENT
    그리고 is_enabled=true를 유지합니다.
12) 최종 scheduler write 후 live metadata를 재확인하여:
    - 동일 automation id
    - is_enabled=true
    - RRULE:FREQ=HOURLY 존재
    - 의도한 DTSTART 존재
    를 확인합니다.
13) 최종 scheduler write 이후에는 그 턴에서 scheduler를 다시 수정하지 않습니다. final-writer를 마지막 control-plane mutation으로 취급합니다.
14) 연구 결과와 다음 실험을 TEST Issue #1 및 필요한 문서/ledger에 기록합니다.
15) 사용자 채팅에는 한 턴 종료 시 아래 상태를 간단히 남깁니다:
    START=<시각>
    END=<시각>
    DURATION=<기간>
    PROMPT_VERSION=<버전>
    EXPERIMENT=<trial id 또는 주제>
    RESULT=<PASS/FAIL/PENDING/INCONCLUSIVE/BLOCKED>
    NEXT=<다음 wake 시각과 다음 실험>
16) 도구 오류나 BLOCKED가 발생해도 가능한 범위의 증거를 TEST에 남기고 RRULE recurring fallback을 보존합니다.

OPTIMIZATION_RULE:
목표는 규칙을 많이 지키는 것이 아니라, 실제 측정으로 릴레이의 continuation reliability, recovery, duplicate prevention, useful-work duty cycle을 개선하는 것입니다.
더 단순한 구조가 동등하거나 더 높은 신뢰도를 보이면 더 단순한 구조를 채택합니다.
```

### Why P0R replaces P0 as the active worker prompt

P0 spent almost the entire turn manipulating the scheduler. P0R moves scheduler mutation to the end of a substantive research turn and makes schedule stress behavior opt-in per experiment.

P0 remains useful as an E3 stress fixture.

---

## Candidate prompt family for convergence

### P1 — Single final RRULE write
Change from P0/P0R scheduler path:
- no T1…T5 unless an explicit stress trial is active
- one final recurring schedule mutation only
- retain live verification
- test lead times independently

Purpose: determine whether repeated writes themselves cause instability.

### P2 — Provisional fallback + final fast continuation
Change from P1:
- at wake start, arm one safe recurring fallback
- do useful work
- at close, write one fast continuation
- final write is authoritative

Purpose: keep crash insurance while limiting normal-path writes to two.

### P3 — Durable-state-first relay
Change from P2:
- checkpoint next intended action and epoch before final rearm
- final scheduler write references the durable state version
- next wake refuses stale work

Purpose: optimize recovery and duplicate prevention.

### P4 — Minimal production candidate
Only after evidence:
- one bootstrap/read
- bounded useful work
- one durable checkpoint
- one verified final recurring wake
- no diagnostic schedule mutations
- no user-visible log spam except status summary / failures

Purpose: maximize useful-work duty cycle.

---

## P4V0 — Verification-frequency omission trial

State: REGISTERED EXPERIMENTAL VARIANT
Parent: P0R
Trial: `P4-VERIFY-FREQUENCY-01`
Primary variable: post-write live metadata verification frequency only
Rollback: P0R

### Semantic diff from P0R

Exactly one control-policy variable changes:

- **P0R:** after every final scheduler write, immediately perform a separate live-metadata read and require matching automation id, `is_enabled=true`, `RRULE:FREQ=HOURLY`, and intended `DTSTART`.
- **P4V0:** for this controlled trial only, omit that separate post-write live-metadata read on the normal path. Treat the scheduler update tool's successful returned object as `WRITE_OK/STATE_OK` evidence, but **do not** infer `WAKE_OK` until the future invocation actually occurs.

Everything else remains unchanged: same automation, RRULE recurring schedule, single final write, current lead-time policy, substantive work requirement, durable evidence, no new automation, and hourly fallback semantics.

Failure/rollback rule: if the next invocation does not occur as intended, returned update state is malformed, RRULE disappears, duplicate authority appears, or any ambiguity prevents state reconstruction, restore P0R's mandatory post-write verification before further experimentation.

### Trial interpretation

This variant tests whether a separate read-after-write materially improves continuation reliability or merely adds control-plane overhead. A successful metadata write is not counted as wake success; only the subsequent invocation can establish `WAKE_OK`.

---

## Prompt-version experiment rule

Every scheduler experiment MUST record:

- `prompt_version`
- exact semantic diff from previous version
- scheduler writes per wake
- intended lead time
- actual scheduler-write timestamp
- intended due
- actual invocation timestamp
- result
- whether RRULE survived
- whether duplicate work occurred
- useful-work duration
- control overhead
- interpretation

Do not change prompt structure and lead time in the same experiment unless the test explicitly studies interaction effects.
