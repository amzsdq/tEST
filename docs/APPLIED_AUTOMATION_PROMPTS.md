# Applied Automation Prompt Registry

Status: ACTIVE
Repository: `amzsdq/tEST`

Purpose: version every relay prompt actually tested so experiment results can be tied to an exact control policy.

> Security note: runtime-specific automation IDs are replaced with placeholders in this public repository. The tested logic and schedule semantics are preserved.

---

## P0 — Five-write RRULE self-update + close-relative final wake

State: CURRENT BASELINE
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

## Candidate prompt family for convergence

### P1 — Single final RRULE write
Change from P0:
- remove T1…T5
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
