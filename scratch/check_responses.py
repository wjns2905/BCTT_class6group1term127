import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

transcript_path = r'C:\Users\camka\.gemini\antigravity\brain\50d7ed23-5f2b-4287-91eb-56c336819532\.system_generated\logs\transcript.jsonl'
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        step = data.get('step_index')
        if step in [3974, 4040, 4058, 4080, 4513]:
            print(f"Step {step} response preview:")
            content = data.get('content', '')
            print(content[:500] if content else 'No content')
            print("-" * 50)
