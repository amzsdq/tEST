# Clock wrapper invariant

The connected GitHub create_file action exposes repository, path, content, message, and optional branch. It does not expose author-date or committer-date inputs.

For clock sessions this is important: the runtime cannot provide its own timestamp through the marker-write action. The created commit is then fetched by SHA and its timestamp is used for START or END.

The dedicated long-turn-clock branch was verified with both a normal file and a nested run-marker path.
