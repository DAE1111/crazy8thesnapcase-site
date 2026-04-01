import streamlit as st
import base64
import random
import os
import streamlit.components.v1 as components

# ============================================================
#  STEP 1 — BASIC INFO
# ============================================================

ARTIST_NAME   = ""
TAGLINE       = ""
PAGE_ICON     = "🎵"
LOGO_FILE     = ""
BG_FILE       = ""

# ============================================================
#  STEP 2 — COLORS
# ============================================================

TEXT_COLOR    = "#13D842"
BG_COLOR      = "#000000"

# ============================================================
#  STEP 3 — NAVIGATION LABELS
# ============================================================

NAV_HOME      = "Home"
NAV_MUSIC     = "Discography"
NAV_STORE     = "Store"

# ============================================================
#  STEP 4 — HOME PAGE
# ============================================================

BIO = """
Crazy8 The Snap Case is an artist who defies definition. Hailing from the depths of Arkansas, he is a raw and unrelenting force, a lyricist, producer, and sonic architect who crafts music that lives in the shadows. His sound pulls from the darkest corners of horrorcore and phonk, painting vivid portraits of street life, the occult, and the chaos that lurks beneath the surface of everyday America. Unapologetic and unbothered, Crazy8 operates on his own frequency, every bar razor sharp, every beat a descent into something darker. As a co-founder of Hellbound Disciplez, he helped build one of the underground's most uncompromising acts, but make no mistake, Crazy8 The Snap Case is a force all his own.
"""

LOCATION = ""
SPOTIFY_LINK = ""

# ============================================================
#  STEP 5 — DISCOGRAPHY
# ============================================================

ALBUMS = [
    {"title": "SULFER SPRINGS", "year": 2025, "tracks": 9, "url": "https://open.spotify.com/album/3VmKb3ybKs54iKWdfjdzOd"},
]

MIXTAPES = []
EPS = []

SINGLES = [
    {"title": "MARRIED TO THE SAW",                         "year": 2025, "url": "https://open.spotify.com/album/5TLKqKKoQxrVyMOi91M1Rg"},
    {"title": "ITZANE",                                     "year": 2025, "url": "https://open.spotify.com/album/7n662yTYYjHTskRh8NgO4n"},
    {"title": "CADILLACA$$",                                "year": 2025, "url": "https://open.spotify.com/album/4AnG3SNYvMblkSPI8l4nRc"},
    {"title": "HYPHY",                                      "year": 2025, "url": "https://open.spotify.com/album/1d9I5fkCzMpq3BvYS837xZ"},
    {"title": "LOADED UP",                                  "year": 2025, "url": "https://open.spotify.com/album/18Odgxh1dNFTj5mImfhO9d"},
    {"title": "WHAS HAPNIN",                                "year": 2025, "url": "https://open.spotify.com/album/5xGamZOOgQAXQgkvYyz0i8"},
    {"title": "MY SHXT BANGS",                              "year": 2025, "url": "https://open.spotify.com/album/0VGQ94N3TinogyxsRspfq6"},
    {"title": "MR. PUSHA",                                  "year": 2025, "url": "https://open.spotify.com/album/3iakwqCPKIbwL8MPBGkOim"},
    {"title": "BUSY",                                       "year": 2025, "url": "https://open.spotify.com/album/5ZFf0VQ6jo7hMzx8R2DK0Y"},
    {"title": "FLATLINE (SLOWED AND CHOPPED BY YEDVA)",     "year": 2025, "url": "https://open.spotify.com/album/7t4hNGIklRzCPg9QPT7vih"},
    {"title": "THE ONE (SLOWED AND CHOPPED BY KRYPTID)",    "year": 2025, "url": "https://open.spotify.com/album/0aRslcKzTRSqF13t9QWdDQ"},
    {"title": "THE ONE",                                    "year": 2025, "url": "https://open.spotify.com/album/5H0nvmEdlzEghN1DkX6eVH"},
    {"title": "FLATLINE",                                   "year": 2025, "url": "https://open.spotify.com/album/6N109YWEKxB4fvn3lAQRql"},
    {"title": "BANGIN ON THA TRACK",                        "year": 2025, "url": "https://open.spotify.com/album/67f7V3jNlF7nx4E7CAAkpF"},
    {"title": "GRAB THA GAUGE",                             "year": 2025, "url": "https://open.spotify.com/album/2JPQops840z6Oyh4Cx0FuM"},
    {"title": "DIE",                                        "year": 2025, "url": "https://open.spotify.com/album/3zBL1fsFLMp747vo7FHguN"},
    {"title": "CHAINSAW WHIP",                              "year": 2025, "url": "https://open.spotify.com/album/3HtZxDuejErRzQIVP9qOwm"},
    {"title": "REBEL",                                      "year": 2025, "url": "https://open.spotify.com/album/0wkjsatfathTXkihOAb2VX"},
    {"title": "GET MONEY",                                  "year": 2025, "url": "https://open.spotify.com/album/75mJW5sPQibh9rzlj3tgPS"},
    {"title": "IN MUH SHXT",                                "year": 2024, "url": "https://open.spotify.com/album/041bTZrbDgS1MmpNu5bmem"},
    {"title": "SNAPCASE",                                   "year": 2024, "url": "https://open.spotify.com/album/0i8937Xjizz9gWgERGZb5z"},
    {"title": "MR. HEAD BUSSA (OSOMANE PHONK REMIX)",       "year": 2024, "url": "https://open.spotify.com/album/1Ma6ldla8rQ96OgNf73yVA"},
    {"title": "MR. HEAD BUSSA",                             "year": 2023, "url": "https://open.spotify.com/album/6hJInkHw6JYSecAqO4jX5V"},
]

