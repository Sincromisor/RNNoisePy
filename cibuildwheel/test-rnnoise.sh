#!/bin/bash

set -euo pipefail
set -x

env

. $VIRTUAL_ENV/bin/activate

python -c 'import sys; print(sys.executable)'
python --version

# python -m pip install --upgrade pip setuptools wheel

python - <<'PY'
import sys, sysconfig
print("executable:", sys.executable)
print("implementation:", sys.implementation.name)
print("version:", sys.version.split()[0])
print("abiflags:", getattr(sys, "abiflags", None))
print("SOABI:", sysconfig.get_config_var("SOABI"))
PY

python -m pip install --no-deps /tmp/cibuildwheel/repaired_wheel/*.whl numpy

# run the example with the same interpreter
python /project/examples/rnnoise-test.py
