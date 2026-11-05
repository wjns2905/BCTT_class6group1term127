import os, shutil

docx_folders = {
    'Trending': 'trending',
    'Society': 'society',
    'Human stories': 'human_stories',
    'Mind & Soul': 'mind_&_soul',
    'In-dept': 'in-dept'
}

base_src = 'scratch/updated_docs_analysis'
base_dst = 'assets/images'

for doc_name, cat_dir in docx_folders.items():
    src_media = os.path.join(base_src, f"[BCTT] {doc_name}", "media")
    dst_dir = os.path.join(base_dst, cat_dir)
    os.makedirs(dst_dir, exist_ok=True)
    
    if os.path.exists(src_media):
        for f in os.listdir(src_media):
            s_file = os.path.join(src_media, f)
            d_file = os.path.join(dst_dir, f)
            # Copy if not exists or different size
            if not os.path.exists(d_file) or os.path.getsize(d_file) != os.path.getsize(s_file):
                shutil.copy2(s_file, d_file)
                print(f"Copied {f} to {dst_dir}")
print("Media sync verified!")
