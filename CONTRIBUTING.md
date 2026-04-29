
Contributing to GRAVI-NEURAL

How to Contribute

1. Report bugs via GitHub/GitLab Issues
2. Suggest features with label enhancement
3. Submit code changes via Pull Requests

Development Workflow

```bash
git clone https://github.com/YOUR_USERNAME/GRAVI-NEURAL
cd GRAVI-NEURAL
pip install -e .[dev]
pre-commit install
git checkout -b feature/your-feature-name
pytest tests/ -v
git commit -m "feat: your description"
git push origin feature/your-feature-name
```

Code Style

· Python: PEP 8 (use black)
· Type hints required
· Docstrings: Google style

Testing

All tests must pass: pytest tests/ -v
New features require tests

Questions?

Open an issue or email: gitdeeper@gmail.com
