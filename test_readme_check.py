from pathlib import Path

import readme_check as rc


def test_bad_links_detected():
    assert rc.find_bad_links("[a](http://x.com)") == [("a", "http://x.com")]
    assert rc.find_bad_links("[](https://x.com)")
    assert rc.find_bad_links("[a](https://x.com)") == []


def test_secrets_detected():
    assert rc.find_secrets("key ghp_" + "a" * 30)
    assert rc.find_secrets("nothing here") == []


def test_repo_readme_is_clean():
    assert rc.main(str(Path(__file__).parent / "README.md")) == 0


def test_constitution_has_rules():
    text = (Path(__file__).parent / "CONSTITUTION.md").read_text(encoding="utf-8")
    assert "Never push or publish anything." in text
