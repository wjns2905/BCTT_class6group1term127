# -*- coding: utf-8 -*-
"""
Script to update Hot Paper from update folder to Top 1 Trending across the entire website.
"""

import os
import json
import re

BASE_DIR = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127"
DATA_PATH = os.path.join(BASE_DIR, "js", "data.js")
APP_PATH = os.path.join(BASE_DIR, "js", "app.js")
TRANS_PATH = os.path.join(BASE_DIR, "js", "translations.js")
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
TRENDING_PATH = os.path.join(BASE_DIR, "trending.html")

# =====================================================================
# 1. DEFINE ARTICLE CONTENT (VI & EN)
# =====================================================================

content_vi = [
    "Mới đây, vào ngày 12/11, tài khoản mạng xã hội Threads có tên <strong>ngoc.forever</strong> của Ngọc Mãi (Hải Phòng) đã chia sẻ hình ảnh một chiếc mũ có nhiều đồng tiền lẻ bên trong cùng chiếc áo khoác cũ. Bài đăng mang tiêu đề <em>“Hoá ra trên đời này vẫn còn nhiều đáng yêu đến thế!”</em> nhanh chóng thu hút được sự quan tâm của cộng đồng mạng với hơn 500.000 lượt xem và hàng chục nghìn lượt tương tác.",
    """<figure class="article-body-figure" style="margin:2rem 0; text-align:center;">
  <img src="assets/images/trending/ngoc_mai/threads_post.jpg" alt="Bài đăng từ tài khoản Threads ngoc.forever của Ngọc Mãi" style="max-width:100%; height:auto; max-height:550px; border-radius:12px; box-shadow:0 6px 20px rgba(0,0,0,0.08); display:block; margin:0 auto;">
  <figcaption class="article-body-figcaption" style="font-family:var(--font-sans); font-size:0.875rem; color:var(--color-text-muted); margin-top:0.65rem; font-style:italic; line-height:1.5;">Bài đăng từ tài khoản Threads có tên ngoc.forever của Ngọc Mãi. (Nguồn: Threads)</figcaption>
</figure>""",
    "Trong bài viết, Ngọc Mãi kể rằng, tối 11/11, sau khi tham dự sinh nhật bạn và uống say, cô quyết định đi bộ về nhà vì khoảng cách không xa. Tuy nhiên, khi đi qua khu vực công viên Ulus, cô bất ngờ ngã xuống một chiếc ghế đá và ngủ thiếp đi.",
    "Đến rạng sáng ngày 12/11, khi tỉnh dậy, Ngọc Mãi phát hiện trong chiếc mũ không may rơi xuống đất của mình xuất hiện nhiều đồng tiền lẻ, đồng thời trên người còn có một chiếc áo khoác ấm. Bất ngờ trước những gì xảy ra, cô quyết định chia sẻ câu chuyện ấm áp lên Threads.",
    """<figure class="article-body-figure" style="margin:2rem 0; text-align:center;">
  <img src="assets/images/trending/ngoc_mai/hat_and_jacket.jpg" alt="Hình ảnh chiếc mũ và áo khoác trong bài viết của Ngọc Mãi" style="max-width:100%; height:auto; max-height:550px; border-radius:12px; box-shadow:0 6px 20px rgba(0,0,0,0.08); display:block; margin:0 auto;">
  <figcaption class="article-body-figcaption" style="font-family:var(--font-sans); font-size:0.875rem; color:var(--color-text-muted); margin-top:0.65rem; font-style:italic; line-height:1.5;">Hình ảnh chiếc mũ và áo khoác trong bài viết của Ngọc Mãi. (Nguồn: Nhân vật cung cấp)</figcaption>
</figure>""",
    "### Những hành động tử tế được ghi lại qua camera",
    "Theo hình ảnh trích xuất từ camera an ninh tại khu vực, sự việc được ghi nhận trong khoảng thời gian từ 22h57 đến 23h22 ngày 11/11. Ngọc Mãi xuất hiện tại khu vực ghế đá, sau đó vô tình ngã xuống và nằm co người trên ghế. Trong lúc này, chiếc mũ trên đầu cô rơi xuống đất, phần lòng mũ ngửa lên trên.",
    """<div class="article-cctv-video-wrap" style="margin:2.5rem 0; border-radius:14px; overflow:hidden; background:#000; box-shadow:0 8px 28px rgba(0,0,0,0.18);">
  <video controls playsinline preload="metadata" poster="assets/images/trending/ngoc_mai/hat_and_jacket.jpg" style="width:100%; max-height:500px; display:block; margin:0 auto; background:#000;">
    <source src="assets/videos/cctv_ulus_park_kindness.mp4" type="video/mp4">
    Trình duyệt của bạn không hỗ trợ phát video HTML5.
  </video>
  <div style="background:#141414; color:#E0E0E0; padding:0.75rem 1.25rem; font-size:0.85rem; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; border-top:1px solid #282828;">
    <span><i class="fas fa-video" style="color:var(--color-brand-accent, #80182A);"></i> <strong>Camera an ninh khu vực:</strong> Đoạn video trích xuất ghi lại toàn bộ sự việc lòng tốt của những người qua đường.</span>
    <span style="background:rgba(255,255,255,0.15); padding:2px 8px; border-radius:4px; font-size:0.75rem; font-weight:700;">CCTV FOOTAGE • 1080p</span>
  </div>
</div>""",
    "Một người đi bộ ngang qua nhận thấy cô gái nằm một mình trên ghế đã dừng lại, tiến đến gần và dùng áo khoác đắp lên người cô. Sau đó, một số người khác cũng ghé lại, nhẹ nhàng đặt tiền vào trong chiếc mũ của Ngọc Mãi. Những hình ảnh này phần nào lý giải cho số tiền lẻ trong chiếc mũ và chiếc áo khoác mà cô phát hiện khi tỉnh dậy vào hôm sau.",
    "### “Trông cô ấy tội quá!”",
    "Dưới bài đăng, một tài khoản Threads mang tên <strong>phanhbui</strong> đã gây chú ý khi để lại bình luận cho biết mình đã trực tiếp chứng kiến sự việc: <em>“ô tôi hôm qua có gặp bạn này đây, đi qua thấy bạn nằm co ro mà thấy dưới mũ có mấy đồng tiền nên cũng fomo ủng hộ kkk”</em>.",
    """<figure class="article-body-figure" style="margin:2rem 0; text-align:center;">
  <img src="assets/images/trending/ngoc_mai/comment_phanhbui.jpg" alt="Bình luận của tài khoản phanhbui trên Threads" style="max-width:100%; height:auto; max-height:550px; border-radius:12px; box-shadow:0 6px 20px rgba(0,0,0,0.08); display:block; margin:0 auto;">
  <figcaption class="article-body-figcaption" style="font-family:var(--font-sans); font-size:0.875rem; color:var(--color-text-muted); margin-top:0.65rem; font-style:italic; line-height:1.5;">Một tài khoản có tên phanhbui cho biết mình là người chứng kiến sự việc. (Nguồn: Threads)</figcaption>
</figure>""",
    "Liên hệ với chị Phanh Bui - chủ nhân của bình luận trên và cũng là người trực tiếp để lại tiền trong chiếc mũ của Ngọc Mãi, chị cho biết bản thân dừng lại vì thấy cô gái nằm một mình trên ghế đá giữa thời tiết lạnh. Chia sẻ về hành động của mình, chị Phanh Bui cho biết:",
    """<blockquote class="article-pullquote" style="margin:2rem 0; padding:1.25rem 1.75rem; border-left:4px solid var(--color-brand-primary, #54111E); background:rgba(84,17,30,0.04); border-radius:0 10px 10px 0; font-family:var(--font-serif); font-size:1.15rem; font-style:italic; line-height:1.7; color:var(--color-text-headline);">
  “Trời thì vừa lạnh, vừa tối mà cô gái mặc mỗi cái áo mỏng tang nằm trên ghế, trông cô ấy tội quá! Đúng lúc tôi vừa đi làm về, thấy ở dưới mũ có vài đồng tiền lẻ, tưởng cô ấy cũng là người lang thang nên bỏ tiền vào giúp đỡ.”
  <footer style="margin-top:0.6rem; font-family:var(--font-sans); font-size:0.875rem; font-style:normal; font-weight:700; color:var(--color-brand-primary);">— Chị Phanh Bui (Người chứng kiến và giúp đỡ)</footer>
</blockquote>""",
    """<figure class="article-body-figure" style="margin:2rem 0; text-align:center;">
  <img src="assets/images/trending/ngoc_mai/passerby_kindness.jpg" alt="Người qua đường để lại tiền giúp đỡ" style="max-width:100%; height:auto; max-height:550px; border-radius:12px; box-shadow:0 6px 20px rgba(0,0,0,0.08); display:block; margin:0 auto;">
  <figcaption class="article-body-figcaption" style="font-family:var(--font-sans); font-size:0.875rem; color:var(--color-text-muted); margin-top:0.65rem; font-style:italic; line-height:1.5;">Nhìn thấy Ngọc Mãi co ro trên ghế và những đồng tiền lẻ trong chiếc mũ đặt bên cạnh, chị tưởng cô là người lang thang nên đã bỏ tiền vào để giúp đỡ. (Nguồn: Hearticles)</figcaption>
</figure>""",
    "### Sự tử tế từ những người xa lạ",
    "Chia sẻ về sự việc, Ngọc Mãi cho biết cô khá bất ngờ và cảm thấy đôi chút hối hận khi để một tình huống ngoài ý muốn dẫn đến sự hiểu lầm như vậy. Tuy nhiên, điều khiến cô cảm thấy ấm lòng và cảm động là sự quan tâm của những người xa lạ trong những ngày Hà Nội bắt đầu trở lạnh.",
    "Ngọc Mãi còn tâm sự thêm, nếu người nằm trên ghế đá hôm ấy thực sự là một người không có nơi ở ổn định, những hành động nhỏ như vậy có thể đã giúp họ có thêm một bữa ăn ấm áp. Câu chuyện vì thế không chỉ dừng lại ở một tình huống hài hước, mà còn cho chúng ta thêm niềm tin về những hành động tử tế, bình dị vẫn luôn còn hiện diện giữa cuộc sống hàng ngày.",
    """<figure class="article-body-figure" style="margin:2rem 0; text-align:center;">
  <img src="assets/images/trending/ngoc_mai/ngoc_mai_reflection.jpg" alt="Ngọc Mãi chia sẻ cảm nghĩ" style="max-width:100%; height:auto; max-height:550px; border-radius:12px; box-shadow:0 6px 20px rgba(0,0,0,0.08); display:block; margin:0 auto;">
  <figcaption class="article-body-figcaption" style="font-family:var(--font-sans); font-size:0.875rem; color:var(--color-text-muted); margin-top:0.65rem; font-style:italic; line-height:1.5;">Ngọc Mãi chia sẻ nếu người nằm trên ghế đá hôm ấy thực sự là một người lang thang, những hành động nhỏ như vậy có thể giúp họ có thêm một bữa ăn ấm áp. (Nguồn: Hearticles)</figcaption>
</figure>""",
    "Khép lại cuộc trò chuyện, cô không quên nhắn nhủ mọi người không nên làm theo hành động lạm dụng đồ uống có cồn của mình. Dù câu chuyện mang đến nhiều cảm xúc tích cực, việc uống say rồi tự ý đi lại một mình ở nơi công cộng vẫn tiềm ẩn những rủi ro về an toàn cá nhân.",
    """<!-- PHẦN MỞ RỘNG (EXTENDED READ) -->
<div class="article-extended-box" style="margin:3rem 0; padding:1.75rem; border-radius:14px; background:linear-gradient(135deg, rgba(84,17,30,0.05) 0%, rgba(128,24,42,0.08) 100%); border:1px solid rgba(84,17,30,0.15); box-shadow:0 6px 22px rgba(84,17,30,0.05);">
  <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.75rem;">
    <span style="background:var(--color-brand-primary, #54111E); color:#FFF; font-size:0.75rem; font-weight:800; padding:0.25rem 0.65rem; border-radius:4px; letter-spacing:0.06em; text-transform:uppercase;">
      <i class="fas fa-book-reader"></i> GÓC NHÌN CHUYÊN SÂU • EXTENDED READ
    </span>
  </div>
  <h3 style="font-family:var(--font-editorial); font-size:1.35rem; font-weight:800; color:var(--color-brand-primary); margin:0 0 0.75rem 0;">
    Một hành động nhỏ có thể tạo nên sự khác biệt
  </h3>
  <p style="font-size:1rem; line-height:1.75; color:var(--color-text-body); margin-bottom:1rem; text-align:justify;">
    Không phải lúc nào sự giúp đỡ cũng cần bắt đầu từ những điều lớn lao. Đôi khi, chỉ một chiếc áo khoác được đặt lên vai người đang co ro trong đêm lạnh, một chút tiền lẻ ủng hộ hay đơn giản là việc dừng chân hỏi thăm cũng có thể mang lại sự ấm áp cho một người xa lạ. Thế nhưng, khi bắt gặp ai đó có dấu hiệu say xỉn, mệt mỏi hoặc gặp khó khăn nơi công cộng, chúng ta nên giúp đỡ như thế nào để vừa thể hiện sự quan tâm, vừa đảm bảo an toàn cho họ và chính mình?
  </p>
  <a href="https://vietnamnet.vn/giup-do-nguoi-khac-la-tot-nhung-ban-nhat-dinh-phai-biet-4-quy-tac-an-nay-2297310.html" target="_blank" rel="noopener noreferrer" class="fashion-btn-pill" style="display:inline-flex; align-items:center; gap:0.5rem; background:var(--color-brand-primary, #54111E); color:#FFFFFF !important; text-decoration:none; padding:0.55rem 1.25rem; font-size:0.875rem; font-weight:600; border-radius:99px; transition:all 0.2s ease;">
    <span>Learn more → Giúp đỡ người khác là tốt nhưng bạn nhất định phải biết 4 quy tắc ẩn này</span>
    <i class="fas fa-external-link-alt" style="font-size:0.75rem;"></i>
  </a>
</div>""",
    """<!-- PHẦN QUIZZ (INTERACTIVE SITUATIONAL POLL) -->
<div class="article-quiz-container" id="articleQuizCard" style="margin:3rem 0; padding:1.75rem; border-radius:14px; background:#FFFFFF; border:1px solid var(--color-border-hairline); box-shadow:0 6px 24px rgba(0,0,0,0.06);">
  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; flex-wrap:wrap; gap:0.5rem;">
    <span style="background:rgba(84,17,30,0.1); color:var(--color-brand-primary, #54111E); font-size:0.75rem; font-weight:800; padding:0.3rem 0.75rem; border-radius:4px; letter-spacing:0.06em; text-transform:uppercase;">
      <i class="fas fa-poll-h"></i> THẢO LUẬN & TRẮC NGHIỆM TÌNH HUỐNG
    </span>
    <span style="font-size:0.8125rem; color:var(--color-text-muted);"><i class="far fa-chart-bar"></i> 1.240 độc giả đã tham gia</span>
  </div>
  <h3 style="font-family:var(--font-editorial); font-size:1.25rem; font-weight:800; color:var(--color-text-headline); line-height:1.5; margin:0 0 1.25rem 0;">
    Nếu bắt gặp một người lạ nằm co ro trên ghế đá giữa đêm lạnh, bạn sẽ làm gì?
  </h3>
  <div class="quiz-options-list" style="display:flex; flex-direction:column; gap:0.65rem;">
    <button class="quiz-option-btn" onclick="voteArticleQuiz('A')" id="quizOpt_A" style="width:100%; text-align:left; padding:0.85rem 1.15rem; border:1px solid var(--color-border-hairline); border-radius:10px; background:#FAFAFA; font-size:0.95rem; font-weight:600; color:var(--color-text-headline); cursor:pointer; transition:all 0.2s; position:relative; overflow:hidden;">
      <span class="quiz-opt-text"><i class="far fa-circle" style="margin-right:0.5rem; color:var(--color-brand-accent);"></i> A. Dừng lại hỏi thăm và kiểm tra tình trạng của họ</span>
      <div class="quiz-bar" id="quizBar_A" style="position:absolute; inset:0; background:rgba(84,17,30,0.12); width:0%; transition:width 0.6s ease; z-index:0; display:none;"></div>
      <span class="quiz-percent" id="quizPct_A" style="float:right; font-weight:700; color:var(--color-brand-primary); display:none; position:relative; z-index:1;">68%</span>
    </button>
    <button class="quiz-option-btn" onclick="voteArticleQuiz('B')" id="quizOpt_B" style="width:100%; text-align:left; padding:0.85rem 1.15rem; border:1px solid var(--color-border-hairline); border-radius:10px; background:#FAFAFA; font-size:0.95rem; font-weight:600; color:var(--color-text-headline); cursor:pointer; transition:all 0.2s; position:relative; overflow:hidden;">
      <span class="quiz-opt-text"><i class="far fa-circle" style="margin-right:0.5rem; color:var(--color-brand-accent);"></i> B. Để lại một chút tiền hoặc đồ dùng cần thiết</span>
      <div class="quiz-bar" id="quizBar_B" style="position:absolute; inset:0; background:rgba(84,17,30,0.12); width:0%; transition:width 0.6s ease; z-index:0; display:none;"></div>
      <span class="quiz-percent" id="quizPct_B" style="float:right; font-weight:700; color:var(--color-brand-primary); display:none; position:relative; z-index:1;">12%</span>
    </button>
    <button class="quiz-option-btn" onclick="voteArticleQuiz('C')" id="quizOpt_C" style="width:100%; text-align:left; padding:0.85rem 1.15rem; border:1px solid var(--color-border-hairline); border-radius:10px; background:#FAFAFA; font-size:0.95rem; font-weight:600; color:var(--color-text-headline); cursor:pointer; transition:all 0.2s; position:relative; overflow:hidden;">
      <span class="quiz-opt-text"><i class="far fa-circle" style="margin-right:0.5rem; color:var(--color-brand-accent);"></i> C. Tìm người hỗ trợ nếu họ có dấu hiệu không tỉnh táo</span>
      <div class="quiz-bar" id="quizBar_C" style="position:absolute; inset:0; background:rgba(84,17,30,0.12); width:0%; transition:width 0.6s ease; z-index:0; display:none;"></div>
      <span class="quiz-percent" id="quizPct_C" style="float:right; font-weight:700; color:var(--color-brand-primary); display:none; position:relative; z-index:1;">16%</span>
    </button>
    <button class="quiz-option-btn" onclick="voteArticleQuiz('D')" id="quizOpt_D" style="width:100%; text-align:left; padding:0.85rem 1.15rem; border:1px solid var(--color-border-hairline); border-radius:10px; background:#FAFAFA; font-size:0.95rem; font-weight:600; color:var(--color-text-headline); cursor:pointer; transition:all 0.2s; position:relative; overflow:hidden;">
      <span class="quiz-opt-text"><i class="far fa-circle" style="margin-right:0.5rem; color:var(--color-brand-accent);"></i> D. Tiếp tục di chuyển vì không biết nên xử lý thế nào</span>
      <div class="quiz-bar" id="quizBar_D" style="position:absolute; inset:0; background:rgba(84,17,30,0.12); width:0%; transition:width 0.6s ease; z-index:0; display:none;"></div>
      <span class="quiz-percent" id="quizPct_D" style="float:right; font-weight:700; color:var(--color-brand-primary); display:none; position:relative; z-index:1;">4%</span>
    </button>
  </div>
  <div id="quizFeedbackMessage" style="display:none; margin-top:1.25rem; padding:0.85rem 1rem; border-radius:8px; background:rgba(84,17,30,0.06); color:var(--color-brand-primary); font-size:0.9rem; font-weight:600;">
    <i class="fas fa-heart"></i> Cảm ơn bạn đã chia sẻ quan điểm! Mỗi hành động xuất phát từ sự tử tế và lòng trắc ẩn đều góp phần làm cho cuộc sống này thêm ấm áp.
  </div>
</div>"""
]

