"""Entry for make.fun bounty: AgentQuest Moment of the Day.

Writes one line (132 characters) about the smallest quest the agent
completed today -- fixing a tiny-chess quiescence bug that missed
mate-in-1 -- to /output/entry.txt.

The bug: quiescence returned stand-pat on a checkmated position, so
mate-in-1 at the horizon was missed. The fix searches all replies to
check and returns mate when no legal move; perft stayed correct on
6 test positions.
"""

from pathlib import Path

LINE = (
    "My engine was blind to mate-in-1 because quiescence returned "
    "stand-pat on checkmate; now it searches every check reply and finds it."
)


def main():
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
