import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

planned_images = [
    # trending
    "assets/images/society/image24.jpg", # trending-11
    "assets/images/trending/image20.png", # trending-12
    "assets/images/trending/image21.png", # trending-13
    "assets/images/trending/image22.png", # trending-14
    "assets/images/trending/image24.png", # trending-15
    "assets/images/trending/image25.png", # trending-16
    "assets/images/trending/image26.png", # trending-17
    # society
    "assets/images/society/image23.jpg", # society-9
    "assets/images/society/image25.jpg", # society-10
    "assets/images/society/image26.jpg", # society-11
    # human-stories
    "assets/images/human_stories/image16.jpg", # human-11
    "assets/images/human_stories/image21.jpg", # human-12
    "assets/images/human_stories/image24.jpg", # human-13
    "assets/images/human_stories/image25.jpg", # human-14
    "assets/images/human_stories/image26.jpg", # human-15
    # mind-soul
    "assets/images/mind_&_soul/image20.png", # mind-9 (Banh cuon)
    "assets/images/mind_&_soul/image11.jpg", # mind-10
    "assets/images/mind_&_soul/image12.jpg", # mind-11
    "assets/images/mind_&_soul/image13.jpg", # mind-12
    "assets/images/mind_&_soul/image15.jpg", # mind-13
    "assets/images/mind_&_soul/image16.jpg", # mind-14
    # in-depth
    "assets/images/society/image31.jpg", # indepth-9 (Tycoon villa)
    "assets/images/in-dept/image10.jpg", # indepth-10
    "assets/images/in-dept/image11.jpg", # indepth-11
    "assets/images/in-dept/image12.jpg", # indepth-12
    "assets/images/in-dept/image13.jpg", # indepth-13
    "assets/images/in-dept/image14.jpg", # indepth-14
    "assets/images/in-dept/image15.jpg", # indepth-15
    "assets/images/in-dept/image16.jpg", # indepth-16
    "assets/images/in-dept/image17.jpg", # indepth-17
]

missing = []
for p in planned_images:
    if not os.path.exists(p):
        missing.append(p)

if missing:
    print("MISSING IMAGES:", missing)
else:
    print(f"ALL {len(planned_images)} PLANNED IMAGES EXIST ON DISK!")