content_en = [
    "Recently, on November 12, a Threads social media account named <strong>ngoc.forever</strong> belonging to Ngoc Mai (Hai Phong) shared a photograph of a fallen cap containing small banknotes alongside an old jacket. The post, titled <em>“Turns out there is still so much love in this world!”</em>, rapidly captured immense attention across social media with over 500,000 views and tens of thousands of interactions.",
    """<figure class="article-body-figure" style="margin:2rem 0; text-align:center;">
  <img src="assets/images/trending/ngoc_mai/threads_post.jpg" alt="Viral post from Threads account ngoc.forever by Ngoc Mai" style="max-width:100%; height:auto; max-height:550px; border-radius:12px; box-shadow:0 6px 20px rgba(0,0,0,0.08); display:block; margin:0 auto;">
  <figcaption class="article-body-figcaption" style="font-family:var(--font-sans); font-size:0.875rem; color:var(--color-text-muted); margin-top:0.65rem; font-style:italic; line-height:1.5;">Viral post from Threads account ngoc.forever by Ngoc Mai. (Source: Threads)</figcaption>
</figure>""",
    "In her post, Ngoc Mai recounted that on the evening of November 11, after attending a friend's birthday party and drinking heavily, she decided to walk home since the distance was not far. However, while passing through Ulus park area, she unexpectedly collapsed onto a stone bench and fell sound asleep.",
    "Early in the morning of November 12, upon waking up, Ngoc Mai discovered that her cap, which had accidentally fallen to the ground, contained numerous small change banknotes, and a warm jacket was gently draped over her body. Overwhelmed with gratitude and astonishment at what had transpired, she decided to share the heartfelt story on Threads.",
    """<figure class="article-body-figure" style="margin:2rem 0; text-align:center;">
  <img src="assets/images/trending/ngoc_mai/hat_and_jacket.jpg" alt="Photo of the cap with cash and the warm jacket" style="max-width:100%; height:auto; max-height:550px; border-radius:12px; box-shadow:0 6px 20px rgba(0,0,0,0.08); display:block; margin:0 auto;">
  <figcaption class="article-body-figcaption" style="font-family:var(--font-sans); font-size:0.875rem; color:var(--color-text-muted); margin-top:0.65rem; font-style:italic; line-height:1.5;">The photo of the cap with banknotes and the warm jacket in Ngoc Mai's viral story. (Source: Courtesy of the subject)</figcaption>
</figure>""",
    "### Acts of Kindness Recorded on Security Cameras",
    "According to surveillance footage extracted from the local security camera system, the incident was recorded between 22:57 and 23:22 on the night of November 11. Ngoc Mai appeared near the stone bench area, then accidentally fell down and curled up asleep on the bench. In the process, her cap fell to the ground with the inside facing upward.",
    """<div class="article-cctv-video-wrap" style="margin:2.5rem 0; border-radius:14px; overflow:hidden; background:#000; box-shadow:0 8px 28px rgba(0,0,0,0.18);">
  <video controls playsinline preload="metadata" poster="assets/images/trending/ngoc_mai/hat_and_jacket.jpg" style="width:100%; max-height:500px; display:block; margin:0 auto; background:#000;">
    <source src="assets/videos/cctv_ulus_park_kindness.mp4" type="video/mp4">
    Your browser does not support HTML5 video playback.
  </video>
  <div style="background:#141414; color:#E0E0E0; padding:0.75rem 1.25rem; font-size:0.85rem; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; border-top:1px solid #282828;">
    <span><i class="fas fa-video" style="color:var(--color-brand-accent, #80182A);"></i> <strong>Local Security Surveillance:</strong> Full CCTV footage capturing the spontaneous acts of kindness by strangers.</span>
    <span style="background:rgba(255,255,255,0.15); padding:2px 8px; border-radius:4px; font-size:0.75rem; font-weight:700;">CCTV FOOTAGE • 1080p</span>
  </div>
</div>""",
    "A passerby walking past noticed the young woman lying alone on the bench, stopped, approached gently, and used an extra jacket to cover her against the night chill. Shortly afterward, several other pedestrians stopped by, delicately dropping banknotes into Ngoc Mai's fallen cap. These authentic surveillance images explained the loose change and warm jacket she found upon awakening the following morning.",
    "### “She Looked So Pitiful!”",
    "Beneath the viral post, a Threads user named <strong>phanhbui</strong> caught wide attention by commenting that she had directly witnessed the scene: <em>“Oh I saw you yesterday! Walking past I saw you curled up shivering and saw some small change in your cap, so I got the fomo urge to contribute too haha”</em>.",
    """<figure class="article-body-figure" style="margin:2rem 0; text-align:center;">
  <img src="assets/images/trending/ngoc_mai/comment_phanhbui.jpg" alt="Comment by user phanhbui on Threads" style="max-width:100%; height:auto; max-height:550px; border-radius:12px; box-shadow:0 6px 20px rgba(0,0,0,0.08); display:block; margin:0 auto;">
  <figcaption class="article-body-figcaption" style="font-family:var(--font-sans); font-size:0.875rem; color:var(--color-text-muted); margin-top:0.65rem; font-style:italic; line-height:1.5;">Threads user phanhbui confirmed witnessing the scene and leaving money. (Source: Threads)</figcaption>
</figure>""",
    "Contacting Ms. Phanh Bui — the author of the comment and the person who directly dropped money into Ngoc Mai's cap — she explained that she stopped because she saw a girl lying alone on a stone bench in the cold weather. Reflecting on her action, Ms. Phanh Bui shared:",
    """<blockquote class="article-pullquote" style="margin:2rem 0; padding:1.25rem 1.75rem; border-left:4px solid var(--color-brand-primary, #54111E); background:rgba(84,17,30,0.04); border-radius:0 10px 10px 0; font-family:var(--font-serif); font-size:1.15rem; font-style:italic; line-height:1.7; color:var(--color-text-headline);">
  “It was dark and freezing cold, and the girl was wearing only a flimsy shirt lying on the bench. She looked so pitiful! I was heading home from work, saw a few small notes under her cap, thought she was homeless, so I put some money in to help.”
  <footer style="margin-top:0.6rem; font-family:var(--font-sans); font-size:0.875rem; font-style:normal; font-weight:700; color:var(--color-brand-primary);">— Ms. Phanh Bui (Eyewitness & Good Samaritan)</footer>
</blockquote>""",
    """<figure class="article-body-figure" style="margin:2rem 0; text-align:center;">
  <img src="assets/images/trending/ngoc_mai/passerby_kindness.jpg" alt="Passerby leaving money to help" style="max-width:100%; height:auto; max-height:550px; border-radius:12px; box-shadow:0 6px 20px rgba(0,0,0,0.08); display:block; margin:0 auto;">
  <figcaption class="article-body-figcaption" style="font-family:var(--font-sans); font-size:0.875rem; color:var(--color-text-muted); margin-top:0.65rem; font-style:italic; line-height:1.5;">Seeing Ngoc Mai shivering on the bench with change in the cap, she thought she was homeless and offered help. (Source: Hearticles)</figcaption>
</figure>""",
    "### Unconditional Kindness from Strangers",
    "Reflecting on the incident, Ngoc Mai expressed surprise and felt a bit remorseful for allowing an unintended situation to create such a comical misunderstanding. Nevertheless, what deeply touched her heart was the genuine warmth and concern from complete strangers during the chilly early winter days in Hanoi.",
    "Ngoc Mai added that if the person lying on that bench that night had truly been an unhoused individual, such small gestures might have provided them with a warm, comforting meal. The story thus goes beyond a humorous misunderstanding, reaffirming our faith in the quiet, everyday kindness that always exists around us.",
    """<figure class="article-body-figure" style="margin:2rem 0; text-align:center;">
  <img src="assets/images/trending/ngoc_mai/ngoc_mai_reflection.jpg" alt="Ngoc Mai reflecting on everyday kindness" style="max-width:100%; height:auto; max-height:550px; border-radius:12px; box-shadow:0 6px 20px rgba(0,0,0,0.08); display:block; margin:0 auto;">
  <figcaption class="article-body-figcaption" style="font-family:var(--font-sans); font-size:0.875rem; color:var(--color-text-muted); margin-top:0.65rem; font-style:italic; line-height:1.5;">Ngoc Mai reflected that if the person had truly been homeless, such small acts could have provided a warm meal. (Source: Hearticles)</figcaption>
</figure>""",
    "Concluding our conversation, she did not forget to remind everyone against reckless alcohol consumption. Although the narrative brought overwhelmingly positive emotions, getting intoxicated and wandering alone in public spaces still carries inherent safety risks.",
    """<!-- EXTENDED READ BOX -->
<div class="article-extended-box" style="margin:3rem 0; padding:1.75rem; border-radius:14px; background:linear-gradient(135deg, rgba(84,17,30,0.05) 0%, rgba(128,24,42,0.08) 100%); border:1px solid rgba(84,17,30,0.15); box-shadow:0 6px 22px rgba(84,17,30,0.05);">
  <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.75rem;">
    <span style="background:var(--color-brand-primary, #54111E); color:#FFF; font-size:0.75rem; font-weight:800; padding:0.25rem 0.65rem; border-radius:4px; letter-spacing:0.06em; text-transform:uppercase;">
      <i class="fas fa-book-reader"></i> EXTENDED PERSPECTIVE
    </span>
  </div>
  <h3 style="font-family:var(--font-editorial); font-size:1.35rem; font-weight:800; color:var(--color-brand-primary); margin:0 0 0.75rem 0;">
    A small act of kindness can make a huge difference
  </h3>
  <p style="font-size:1rem; line-height:1.75; color:var(--color-text-body); margin-bottom:1rem; text-align:justify;">
    Kindness doesn't always have to begin with grand gestures. Sometimes, simply draping a warm jacket over someone shivering in the chill of the night, dropping some spare change, or gently asking if they are okay can bring immense warmth to a stranger. Yet, when encountering someone intoxicated, exhausted, or in distress in public, how should we step in to show compassion while ensuring both their safety and our own?
  </p>
  <a href="https://vietnamnet.vn/giup-do-nguoi-khac-la-tot-nhung-ban-nhat-dinh-phai-biet-4-quy-tac-an-nay-2297310.html" target="_blank" rel="noopener noreferrer" class="fashion-btn-pill" style="display:inline-flex; align-items:center; gap:0.5rem; background:var(--color-brand-primary, #54111E); color:#FFFFFF !important; text-decoration:none; padding:0.55rem 1.25rem; font-size:0.875rem; font-weight:600; border-radius:99px; transition:all 0.2s ease;">
    <span>Learn more → Helping others is admirable, but you must know these 4 unspoken rules</span>
    <i class="fas fa-external-link-alt" style="font-size:0.75rem;"></i>
  </a>
</div>""",
    """<!-- INTERACTIVE SITUATIONAL POLL -->
<div class="article-quiz-container" id="articleQuizCard" style="margin:3rem 0; padding:1.75rem; border-radius:14px; background:#FFFFFF; border:1px solid var(--color-border-hairline); box-shadow:0 6px 24px rgba(0,0,0,0.06);">
  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; flex-wrap:wrap; gap:0.5rem;">
    <span style="background:rgba(84,17,30,0.1); color:var(--color-brand-primary, #54111E); font-size:0.75rem; font-weight:800; padding:0.3rem 0.75rem; border-radius:4px; letter-spacing:0.06em; text-transform:uppercase;">
      <i class="fas fa-poll-h"></i> SITUATIONAL COMMUNITY QUIZ
    </span>
    <span style="font-size:0.8125rem; color:var(--color-text-muted);"><i class="far fa-chart-bar"></i> 1,240 readers participated</span>
  </div>
  <h3 style="font-family:var(--font-editorial); font-size:1.25rem; font-weight:800; color:var(--color-text-headline); line-height:1.5; margin:0 0 1.25rem 0;">
    If you encounter a stranger shivering on a stone bench in the cold of night, what would you do?
  </h3>
  <div class="quiz-options-list" style="display:flex; flex-direction:column; gap:0.65rem;">
    <button class="quiz-option-btn" onclick="voteArticleQuiz('A')" id="quizOpt_A" style="width:100%; text-align:left; padding:0.85rem 1.15rem; border:1px solid var(--color-border-hairline); border-radius:10px; background:#FAFAFA; font-size:0.95rem; font-weight:600; color:var(--color-text-headline); cursor:pointer; transition:all 0.2s; position:relative; overflow:hidden;">
      <span class="quiz-opt-text"><i class="far fa-circle" style="margin-right:0.5rem; color:var(--color-brand-accent);"></i> A. Stop to check in and verify their condition</span>
      <div class="quiz-bar" id="quizBar_A" style="position:absolute; inset:0; background:rgba(84,17,30,0.12); width:0%; transition:width 0.6s ease; z-index:0; display:none;"></div>
      <span class="quiz-percent" id="quizPct_A" style="float:right; font-weight:700; color:var(--color-brand-primary); display:none; position:relative; z-index:1;">68%</span>
    </button>
    <button class="quiz-option-btn" onclick="voteArticleQuiz('B')" id="quizOpt_B" style="width:100%; text-align:left; padding:0.85rem 1.15rem; border:1px solid var(--color-border-hairline); border-radius:10px; background:#FAFAFA; font-size:0.95rem; font-weight:600; color:var(--color-text-headline); cursor:pointer; transition:all 0.2s; position:relative; overflow:hidden;">
      <span class="quiz-opt-text"><i class="far fa-circle" style="margin-right:0.5rem; color:var(--color-brand-accent);"></i> B. Leave some spare change or warm essentials</span>
      <div class="quiz-bar" id="quizBar_B" style="position:absolute; inset:0; background:rgba(84,17,30,0.12); width:0%; transition:width 0.6s ease; z-index:0; display:none;"></div>
      <span class="quiz-percent" id="quizPct_B" style="float:right; font-weight:700; color:var(--color-brand-primary); display:none; position:relative; z-index:1;">12%</span>
    </button>
    <button class="quiz-option-btn" onclick="voteArticleQuiz('C')" id="quizOpt_C" style="width:100%; text-align:left; padding:0.85rem 1.15rem; border:1px solid var(--color-border-hairline); border-radius:10px; background:#FAFAFA; font-size:0.95rem; font-weight:600; color:var(--color-text-headline); cursor:pointer; transition:all 0.2s; position:relative; overflow:hidden;">
      <span class="quiz-opt-text"><i class="far fa-circle" style="margin-right:0.5rem; color:var(--color-brand-accent);"></i> C. Seek security or nearby assistance if they seem unresponsive</span>
      <div class="quiz-bar" id="quizBar_C" style="position:absolute; inset:0; background:rgba(84,17,30,0.12); width:0%; transition:width 0.6s ease; z-index:0; display:none;"></div>
      <span class="quiz-percent" id="quizPct_C" style="float:right; font-weight:700; color:var(--color-brand-primary); display:none; position:relative; z-index:1;">16%</span>
    </button>
    <button class="quiz-option-btn" onclick="voteArticleQuiz('D')" id="quizOpt_D" style="width:100%; text-align:left; padding:0.85rem 1.15rem; border:1px solid var(--color-border-hairline); border-radius:10px; background:#FAFAFA; font-size:0.95rem; font-weight:600; color:var(--color-text-headline); cursor:pointer; transition:all 0.2s; position:relative; overflow:hidden;">
      <span class="quiz-opt-text"><i class="far fa-circle" style="margin-right:0.5rem; color:var(--color-brand-accent);"></i> D. Keep walking because unsure of how to safely assist</span>
      <div class="quiz-bar" id="quizBar_D" style="position:absolute; inset:0; background:rgba(84,17,30,0.12); width:0%; transition:width 0.6s ease; z-index:0; display:none;"></div>
      <span class="quiz-percent" id="quizPct_D" style="float:right; font-weight:700; color:var(--color-brand-primary); display:none; position:relative; z-index:1;">4%</span>
    </button>
  </div>
  <div id="quizFeedbackMessage" style="display:none; margin-top:1.25rem; padding:0.85rem 1rem; border-radius:8px; background:rgba(84,17,30,0.06); color:var(--color-brand-primary); font-size:0.9rem; font-weight:600;">
    <i class="fas fa-heart"></i> Thank you for sharing your thoughts! Every action born of kindness and empathy makes our community warmer.
  </div>
</div>"""
]

