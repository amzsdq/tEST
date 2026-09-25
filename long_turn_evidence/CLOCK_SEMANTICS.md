# Commit-backed clock semantics

The clock path intentionally omits author and committer date inputs. GitHub's Git Commit API documents that when author is omitted, the authenticated user and current date are used; committer defaults from author. Therefore the runtime must never supply its own date when creating clock commits.

Clock requirements:
- omit author.date and committer.date;
- fetch the created commit by SHA;
- use the returned commit timestamp;
- retain the SHA as evidence;
- START and END must be separate created commits in the same session lineage.

A caller-supplied commit date is not accepted as authoritative runtime evidence.
