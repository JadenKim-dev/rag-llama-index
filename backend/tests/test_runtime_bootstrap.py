from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_backend_pins_transformers_below_v5():
    pyproject = (REPO_ROOT / "backend" / "pyproject.toml").read_text()

    assert '"transformers<5"' in pyproject


def test_compose_bootstraps_ollama_model_before_backend():
    compose = (REPO_ROOT / "docker-compose.yml").read_text()

    assert "ollama-init:" in compose
    assert "service_completed_successfully" in compose