new_article_trending_1 = {
    "id": "trending-1",
    "category": "trending",
    "categoryName": "Trending",
    "title": "Cô gái say rượu ngã gục trên ghế, bất ngờ nhận được sự giúp đỡ “đặc biệt” từ người qua đường",
    "title_en": "Drunk Girl Collapses on Park Bench, Unexpectedly Receives 'Special' Kindness from Strangers",
    "subtitle": "“Trông cô ấy tội quá”- một người qua đường chia sẻ khi kể lại khoảnh khắc bắt gặp Ngọc Mãi nằm co ro ngoài công viên và quyết định để lại tiền trong chiếc mũ của cô.",
    "subtitle_en": "'She looked so pitiful,' a passerby recalled discovering Ngoc Mai curled up on a park bench and deciding to leave small change in her fallen cap.",
    "author": "Ngọc Mãi & Ban Biên tập Hearticles",
    "date": "Thursday, November 12, 2026 - 21:00 (GMT+7)",
    "readTime": "5 min read",
    "sourceName": "Threads & Hearticles",
    "sourceUrl": "https://www.threads.net/@ngoc.forever",
    "image": "assets/images/trending/ngoc_mai/hat_and_jacket.jpg",
    "imageCaption": "Hình ảnh chiếc mũ có tiền lẻ và chiếc áo khoác đắp ấm trong câu chuyện của Ngọc Mãi. (Nguồn: Nhân vật cung cấp)",
    "video": "assets/videos/cctv_ulus_park_kindness.mp4",
    "isTopPost": True,
    "isBreaking": True,
    "views": "528.6K",
    "likes": 1450,
    "tags": [
        "Trending",
        "Viral Story",
        "Threads",
        "Human Kindness",
        "Hanoi Nights"
    ],
    "content": content_vi,
    "content_en": content_en
}

