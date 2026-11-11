import os
import pytest

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_python_template_structure():
    py_dir = os.path.join(ROOT_DIR, "templates", "python")
    assert os.path.isdir(py_dir)

    expected_files = [
        "main.py",
        "requirements.txt",
        ".env.example",
        ".gitignore",
        "AGENTS.md",
        "README.md",
    ]
    for filename in expected_files:
        path = os.path.join(py_dir, filename)
        assert os.path.isfile(path), f"Missing expected file: {filename}"

    expected_dirs = ["config", "data", "test_scripts", "archive"]
    for dirname in expected_dirs:
        path = os.path.join(py_dir, dirname)
        assert os.path.isdir(path), f"Missing expected directory: {dirname}"


def test_web_template_structure():
    web_dir = os.path.join(ROOT_DIR, "templates", "web")
    assert os.path.isdir(web_dir)

    expected_files = [
        ".env.example",
        ".gitignore",
        "AGENTS.md",
        "README.md",
    ]
    for filename in expected_files:
        path = os.path.join(web_dir, filename)
        assert os.path.isfile(path), f"Missing expected file: {filename}"

    # Verify public DocumentRoot and security .htaccess
    public_dir = os.path.join(web_dir, "public")
    assert os.path.isdir(public_dir)
    assert os.path.isfile(os.path.join(public_dir, "index.html"))
    assert os.path.isfile(os.path.join(public_dir, ".htaccess"))

    # Verify backend and sensitive directory protection
    for protected in ["server", "data", "config"]:
        p_dir = os.path.join(web_dir, protected)
        assert os.path.isdir(p_dir)
        htaccess_file = os.path.join(p_dir, ".htaccess")
        assert os.path.isfile(htaccess_file), f"Missing security .htaccess in {protected}"


def test_no_secrets_committed():
    forbidden_files = [
        ".env",
        ".env.local",
        ".env.production",
        "credentials.json",
        "service-account.json",
    ]
    for root, dirs, files in os.walk(ROOT_DIR):
        if ".git" in dirs:
            dirs.remove(".git")
        for f in files:
            assert f not in forbidden_files, f"Security risk: found committed secret file {f} in {root}"
