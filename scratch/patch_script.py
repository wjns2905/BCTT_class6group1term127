import sys, re

with open('scratch/apply_full_100_accurate_images.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace video-3 image
target = "'video-3': {\n        'image': 'assets/images/in-dept/cyber_fraud_investigation.jpg'"
repl = "'video-3': {\n        'image': 'assets/images/society/arte_social_fraud_doc.jpg'"

if target in text:
    text = text.replace(target, repl)
    print("Replaced video-3 image successfully!")
else:
    # Try with \r\n
    target_crlf = "'video-3': {\r\n        'image': 'assets/images/in-dept/cyber_fraud_investigation.jpg'"
    repl_crlf = "'video-3': {\r\n        'image': 'assets/images/society/arte_social_fraud_doc.jpg'"
    if target_crlf in text:
        text = text.replace(target_crlf, repl_crlf)
        print("Replaced video-3 (CRLF) successfully!")
    else:
        print("Target string not found, using regex...")
        text = re.sub(
            r"('video-3':\s*\{\s*'image':\s*)'assets/images/in-dept/cyber_fraud_investigation.jpg'",
            r"\1'assets/images/society/arte_social_fraud_doc.jpg'",
            text
        )

with open('scratch/apply_full_100_accurate_images.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved scratch/apply_full_100_accurate_images.py!")