# Move old trending-1 (Lawmakers...) to trending-21 so no data is lost
old_lawmakers_article = {
    "id": "trending-21",
    "category": "trending",
    "categoryName": "Trending",
    "title": "Đại biểu Quốc hội đề xuất các giải pháp đột phá phát triển kinh tế vùng miền núi, biên giới",
    "title_en": "Lawmakers propose measures to boost development in mountainous, border regions",
    "subtitle": "Tập trung đầu tư hạ tầng giao thông kết nối, phát huy thế mạnh nông lâm sản đặc thù và nâng cao sinh kế bền vững cho đồng bào các tỉnh miền núi phía Bắc.",
    "subtitle_en": "National Assembly deputies propose breakthrough measures to foster regional strengths, improve transport infrastructure, and promote socioeconomic development in northern mountainous and border provinces.",
    "author": "Đoàn Thị Lê An & NDO",
    "date": "Saturday, October 31, 2026 - 18:26 (GMT+7)",
    "readTime": "5 min read",
    "sourceName": "Báo Nhân Dân",
    "sourceUrl": "https://en.nhandan.vn/lawmakers-propose-measures-to-boost-development-in-mountainous-border-regions-post168532.html",
    "image": "assets/images/trending/lawmakers_lead.jpg",
    "imageCaption": "NA deputy Doan Thi Le An from Cao Bang Province speaks at the National Assembly discussion. (Photo: NDO)",
    "video": "",
    "isTopPost": False,
    "isBreaking": False,
    "views": "14.2K",
    "likes": 328,
    "tags": ["National Assembly", "Mountainous Regions", "Economy", "Vietnam"]
}

