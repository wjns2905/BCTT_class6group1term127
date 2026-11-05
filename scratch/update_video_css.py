import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\css\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update iframe rules to include video and .video-native-player
old_rule_1 = """.video-responsive-embed iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: 0;
}"""

new_rule_1 = """.video-responsive-embed iframe,
.video-responsive-embed video,
.video-native-player {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: 0;
  background: #000000;
  object-fit: contain;
}"""

old_rule_2 = """.video-responsive-embed iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: none;
}"""

new_rule_2 = """.video-responsive-embed iframe,
.video-responsive-embed video,
.video-native-player {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: none;
  background: #000000;
  object-fit: contain;
}"""

if old_rule_1 in css:
    css = css.replace(old_rule_1, new_rule_1)
    print("Replaced old_rule_1")
else:
    print("old_rule_1 not found directly")

if old_rule_2 in css:
    css = css.replace(old_rule_2, new_rule_2)
    print("Replaced old_rule_2")
else:
    print("old_rule_2 not found directly")

# Add additional styling for video controls, playing indicator
extra_css = """
/* ===================================================================
   ENHANCED DIRECT INLINE VIDEO PLAYER & HLS STREAMING
   =================================================================== */
.video-native-player::-webkit-media-controls-panel {
  background: linear-gradient(to top, rgba(0, 0, 0, 0.85) 0%, rgba(0, 0, 0, 0.4) 60%, transparent 100%);
}

.video-playing-indicator {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  background: #54111E;
  color: #FFF;
  font-size: 0.7rem;
  font-weight: 800;
  padding: 0.2rem 0.55rem;
  border-radius: 9999px;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  box-shadow: 0 2px 8px rgba(84, 17, 30, 0.4);
}

.video-playing-dot {
  width: 6px;
  height: 6px;
  background: #4ADE80;
  border-radius: 50%;
  animation: pulseDot 1.5s infinite;
}

@keyframes pulseDot {
  0% { transform: scale(0.9); opacity: 0.8; }
  50% { transform: scale(1.4); opacity: 1; }
  100% { transform: scale(0.9); opacity: 0.8; }
}

.playlist-card.active .playlist-play-icon {
  background: #54111E;
  color: #FFF;
}
"""

if ".video-playing-indicator" not in css:
    css += extra_css
    print("Added extra video CSS")

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\css\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css successfully!")
