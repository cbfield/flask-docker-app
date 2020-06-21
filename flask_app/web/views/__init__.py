import os

modules = [
    f for f in os.listdir(os.path.dirname(os.path.abspath(__file__)))
    if f.endswith('.py') and f != '__init__.py']

blueprints = []
for module in modules:
    mod = __import__(name=f'web.views.{module[:-3]}',fromlist=['views'])
    blueprints.append(mod.views)