# =====================================================================
# 2. UPDATE JS/DATA.JS
# =====================================================================
print("Updating js/data.js...")
with open(DATA_PATH, "r", encoding="utf-8") as f:
    data_content = f.read()

start_marker = "const ARTICLES_DATA = "
start_idx = data_content.find(start_marker) + len(start_marker)
end_idx = data_content.rfind("];") + 1

articles_json = json.loads(data_content[start_idx:end_idx])

# Find index of trending-1
t1_idx = None
for i, a in enumerate(articles_json):
    if a.get("id") == "trending-1":
        t1_idx = i
        # Preserving original content for trending-21
        old_lawmakers_article["content"] = a.get("content", [])
        break

if t1_idx is not None:
    articles_json[t1_idx] = new_article_trending_1
    articles_json.append(old_lawmakers_article)
else:
    articles_json.insert(0, new_article_trending_1)

new_articles_json_str = json.dumps(articles_json, ensure_ascii=False, indent=2)
new_data_content = data_content[:start_idx] + new_articles_json_str + data_content[end_idx:]

with open(DATA_PATH, "w", encoding="utf-8") as f:
    f.write(new_data_content)
print("SUCCESS: Updated js/data.js with new trending-1 article.")

# =====================================================================
# 3. UPDATE JS/APP.JS (Support content_en, local mp4, and quiz voting)
# =====================================================================
print("Updating js/app.js...")
with open(APP_PATH, "r", encoding="utf-8") as f:
    app_code = f.read()

