import streamlit as st

from core.rsa_utils import (
    rsa_sign_message,
    rsa_verify_signature,
)


def render():

    st.title("Digital Signature")

    st.info(
        "Use RSA Digital Signature to verify message authenticity and integrity."
    )

    # ==========================================
    # VISUALIZATION
    # ==========================================

    with st.expander(
        "How Digital Signature Works"
    ):

        st.markdown(
            """
            MESSAGE  
            ↓  
            SHA256 HASH  
            ↓  
            PRIVATE KEY SIGNING  
            ↓  
            DIGITAL SIGNATURE  
            ↓  
            VERIFY USING PUBLIC KEY
            """
        )

    # ==========================================
    # TABS
    # ==========================================

    tab_sign, tab_verify = st.tabs(
        [
            "Sign Message",
            "Verify Signature",
        ]
    )

    # ==================================================
    # SIGN TAB
    # ==================================================

    with tab_sign:

        st.subheader(
            "Create Digital Signature"
        )

        private_key_input = st.text_area(
            "Paste Private Key (PEM Format)",
            height=180,
        )

        message_input = st.text_area(
            "Message to Sign"
        )

        if st.button(
            "Generate Signature"
        ):

            if not private_key_input:

                st.warning(
                    "Private Key is required."
                )

            elif not message_input:

                st.warning(
                    "Message is required."
                )

            else:

                with st.spinner(
                    "Generating digital signature..."
                ):

                    private_key_bytes = (
                        private_key_input.encode()
                    )

                    signature, error = (
                        rsa_sign_message(
                            message_input,
                            private_key_bytes,
                        )
                    )

                if error:

                    st.error(error)

                else:

                    signature_hex = (
                        signature.hex()
                    )

                    st.toast(
                        "Signature Created"
                    )
                    
                    st.session_state["history"].append({

                        "action": "Digital Signature",

                        "detail": "RSA Signature Generated"

                    })

                    st.success(
                        "Digital signature generated successfully."
                    )

                    # ======================
                    # STORE SESSION
                    # ======================

                    st.session_state[
                        "last_signature"
                    ] = signature_hex

                    st.session_state[
                        "last_message"
                    ] = message_input

                    # ======================
                    # DISPLAY
                    # ======================

                    col1, col2 = st.columns(2)

                    with col1:

                        st.markdown(
                            "### Original Message"
                        )

                        st.code(
                            message_input,
                            language="text",
                        )

                    with col2:

                        st.markdown(
                            "### Signature (HEX)"
                        )

                        st.code(
                            signature_hex[:120]
                            + "..."
                        )

                    # ======================
                    # METRICS
                    # ======================

                    c1, c2, c3 = st.columns(3)

                    c1.metric(
                        "Hash Algorithm",
                        "SHA256"
                    )

                    c2.metric(
                        "Key Type",
                        "RSA-2048"
                    )

                    c3.metric(
                        "Signature Status",
                        "VALID"
                    )

                    # ======================
                    # DOWNLOAD
                    # ======================

                    st.download_button(
                        "Download Signature",
                        signature_hex,
                        file_name="signature.txt",
                        mime="text/plain",
                    )

    # ==================================================
    # VERIFY TAB
    # ==================================================

    with tab_verify:

        st.subheader(
            "Verify Digital Signature"
        )

        public_key_input = st.text_area(
            "Paste Public Key (PEM Format)",
            height=180,
        )

        verify_message = st.text_area(
            "Message to Verify",
            value=st.session_state.get(
                "last_message",
                ""
            ),
        )

        signature_input = st.text_area(
            "Signature (HEX)",
            value=st.session_state.get(
                "last_signature",
                ""
            ),
            height=150,
        )

        if st.button(
            "Verify Signature"
        ):

            if (
                not public_key_input
                or not verify_message
                or not signature_input
            ):

                st.warning(
                    "Please complete all fields."
                )

            else:

                try:

                    with st.spinner(
                        "Verifying signature..."
                    ):

                        public_key_bytes = (
                            public_key_input.encode()
                        )

                        signature_bytes = (
                            bytes.fromhex(
                                signature_input
                            )
                        )

                        is_valid, error = (
                            rsa_verify_signature(
                                verify_message,
                                signature_bytes,
                                public_key_bytes,
                            )
                        )

                    # ==================
                    # RESULT
                    # ==================

                    if is_valid:

                        st.success(
                            "Signature Verified Successfully"
                        )

                        st.balloons()

                        status = "AUTHENTIC"

                    else:

                        st.error(
                            "Invalid Signature Detected"
                        )

                        status = "FAILED"

                    # ==================
                    # METRICS
                    # ==================

                    c1, c2, c3 = st.columns(3)

                    c1.metric(
                        "Verification",
                        status
                    )

                    c2.metric(
                        "Integrity",
                        "CHECKED"
                    )

                    c3.metric(
                        "Security Level",
                        "HIGH"
                    )

                except Exception as e:

                    st.error(
                        f"Verification Error: {str(e)}"
                    )

    # ==================================================
    # INFO SECTION
    # ==================================================

    st.divider()

    with st.expander(
        "Security Explanation"
    ):

        st.markdown(
            """
            ### What is a Digital Signature?

            A digital signature proves:
            
            - The message really came from the sender
            - The message was not modified
            - The sender owns the private key

            ### Workflow

            1. Sender signs the message using a Private Key
            2. Receiver verifies using the Public Key
            3. If verification succeeds:
                - authenticity confirmed
                - integrity preserved

            ### Security Advantage

            Only the owner of the Private Key can create a valid signature.
            """
        )