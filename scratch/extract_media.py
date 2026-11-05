import os, sys, zipfile
from PIL import Image
sys.stdout.reconfigure(encoding='utf-8')

docx_path = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\Tài nguyên\[BCTT] Update giao diện.docx'
out_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\scratch\extracted_update_media'
os.makedirs(out_dir, exist_ok=True)

with zipfile.ZipFile(docx_path) as z:
    for name in z.namelist():
        if name.startswith('word/media/'):
            filename = os.path.basename(name)
            out_file = os.path.join(out_dir, filename)
            with open(out_file, 'wb') as f:
                f.write(z.read(name))
            try:
                im = Image.open(out_file)
                print(f"{filename}: size={im.size}, format={im.format}")
            except Exception as e:
                print(f"{filename}: error {e}")