# 3.1 Support content_en in openArticleModal
old_content_render = """  let bodyHtml = '';
  if (typeof article.content === 'string') {
    bodyHtml = article.content;
  } else if (Array.isArray(article.content)) {"""

new_content_render = """  let bodyHtml = '';
  const contentSource = (isEn && article.content_en) ? article.content_en : article.content;
  if (typeof contentSource === 'string') {
    bodyHtml = contentSource;
  } else if (Array.isArray(contentSource)) {"""

if old_content_render in app_code:
    app_code = app_code.replace(old_content_render, new_content_render)
    print("SUCCESS: Enabled content_en bilingual rendering in openArticleModal.")

# 3.2 Support local mp4 in renderModalVideoBlock
old_render_video = """function renderModalVideoBlock(article, isEn, title) {
  if (!article.video && !article.streamUrl) return '';

  // Case 1: Direct native/HLS stream URL"""

new_render_video = """function renderModalVideoBlock(article, isEn, title) {
  if (!article.video && !article.streamUrl) return '';

  // Case 0: Local MP4 video file
  if (article.video && article.video.endsWith('.mp4')) {
    return `
    <div class="video-responsive-embed" style="margin-bottom: 2rem; border-radius: 12px; overflow:hidden; background:#000; box-shadow: 0 4px 18px rgba(0,0,0,0.14);">
      <video id="activeModalNativePlayer" controls playsinline poster="${article.image}" preload="metadata" style="width:100%; max-height:500px; display:block; margin:0 auto; background:#000;">
        <source src="${article.video}" type="video/mp4">
        ${isEn ? 'Your browser does not support HTML5 video.' : 'Trình duyệt của bạn không hỗ trợ video HTML5.'}
      </video>
      <div style="background:#161616; color:#E0E0E0; padding:0.65rem 1rem; font-size:0.8125rem; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; border-top:1px solid #282828;">
        <span><i class="fas fa-video" style="color:var(--color-brand-accent, #80182A);"></i> ${isEn ? 'Security Camera Surveillance: Full footage recording the incident.' : 'Camera an ninh khu vực: Toàn bộ video ghi lại sự việc tử tế của người qua đường.'}</span>
        <span style="background:rgba(255,255,255,0.12); padding:2px 8px; border-radius:4px; font-size:0.75rem; font-weight:700;">1080p MP4</span>
      </div>
    </div>
    `;
  }

  // Case 1: Direct native/HLS stream URL"""

