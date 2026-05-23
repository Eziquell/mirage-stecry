import streamlit as st
import cv2
import numpy as np

from core.stegano import embed_data


def render():

    st.title("Image Encoder (LSB)")

    st.info(
        "Embed encrypted secret messages into PNG images using LSB steganography."
    )

    uploaded_file = st.file_uploader(
        "Upload Cover Image",
        type=["png"]
    )

    if uploaded_file:

        image = cv2.imdecode(
            np.frombuffer(uploaded_file.read(), np.uint8),
            cv2.IMREAD_COLOR,
        )

        # ==========================================
        # IMAGE PREVIEW
        # ==========================================

        st.image(
            cv2.cvtColor(image, cv2.COLOR_BGR2RGB),
            caption="Cover Image",
            use_container_width=True,
        )

        # ==========================================
        # CAPACITY CALCULATION
        # ==========================================

        max_bytes = (
            image.shape[0]
            * image.shape[1]
            * image.shape[2]
        ) // 8 - 2

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
            "Capacity",
            f"{max_bytes} chars"
        )

        st.divider()

        # ==========================================
        # PAYLOAD
        # ==========================================

        payload = st.text_area(
            "Secret Payload"
        )

        lsb_password = st.text_input(
            "LSB Password",
            type="password"
        )

        method = st.radio(
            "Embedding Method",
            [
                "Sequential LSB",
                "Random LSB",
            ]
        )

        # ==========================================
        # EMBED BUTTON
        # ==========================================

        if st.button("Embed Payload"):
            if not payload:
                st.warning(
                    "Please enter a secret payload."
                )

            elif not lsb_password:

                st.error(
                    "Password/key is required."
                )

            else:
                with st.spinner(
                    "Embedding secret payload..."
                ):

                    stego_image, error = embed_data(
                        image.copy(),
                        payload,
                        method,
                        lsb_password,
                    )

                if error:

                    st.error(error)

                else:

                    st.toast(
                        "Payload Embedded Successfully"
                    )
                    
                    st.session_state["history"].append({

                        "action": "LSB Embedding",

                        "detail": f"{method} | {len(payload)} chars"

                    })

                    st.success(
                        "Stego image created successfully."
                    )

                    # ==================================
                    # SAVE SESSION
                    # ==================================

                    st.session_state["orig"] = image
                    st.session_state["stego"] = stego_image

                    # ==================================
                    # PREVIEW
                    # ==================================

                    st.image(
                        cv2.cvtColor(
                            stego_image,
                            cv2.COLOR_BGR2RGB,
                        ),
                        caption="Stego Image",
                        use_container_width=True,
                    )

                    # ==================================
                    # DOWNLOAD
                    # ==================================

                    _, buffer = cv2.imencode(
                        ".png",
                        stego_image,
                    )

                    st.download_button(
                        "Download Stego Image",
                        buffer.tobytes(),
                        file_name="mirage_stego.png",
                        mime="image/png",
                    )

                    # ==================================
                    # STEALTH METRICS
                    # ==================================

                    st.divider()

                    c1, c2, c3 = st.columns(3)

                    c1.metric(
                        "Embedding Method",
                        method
                    )

                    c2.metric(
                        "Payload Length",
                        len(payload)
                    )

                    c3.metric(
                        "Stealth Status",
                        "ACTIVE"
                    )