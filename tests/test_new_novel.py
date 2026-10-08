import json
import tempfile
import unittest
from pathlib import Path

from scripts.new_novel import replace_placeholders


class ReplacePlaceholdersTest(unittest.TestCase):
    def test_escapes_title_for_yaml_without_changing_display_title(self) -> None:
        title = '他说"你好"\\然后离开\n第二行'
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "novel.yaml").write_text(
                "title: {{NOVEL_TITLE_YAML}}\nid: {{NOVEL_SLUG}}\n",
                encoding="utf-8",
            )
            (root / "README.md").write_text("# {{NOVEL_TITLE}}\n", encoding="utf-8")

            replace_placeholders(root, title, "quoted-title", "2026-10-08")

            yaml_title = (root / "novel.yaml").read_text(encoding="utf-8").splitlines()[0]
            self.assertEqual(json.loads(yaml_title.removeprefix("title: ")), title)
            self.assertEqual((root / "README.md").read_text(encoding="utf-8"), f"# {title}\n")

    def test_does_not_replace_placeholder_text_inside_title(self) -> None:
        title = "保留 {{DATE}}"
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(
                "# {{NOVEL_TITLE}}\nCreated: {{DATE}}\n",
                encoding="utf-8",
            )

            replace_placeholders(root, title, "placeholder-title", "2026-10-08")

            self.assertEqual(
                (root / "README.md").read_text(encoding="utf-8"),
                "# 保留 {{DATE}}\nCreated: 2026-10-08\n",
            )


if __name__ == "__main__":
    unittest.main()
