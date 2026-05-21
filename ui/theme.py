import streamlit as st


def apply_theme():

    st.markdown(
        """
        <style>

        /* =========================================
           GLOBAL APP
        ========================================= */

        .stApp {
            background:
                radial-gradient(circle at top left, #132238, #0b0f19);

            color: white;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        /* =========================================
           SIDEBAR
        ========================================= */

        section[data-testid="stSidebar"] {

            background:
                linear-gradient(
                    180deg,
                    #0f172a,
                    #111827
                );

            border-right:
                1px solid rgba(255,255,255,0.08);
        }

        /* =========================================
           TITLES
        ========================================= */

        .mirage-title {

            text-align: center;

            color: #00ffcc;

            font-size: 48px;

            font-weight: 800;

            letter-spacing: 2px;

            text-shadow:
                0 0 10px rgba(0,255,204,0.4),
                0 0 20px rgba(0,255,204,0.2);
        }

        .mirage-subtitle {

            text-align: center;

            color: #94a3b8;

            margin-top: -8px;

            margin-bottom: 25px;

            font-style: italic;
        }

        /* =========================================
           CARDS
        ========================================= */

        .mirage-card {

            background:
                rgba(255,255,255,0.03);

            border:
                1px solid rgba(255,255,255,0.08);

            border-radius: 18px;

            padding: 22px;

            backdrop-filter: blur(12px);

            box-shadow:
                0 0 25px rgba(0,255,204,0.08);
        }

        /* =========================================
           BUTTONS
        ========================================= */

        .stButton > button {

            width: 100%;

            border-radius: 12px;

            border: none;

            background:
                linear-gradient(
                    90deg,
                    #00a3c4,
                    #00ffcc
                );

            color: black;

            font-weight: bold;

            transition: 0.3s ease;

            box-shadow:
                0 0 15px rgba(0,255,204,0.2);
        }

        .stButton > button:hover {

            transform: scale(1.02);

            box-shadow:
                0 0 20px rgba(0,255,204,0.45);
        }

        /* =========================================
           INPUTS
        ========================================= */

        .stTextInput input,
        .stTextArea textarea {

            background: #111827 !important;

            color: white !important;

            border-radius: 12px !important;

            border:
                1px solid rgba(0,255,204,0.25) !important;
        }

        /* =========================================
           RADIO + SELECTBOX
        ========================================= */

        .stSelectbox div[data-baseweb="select"] {

            background: #111827;
            border-radius: 12px;
        }

        div[role="radiogroup"] {

            padding: 10px;

            border-radius: 12px;

            background:
                rgba(255,255,255,0.03);
        }

        /* =========================================
           METRICS
        ========================================= */

        div[data-testid="metric-container"] {

            background:
                rgba(255,255,255,0.03);

            border:
                1px solid rgba(255,255,255,0.06);

            padding: 16px;

            border-radius: 16px;

            box-shadow:
                0 0 18px rgba(0,255,204,0.06);
        }

        /* =========================================
           CODE BLOCK
        ========================================= */

        pre {

            border-radius: 14px !important;

            border:
                1px solid rgba(0,255,204,0.15);

            background: #0f172a !important;
        }

        /* =========================================
           TABS
        ========================================= */

        button[data-baseweb="tab"] {

            border-radius: 12px 12px 0 0;

            background:
                rgba(255,255,255,0.03);

            color: white;
        }

        /* =========================================
           EXPANDER
        ========================================= */

        details {

            background:
                rgba(255,255,255,0.03);

            border-radius: 12px;

            padding: 10px;

            border:
                1px solid rgba(255,255,255,0.06);
        }

        /* =========================================
           SCROLLBAR
        ========================================= */

        ::-webkit-scrollbar {

            width: 10px;
        }

        ::-webkit-scrollbar-thumb {

            background:
                linear-gradient(
                    180deg,
                    #00a3c4,
                    #00ffcc
                );

            border-radius: 20px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )