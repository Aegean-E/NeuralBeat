"""Regression shield: ttkbootstrap-only keyword arguments must stay on ttkbootstrap widgets.

Passing ``bootstyle`` to a standard ``ttk``/``tk`` widget forwards the unknown
option straight to Tcl, which raises ``_tkinter.TclError: unknown option
"-bootstyle"`` while the UI is built and crashes the app before the window
opens. The UI logic tests mock tkinter and ttkbootstrap, so this bug class is
invisible to them; this test checks the invariant statically on SourceCode.py.
"""

import ast
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SOURCE_FILE = PROJECT_ROOT / "SourceCode.py"

TTKBOOTSTRAP_ONLY_KEYWORDS = {"bootstyle"}


def find_bootstyle_violations(source):
    tree = ast.parse(source)
    violations = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
            continue
        if not any(kw.arg in TTKBOOTSTRAP_ONLY_KEYWORDS for kw in node.keywords):
            continue
        receiver = node.func.value
        receiver_name = receiver.id if isinstance(receiver, ast.Name) else None
        if receiver_name != "tb":
            violations.append(
                "line {}: '{}.{}(...)' receives a ttkbootstrap-only keyword".format(
                    node.lineno, receiver_name or "?", node.func.attr
                )
            )
    return violations


class TestBootstyleUsage(unittest.TestCase):
    def test_bootstyle_only_on_ttkbootstrap_widgets(self):
        violations = find_bootstyle_violations(SOURCE_FILE.read_text(encoding="utf-8"))
        self.assertEqual(
            violations,
            [],
            "bootstyle must only be passed to ttkbootstrap (tb.*) widgets:\n"
            + "\n".join(violations),
        )


if __name__ == "__main__":
    unittest.main()
