import yaml
import sys
import os

def load_yaml(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def extract_api_info(spec):
    if not spec: return {}
    paths = spec.get('paths', {})
    endpoints = {}
    
    for path, methods in paths.items():
        if not path.startswith('/'): continue
        for method, details in methods.items():
            if method.lower() not in ['get', 'post', 'put', 'delete', 'patch']: continue
            
            key = f"{method.upper()} {path}"
            
            summary = details.get('summary', '')
            parameters = [p.get('name', '') for p in details.get('parameters', []) if 'name' in p]
            
            endpoints[key] = {
                'summary': summary,
                'parameters': parameters,
            }
            
    components = spec.get('components', {}).get('schemas', {})
    
    return {
        'endpoints': endpoints,
        'schemas': set(components.keys())
    }

def main():
    old_file = r'ii_docs\api-merged.yaml'
    new_file = r'ii_docs\combined (3).yaml'
    
    old_spec = load_yaml(old_file)
    new_spec = load_yaml(new_file)
    
    old_info = extract_api_info(old_spec)
    new_info = extract_api_info(new_spec)
    
    old_ep = set(old_info['endpoints'].keys())
    new_ep = set(new_info['endpoints'].keys())
    
    added_ep = new_ep - old_ep
    removed_ep = old_ep - new_ep
    common_ep = old_ep & new_ep
    
    modified_ep = []
    for ep in common_ep:
        if old_info['endpoints'][ep] != new_info['endpoints'][ep]:
            modified_ep.append(ep)
            
    old_sc = old_info['schemas']
    new_sc = new_info['schemas']
    
    added_sc = new_sc - old_sc
    removed_sc = old_sc - new_sc
    
    # generate markdown
    md = []
    md.append("# Сводка изменений в API")
    md.append(f"\nСравнение старой версии (`{os.path.basename(old_file)}`) с новой (`{os.path.basename(new_file)}`).")
    
    md.append("\n## Эндпоинты (Маршруты)")
    
    if added_ep:
        md.append("\n### 🟢 Добавлены новые эндпоинты:")
        for ep in sorted(added_ep):
            summary = new_info['endpoints'][ep]['summary']
            md.append(f"- **{ep}**" + (f" - {summary}" if summary else ""))
    else:
        md.append("\n### 🟢 Добавленных эндпоинтов нет.")
        
    if removed_ep:
        md.append("\n### 🔴 Удалены эндпоинты:")
        for ep in sorted(removed_ep):
            md.append(f"- **{ep}**")
    else:
        md.append("\n### 🔴 Удаленных эндпоинтов нет.")
        
    if modified_ep:
        md.append("\n### 🟡 Изменены эндпоинты (параметры/описание):")
        for ep in sorted(modified_ep):
            md.append(f"- **{ep}**")
    
    md.append("\n## Схемы данных (Models/Schemas)")
    
    if added_sc:
        md.append("\n### 🟢 Добавлены новые схемы:")
        for sc in sorted(added_sc):
            md.append(f"- `{sc}`")
    else:
        md.append("\n### 🟢 Добавленных схем нет.")
        
    if removed_sc:
        md.append("\n### 🔴 Удалены схемы:")
        for sc in sorted(removed_sc):
            md.append(f"- `{sc}`")
    else:
        md.append("\n### 🔴 Удаленных схем нет.")
        
    with open('ii_docs/api_changes_summary.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))
        
    print("MD file generated at ii_docs/api_changes_summary.md")

if __name__ == '__main__':
    main()
