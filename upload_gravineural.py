#!/usr/bin/env python3

"""GRAVI-NEURAL Upload v1.0.0 - PyPI"""

import requests
import hashlib
import os
import glob

TOKEN = "YOUR_TOKEN_HERE"

print("="*60)
print("🔴 GRAVI-NEURAL v1.0.0 Upload - PyPI")
print("="*60)

# قراءة README.md
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()
print(f"📄 README.md: {len(readme)} characters")

# البحث عن ملفات التوزيع
wheel_files = glob.glob("dist/*.whl")
tar_files = glob.glob("dist/*.tar.gz")

if not wheel_files and not tar_files:
    print("\n❌ No distribution files found. Building package...")
    os.system("python -m build")
    
    wheel_files = glob.glob("dist/*.whl")
    tar_files = glob.glob("dist/*.tar.gz")

print(f"\n📦 Files to upload:")
for f in wheel_files + tar_files:
    print(f"   • {os.path.basename(f)}")

# PyPI valid classifiers
classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Topic :: Scientific/Engineering :: Physics',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Scientific/Engineering :: Astronomy',
]

for filepath in wheel_files + tar_files:
    filename = os.path.basename(filepath)
    print(f"\n📤 Uploading: {filename}")

    if filename.endswith('.tar.gz'):
        filetype = 'sdist'
        pyversion = 'source'
    else:
        filetype = 'bdist_wheel'
        pyversion = 'py3'

    with open(filepath, 'rb') as f:
        content = f.read()
    md5_hash = hashlib.md5(content).hexdigest()
    sha256_hash = hashlib.sha256(content).hexdigest()

    data = {
        ':action': 'file_upload',
        'metadata_version': '2.1',
        'name': 'gravi-neural-engine',
        'version': '1.0.0',
        'filetype': filetype,
        'pyversion': pyversion,
        'md5_digest': md5_hash,
        'sha256_digest': sha256_hash,
        'description': readme,
        'description_content_type': 'text/markdown',
        'author': 'Samir Baladi',
        'author_email': 'gitdeeper@gmail.com',
        'license': 'MIT',
        'summary': 'GRAVI-NEURAL: Covariant Neural Characterization of Metric Tensor Perturbations',
        'home_page': 'https://gravi-neural.netlify.app',
        'requires_python': '>=3.11',
        'keywords': 'general-relativity, einstein-field-equations, gravitational-waves',
    }
    
    for i, classifier in enumerate(classifiers, 1):
        data[f'classifier.{i}'] = classifier

    with open(filepath, 'rb') as f:
        response = requests.post(
            'https://upload.pypi.org/legacy/',
            files={'content': (filename, f, 'application/octet-stream')},
            data=data,
            auth=('__token__', TOKEN),
            timeout=60,
            headers={'User-Agent': 'GRAVI-NEURAL-Uploader/1.0'}
        )

    print(f"   Status: {response.status_code}")

    if response.status_code == 200:
        print("   ✅✅✅ Successfully uploaded!")
    else:
        print(f"   ❌ Error: {response.text[:500]}")

print("\n" + "="*60)
print("🔗 https://pypi.org/project/gravi-neural-engine/")
print("="*60)
print("\n📦 Install with: pip install gravi-neural-engine")
