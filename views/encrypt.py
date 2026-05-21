import streamlit as st
import streamlit.components.v1 as components
import urllib.parse

from core.crypto import (
    vigenere_cipher,
    xor_encrypt,
    xor_decrypt,
)

from core.rsa_utils import (
    generate_rsa_keys,
)


def render():

    st.title("Encrypt / Decrypt")

    st.info(
        "Encrypt secret messages before embedding them into images."
    )

    col1, col2 = st.columns(2)

    # ==================================================
    # CLASSIC CRYPTO
    # ==================================================

    with col1:

        st.subheader("Classic Cryptography")

        algorithm = st.selectbox(
            "Select Cipher",
            [
                "Vigenere Cipher",
                "XOR Cipher",
            ]
        )

        text_input = st.text_area(
            "Input Text"
        )

        key_input = st.text_input(
            "Secret Key",
            type="password"
        )

        ca, cb = st.columns(2)

        # ==========================
        # ENCRYPT
        # ==========================

        if ca.button("Encrypt Text"):

            if text_input and key_input:

                with st.spinner("Encrypting payload..."):

                    if algorithm == "Vigenere Cipher":

                        result = vigenere_cipher(
                            text_input,
                            key_input,
                        )

                    else:

                        result = xor_encrypt(
                            text_input,
                            key_input,
                        )

                st.toast("Encryption Complete")

                st.session_state["history"].append({

                    "action": "Encryption",

                    "detail": f"{algorithm} executed"

                })


                st.code(
                    result,
                    language="text"
                )

        # ==========================
        # DECRYPT
        # ==========================

        if cb.button("Decrypt Text"):

            if text_input and key_input:

                with st.spinner("Decrypting payload..."):

                    if algorithm == "Vigenere Cipher":

                        result = vigenere_cipher(
                            text_input,
                            key_input,
                            mode="decrypt",
                        )

                    else:

                        result = xor_decrypt(
                            text_input,
                            key_input,
                        )

                st.toast("Decryption Complete")
                
                st.session_state["history"].append({

                    "action": "Decryption",

                    "detail": f"{algorithm} decrypted"

                })

                st.success(result)

    # ==================================================
    # RSA SECTION
    # ==================================================

    with col2:

        st.subheader(
            "Modern Cryptography (RSA)"
        )

        if st.button("Generate RSA Key Pair"):

            with st.spinner("Generating RSA keys..."):

                pub_pem, priv_pem = generate_rsa_keys()

                st.session_state["pub_pem"] = pub_pem
                st.session_state["priv_pem"] = priv_pem

            st.toast("RSA Keys Generated")

        # ==========================================
        # SHOW RSA KEYS
        # ==========================================

        if "pub_pem" in st.session_state:

            pub_pem_str = (
                st.session_state["pub_pem"]
                .decode()
            )

            priv_pem_str = (
                st.session_state["priv_pem"]
                .decode()
            )

            encoded_pub = urllib.parse.quote(
                pub_pem_str
            )

            encoded_priv = urllib.parse.quote(
                priv_pem_str
            )

            components.html(
                f"""
                <div style="
                    display:flex;
                    gap:20px;
                    flex-wrap:wrap;
                    font-family:sans-serif;
                    color:white;

                    background:rgba(255,255,255,0.02);
                    padding:20px;
                    border-radius:16px;
                    backdrop-filter:blur(8px);

                    border:1px solid rgba(255,255,255,0.08);
                ">

                    <!-- PUBLIC KEY -->
                    <div style="flex:1; min-width:300px;">

                        <label style="
                            font-weight:bold;
                            color:#00ffcc;
                            display:block;
                            margin-bottom:10px;
                            font-size:18px;
                        ">
                            Public Key
                        </label>

                        <textarea id="pubkey"
                            style="
                                width:100%;
                                height:180px;
                                padding:12px;
                                border-radius:10px;
                                border:1px solid #00a3c4;
                                resize:none;

                                background:#111827;
                                color:#00ffcc;

                                font-family:monospace;

                                box-shadow:0 0 10px rgba(0,255,204,0.2);
                            ">{pub_pem_str}</textarea>

                        <div style="margin-top:12px;">

                            <button
                                onclick="
                                    navigator.clipboard.writeText(
                                        document.getElementById('pubkey').value
                                    );
                                "
                                style="
                                    padding:10px 14px;
                                    border:none;
                                    border-radius:8px;
                                    background:#00a3c4;
                                    color:white;
                                    cursor:pointer;
                                    font-weight:bold;
                                ">
                                Copy Public Key
                            </button>

                            <a
                                href="data:text/plain;charset=utf-8,{encoded_pub}"
                                download="public_key.pem"
                                style="
                                    margin-left:10px;
                                    padding:10px 14px;
                                    border-radius:8px;
                                    background:#4caf50;
                                    color:white;
                                    text-decoration:none;
                                    font-weight:bold;
                                ">
                                Download
                            </a>

                        </div>
                    </div>

                    <!-- PRIVATE KEY -->
                    <div style="flex:1; min-width:300px;">

                        <label style="
                            font-weight:bold;
                            color:#ff5c7a;
                            display:block;
                            margin-bottom:10px;
                            font-size:18px;
                        ">
                            Private Key
                        </label>

                        <textarea id="privkey"
                            style="
                                width:100%;
                                height:180px;
                                padding:12px;
                                border-radius:10px;
                                border:1px solid #ff5c7a;
                                resize:none;

                                background:#111827;
                                color:#ffb3c1;

                                font-family:monospace;

                                box-shadow:0 0 10px rgba(255,92,122,0.2);
                            ">{priv_pem_str}</textarea>

                        <div style="margin-top:12px;">

                            <button
                                onclick="
                                    navigator.clipboard.writeText(
                                        document.getElementById('privkey').value
                                    );
                                "
                                style="
                                    padding:10px 14px;
                                    border:none;
                                    border-radius:8px;
                                    background:#ff5c7a;
                                    color:white;
                                    cursor:pointer;
                                    font-weight:bold;
                                ">
                                Copy Private Key
                            </button>

                            <a
                                href="data:text/plain;charset=utf-8,{encoded_priv}"
                                download="private_key.pem"
                                style="
                                    margin-left:10px;
                                    padding:10px 14px;
                                    border-radius:8px;
                                    background:#f39c12;
                                    color:white;
                                    text-decoration:none;
                                    font-weight:bold;
                                ">
                                Download
                            </a>

                        </div>
                    </div>

                </div>
                """,
                height=900,
                scrolling=True,
            )