import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt

from core.forensic import (
    calculate_lsb_density,
    generate_bit_planes,
)


def render():

    st.title("Steganalysis Attack Mode")

    st.warning(
        "Analyze suspicious images and detect possible hidden payload activity."
    )

    uploaded = st.file_uploader(
        "Upload Suspicious Image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded:

        # ==========================================
        # LOAD IMAGE
        # ==========================================

        image = cv2.imdecode(
            np.frombuffer(
                uploaded.read(),
                np.uint8
            ),
            cv2.IMREAD_COLOR,
        )

        rgb = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2RGB,
        )

        st.image(
            rgb,
            caption="Analyzed Image",
            use_container_width=True,
        )

        st.divider()

        # ==========================================
        # BASIC INFO
        # ==========================================

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Width",
            image.shape[1]
        )

        col2.metric(
            "Height",
            image.shape[0]
        )

        col3.metric(
            "Channels",
            image.shape[2]
        )

        # ==========================================
        # LSB DENSITY
        # ==========================================

        st.subheader(
            "LSB Density Analysis"
        )

        density = calculate_lsb_density(
            image
        )

        st.metric(
            "LSB Density",
            f"{density:.2f}%"
        )

        # ==========================================
        # DETECTION LOGIC
        # ==========================================
        if density > 90 or density < 10:
            st.error(
                "Abnormal LSB distribution detected."
            )

            stealth_risk = "HIGH"
            st.session_state["history"].append({
                "action": "Steganalysis",
                "detail": f"Risk Level: {stealth_risk}"
            })

        elif density > 80 or density < 20:
            st.warning(
                "Slight anomaly detected."
            )

            stealth_risk = "MEDIUM"
            st.session_state["history"].append({
                "action": "Steganalysis",
                "detail": f"Risk Level: {stealth_risk}"
            })

        else:
            st.success(
                "LSB distribution appears natural."
            )

            stealth_risk = "LOW"
            st.session_state["history"].append({
                "action": "Steganalysis",
                "detail": f"Risk Level: {stealth_risk}"
            })
            
        # ==========================================
        # PROBABILITY ESTIMATION
        # ==========================================
        if stealth_risk == "LOW":
            probability = "1%"
        elif stealth_risk == "MEDIUM":
            probability = "39%"
        else:
            probability = "80%"    
            
        # ==========================================
        # RISK METRICS
        # ==========================================
        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Detection Risk",
            stealth_risk
        )

        c2.metric(
            "Forensic Scan",
            "COMPLETE"
        )

        c3.metric(
            "Payload Probability",
            # f"{abs(50 - density) * 2:.1f}%"
            probability
        )

        st.divider()

        # ==========================================
        # BIT PLANE ANALYSIS
        # ==========================================

        st.subheader(
            "Bit Plane Slicing"
        )

        bit_planes = generate_bit_planes(
            image
        )

        cols = st.columns(4)

        for i, plane in enumerate(bit_planes):

            cols[i % 4].image(
                plane,
                caption=f"Bit Plane {i}",
                use_container_width=True,
            )

        st.info(
            "Lower bit planes usually contain hidden steganographic payloads."
        )

        st.divider()

        # ==========================================
        # HISTOGRAM ANALYSIS
        # ==========================================

        st.subheader(
            "Pixel Distribution Histogram"
        )

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY,
        )

        fig, ax = plt.subplots()

        ax.hist(
            gray.flatten(),
            bins=256,
            alpha=0.8,
        )

        ax.set_title(
            "Pixel Intensity Distribution"
        )

        ax.set_xlabel(
            "Pixel Value"
        )

        ax.set_ylabel(
            "Frequency"
        )

        st.pyplot(fig)

        st.divider()

        # ==========================================
        # ANOMALY MAP
        # ==========================================

        st.subheader(
            "Anomaly Heatmap"
        )

        lsb_plane = gray & 1

        heatmap = cv2.applyColorMap(
            lsb_plane.astype(np.uint8) * 255,
            cv2.COLORMAP_JET,
        )

        st.image(
            heatmap,
            caption="LSB Heatmap",
            use_container_width=True,
        )

        st.divider()

        # ==========================================
        # FINAL FORENSIC REPORT
        # ==========================================

        st.subheader(
            "Forensic Conclusion"
        )

        if stealth_risk == "HIGH":

            st.error(
                """
                Possible steganographic payload detected.
                
                Indicators:
                - abnormal LSB density
                - suspicious lower bit-plane activity
                - high anomaly visibility
                """
            )

        elif stealth_risk == "MEDIUM":

            st.warning(
                """
                Minor anomaly detected.
                
                Additional forensic inspection recommended.
                """
            )

        else:

            st.success(
                """
                No strong steganographic indicators detected.
                
                Image appears visually natural.
                """
            )