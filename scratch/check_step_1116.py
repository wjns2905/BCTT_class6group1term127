import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

transcript_path = r'C:\Users\camka\.gemini\antigravity\brain\50d7ed23-5f2b-4287-91eb-56c336819532\.system_generated\logs\transcript_full.jsonl'
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        step = data.get('step_index')
        if step in [1116, 1117, 1118, 1128]:
            print(f"Step {step}:")
            print(json.dumps(data, indent=2, ensure_ascii=False)[:1000])
            print("="*40)
