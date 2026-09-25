# Admission differential result

The current admission implementation was compared against the staged 11-case LT04 boundary matrix.

Exactly two cases differ:
- elapsed 900, safe=true, qualifying_work=true: current RESERVE_ENTRY; required CONTINUE_STRETCH.
- elapsed 1199, safe=true, qualifying_work=true: current RESERVE_ENTRY; required CONTINUE_STRETCH.

All other staged boundary cases match the intended policy. This confirms the required production change is narrow: preserve validation and existing below-target/unsafe/reserve behavior, and add the safe useful-work stretch branch between target and stretch.
