import streamlit as st
import cv2
import numpy as np

from core.stegano import extract_data


def render():

    st.title("Image Decoder (LSB)")

    st.info(
        "Extract hidden payloads from stego images."
    )

    uploaded_stego = st.file_uploader(
        "Upload Stego Image",
        type=["png"]
    )

    if uploaded_stego:

        stego_image = cv2.imdecode(
            np.frombuffer(
                uploaded_stego.read(),
                np.uint8
            ),
            cv2.IMREAD_COLOR,
        )

        # ==========================================
        # PREVIEW IMAGE
        # ==========================================

        st.image(
            cv2.cvtColor(
                stego_image,
                cv2.COLOR_BGR2RGB,
            ),
            caption="Stego Image",
            use_container_width=True,
        )

        st.divider()

        # ==========================================
        # EXTRACTION SETTINGS
        # ==========================================

        extraction_method = st.radio(
            "Extraction Method",
            [
                "Sequential LSB",
                "Random LSB",
            ]
        )

        extraction_password = st.text_input(
            "LSB Password",
            type="password"
        )

        # ==========================================
        # EXTRACT BUTTON
        # ==========================================

        if st.button("Extract Payload"):

            with st.spinner(
                "Extracting hidden payload..."
            ):

                extracted_text = extract_data(
                    stego_image,
                    extraction_method,
                    extraction_password,
                )

            # ======================================
            # RESULT
            # ======================================

            st.toast(
                "Payload Extraction Complete"
            )
                
            st.session_state["history"].append({
                "action": "Payload Extraction",
                "detail": extraction_method
            })
            
            if extracted_text == "Invalid password or corrupted image!":
                st.error(extracted_text)
            else:
                st.success(
                    "Hidden payload extracted successfully."
                )
            
            st.subheader(
                "Extracted Payload"
            )

            st.code(
                extracted_text,
                language="text"
            )

            # ======================================
            # FORENSIC INFO
            # ======================================

            st.divider()

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Method",
                extraction_method
            )

            if extracted_text == "Invalid password or corrupted image!":

                payload_len = 0
                status = "FAILED"

            else:

                payload_len = len(extracted_text)
                status = "RECOVERED"

            c2.metric(
                "Payload Length",
                payload_len
            )

            c3.metric(
                "Status",
                status
            )

            # ======================================
            # DOWNLOAD PAYLOAD
            # ======================================

            st.download_button(
                "Download Extracted Payload",
                extracted_text,
                file_name="mirage_payload.txt",
                mime="text/plain",
            )