if old_render_video in app_code:
    app_code = app_code.replace(old_render_video, new_render_video)
    print("SUCCESS: Added local MP4 rendering support in renderModalVideoBlock.")

# 3.3 Add voteArticleQuiz function
quiz_func = """
/* ===================================================================
   INTERACTIVE ARTICLE QUIZ HANDLER
   =================================================================== */
function voteArticleQuiz(selectedOpt) {
  const isEn = (currentLanguage === 'en');
  const percentages = { 'A': '68%', 'B': '12%', 'C': '16%', 'D': '4%' };
  const options = ['A', 'B', 'C', 'D'];

  options.forEach(opt => {
    const btn = document.getElementById('quizOpt_' + opt);
    const bar = document.getElementById('quizBar_' + opt);
    const pct = document.getElementById('quizPct_' + opt);

    if (btn) {
      btn.disabled = true;
      btn.style.cursor = 'default';
      if (opt === selectedOpt) {
        btn.style.borderColor = 'var(--color-brand-primary, #54111E)';
        btn.style.background = 'rgba(84,17,30,0.06)';
        const textSpan = btn.querySelector('.quiz-opt-text');
        if (textSpan) {
          textSpan.innerHTML = textSpan.innerHTML.replace('fa-circle', 'fa-check-circle');
        }
      }
    }
    if (bar) {
      bar.style.display = 'block';
      setTimeout(() => { bar.style.width = percentages[opt]; }, 60);
    }
    if (pct) {
      pct.style.display = 'inline';
    }
  });

  const feedback = document.getElementById('quizFeedbackMessage');
  if (feedback) {
    feedback.style.display = 'block';
  }
}
window.voteArticleQuiz = voteArticleQuiz;
"""

if "function voteArticleQuiz" not in app_code:
    app_code += "\n" + quiz_func
    print("SUCCESS: Added voteArticleQuiz to js/app.js.")

with open(APP_PATH, "w", encoding="utf-8") as f:
    f.write(app_code)
print("Finished updating js/app.js.")


# =====================================================================
# 4. UPDATE JS/TRANSLATIONS.JS
# =====================================================================
print("Updating js/translations.js...")
with open(TRANS_PATH, "r", encoding="utf-8") as f:
    trans_code = f.read()

# Update VI translations
trans_code = trans_code.replace(
    'focal_badge: \'<i class="fas fa-landmark"></i> TIÊU ĐIỂM BÁO CHÍ ĐỐI NGOẠI\',',
    'focal_badge: \'<i class="fas fa-fire"></i> TIÊU ĐIỂM THỊNH HÀNH • BÀI NÓNG SỐ 1\','
)
trans_code = trans_code.replace(
    'focal_lead_title: "Lawmakers propose measures to boost development in mountainous, border regions",',
    'focal_lead_title: "Cô gái say rượu ngã gục trên ghế, bất ngờ nhận được sự giúp đỡ “đặc biệt” từ người qua đường",'
)
trans_code = trans_code.replace(
    'focal_lead_sapo: "Đại biểu Quốc hội đề xuất các giải pháp đột phá nhằm phát huy thế mạnh vùng, tăng cường liên kết và thúc đẩy phát triển kinh tế - xã hội tại các khu vực trung du, miền núi và biên giới.",',
    'focal_lead_sapo: "“Trông cô ấy tội quá”- một người qua đường chia sẻ khi kể lại khoảnh khắc bắt gặp Ngọc Mãi nằm co ro ngoài công viên và quyết định để lại tiền trong chiếc mũ của cô.",'
)
trans_code = trans_code.replace(
    'focal_lead_author: \'<i class="far fa-user"></i> Doan Thi Le An & Nhan Dan Daily\',',
    'focal_lead_author: \'<i class="far fa-user"></i> Ngọc Mãi & Ban Biên tập Hearticles\','
)
trans_code = trans_code.replace(
    'focal_lead_meta: \'<i class="far fa-clock"></i> 5 min read • Báo Nhân Dân\',',
    'focal_lead_meta: \'<i class="far fa-clock"></i> 5 phút đọc • Threads & Hearticles\','
)

# Update VI category spotlight in translations
trans_code = trans_code.replace(
    'cat_feat_trending_kicker: "TIÊU ĐIỂM CHUYÊN MỤC · BÀI 4 TRENDING",',
    'cat_feat_trending_kicker: "TIÊU ĐIỂM BÁO NÓNG · TOP 1 THỊNH HÀNH",'
)
trans_code = trans_code.replace(
    'cat_feat_trending_title: "Gánh mưu sinh: Hồn cốt bình dị trên từng góc phố cổ Hội An",',
    'cat_feat_trending_title: "Cô gái say rượu ngã gục trên ghế, bất ngờ nhận được sự giúp đỡ “đặc biệt” từ người qua đường",'
)
trans_code = trans_code.replace(
    'cat_feat_trending_excerpt: "Hình ảnh đôi quang gánh trĩu nặng nhịp sống mưu sinh, vẻ đẹp cần lao mộc mạc và ký ức di sản rêu phong qua từng con ngõ cổ dưới góc nhìn báo chí VnExpress.",',
    'cat_feat_trending_excerpt: "“Trông cô ấy tội quá”- một người qua đường chia sẻ khi kể lại khoảnh khắc bắt gặp Ngọc Mãi nằm co ro ngoài công viên và quyết định để lại tiền trong chiếc mũ của cô.",'
)

