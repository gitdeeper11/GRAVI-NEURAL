# Installation Guide for GRAVI-NEURAL

## Quick Install (PyPI)

```bash
pip install gravineural-engine
```

Install from Source

```bash
git clone https://github.com/gitdeeper11/GRAVI-NEURAL.git
cd GRAVI-NEURAL
pip install -e .
```

Verify Installation

```python
import gravineural
print(gravineural.__version__)  # 1.0.0
```

Requirements

· Python ≥ 3.11
· numpy ≥ 1.24.0
· scipy ≥ 1.10.0
· torch ≥ 2.0.0

Platform Support

· ✅ Linux
· ✅ macOS
· ✅ Windows
· ✅ Termux (Android)

Docker

```bash
docker build -t gravineural:latest .
docker run --rm gravineural:latest --help
```

For issues, open a ticket on GitHub/GitLab.
