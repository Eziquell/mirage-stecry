import streamlit as st


def cyber_card(
    title,
    value,
    color="#00ffcc",
    icon="⚡"
):

    st.markdown(
        f"""
        <div style="
            background:rgba(255,255,255,0.03);

            border:1px solid rgba(255,255,255,0.08);

            border-left:5px solid {color};

            padding:18px;

            border-radius:16px;

            box-shadow:
                0 0 18px rgba(0,255,204,0.08);

            margin-bottom:12px;
        ">

            <div style="
                color:#94a3b8;
                font-size:14px;
                margin-bottom:6px;
            ">
                {icon} {title}
            </div>

            <div style="
                color:white;
                font-size:28px;
                font-weight:bold;
            ">
                {value}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


def status_card(
    title,
    status,
    level="normal"
):

    colors = {
        "safe": "#00ff99",
        "warning": "#f39c12",
        "danger": "#ff5c7a",
        "normal": "#00a3c4",
    }

    color = colors.get(level, "#00a3c4")

    st.markdown(
        f"""
        <div style="
            background:rgba(255,255,255,0.03);

            border:1px solid rgba(255,255,255,0.08);

            padding:18px;

            border-radius:16px;

            margin-bottom:12px;

            box-shadow:
                0 0 20px rgba(0,0,0,0.2);
        ">

            <div style="
                color:#94a3b8;
                font-size:14px;
            ">
                {title}
            </div>

            <div style="
                color:{color};

                font-size:22px;

                font-weight:bold;

                margin-top:6px;
            ">
                {status}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


def info_panel(
    title,
    text,
):

    st.markdown(
        f"""
        <div style="
            background:
                linear-gradient(
                    135deg,
                    rgba(0,163,196,0.15),
                    rgba(0,255,204,0.05)
                );

            border:
                1px solid rgba(0,255,204,0.15);

            padding:18px;

            border-radius:16px;

            margin-top:10px;

            margin-bottom:10px;
        ">

            <div style="
                color:#00ffcc;

                font-size:18px;

                font-weight:bold;

                margin-bottom:10px;
            ">
                {title}
            </div>

            <div style="
                color:#d1d5db;

                line-height:1.7;
            ">
                {text}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )