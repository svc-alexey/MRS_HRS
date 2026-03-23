import yaml
import sys

def load_yaml(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

old_spec = load_yaml(r'ii_docs\api-merged.yaml')
new_spec = load_yaml(r'ii_docs\combined (3).yaml')

endpoints = [
    ('/menu-item', 'patch'),
    ('/menu-item/{stringNumberId}/reprice', 'patch'),
    ('/menu-items', 'patch')
]

for path, method in endpoints:
    print(f"=== {method.upper()} {path} ===")
    old_data = old_spec.get('paths', {}).get(path, {}).get(method)
    new_data = new_spec.get('paths', {}).get(path, {}).get(method)
    
    print("--- OLD ---")
    print(yaml.dump(old_data, allow_unicode=True, default_flow_style=False, sort_keys=False))
    print("--- NEW ---")
    print(yaml.dump(new_data, allow_unicode=True, default_flow_style=False, sort_keys=False))
    print("\n")
