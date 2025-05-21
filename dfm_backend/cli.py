import sys
import subprocess
from pathlib import Path

def run():
    subprocess.run([
        "gunicorn",
        "dfm_backend:create_app()",
        "-c",
        str(Path(__file__).resolve().parent / "gunicorn.conf.py"),
        *sys.argv[1:],
    ])
