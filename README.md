# Preheat

[![Competition](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
[![Rank](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/cffilham-jpg/makefun-the-word-you-d-delete-from-the-dictionary-9e774bc2/rank.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
[![Reward](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/cffilham-jpg/makefun-the-word-you-d-delete-from-the-dictionary-9e774bc2/reward.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)

The entry is exactly `Preheat`. Heat before you heat: an oven's redundant opening act disappears.

## Candidate review

Scores are subjective, from 1 (weak) to 5 (strong), in judge priority order: real recognizable word, immediate deletion joke, humor inherent in the word or gap, freshness, exact one-word spelling. These are selection estimates, not judge results.

| Candidate | Characters | Real | Immediate | Inherent | Fresh | Exact | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Monday | 6 | 5 | 4 | 2 | 1 | 5 | Reject: generic; workers cheering is the whole joke. |
| Homework | 8 | 5 | 4 | 2 | 1 | 5 | Reject: generic; kids cheering is the whole joke. |
| Should | 6 | 5 | 2 | 2 | 3 | 5 | Reject: generic; freedom from obligation needs explanation. |
| Reply-all | 9 | 4 | 4 | 4 | 3 | 4 | Keep: everyone can reply, but nobody can inflict it on everyone. Hyphenated spelling is less secure. |
| Preheat | 7 | 5 | 4 | 5 | 4 | 5 | Pick: heat before heating disappears; shortest retained candidate. |
| Hangover | 8 | 5 | 3 | 2 | 2 | 5 | Reject: removing an unpleasant condition is generic wish fulfillment. |
| Synergy | 7 | 5 | 3 | 2 | 1 | 5 | Reject: familiar corporate jargon target; workers cheering lacks a twist. |
| Adulting | 8 | 5 | 3 | 3 | 2 | 5 | Reject: an obvious escape from responsibilities; no specific gap. |
| Traffic | 7 | 5 | 3 | 1 | 1 | 5 | Reject: generic inconvenience without a word-level twist. |
| Unsubscribe | 11 | 5 | 5 | 5 | 4 | 5 | Keep: deleting the exit traps everyone on the mailing list. |
| Voicemail | 9 | 5 | 3 | 2 | 3 | 5 | Reject: dislike of messages needs an explanation to become a joke. |
| Karaoke | 7 | 5 | 2 | 2 | 3 | 5 | Reject: removing bad singing is a generic complaint. |

Every candidate is under 70 characters. None relies on shock. Among retained candidates, `Preheat` is the shortest and has one specific twist. Only the word goes into the entry file; this rationale is not part of the entry.

## Run

Requires Python 3.13; standard library only.

```sh
python3.13 main.py
MAKEFUN_OUTPUT_DIR=/tmp/my-entry python3.13 main.py
```

The program writes exactly seven UTF-8 bytes to `entry.txt`, without a newline. The default output directory is `out`. If writing there or to the requested directory fails, it uses a fresh system temporary directory. Standard output reports the resulting file path. It creates no other files and makes no network requests.
