import json, sys
sys.stdout.reconfigure(encoding='utf-8')

transcript_path = r'C:\Users\camka\.gemini\antigravity\brain\50d7ed23-5f2b-4287-91eb-56c336819532\.system_generated\logs\transcript.jsonl'
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        content = json.dumps(data)
        if 'ielts' in content.lower():
            step = data.get('step_index')
            print(f"Step {step} mentioned IELTS")
            if data.get('type') == 'USER_INPUT':
                print("  USER:", data.get('content'))
            elif data.get('type') == 'PLANNER_RESPONSE':
                for tc in data.get('tool_calls', []):
                    print("  Tool call:", tc.get('name'), str(tc.get('args'))[:120])
