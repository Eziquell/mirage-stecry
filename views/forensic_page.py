import streamlit as st
import matplotlib.pyplot as plt
from ui.cards import cyber_card

from core.forensic import (
    calculate_psnr,
    calculate_mse,
    generate_error_map,
    calculate_lsb_density,
    generate_bit_planes,
)


def render():

    st.title("Quality & Forensics")

    st.info(
        "Analyze stego image quality, stealth level, and hidden bit-plane patterns."
    )

    # ==========================================
    # SESSION CHECK
    # ==========================================

    if "stego" not in st.session_state:

        st.error(
            "No stego image found. Please use Image Encoder first."
        )

        return

    original = st.session_state["orig"]
    stego = st.session_state["stego"]

    # ==========================================
    # TABS
    # ==========================================

    tab1, tab2, tab3 = st.tabs(
        [
            "Quality Metrics",
            "Bit Plane Analysis",
            "Steganalysis",
        ]
    )

    # ==================================================
    # TAB 1 — QUALITY
    # ==================================================

    with tab1:

        st.subheader(
            "Image Quality Analysis"
        )

        psnr_value = calculate_psnr(
            original,
            stego
        )

        mse_value = calculate_mse(
            original,
            stego
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "PSNR",
            f"{psnr_value:.2f} dB"
        )

        c2.metric(
            "MSE",
            f"{mse_value:.6f}"
        )

        if psnr_value > 40:

            stealth_status = "EXCELLENT"

        elif psnr_value > 30:

            stealth_status = "GOOD"

        else:

            stealth_status = "VISIBLE"

        c3.metric(
            "Stealth Level",
            stealth_status
        )

        st.divider()

        # ======================================
        # ERROR MAP
        # ======================================

        st.subheader(
            "Enhanced Error Map"
        )

        heatmap = generate_error_map(
            original,
            stego
        )

        st.image(
            heatmap,
            caption="Pixel Modification Heatmap",
            use_container_width=True,
        )

        # ======================================
        # HISTOGRAM
        # ======================================

        st.subheader(
            "Histogram Comparison"
        )

        fig, ax = plt.subplots()

        ax.hist(
            original.flatten(),
            bins=256,
            alpha=0.5,
            label="Original",
            color="blue",
        )

        ax.hist(
            stego.flatten(),
            bins=256,
            alpha=0.5,
            label="Stego",
            color="red",
        )

        ax.legend()

        st.pyplot(fig)

    # ==================================================
    # TAB 2 — BIT PLANE
    # ==================================================

    with tab2:

        st.subheader(
            "Bit Plane Slicing"
        )

        bit_planes = generate_bit_planes(
            stego
        )

        cols = st.columns(4)

        for i, plane in enumerate(bit_planes):

            cols[i % 4].image(
                plane,
                caption=f"Bit Plane {i}",
                use_container_width=True,
            )

        st.info(
            "Lower bit planes contain most hidden payload modifications."
        )

    # ==================================================
    # TAB 3 — STEGANALYSIS
    # ==================================================

    with tab3:

        st.subheader(
            "LSB Density Analysis"
        )

        density = calculate_lsb_density(
            stego
        )

        st.metric(
            "LSB Density",
            f"{density:.2f}%"
        )

        # ======================================
        # DETECTION STATUS
        # ======================================

        if density > 60 or density < 40:

            st.error(
                "Suspicious LSB distribution detected."
            )

            risk = "HIGH"

        else:

            st.success(
                "LSB distribution appears natural."
            )

            risk = "LOW"

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Detection Risk",
            risk
        )

        c2.metric(
            "Pixel Distribution",
            "ANALYZED"
        )

        c3.metric(
            "Forensic Status",
            "COMPLETE"
        )

        st.divider()

        st.markdown(
            """
            ### Analysis Notes
            
            - High PSNR indicates better visual stealth.
            - Low MSE means fewer pixel modifications.
            - Random LSB generally provides better stealth than Sequential LSB.
            - Abnormal LSB density may indicate hidden payload activity.
            """
        )