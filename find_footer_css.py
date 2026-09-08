import json

with open('/root/.gemini/antigravity-cli/brain/fea604d0-f4e9-4aa2-bdc3-0efbb250a87f/.system_generated/logs/transcript_full.jsonl', 'r') as f:
    for line in f:
        try:
            data = json.loads(line)
            content = data.get('content', '')
            if '.scroll-footer {' in content or '.footer-nav-cell' in content:
                print(content[:1000])
        except:
            pass
