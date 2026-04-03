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

TEXT_COLOR    = "#0DA832"
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
        font-size: 44px !important;
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
        text-shadow: -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff, 1px 1px 0 #fff;
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
        text-shadow: -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff, 1px 1px 0 #fff;
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
  border:1px solid #0DA832;
  border-radius:4px;
  padding:6px 12px;
  animation:cr8NavPulse 2s ease-in-out infinite;
  pointer-events:none;
}
#cr8-nav-hint .nh-text {
  font-family:'Times New Roman',Times,serif;
  font-weight:bold;
  font-size:11px;
  color:#0DA832;
  letter-spacing:1px;
  white-space:normal;
  word-break:break-word;
  width:72px;
  text-align:center;
  line-height:1.4;
  text-shadow:0 0 6px #0DA832;
}
</style>
<div id="cr8-nav-hint">
  <span class="nh-text">TAP THE ARROW TO NAVIGATE</span>
</div>
""", unsafe_allow_html=True)


# ---- Spider Web + Egg Sac Effect ----
components.html("""
<script>
(function() {
  var doc = window.parent.document;
  if (doc.getElementById('cr8-spider-init')) return;
  var marker = doc.createElement('div');
  marker.id = 'cr8-spider-init';
  marker.style.display = 'none';
  doc.body.appendChild(marker);

  var sty = doc.createElement('style');
  sty.textContent = `
    #cr8-web-canvas {
      position:fixed; top:0; right:0;
      width:280px; height:280px;
      pointer-events:none; z-index:8000;
    }
    #cr8-egg-wrap {
      position:fixed; top:0; right:0;
      width:280px; height:280px;
      pointer-events:none; z-index:8001;
    }
    #cr8-egg-sac {
      position:absolute;
      width:54px; height:66px;
      border-radius:45% 45% 52% 52%;
      cursor:pointer; pointer-events:all; overflow:hidden;
    }
    #cr8-egg-canvas {
      position:absolute; top:0; left:0;
      width:100%; height:100%;
      border-radius:45% 45% 52% 52%;
    }
    #cr8-spider-canvas {
      position:fixed; top:0; left:0;
      width:100vw; height:100vh;
      pointer-events:none; z-index:7999;
    }
    #cr8-egg-label {
      position:absolute; bottom:-22px; left:50%;
      transform:translateX(-50%);
      font-family:'Times New Roman',serif; font-weight:bold;
      font-size:10px; color:#0DA832; white-space:nowrap;
      text-shadow:0 0 6px #0DA832; pointer-events:none;
      animation:labelpulse 1.4s ease-in-out infinite;
    }
    @keyframes labelpulse { 0%,100%{opacity:1;} 50%{opacity:0.4;} }
    @keyframes sacsway {
      0%,100%{transform:rotate(-4deg);transform-origin:top center;}
      50%{transform:rotate(4deg);transform-origin:top center;}
    }
  `;
  doc.head.appendChild(sty);

  // Web canvas
  var webCanvas = doc.createElement('canvas');
  webCanvas.id = 'cr8-web-canvas';
  webCanvas.width = 280; webCanvas.height = 280;
  doc.body.appendChild(webCanvas);
  var wctx = webCanvas.getContext('2d');

  function drawWeb() {
    wctx.clearRect(0,0,280,280);
    var ox=280, oy=0, numSpokes=14, numRings=9, maxR=275;
    var spokes=[];
    for(var i=0;i<=numSpokes;i++){
      var ang=Math.PI+(i/numSpokes)*(Math.PI/2);
      spokes.push([ox+Math.cos(ang)*maxR, oy+Math.sin(ang)*maxR]);
    }
    wctx.strokeStyle='rgba(210,200,175,0.55)'; wctx.lineWidth=0.8;
    for(var i=0;i<spokes.length;i++){
      wctx.beginPath(); wctx.moveTo(ox,oy);
      wctx.lineTo(spokes[i][0],spokes[i][1]); wctx.stroke();
    }
    for(var r=1;r<=numRings;r++){
      var t=r/numRings, pts=[];
      for(var i=0;i<spokes.length;i++){
        var jit=1.0+Math.sin(i*2.3+r*1.9)*0.045;
        pts.push([ox+(spokes[i][0]-ox)*t*jit, oy+(spokes[i][1]-oy)*t*jit]);
      }
      pts.push([pts[0][0],pts[0][1]]);
      wctx.globalAlpha=0.18+(1-t)*0.5;
      wctx.lineWidth=r<=2?0.9:0.45;
      wctx.beginPath(); wctx.moveTo(pts[0][0],pts[0][1]);
      for(var i=1;i<pts.length;i++) wctx.lineTo(pts[i][0],pts[i][1]);
      wctx.stroke();
      if(r===3||r===6||r===8){
        for(var i=0;i<pts.length-1;i++){
          wctx.globalAlpha=0.25+Math.random()*0.3;
          wctx.fillStyle='rgba(200,225,255,0.7)';
          wctx.beginPath();
          wctx.arc(pts[i][0],pts[i][1],0.7+Math.random()*0.8,0,Math.PI*2);
          wctx.fill();
        }
      }
    }
    wctx.globalAlpha=1.0;
    wctx.strokeStyle='rgba(200,185,155,0.65)'; wctx.lineWidth=0.9;
    wctx.beginPath(); wctx.moveTo(226,8); wctx.lineTo(218,52); wctx.stroke();
  }
  drawWeb();

  // Egg sac
  var eggWrap=doc.createElement('div'); eggWrap.id='cr8-egg-wrap';
  doc.body.appendChild(eggWrap);
  var sacEl=doc.createElement('div'); sacEl.id='cr8-egg-sac';
  sacEl.style.cssText='left:191px;top:52px;animation:sacsway 2.8s ease-in-out infinite;';
  eggWrap.appendChild(sacEl);
  var eggCanvas=doc.createElement('canvas'); eggCanvas.id='cr8-egg-canvas';
  eggCanvas.width=54; eggCanvas.height=66;
  sacEl.appendChild(eggCanvas);
  var ectx=eggCanvas.getContext('2d');
  var label=doc.createElement('div'); label.id='cr8-egg-label';
  label.textContent='CLICK ME'; sacEl.appendChild(label);

  var babies=[];
  for(var b=0;b<22;b++){
    babies.push({
      x:12+Math.random()*30, y:12+Math.random()*42,
      vx:(Math.random()-0.5)*0.5, vy:(Math.random()-0.5)*0.5,
      r:1.8+Math.random()*2.2,
      col:Math.random()<0.5?'#1a0a00':'#0a0a0a',
      legPhase:Math.random()*Math.PI*2
    });
  }

  function animateSac(){
    eggCanvas.width=sacEl.offsetWidth||54;
    eggCanvas.height=sacEl.offsetHeight||66;
    var W=eggCanvas.width, H=eggCanvas.height;
    ectx.clearRect(0,0,W,H);
    var grad=ectx.createRadialGradient(W*0.4,H*0.3,2,W*0.5,H*0.5,W*0.7);
    grad.addColorStop(0,'#d4b896'); grad.addColorStop(0.4,'#b8956a');
    grad.addColorStop(0.7,'#8a6840'); grad.addColorStop(1,'#6a4e2a');
    ectx.beginPath(); ectx.ellipse(W/2,H/2,W/2,H/2,0,0,Math.PI*2);
    ectx.fillStyle=grad; ectx.fill();
    ectx.strokeStyle='rgba(200,175,140,0.18)'; ectx.lineWidth=0.8;
    for(var s=0;s<5;s++){
      ectx.beginPath(); ectx.moveTo(W*(0.2+s*0.15),0);
      ectx.lineTo(W*(0.1+s*0.18),H); ectx.stroke();
    }
    ectx.beginPath(); ectx.ellipse(W*0.35,H*0.28,W*0.18,H*0.1,-0.6,0,Math.PI*2);
    ectx.fillStyle='rgba(255,255,255,0.22)'; ectx.fill();
    babies.forEach(function(b){
      b.legPhase+=0.18;
      b.vx+=(Math.random()-0.5)*0.12; b.vy+=(Math.random()-0.5)*0.12;
      var spd=Math.sqrt(b.vx*b.vx+b.vy*b.vy);
      if(spd>0.6){b.vx=(b.vx/spd)*0.6;b.vy=(b.vy/spd)*0.6;}
      b.x+=b.vx; b.y+=b.vy;
      if(b.x<b.r+4){b.x=b.r+4;b.vx=Math.abs(b.vx);}
      if(b.x>W-b.r-4){b.x=W-b.r-4;b.vx=-Math.abs(b.vx);}
      if(b.y<b.r+4){b.y=b.r+4;b.vy=Math.abs(b.vy);}
      if(b.y>H-b.r-6){b.y=H-b.r-6;b.vy=-Math.abs(b.vy);}
      ectx.beginPath(); ectx.arc(b.x,b.y,b.r,0,Math.PI*2);
      ectx.fillStyle=b.col; ectx.fill();
      for(var l=0;l<8;l++){
        var baseAng=(l/8)*Math.PI*2;
        var wave=Math.sin(b.legPhase+l*0.8)*0.4;
        var ang1=baseAng+wave;
        var lx1=b.x+Math.cos(ang1)*(b.r*2.2);
        var ly1=b.y+Math.sin(ang1)*(b.r*2.2);
        var ang2=ang1+(l<4?0.5:-0.5);
        var lx2=lx1+Math.cos(ang2)*(b.r*1.8);
        var ly2=ly1+Math.sin(ang2)*(b.r*1.8);
        ectx.beginPath(); ectx.moveTo(b.x,b.y);
        ectx.lineTo(lx1,ly1); ectx.lineTo(lx2,ly2);
        ectx.strokeStyle=b.col; ectx.lineWidth=0.5; ectx.stroke();
      }
    });
    requestAnimationFrame(animateSac);
  }
  animateSac();

  // Spider canvas
  var spiderCanvas=doc.createElement('canvas'); spiderCanvas.id='cr8-spider-canvas';
  doc.body.appendChild(spiderCanvas);
  var sctx=spiderCanvas.getContext('2d');
  function resizeSC(){spiderCanvas.width=window.parent.innerWidth;spiderCanvas.height=window.parent.innerHeight;}
  resizeSC(); window.parent.addEventListener('resize',resizeSC);

  var activeSpiders=[], hatched=false;

  function Spider(sx,sy){
    this.x=sx; this.y=sy;
    this.vx=(Math.random()-0.5)*7; this.vy=(Math.random()-0.5)*7;
    this.size=3.5+Math.random()*3;
    this.angle=Math.atan2(this.vy,this.vx);
    this.life=0; this.maxLife=300+Math.random()*200;
    this.col=['#111','#1a0800','#0d0d0d','#2a1200'][Math.floor(Math.random()*4)];
    this.stepTimer=0; this.stepInterval=8+Math.floor(Math.random()*6);
    this.legs=[];
    for(var i=0;i<8;i++){
      var side=i<4?-1:1, idx=i<4?i:i-4;
      var baseAng=this.angle+side*(0.3+idx*0.22);
      var reach=this.size*(3.5+idx*0.3);
      this.legs.push({
        side:side, idx:idx,
        footX:this.x+Math.cos(baseAng)*reach,
        footY:this.y+Math.sin(baseAng)*reach,
        targetX:this.x+Math.cos(baseAng)*reach,
        targetY:this.y+Math.sin(baseAng)*reach,
        stepping:false, stepT:0, prevFootX:0, prevFootY:0
      });
    }
  }

  Spider.prototype.update=function(){
    this.life++;
    var W=spiderCanvas.width, H=spiderCanvas.height;
    this.vx+=(Math.random()-0.5)*0.35; this.vy+=(Math.random()-0.5)*0.35;
    var spd=Math.sqrt(this.vx*this.vx+this.vy*this.vy);
    if(spd>5){this.vx=(this.vx/spd)*5;this.vy=(this.vy/spd)*5;}
    if(spd<0.8){this.vx*=1.5;this.vy*=1.5;}
    this.x+=this.vx; this.y+=this.vy;
    if(this.x<10){this.x=10;this.vx=Math.abs(this.vx);}
    if(this.x>W-10){this.x=W-10;this.vx=-Math.abs(this.vx);}
    if(this.y<10){this.y=10;this.vy=Math.abs(this.vy);}
    if(this.y>H-10){this.y=H-10;this.vy=-Math.abs(this.vy);}
    this.angle=Math.atan2(this.vy,this.vx);
    this.stepTimer++;
    for(var i=0;i<8;i++){
      var leg=this.legs[i];
      var reach=this.size*(3.2+leg.idx*0.3);
      var shoulderAng=this.angle+leg.side*(0.28+leg.idx*0.22);
      var idealX=this.x+Math.cos(shoulderAng)*reach;
      var idealY=this.y+Math.sin(shoulderAng)*reach;
      var dx=idealX-leg.footX, dy=idealY-leg.footY;
      var dist=Math.sqrt(dx*dx+dy*dy);
      if(leg.stepping){
        leg.stepT+=0.2;
        var t=Math.min(leg.stepT,1);
        var et=t<0.5?2*t*t:-1+(4-2*t)*t;
        leg.footX=leg.prevFootX+(leg.targetX-leg.prevFootX)*et;
        leg.footY=leg.prevFootY+(leg.targetY-leg.prevFootY)*et-Math.sin(t*Math.PI)*this.size*1.4;
        if(t>=1){leg.stepping=false;leg.footX=leg.targetX;leg.footY=leg.targetY;}
      } else if(dist>reach*0.9&&this.stepTimer%this.stepInterval===(i*2)%this.stepInterval){
        leg.prevFootX=leg.footX; leg.prevFootY=leg.footY;
        leg.targetX=this.x+Math.cos(shoulderAng)*reach*1.5+this.vx*4;
        leg.targetY=this.y+Math.sin(shoulderAng)*reach*1.5+this.vy*4;
        leg.stepping=true; leg.stepT=0;
      }
    }
  };

  Spider.prototype.draw=function(ctx){
    var alpha=Math.max(0,1-this.life/this.maxLife);
    ctx.globalAlpha=alpha;
    var s=this.size;
    for(var i=0;i<8;i++){
      var leg=this.legs[i];
      var shoulderAng=this.angle+leg.side*(0.28+leg.idx*0.22);
      var shX=this.x+Math.cos(shoulderAng)*s*0.7;
      var shY=this.y+Math.sin(shoulderAng)*s*0.7;
      var midX=(shX+leg.footX)*0.5, midY=(shY+leg.footY)*0.5;
      var perpAng=shoulderAng+Math.PI/2;
      var kneeX=midX+Math.cos(perpAng)*s*1.4*leg.side;
      var kneeY=midY+Math.sin(perpAng)*s*1.4*leg.side;
      ctx.beginPath(); ctx.moveTo(shX,shY);
      ctx.lineTo(kneeX,kneeY); ctx.lineTo(leg.footX,leg.footY);
      ctx.strokeStyle=this.col; ctx.lineWidth=s*0.28;
      ctx.lineCap='round'; ctx.lineJoin='round'; ctx.stroke();
      ctx.beginPath(); ctx.arc(leg.footX,leg.footY,s*0.15,0,Math.PI*2);
      ctx.fillStyle=this.col; ctx.fill();
    }
    ctx.save(); ctx.translate(this.x,this.y); ctx.rotate(this.angle);
    var abdGrad=ctx.createRadialGradient(-s*0.3,-s*0.2,0,0,s*0.8,s*1.8);
    abdGrad.addColorStop(0,'#2a1a00'); abdGrad.addColorStop(1,this.col);
    ctx.beginPath(); ctx.ellipse(0,s*0.9,s*0.85,s*1.4,0,0,Math.PI*2);
    ctx.fillStyle=abdGrad; ctx.fill();
    ctx.beginPath(); ctx.ellipse(-s*0.2,s*0.4,s*0.28,s*0.18,-0.5,0,Math.PI*2);
    ctx.fillStyle='rgba(255,255,255,0.1)'; ctx.fill();
    ctx.beginPath(); ctx.ellipse(0,-s*0.15,s*0.7,s*0.6,0,0,Math.PI*2);
    ctx.fillStyle=this.col; ctx.fill();
    var eyePos=[[-s*0.38,-s*0.6],[-s*0.13,-s*0.7],[s*0.13,-s*0.7],[s*0.38,-s*0.6],
                [-s*0.25,-s*0.44],[-s*0.08,-s*0.5],[s*0.08,-s*0.5],[s*0.25,-s*0.44]];
    var eyeCol=['#cc0000','#dd3300','#cc0000','#cc0000','#fff','#fff','#fff','#fff'];
    eyePos.forEach(function(ep,ei){
      ctx.beginPath(); ctx.arc(ep[0],ep[1],s*0.1,0,Math.PI*2);
      ctx.fillStyle=eyeCol[ei]; ctx.fill();
    });
    ctx.beginPath(); ctx.moveTo(-s*0.38,-s*0.58); ctx.lineTo(-s*0.85,-s*1.0);
    ctx.strokeStyle=this.col; ctx.lineWidth=s*0.2; ctx.stroke();
    ctx.beginPath(); ctx.moveTo(s*0.38,-s*0.58); ctx.lineTo(s*0.85,-s*1.0); ctx.stroke();
    ctx.restore(); ctx.globalAlpha=1;
  };

  sacEl.addEventListener('click',function(){
    if(hatched) return;
    hatched=true; sacEl.style.display='none';
    var rect=sacEl.getBoundingClientRect();
    var cx=rect.left+rect.width/2, cy=rect.top+rect.height/2;
    for(var i=0;i<38;i++) activeSpiders.push(new Spider(cx,cy));
  });

  function loop(){
    sctx.clearRect(0,0,spiderCanvas.width,spiderCanvas.height);
    for(var i=activeSpiders.length-1;i>=0;i--){
      activeSpiders[i].update();
      activeSpiders[i].draw(sctx);
      if(activeSpiders[i].life>=activeSpiders[i].maxLife) activeSpiders.splice(i,1);
    }
    if(hatched&&activeSpiders.length===0){
      hatched=false; sacEl.style.display='block';
    }
    requestAnimationFrame(loop);
  }
  loop();
})();
</script>
""", height=0)


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
  background:#0DA832; border-radius:50%;
  box-shadow:0 0 6px #0DA832,0 0 12px #0DA832;
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
  color:#0DA832; background:rgba(0,0,0,0.85);
  border:3px solid #0DA832;
  padding:2vh 5vw; letter-spacing:8px;
  cursor:pointer; white-space:nowrap;
  text-shadow:0 0 20px #0DA832,0 0 40px #0DA832;
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
  text-shadow:0 0 4px #00CFFF,0 0 12px #00CFFF,0 0 30px #0088ff,0 0 40px #0DA832,2px 2px 0px rgba(255,0,200,0.4);
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
  0%,100% {{ box-shadow:0 0 10px #0DA832,0 0 20px #0DA832; }}
  50%      {{ box-shadow:0 0 30px #0DA832,0 0 60px #0DA832; }}
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
