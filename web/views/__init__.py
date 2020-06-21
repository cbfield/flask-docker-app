import importlib.util

import os

pwd = os.path.dirname(os.path.abspath(__file__))
modules = os.listdir(pwd)

blueprints = []
for module in modules:
    if (not module.endswith('.py')) or (module == '__init__.py'):
        continue

    spec = importlib.util.spec_from_file_location(f'{module.replace(".py","")}', f'{pwd}/{module}')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    
    blueprints.append(mod.views)
