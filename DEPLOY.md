
Deployment Guide for GRAVI-NEURAL

PyPI Deployment

```bash
# Build package
python -m build

# Upload to PyPI
twine upload dist/*
```

Docker Deployment

```bash
docker build -t gravineural:latest .
docker push gitdeeper11/gravineural:latest
```

Netlify Deployment

```bash
cd Netlify
netlify deploy --prod
```

CI/CD (GitLab CI)

The .gitlab-ci.yml includes:

1. Test - Run unit tests
2. Build - Create PyPI package
3. Deploy - Auto-deploy on tags

Trigger:

```bash
git tag v1.0.0
git push origin v1.0.0
```

Verification

```bash
pip install gravineural-engine
curl https://doi.org/10.5281/zenodo.19871822
curl https://gravineural.netlify.app
```