# Update EN translations
trans_code = trans_code.replace(
    'focal_badge: \'<i class="fas fa-landmark"></i> FOREIGN DIPLOMACY SPOTLIGHT\',',
    'focal_badge: \'<i class="fas fa-fire"></i> TRENDING SPOTLIGHT • TOP 1 VIRAL STORY\','
)
# For EN focal_lead_title:
trans_code = re.sub(
    r'focal_lead_title:\s*"Lawmakers propose measures to boost development in mountainous, border regions",\s*focal_lead_sapo:\s*"National Assembly deputies proposed breakthrough measures to capitalise on regional strengths, strengthen connectivity and promote socio-economic development in midland, mountainous and border areas during discussions on the 2026 socio-economic development and state budget plans\.",\s*focal_lead_author:\s*\'<i class="far fa-user"></i> Doan Thi Le An & Nhan Dan Daily\',\s*focal_lead_meta:\s*\'<i class="far fa-clock"></i> 5 min read • Nhan Dan Daily\',',
    '''focal_lead_title: "Drunk Girl Collapses on Park Bench, Unexpectedly Receives 'Special' Kindness from Strangers",
    focal_lead_sapo: "'She looked so pitiful,' a passerby recalled discovering Ngoc Mai curled up on a park bench and deciding to leave small change in her fallen cap.",
    focal_lead_author: '<i class="far fa-user"></i> Ngoc Mai & Hearticles Editorial',
    focal_lead_meta: '<i class="far fa-clock"></i> 5 min read • Threads & Hearticles',''',
    trans_code
)

trans_code = trans_code.replace(
    'cat_feat_trending_kicker: "CATEGORY SPOTLIGHT · ARTICLE 4 TRENDING",',
    'cat_feat_trending_kicker: "HOT PAPER · TOP 1 TRENDING SPOTLIGHT",'
)
trans_code = trans_code.replace(
    'cat_feat_trending_title: "Street Vendors: The Gentle Soul Across Hoi An Ancient Alleys",',
    'cat_feat_trending_title: "Drunk Girl Collapses on Park Bench, Unexpectedly Receives \'Special\' Kindness from Strangers",'
)
trans_code = trans_code.replace(
    'cat_feat_trending_excerpt: "The heavy carrying poles bearing daily livelihoods, rustic labor beauty, and mossy heritage memories across ancient alleys portrayed through VnExpress journalism.",',
    'cat_feat_trending_excerpt: "\'She looked so pitiful,\' a passerby recalled discovering Ngoc Mai curled up on a park bench and deciding to leave small change in her fallen cap.",'
)

with open(TRANS_PATH, "w", encoding="utf-8") as f:
    f.write(trans_code)
print("SUCCESS: Updated js/translations.js with bilingual Hot Paper titles and sapos.")


# =====================================================================
# 5. UPDATE INDEX.HTML (Hero Center Top Post)
# =====================================================================
print("Updating index.html...")
with open(INDEX_PATH, "r", encoding="utf-8") as f:
    index_html = f.read()

# Update image and alt in hero-center-top-post
index_html = index_html.replace(
    'src="assets/images/trending/lawmakers_lead.jpg" alt="Quốc hội thảo luận vùng biên giới"',
    'src="assets/images/trending/ngoc_mai/hat_and_jacket.jpg" alt="Cô gái say rượu ngã gục trên ghế đá và lòng tốt của người qua đường"'
)

# Update text inside index.html for default display
index_html = re.sub(
    r'<h1 class="center-post-title" data-i18n="focal_lead_title">[\s\S]*?</h1>',
    """<h1 class="center-post-title" data-i18n="focal_lead_title">
              Drunk Girl Collapses on Park Bench, Unexpectedly Receives 'Special' Kindness from Strangers
            </h1>""",
    index_html
)

index_html = re.sub(
    r'<p class="center-post-sapo" data-i18n="focal_lead_sapo">[\s\S]*?</p>',
    """<p class="center-post-sapo" data-i18n="focal_lead_sapo">
              'She looked so pitiful,' a passerby recalled discovering Ngoc Mai curled up on a park bench and deciding to leave small change in her fallen cap.
            </p>""",
    index_html
)

index_html = re.sub(
    r'<span class="center-post-author" data-i18n="focal_lead_author">[\s\S]*?</span>',
    """<span class="center-post-author" data-i18n="focal_lead_author"><i class="far fa-user"></i> Ngoc Mai &amp; Hearticles Editorial</span>""",
    index_html
)

index_html = re.sub(
    r'<span class="center-post-time" data-i18n="focal_lead_meta">[\s\S]*?</span>',
    """<span class="center-post-time" data-i18n="focal_lead_meta"><i class="far fa-clock"></i> 5 min read • Threads &amp; Hearticles</span>""",
    index_html
)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(index_html)
print("SUCCESS: Updated index.html hero post.")


# =====================================================================
# 6. UPDATE TRENDING.HTML (Category Featured Card)
# =====================================================================
print("Updating trending.html...")
with open(TRENDING_PATH, "r", encoding="utf-8") as f:
    trending_html = f.read()

# Point featured card to trending-1
trending_html = trending_html.replace(
    '<article class="category-featured-card" onclick="openArticleModal(\'trending-4\')">',
    '<article class="category-featured-card" onclick="openArticleModal(\'trending-1\')">'
)

trending_html = trending_html.replace(
    'src="assets/images/trending/image8.jpg" alt="Gánh mưu sinh Hội An dưới mưa"',
    'src="assets/images/trending/ngoc_mai/hat_and_jacket.jpg" alt="Cô gái say rượu ngã gục trên ghế đá và lòng tốt của người qua đường"'
)

trending_html = re.sub(
    r'<span class="category-featured-kicker" data-i18n="cat_feat_trending_kicker">[\s\S]*?</span>',
    """<span class="category-featured-kicker" data-i18n="cat_feat_trending_kicker">HOT PAPER · TOP 1 TRENDING SPOTLIGHT</span>""",
    trending_html
)

trending_html = re.sub(
    r'<h2 class="category-featured-title" data-i18n="cat_feat_trending_title">[\s\S]*?</h2>',
    """<h2 class="category-featured-title" data-i18n="cat_feat_trending_title">Drunk Girl Collapses on Park Bench, Unexpectedly Receives 'Special' Kindness from Strangers</h2>""",
    trending_html
)

trending_html = re.sub(
    r'<p class="category-featured-excerpt" data-i18n="cat_feat_trending_excerpt">[\s\S]*?</p>',
    """<p class="category-featured-excerpt" data-i18n="cat_feat_trending_excerpt">
          'She looked so pitiful,' a passerby recalled discovering Ngoc Mai curled up on a park bench and deciding to leave small change in her fallen cap.
        </p>""",
    trending_html
)

with open(TRENDING_PATH, "w", encoding="utf-8") as f:
    f.write(trending_html)
print("SUCCESS: Updated trending.html category spotlight card.")

print("\nALL UPDATES COMPLETED SUCCESSFULLY!")