# ============================================================
#  APP — Nothing below this line needs to be edited
# ============================================================

def load_asset(filename):
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return None

font_warsuck    = load_asset("Warsuck.ttf")
cr8_bg          = load_asset("CR8_BACKGROUND.png")
cr8_logo        = load_asset("CR8_LOGO.png")
skull_break_b64 = load_asset("SKULL_BREAK.png")
cr8_bio_img     = load_asset("CR8_BIO_.jpg")
audio_static    = load_asset("Old TV static.mp3")
audio_click     = load_asset("CLICK.mp3")
audio_static1   = load_asset("static_sound1.mp3")
audio_music     = load_asset("CR8 WEB MUSIC1.mp3")

font_face_css = ""
if font_warsuck:
    font_face_css = f"""
    @font-face {{
        font-family: 'Warsuck';
        src: url('data:font/ttf;base64,{font_warsuck}') format('truetype');
    }}"""

bg_css = f"url('data:image/png;base64,{cr8_bg}')" if cr8_bg else BG_COLOR

st.set_page_config(page_title=ARTIST_NAME or "Artist Site", page_icon=PAGE_ICON, layout="wide")

st.markdown(f"""
<style>
    {font_face_css}
    .stApp {{
        background-image: {bg_css};
        background-size: 100% 100%;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center center;
        color: {TEXT_COLOR};
    }}
    [data-testid="stSidebar"] {{
        background-image: {bg_css};
        background-size: 100% 100%;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center center;
        border-right: 2px solid {TEXT_COLOR};
    }}
    h1,h2,h3,h4,h5,h6,p,label,.stRadio label {{
        color: {TEXT_COLOR} !important;
        font-family: 'Times New Roman', Times, serif;
        font-weight: bold;
        font-size: 28px !important;
        text-shadow: -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff, 1px 1px 0 #fff;
    }}
    h1,h2,h3,h4,h5,h6 {{
        font-family: 'Warsuck', serif !important;
        font-size: 48px !important;
        letter-spacing: 4px;
        text-shadow: -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff, 1px 1px 0 #fff, 0 0 10px {TEXT_COLOR};
    }}
    [data-testid="stMain"] p,
    [data-testid="stMain"] li,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] li,
    [data-testid="stSidebar"] label {{
        font-size: 28px !important;
        text-shadow: -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff, 1px 1px 0 #fff;
    }}
    hr {{ border-color: {TEXT_COLOR}; }}
    img {{ display: block; margin: auto; }}
    * {{ cursor: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3Cpolygon points='2,2 2,20 8,14 12,22 15,21 11,13 20,13' fill='%2313D842' stroke='%23000' stroke-width='1.5'/%3E%3C/svg%3E") 2 2, auto !important; }}
    .disc-link {{ text-align: center; }}
    .disc-link a {{
        color: {TEXT_COLOR};
        text-decoration: none;
        font-family: 'Times New Roman', Times, serif;
        font-weight: bold;
        font-size: 1.05rem;
        transition: color 0.2s ease, text-shadow 0.2s ease;
    }}
    .disc-link a:hover {{
        color: #ffffff;
        text-shadow: 0 0 10px {TEXT_COLOR}, 0 0 20px {TEXT_COLOR};
    }}
    .disc-year {{
        color: {TEXT_COLOR};
        opacity: 0.6;
        font-size: 0.9rem;
        margin-left: 0.5rem;
    }}
</style>
""", unsafe_allow_html=True)

