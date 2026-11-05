import urllib.request, os, json, re, sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

# High quality, curated, verified Unsplash direct URLs for every specific topic:
TOPIC_IMAGE_URLS = {
    # Trending
    'assets/images/trending/ai_newsroom_journalism.jpg': 'https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=900&q=80',
    'assets/images/trending/vintage_film_camera.jpg': 'https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=900&q=80',
    'assets/images/trending/robusta_coffee_vietnam.jpg': 'https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=900&q=80',
    'assets/images/trending/rooftop_pocket_forest.jpg': 'https://images.unsplash.com/photo-1533750349088-cd871a92f312?w=900&q=80',
    'assets/images/trending/art_toy_blind_box.jpg': 'https://images.unsplash.com/photo-1566576912321-d58ddd7a6088?w=900&q=80',
    'assets/images/trending/heritage_train_travel.jpg': 'https://images.unsplash.com/photo-1474487548417-781cb71495f3?w=900&q=80',
    'assets/images/trending/military_history_museum.jpg': 'https://images.unsplash.com/photo-1569154941061-e231b4725ef1?w=900&q=80',
    'assets/images/trending/vietnamese_heritage_attire.jpg': 'https://images.unsplash.com/photo-1583394838336-acd977736f90?w=900&q=80',
    'assets/images/trending/electric_vehicle_green.jpg': 'https://images.unsplash.com/photo-1563720223185-11003d516935?w=900&q=80',
    'assets/images/trending/hanoi_street_food.jpg': 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=900&q=80',
    'assets/images/trending/podcast_healing_audio.jpg': 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=900&q=80',
    'assets/images/trending/agricultural_ecommerce.jpg': 'https://images.unsplash.com/photo-1595974482597-4b8da8879bc5?w=900&q=80',
    'assets/images/trending/esports_championship.jpg': 'https://images.unsplash.com/photo-1542751371-adc38448a05e?w=900&q=80',
    'assets/images/trending/indie_music_acoustic.jpg': 'https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=900&q=80',

    # Society
    'assets/images/society/offshore_wind_energy.jpg': 'https://images.unsplash.com/photo-1466611653911-95081537e5b7?w=900&q=80',
    'assets/images/society/ethnic_minority_heritage.jpg': 'https://images.unsplash.com/photo-1528164344705-475426879c0d?w=900&q=80',
    'assets/images/society/hanoi_metro_railway.jpg': 'https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?w=900&q=80',
    'assets/images/society/rural_kids_coding_class.jpg': 'https://images.unsplash.com/photo-1509062522246-3755977927d7?w=900&q=80',
    'assets/images/society/telemedicine_remote_doctor.jpg': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=900&q=80',
    'assets/images/society/mekong_saline_adaptation.jpg': 'https://images.unsplash.com/photo-1500937386664-56d1dfef3854?w=900&q=80',
    'assets/images/society/highland_mobile_library.jpg': 'https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=900&q=80',
    'assets/images/society/community_safe_shelter.jpg': 'https://images.unsplash.com/photo-1469571486292-0ba58a3f068b?w=900&q=80',
    'assets/images/society/vietnamese_ao_dai_finland.jpg': 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=900&q=80',
    'assets/images/society/child_online_safety.jpg': 'https://images.unsplash.com/photo-1485546246426-74dc88dec4d9?w=900&q=80',
    'assets/images/society/thai_nguyen_tea_hills.jpg': 'https://images.unsplash.com/photo-1536257104079-aa99c6460a5a?w=900&q=80',
    'assets/images/society/hanoi_community_fitness.jpg': 'https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=900&q=80',
    'assets/images/society/youth_caring_elderly.jpg': 'https://images.unsplash.com/photo-1516307365426-bea591f05011?w=900&q=80',
    'assets/images/society/waste_sorting_recycling.jpg': 'https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?w=900&q=80',

    # Human Stories
    'assets/images/human_stories/mountain_teacher_trail.jpg': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=900&q=80',
    'assets/images/human_stories/emotional_family_reunion.jpg': 'https://images.unsplash.com/photo-1511895426328-dc8714191300?w=900&q=80',
    'assets/images/human_stories/charity_soup_kitchen.jpg': 'https://images.unsplash.com/photo-1593113598332-cd288d649433?w=900&q=80',
    'assets/images/human_stories/forest_ranger_patrol.jpg': 'https://images.unsplash.com/photo-1448375240586-882707db888b?w=900&q=80',
    'assets/images/human_stories/creative_culinary_bento.jpg': 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=900&q=80',
    'assets/images/human_stories/extraordinary_mother_love.jpg': 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=900&q=80',
    'assets/images/human_stories/disabled_mentor_teaching.jpg': 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=900&q=80',
    'assets/images/human_stories/flood_rescue_volunteers.jpg': 'https://images.unsplash.com/photo-1547683905-f686c993aae5?w=900&q=80',
    'assets/images/human_stories/night_street_classroom.jpg': 'https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=900&q=80',
    'assets/images/human_stories/free_volunteer_ambulance.jpg': 'https://images.unsplash.com/photo-1587745416684-47953f16f02f?w=900&q=80',
    'assets/images/human_stories/elderly_land_donors.jpg': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=900&q=80',
    'assets/images/human_stories/cerebral_palsy_scholar.jpg': 'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=900&q=80',
    'assets/images/human_stories/heirloom_rice_engineer.jpg': 'https://images.unsplash.com/photo-1530507629858-e4977d30e9e0?w=900&q=80',
    'assets/images/human_stories/elderly_bike_repair.jpg': 'https://images.unsplash.com/photo-1485965120184-e220f721d03e?w=900&q=80',

    # Mind & Soul
    'assets/images/mind_&_soul/slow_living_peace.jpg': 'https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?w=900&q=80',
    'assets/images/mind_&_soul/tay_nguyen_gong_ceremony.jpg': 'https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=900&q=80',
    'assets/images/mind_&_soul/park_violin_community.jpg': 'https://images.unsplash.com/photo-1612225330812-01a9c6b355ec?w=900&q=80',
    'assets/images/mind_&_soul/healing_oasis_sanctuary.jpg': 'https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=900&q=80',
    'assets/images/mind_&_soul/inclusive_theatre_stage.jpg': 'https://images.unsplash.com/photo-1507676184212-d03ab07a01bf?w=900&q=80',
    'assets/images/mind_&_soul/steamed_banh_cuon_delight.jpg': 'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=900&q=80',
    'assets/images/mind_&_soul/shinrin_yoku_forest_bath.jpg': 'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=900&q=80',
    'assets/images/mind_&_soul/therapeutic_journaling.jpg': 'https://images.unsplash.com/photo-1517842645767-c639042777db?w=900&q=80',
    'assets/images/mind_&_soul/shan_tuyet_ancient_tea.jpg': 'https://images.unsplash.com/photo-1576092768241-dec231879fc3?w=900&q=80',
    'assets/images/mind_&_soul/creative_rest_recovery.jpg': 'https://images.unsplash.com/photo-1518495973542-4542c06a5843?w=900&q=80',
    'assets/images/mind_&_soul/ancient_lithophone_stones.jpg': 'https://images.unsplash.com/photo-1511379938547-c1f69419868d?w=900&q=80',
    'assets/images/mind_&_soul/danshari_minimalism.jpg': 'https://images.unsplash.com/photo-1513694203232-719a280e022f?w=900&q=80',
    'assets/images/mind_&_soul/hand_embroidery_art.jpg': 'https://images.unsplash.com/photo-1544816155-12df9643f363?w=900&q=80',
    'assets/images/mind_&_soul/self_compassion_peace.jpg': 'https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=900&q=80',
    'assets/images/mind_&_soul/mindful_pottery_wheel.jpg': 'https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=900&q=80',
    'assets/images/mind_&_soul/aromatherapy_natural_scent.jpg': 'https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?w=900&q=80',

    # In-depth
    'assets/images/in-dept/hanoi_french_colonial_villa.jpg': 'https://images.unsplash.com/photo-1599707367072-cd6ada2bc375?w=900&q=80',
    'assets/images/in-dept/vietnamese_ceramic_master.jpg': 'https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=900&q=80',
    'assets/images/in-dept/can_gio_mangrove_forest.jpg': 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=900&q=80',
    'assets/images/in-dept/cyber_fraud_investigation.jpg': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=900&q=80',
    'assets/images/in-dept/van_phuc_silk_weaving.jpg': 'https://images.unsplash.com/photo-1607344645866-009c320c5ab8?w=900&q=80',
    'assets/images/in-dept/community_mental_health_circle.jpg': 'https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?w=900&q=80',
    'assets/images/in-dept/my_son_cham_sanctuary.jpg': 'https://images.unsplash.com/photo-1528127269322-539801943592?w=900&q=80',
    'assets/images/in-dept/deepwater_container_port.jpg': 'https://images.unsplash.com/photo-1578575437130-527eed3abbec?w=900&q=80',
    'assets/images/in-dept/medical_ai_robotics.jpg': 'https://images.unsplash.com/photo-1516549655169-df83a0774514?w=900&q=80',
    'assets/images/in-dept/heirloom_seed_bank.jpg': 'https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=900&q=80',
    'assets/images/in-dept/dong_ho_folk_painting.jpg': 'https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=900&q=80',
    'assets/images/in-dept/cat_ba_langur_conservation.jpg': 'https://images.unsplash.com/photo-1540573133985-87b6da6d54a9?w=900&q=80',
    'assets/images/in-dept/hue_imperial_gastronomy.jpg': 'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=900&q=80',
    'assets/images/in-dept/han_nom_digital_archive.jpg': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=900&q=80'
}

print(f"Downloading {len(TOPIC_IMAGE_URLS)} high-resolution topical images...")
success = 0
failed = 0

for path, url in TOPIC_IMAGE_URLS.items():
    if os.path.exists(path) and os.path.getsize(path) > 30000:
        # Check if already downloaded
        try:
            with Image.open(path) as im:
                if im.size[0] >= 600 and im.size[1] >= 400:
                    success += 1
                    continue
        except:
            pass

    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = resp.read()
        
        with open(path, 'wb') as f:
            f.write(data)
        
        # Verify
        with Image.open(path) as im:
            w, h = im.size
            if w >= 600 and h >= 400:
                success += 1
                print(f"✓ [{success}] Saved: {path} ({w}x{h}, {len(data)//1024} KB)")
            else:
                print(f"⚠ [{path}] Dimensions too small: {w}x{h}")
    except Exception as e:
        failed += 1
        print(f"✗ Failed {path}: {e}")

print(f"\nResult: {success} succeeded, {failed} failed.")
