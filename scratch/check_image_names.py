import docx
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Let's check images in assets/images/society/ and assets/images/mind_&_soul/
soc_imgs = os.listdir('assets/images/society')
mind_imgs = os.listdir('assets/images/mind_&_soul')
print("Society images:", soc_imgs[:15])
print("Mind images:", mind_imgs[:15])
