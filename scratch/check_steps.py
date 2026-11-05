import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

transcript_path = r'C:\Users\camka\.gemini\antigravity\brain\50d7ed23-5f2b-4287-91eb-56c336819532\.system_generated\logs\transcript.jsonl'
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        step = data.get('step_index')
        if step and 3970 <= step <= 4140:
            if data.get('type') == 'PLANNER_RESPONSE':
                tool_calls = [tc.get('name') for tc in data.get('tool_calls', [])]
                text = data.get('content', '')
                print(f"Step {step}: tools={tool_calls}, text={text[:150]!r}")
            elif data.get('type') == 'USER_INPUT':
                print(f"Step {step} USER: {data.get('content')[:100]!r}")
