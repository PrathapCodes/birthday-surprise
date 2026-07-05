import streamlit as st
import time

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="A Surprise for Akshata 🎁",
    page_icon="🎁",
    layout="centered"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#ffe4ec,#ffd6f5,#f5d8ff,#fff0d6);
}

/* Hide Streamlit header/footer */
header, footer{
    visibility:hidden;
}

.title{
    text-align:center;
    font-size:60px;
    font-weight:bold;
    color:#e91e63;
    margin-top:30px;
}

.subtitle{
    text-align:center;
    font-size:24px;
    color:#555;
    margin-bottom:35px;
}

.big-title{
    text-align:center;
    font-size:62px;
    font-weight:bold;
    color:#d81b60;
    text-shadow:0 0 20px rgba(255,105,180,0.45);
    animation: glow 2s infinite alternate;
}

.message{

    background:#ffffff;

    padding:40px;

    border-radius:22px;

    color:#333333;

    font-size:22px;

    line-height:2;

    text-align:center;

    box-shadow:0 15px 35px rgba(0,0,0,.15);

    border:2px solid #ffd6ea;

    margin-top:25px;
}

.footer{
    text-align:center;
    color:#555;
    font-size:18px;
    margin-top:40px;
}

@keyframes glow{

from{
text-shadow:0 0 8px #ff8cc8;
}

to{
text-shadow:0 0 25px #ff1493;
}

}

div.stButton>button{

background:linear-gradient(90deg,#ff1493,#ff5ca8);

color:white;

font-size:24px;

font-weight:bold;

border:none;

border-radius:14px;

padding:14px 35px;

transition:.3s;

}

div.stButton>button:hover{

background:linear-gradient(90deg,#ff5ca8,#ff1493);

transform:scale(1.05);

}

</style>
""", unsafe_allow_html=True)

# ---------------- LANDING ---------------- #

st.markdown("""
<div class="title">
👋 Hey, Birthday Girl! 💖
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
✨ I made something special just for you... 🎁
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- BUTTON ---------------- #

if st.button("🎁 Open Your Surprise"):

    progress = st.progress(0)

    for i in range(101):
        progress.progress(i)
        time.sleep(0.015)

    st.balloons()
    st.snow()

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="big-title">

🎂 Happy Birthday,<br>

Akshata! ❤️

</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="message">

<h2 style="color:#e91e63;">
💖 Dear Akshata ❤️
</h2>

<p>

Wishing you the happiest birthday! 🎂✨

</p>

<p>

May your smile always shine brighter than the stars. 🌟

</p>

<p>

May every dream you chase become reality. 🌈

</p>

<p>

May this year bring you endless happiness,
beautiful memories,
good health,
success,
and everything your heart wishes for. 💕

</p>

<p>

Never stop smiling.
<br>
Never stop believing in yourself.
<br>
Keep spreading your wonderful positivity everywhere you go. 🌸

</p>

<p>

You deserve all the happiness in the world today and always. ❤️

</p>

<h2 style="color:#ff1493;">

🎉 Happy Birthday, Akshata! 🎂🥳

</h2>

</div>
""", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("## 🎵 Birthday Song")

    st.video("https://www.youtube.com/watch?v=90w2RegGf9w")

    st.markdown("---")

    st.markdown("""
# 💝 Birthday Wishes

🎂 Enjoy Every Moment ❤️

⭐ Keep Shining ✨

🌸 Stay Happy 😊

💖 Stay Blessed 🌷

🚀 Keep Achieving Your Dreams 💫

🌈 Smile Always ❤️
""")

    st.success("🎉 Surprise Completed!")

st.markdown("""
<div class="footer">

Made with ❤️ especially for Akshata

</div>
""", unsafe_allow_html=True)