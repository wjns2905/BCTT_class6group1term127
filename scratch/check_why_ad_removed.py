import json, sys
sys.stdout.reconfigure(encoding='utf-8')

transcript_path = r'C:\Users\camka\.gemini\antigravity\brain\50d7ed23-5f2b-4287-91eb-56c336819532\.system_generated\logs\transcript.jsonl'
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        step = data.get('step_index')
        if step and 3810 <= step <= 3980:
            if data.get('type') == 'USER_INPUT':
                print(f"Step {step} USER: {data.get('content')}")
            elif data.get('type') == 'PLANNER_RESPONSE':
                text = data.get('content', '')
                if text:
                    print(f"Step {step} ASSISTANT: {text[:200]}")
