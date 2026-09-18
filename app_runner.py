import os
import sys
import subprocess

# Определяем корень проекта с учетом специфики бандла macOS (.app)
exe_dir = os.path.dirname(sys.executable)
BASE_DIR = os.path.abspath(os.path.join(exe_dir, "../../../")) if "Contents/MacOS" in exe_dir else exe_dir

# Просто молча будим твой run_desktop.sh и выходим из памяти!
script_path = os.path.join(BASE_DIR, "run_desktop.sh")
subprocess.Popen(["bash", script_path], cwd=BASE_DIR)