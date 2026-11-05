import sys, json

sys.stdout.reconfigure(encoding='utf-8')
with open(r'C:\Users\camka\.gemini\antigravity\brain\50d7ed23-5f2b-4287-91eb-56c336819532\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        if obj.get('type') == 'USER_INPUT':
            txt = obj.get('content', '')
            if any(k in txt.lower() for k in ['logo', 'banner', 'ảnh', 'catories', 'chữ']):
                print(f"Step {obj.get('step_index')}: {txt[:120]}")
