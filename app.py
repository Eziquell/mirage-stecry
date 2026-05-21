import streamlit as st

from views.encrypt import render as encrypt_page
from views.encoder import render as encoder_page
from views.decoder import render as decoder_page
from views.attack import render as attack_page
from views.forensic_page import render as forensic_page
from views.signature import render as signature_page
from ui.theme import apply_theme


st.set_page_config(
    page_title="MIRAGE STECRY",
    layout="wide"
)
apply_theme()

# ==========================================
# SESSION HISTORY
# ==========================================
if "history" not in st.session_state:
    st.session_state["history"] = []

# ==========================================
# MAIN CONTENT
# ==========================================
st.markdown(
    """
    <div class="mirage-title">
        MIRAGE STECRY
    </div>

    <div class="mirage-subtitle">
        What you see is not what you get.
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# SIDEBAR MENU
# ==========================================
menu = st.sidebar.radio(
    "Command Center",
    [
        "Encrypt / Decrypt",
        "Image Encoder",
        "Image Decoder",
        "Steganalysis Attack",
        "Quality & Forensics",
        "Digital Signature"
    ]
)

# ==========================================
# SIDEBAR INFO
# ==========================================
st.sidebar.divider()

st.sidebar.subheader(
    "Recent Activity"
)

history = st.session_state["history"]

if history:

    for item in reversed(history[-5:]):

        st.sidebar.markdown(
            f"""
        <div style="
        background:rgba(255,255,255,0.03);
        padding:10px;
        border-radius:10px;
        margin-bottom:8px;
        border-left:3px solid #00ffcc;
        font-size:13px;
        ">

        <b>{item['action']}</b><br>

        <span style="color:#94a3b8;">
        {item['detail']}
        </span>

        </div>
        """,
            unsafe_allow_html=True,
        )

else:

    st.sidebar.caption(
        "No recent activity."
    )

if menu == "Encrypt / Decrypt":
    encrypt_page()

elif menu == "Image Encoder":
    encoder_page()

elif menu == "Image Decoder":
    decoder_page()

elif menu == "Steganalysis Attack":
    attack_page()

elif menu == "Quality & Forensics":
    forensic_page()

elif menu == "Digital Signature":
    signature_page()