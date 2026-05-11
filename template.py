import os
from pathlib import Path


lst = [
    f'src/__init__.py',
    f'src/components/__init__.py',
    f'src/constants/__init__.py',
    f'src/entity/__init__.py',
    f'src/config/__init__.py',
    f'src/config/configuration.py',
    f'src/logging/__init__.py',
    f'src/exception/__init__.py',
    f'config/params.yaml',
    f'config/config.yaml',
    f'main.py',
    f'requirements.txt',
    f'src/pipeline/__init__.py',
    f'src/utils/__init__.py'
]

for filepath in lst:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
    else:
        pass