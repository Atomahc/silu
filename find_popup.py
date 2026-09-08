import json

with open('/root/.gemini/antigravity-cli/brain/fea604d0-f4e9-4aa2-bdc3-0efbb250a87f/.system_generated/logs/transcript_full.jsonl', 'r') as f:
    for line in f:
        try:
            data = json.loads(line)
            content = data.get('content', '')
            if '.right-popup' in content:
                print(content[:3000])
        except:
            pass