# ---- Nav hint ----
st.markdown("""
<style>
@keyframes cr8NavPulse {
  0%,100% { opacity:1; transform:translateX(0); box-shadow:0 0 8px rgba(19,216,66,0.4); }
  50%      { opacity:0.6; transform:translateX(4px); box-shadow:0 0 16px rgba(19,216,66,0.7); }
}
#cr8-nav-hint {
  position:fixed; top:70px; left:8px; z-index:9999;
  display:flex; align-items:center; gap:6px;
  background:rgba(0,0,0,0.82);
  border:1px solid #13D842;
  border-radius:4px;
  padding:6px 12px;
  animation:cr8NavPulse 2s ease-in-out infinite;
  pointer-events:none;
}
#cr8-nav-hint .nh-text {
  font-family:'Times New Roman',Times,serif;
  font-weight:bold;
  font-size:11px;
  color:#13D842;
  letter-spacing:1px;
  white-space:normal;
  word-break:break-word;
  width:72px;
  text-align:center;
  line-height:1.4;
  text-shadow:0 0 6px #13D842;
}
</style>
<div id="cr8-nav-hint">
  <span class="nh-text">TAP THE ARROW TO NAVIGATE</span>
</div>
""", unsafe_allow_html=True)


# ---- TV Loading Screen ----
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');
#cr8-wrap {{
  position:fixed; top:0; left:0;
  width:100vw; height:100vh;
  background:#000;
  z-index:2147483647;
  display:flex; align-items:center; justify-content:center;
  overflow:hidden;
}}
#tv-body {{
  position:relative;
  width:100vw; height:100vh;
  background:linear-gradient(180deg,#001a00 0%,#000 40%,#001500 100%);
  display:flex; align-items:center; justify-content:center;
  padding:5vh 8vw;
}}
#tv-body::before {{
  content:'';
  position:absolute; top:0; left:0; right:0; height:4vh;
  background:linear-gradient(90deg,#001800,#002a00,#001800,#002a00,#001800);
}}
#tv-body::after {{
  content:'';
  position:absolute; bottom:0; left:0; right:0; height:4vh;
  background:linear-gradient(90deg,#001800,#002a00,#001800,#002a00,#001800);
}}
#tv-screen-bezel {{
  position:relative;
  width:100%; height:100%;
  background:#0d0d0d;
  border-radius:12px;
  box-shadow:inset 0 0 0 8px #111,inset 0 0 0 14px #1a1a1a,inset 0 0 40px rgba(0,0,0,0.95);
  overflow:hidden;
}}
#tv-screen-bezel::before {{
  content:'';
  position:absolute; top:0; left:0; right:0; bottom:0;
  background:radial-gradient(ellipse at center,transparent 60%,rgba(0,0,0,0.5) 100%);
  z-index:4; pointer-events:none; border-radius:12px;
}}
#cr8-canvas {{
  position:absolute; top:0; left:0;
  width:100%; height:100%;
  display:block;
  filter:brightness(1.1) contrast(1.1);
}}
#cr8-scanlines {{
  position:absolute; top:0; left:0; width:100%; height:100%;
  background:repeating-linear-gradient(0deg,rgba(0,0,0,0.28) 0px,rgba(0,0,0,0.28) 1px,transparent 1px,transparent 3px);
  pointer-events:none; z-index:2;
}}
#cr8-glare {{
  position:absolute; top:-10%; left:-5%;
  width:55%; height:55%;
  background:radial-gradient(ellipse,rgba(255,255,255,0.06) 0%,transparent 65%);
  pointer-events:none; z-index:3; border-radius:50%; transform:rotate(-20deg);
}}
#side-panel {{
  position:absolute; right:0; top:0; bottom:0; width:7vw;
  background:linear-gradient(180deg,#001500,#000,#001500);
  display:flex; flex-direction:column;
  align-items:center; justify-content:center; gap:2vh;
  border-left:2px solid #0a0a0a;
}}
#knob-big {{
  width:3.5vw; height:3.5vw;
  background:radial-gradient(circle at 30% 30%,#555,#1a1a1a);
  border-radius:50%;
  box-shadow:0 3px 8px rgba(0,0,0,0.9),inset 0 1px 2px rgba(255,255,255,0.1);
  position:relative;
  cursor:pointer;
  transition:transform 0.15s ease;
}}
#knob-big::after {{
  content:''; position:absolute; top:50%; left:50%;
  width:20%; height:45%; background:#333;
  transform:translate(-50%,-90%); border-radius:2px;
}}
#knob-small {{
  width:2.2vw; height:2.2vw;
  background:radial-gradient(circle at 30% 30%,#444,#111);
  border-radius:50%;
  box-shadow:0 2px 6px rgba(0,0,0,0.9);
  cursor:pointer;
  transition:transform 0.15s ease;
}}
#power-light {{
  width:0.6vw; height:0.6vw;
  background:#13D842; border-radius:50%;
  box-shadow:0 0 6px #13D842,0 0 12px #13D842;
  margin-top:1vh;
}}
@media (max-width:768px) {{
  #cr8-wrap {{
    background:#000 !important;
    align-items:center !important;
    justify-content:center !important;
  }}
  #tv-body {{
    width:100vw !important;
    height:auto !important;
    aspect-ratio:4/3 !important;
    max-height:75vh !important;
    padding:3vh 3vw !important;
    border-radius:8px !important;
  }}
  #side-panel {{
    display:none !important;
  }}
  #tv-body::before {{ height:5% !important; }}
  #tv-body::after  {{ height:5% !important; }}
  #tv-screen-bezel {{ border-radius:6px !important; }}
  #cr8-play-btn {{
    font-size:7vw !important;
    padding:2vh 6vw !important;
    letter-spacing:4px !important;
  }}
  #cr8-txt  {{ font-size:7vw !important; }}
  #cr8-btn  {{ font-size:5.5vw !important; padding:1.5vh 6vw !important; }}
}}
.knob-label {{
  font-family:'Times New Roman',serif;
  font-size:0.65vw; color:#444;
  letter-spacing:1px; text-transform:uppercase;
}}
.txt-mobile  {{ display:none; }}
.txt-desktop {{ display:inline; }}
@media (max-width:768px) {{
  .txt-mobile  {{ display:inline; }}
  .txt-desktop {{ display:none; }}
}}
#cr8-play-btn {{
  position:absolute; top:50%; left:50%;
  transform:translate(-50%,-50%); z-index:6;
  font-family:'VT323', monospace;
  font-size:5vw;
  color:#13D842; background:rgba(0,0,0,0.85);
  border:3px solid #13D842;
  padding:2vh 5vw; letter-spacing:8px;
  cursor:pointer; white-space:nowrap;
  text-shadow:0 0 20px #13D842,0 0 40px #13D842;
  animation:playpulse 1.2s ease-in-out infinite;
}}
@keyframes playpulse {{
  0%,100% {{ box-shadow:0 0 20px rgba(19,216,66,0.5),0 0 60px rgba(19,216,66,0.2); letter-spacing:8px; }}
  50%      {{ box-shadow:0 0 50px rgba(19,216,66,0.9),0 0 100px rgba(19,216,66,0.4); letter-spacing:12px; }}
}}
#cr8-txt {{
  position:absolute; top:50%; left:50%;
  transform:translate(-50%,-50%);
  text-align:center; z-index:5; width:90%;
  font-family:'VT323', monospace;
  font-size:5vw; color:#00CFFF; letter-spacing:8px;
  text-shadow:0 0 4px #00CFFF,0 0 12px #00CFFF,0 0 30px #0088ff,0 0 40px #13D842,2px 2px 0px rgba(255,0,200,0.4);
  background:rgba(15,15,15,0.80);
  padding:1.5vh 4vw; border-radius:4px;
  animation:cr8flicker 0.15s steps(1,end) infinite;
}}
#cr8-btn {{
  display:none;
  position:absolute; top:50%; left:50%;
  transform:translate(-50%,-50%); z-index:5;
  font-family:'VT323', monospace;
  font-size:3vw; color:#00CFFF; background:rgba(0,0,0,0.75);
  border:2px solid #00CFFF;
  padding:1vh 3vw; letter-spacing:6px;
  cursor:pointer; white-space:nowrap;
  text-shadow:0 0 8px #00CFFF,0 0 20px #0088ff;
  box-shadow:0 0 14px #00CFFF,inset 0 0 10px rgba(0,180,255,0.1);
}}
@keyframes cr8pulse {{
  0%,100% {{ box-shadow:0 0 10px #13D842,0 0 20px #13D842; }}
  50%      {{ box-shadow:0 0 30px #13D842,0 0 60px #13D842; }}
}}
@keyframes cr8flicker {{
  0%,89%,100% {{ opacity:1; }} 90% {{ opacity:0.3; }} 95% {{ opacity:0.8; }}
}}
</style>

<div id="cr8-wrap">
  <div id="tv-body">
    <div id="tv-screen-bezel">
      <canvas id="cr8-canvas"></canvas>
      <div id="cr8-scanlines"></div>
      <div id="cr8-glare"></div>
      <button id="cr8-play-btn">&#9654; CLICK TO PLAY</button>
      <div id="cr8-txt" style="display:none;"><span class="txt-desktop">&#9646;&#9646; LOADING &#9646;&#9646;</span><span class="txt-mobile">LOADING</span></div>
      <button id="cr8-btn">&#9654; ENTER SITE</button>
    </div>
    <div id="side-panel">
      <span class="knob-label">CH</span>
      <div id="knob-big"></div>
      <span class="knob-label">VOL</span>
      <div id="knob-small"></div>
      <div id="power-light"></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

components.html(f"""
<script>
(function() {{
  var doc = window.parent.document;
  var canvas = doc.getElementById('cr8-canvas');
  var bezel  = doc.getElementById('tv-screen-bezel');
  var ctx    = canvas.getContext('2d');

  function resize() {{
    canvas.width  = bezel.offsetWidth  || window.parent.innerWidth  * 0.85;
    canvas.height = bezel.offsetHeight || window.parent.innerHeight * 0.85;
  }}
  resize();
  window.parent.addEventListener('resize', resize);

  var lo = document.createElement('canvas');
  var lc = lo.getContext('2d');
  var frame = 0;

  function drawStatic() {{
    frame++;
    if (frame % 2 === 0) {{
      lo.width  = Math.max(1, Math.floor(canvas.width  / 2));
      lo.height = Math.max(1, Math.floor(canvas.height / 2));
      var w = lo.width, h = lo.height;
      var img = lc.createImageData(w, h);
      var d = img.data;
      for (var row = 0; row < h; row++) {{
        var rowShift = (Math.random() - 0.5) * 30;
        var glitch   = Math.random() < 0.018;
        var dropout  = Math.random() < 0.01;
        for (var col = 0; col < w; col++) {{
          var idx = (row * w + col) * 4;
          var v;
          if (glitch) {{
            v = 210 + (Math.random() * 45)|0;
          }} else if (dropout) {{
            v = (Math.random() * 15)|0;
          }} else {{
            var g = Math.random() + Math.random() + Math.random() + Math.random();
            v = Math.max(0, Math.min(255, ((g / 4) * 255 + rowShift)|0));
          }}
          d[idx] = d[idx+1] = d[idx+2] = v;
          d[idx+3] = 255;
        }}
      }}
      if (Math.random() < 0.04) {{
        var by = (Math.random() * h)|0;
        var bh = 1 + (Math.random() * 2)|0;
        for (var r = by; r < Math.min(h, by+bh); r++) {{
          for (var c = 0; c < w; c++) {{
            var bi = (r * w + c) * 4;
            d[bi] = d[bi+1] = d[bi+2] = (Math.random() * 30)|0;
            d[bi+3] = 255;
          }}
        }}
      }}
      lc.putImageData(img, 0, 0);
      ctx.imageSmoothingEnabled = false;
      ctx.drawImage(lo, 0, 0, canvas.width, canvas.height);
    }}
    requestAnimationFrame(drawStatic);
  }}
  drawStatic();

  var staticEl  = new Audio("data:audio/mp3;base64,{audio_static}");
  var staticEl2 = new Audio("data:audio/mp3;base64,{audio_static}");
  var staticEl3 = new Audio("data:audio/mp3;base64,{audio_static}");
  var staticEl4 = new Audio("data:audio/mp3;base64,{audio_static}");
  var staticEl5 = new Audio("data:audio/mp3;base64,{audio_static}");
  [staticEl,staticEl2,staticEl3,staticEl4,staticEl5].forEach(function(s) {{ s.loop = true; s.volume = 1.0; }});

  var musicSnd = new Audio("data:audio/mp3;base64,{audio_music}");
  musicSnd.loop   = false;
  musicSnd.volume = 0.36;

  doc.addEventListener('visibilitychange', function() {{
    if (doc.hidden) {{
      if (!musicSnd.paused) musicSnd.pause();
    }} else {{
      if (musicSnd.paused && musicSnd.currentTime > 0) musicSnd.play().catch(function(){{}});
    }}
  }});

  var knobAngles = {{'knob-big': 0, 'knob-small': 0}};
  ['knob-big', 'knob-small'].forEach(function(id) {{
    var knob = doc.getElementById(id);
    if (!knob) return;
    knob.addEventListener('click', function() {{
      knobAngles[id] = (knobAngles[id] + 45) % 360;
      knob.style.transform = 'rotate(' + knobAngles[id] + 'deg)';
      var s = new Audio("data:audio/mp3;base64,{audio_click}");
      s.volume = 0.5; s.play().catch(function(){{}});
    }});
  }});

  var playBtn = doc.getElementById('cr8-play-btn');
  var txt     = doc.getElementById('cr8-txt');
  var btn     = doc.getElementById('cr8-btn');

  if (playBtn) {{
    playBtn.onclick = function() {{
      [staticEl, staticEl2, staticEl3, staticEl4, staticEl5].forEach(function(s) {{
        s.currentTime = 0;
        s.play().catch(function(){{}});
      }});
      playBtn.style.transition = 'opacity 0.5s ease';
      playBtn.style.opacity = '0';
      setTimeout(function() {{
        playBtn.style.display = 'none';
        if (txt) txt.style.display = 'block';
      }}, 500);

      setTimeout(function() {{
        if (txt) txt.style.display = 'none';
        if (btn) {{
          btn.style.display = 'block';
          btn.style.animation = 'cr8pulse 1.8s ease-in-out infinite';
          btn.onclick = function() {{
            [staticEl, staticEl2, staticEl3, staticEl4, staticEl5].forEach(function(s) {{ s.pause(); s.currentTime = 0; }});
            musicSnd.play().catch(function() {{}});
            var wrap = doc.getElementById('cr8-wrap');
            if (wrap) {{
              wrap.style.transition = 'opacity 1s ease';
              wrap.style.opacity = '0';
              setTimeout(function() {{ wrap.style.display = 'none'; }}, 1000);
            }}
          }};
        }}
      }}, 7000);
    }};
  }}
}})();
</script>
""", height=0)


# ---- Logo ----
if cr8_logo:
    st.markdown('''<style>
.cr8logo-wrap { display:flex; justify-content:center; align-items:center; width:100%; margin:0; padding:0; }
.cr8logo-wrap img { width:1137px; max-width:90vw; opacity:0.50; display:block; height:auto; }
</style>''', unsafe_allow_html=True)
    st.markdown(f'<div class="cr8logo-wrap"><img src="data:image/png;base64,{cr8_logo}"></div>', unsafe_allow_html=True)
elif ARTIST_NAME:
    st.markdown(f'<div style="text-align:center;"><h1>{ARTIST_NAME}</h1></div>', unsafe_allow_html=True)

if TAGLINE:
    st.subheader(TAGLINE)
st.markdown("---")

# ---- Sidebar ----
with st.sidebar:
    st.header("MENU")
    menu = st.radio("", [NAV_HOME, NAV_MUSIC, NAV_STORE])

# ---- Click sound + VCR wave glitch effect ----
components.html(f"""
<script>
(function() {{
  var doc = window.parent.document;
  var clickSnd = new Audio("data:audio/mp3;base64,{audio_click}");
  clickSnd.volume = 0.49;

  if (!doc.getElementById('cr8-glitch-style')) {{
    var st = doc.createElement('style');
    st.id = 'cr8-glitch-style';
    st.textContent = `
      @keyframes cr8wave {{
        0%   {{ transform:translate(0,0) skewX(0deg); filter:brightness(0.35); }}
        25%  {{ transform:translate(-4px,0) skewX(-2deg); filter:brightness(0.25) hue-rotate(90deg) saturate(3); }}
        50%  {{ transform:translate(4px,0) skewX(2deg); filter:brightness(0.28) hue-rotate(200deg) saturate(3); }}
        75%  {{ transform:translate(-2px,0) skewX(-1deg); filter:brightness(0.22) hue-rotate(300deg) saturate(2); }}
        100% {{ transform:translate(0,0) skewX(0deg); filter:brightness(1); }}
      }}
      @keyframes cr8rgbR {{
        0%   {{ opacity:0; transform:translateX(0); }}
        30%  {{ opacity:0.4; transform:translateX(-5px); }}
        70%  {{ opacity:0.3; transform:translateX(3px); }}
        100% {{ opacity:0; transform:translateX(0); }}
      }}
      @keyframes cr8rgbB {{
        0%   {{ opacity:0; transform:translateX(0); }}
        30%  {{ opacity:0.4; transform:translateX(5px); }}
        70%  {{ opacity:0.3; transform:translateX(-3px); }}
        100% {{ opacity:0; transform:translateX(0); }}
      }}
      .cr8-waving {{
        animation: cr8wave 0.7s ease-in-out forwards !important;
      }}
      #cr8-rgb-r {{
        position:fixed; top:0; left:0; width:100vw; height:100vh;
        background:rgba(255,0,0,0.18);
        pointer-events:none; z-index:999997; display:none;
        mix-blend-mode:screen;
      }}
      #cr8-rgb-b {{
        position:fixed; top:0; left:0; width:100vw; height:100vh;
        background:rgba(0,100,255,0.18);
        pointer-events:none; z-index:999997; display:none;
        mix-blend-mode:screen;
      }}
      #cr8-rgb-r.active {{ display:block; animation:cr8rgbR 0.7s ease-in-out forwards; }}
      #cr8-rgb-b.active {{ display:block; animation:cr8rgbB 0.7s ease-in-out forwards; }}
    `;
    doc.head.appendChild(st);

    var rgbR = doc.createElement('div'); rgbR.id = 'cr8-rgb-r'; doc.body.appendChild(rgbR);
    var rgbB = doc.createElement('div'); rgbB.id = 'cr8-rgb-b'; doc.body.appendChild(rgbB);
  }}

  function triggerGlitch() {{
    var app  = doc.querySelector('.stApp');
    var rgbR = doc.getElementById('cr8-rgb-r');
    var rgbB = doc.getElementById('cr8-rgb-b');
    if (app) {{
      app.classList.remove('cr8-waving');
      void app.offsetWidth;
      app.classList.add('cr8-waving');
      setTimeout(function() {{ app.classList.remove('cr8-waving'); }}, 720);
    }}
    if (rgbR) {{
      rgbR.classList.remove('active'); void rgbR.offsetWidth; rgbR.classList.add('active');
      setTimeout(function() {{ rgbR.classList.remove('active'); }}, 720);
    }}
    if (rgbB) {{
      rgbB.classList.remove('active'); void rgbB.offsetWidth; rgbB.classList.add('active');
      setTimeout(function() {{ rgbB.classList.remove('active'); }}, 720);
    }}
  }}

  function playClick() {{
    var s = clickSnd.cloneNode();
    s.volume = 0.49;
    s.play().catch(function(){{}});
  }}

  var staticClick = new Audio("data:audio/mp3;base64,{audio_static1}");
  staticClick.volume = 0.6;

  function attachSounds() {{
    var els = doc.querySelectorAll('a, button, [role="radio"], label, [role="button"]');
    els.forEach(function(el) {{
      if (!el.dataset.cr8click) {{
        el.dataset.cr8click = '1';
        el.addEventListener('click', function() {{
          playClick();
          triggerGlitch();
          var s = staticClick.cloneNode();
          s.volume = 0.6;
          s.play().catch(function(){{}});
        }});
      }}
    }});
  }}

  var siteEntered = false;
  var wrap = doc.getElementById('cr8-wrap');
  if (wrap) {{
    var observer = new MutationObserver(function() {{
      if (!siteEntered && (wrap.style.display === 'none' || parseFloat(wrap.style.opacity) === 0)) {{
        siteEntered = true;
        attachSounds();
        setInterval(attachSounds, 1500);
      }}
    }});
    observer.observe(wrap, {{ attributes:true, attributeFilter:['style'] }});
  }}
}})();
</script>
""", height=0)


# ---- Skull divider helper ----
def skull_divider():
    if skull_break_b64:
        s = (f'<img src="data:image/png;base64,{skull_break_b64}" '
             f'style="height:4rem;vertical-align:middle;display:inline-block;margin:0 1rem;">')
        st.markdown(
            f'<div style="display:flex;align-items:center;justify-content:center;margin:0.75rem 0;">'
            f'{s}{s}{s}</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown("---")

def skull_header(text):
    st.markdown(
        f'<div style="text-align:center;margin-bottom:0.25rem;">'
        f'<h2 style="font-family:Warsuck,serif;color:{TEXT_COLOR};margin:0;line-height:1;'
        f'text-shadow:-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff,1px 1px 0 #fff,0 0 10px {TEXT_COLOR};">{text}</h2>'
        f'</div>',
        unsafe_allow_html=True
    )
    skull_divider()

def skull_subheader(text):
    st.markdown(
        f'<div style="text-align:center;margin-bottom:0.25rem;">'
        f'<h3 style="font-family:Warsuck,serif;color:{TEXT_COLOR};margin:0;line-height:1;'
        f'text-shadow:-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff,1px 1px 0 #fff,0 0 10px {TEXT_COLOR};">{text}</h3>'
        f'</div>',
        unsafe_allow_html=True
    )
    skull_divider()

# ---- Pages ----

if menu == NAV_HOME:
    skull_header("WHO IS CRAZY8 THE SNAP CASE")
    bio_style = (
        'text-align:center;'
        'font-family:Times New Roman,Times,serif;'
        'font-weight:700;'
        'font-size:28px;'
        'color:' + TEXT_COLOR + ';'
        'text-shadow:-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff,1px 1px 0 #fff;'
        'line-height:1.6;'
        'max-width:860px;'
        'margin:0 auto;'
        'padding:0 20px;'
    )
    st.markdown('<div style="' + bio_style + '">' + BIO + '</div>', unsafe_allow_html=True)
    if cr8_bio_img:
        st.markdown(
            f'<div style="text-align:center;margin-top:1rem;">'
            f'<img src="data:image/jpeg;base64,{cr8_bio_img}" '
            f'style="display:block;margin:auto;max-width:455px;width:100%;" loading="lazy">'
            f'</div>',
            unsafe_allow_html=True
        )
    if LOCATION:
        skull_divider()
        st.subheader(LOCATION)

elif menu == NAV_MUSIC:
    skull_header("DISCOGRAPHY")

    if ALBUMS:
        st.markdown(f'<div style="text-align:center;"><h3 style="font-family:Warsuck,serif;color:{TEXT_COLOR};">Albums</h3></div>', unsafe_allow_html=True)
        for a in ALBUMS:
            tracks = f" — {a['tracks']} tracks" if a.get("tracks") else ""
            st.markdown(
                f'<div class="disc-link"><a href="{a["url"]}" target="_blank">{a["title"]}</a>'
                f'<span class="disc-year">({a["year"]}){tracks}</span></div>',
                unsafe_allow_html=True
            )

    if SINGLES:
        st.markdown(f'<div style="text-align:center;margin-top:1rem;"><h3 style="font-family:Warsuck,serif;color:{TEXT_COLOR};">Singles</h3></div>', unsafe_allow_html=True)
        for s in SINGLES:
            st.markdown(
                f'<div class="disc-link"><a href="{s["url"]}" target="_blank">{s["title"]}</a>'
                f'<span class="disc-year">({s["year"]})</span></div>',
                unsafe_allow_html=True
            )

    if SPOTIFY_LINK:
        st.markdown(f"🎧 [Listen on Spotify]({SPOTIFY_LINK})")

elif menu == NAV_STORE:
    skull_header("STORE")
    st.markdown(
        f'''<div style="text-align:center;margin-top:2rem;">
        <p style="font-family:'Times New Roman',serif;font-weight:bold;color:{TEXT_COLOR};font-size:1.1rem;opacity:0.7;">
        Store coming soon.</p>
        </div>''',
        unsafe_allow_html=True
    )
