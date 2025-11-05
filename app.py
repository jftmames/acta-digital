import streamlit as st
import hashlib, time, json

# --- Función utilitaria para crear hash ---
def get_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# --- Función para verificar coincidencia ---
def verify_hash(text, original_hash):
    return get_hash(text) == original_hash


st.title("🧾 Acta Digital — Generar y Verificar Hash")

st.header("1️⃣ Generar hash de un texto")
texto = st.text_area("Escribe el contenido del acta:")
if st.button("Generar hash"):
    if texto:
        hash_generado = get_hash(texto)
        st.session_state["hash_actual"] = hash_generado
        st.success("✅ Hash generado correctamente")
        st.code(hash_generado)
    else:
        st.warning("Introduce un texto antes de generar el hash.")

st.divider()

st.header("2️⃣ Verificar hash")
texto_verificar = st.text_area("Texto a verificar:")
hash_verificar = st.text_input("Hash a comprobar:", value=st.session_state.get("hash_actual", ""))

if st.button("Verificar hash"):
    if texto_verificar and hash_verificar:
        if verify_hash(texto_verificar, hash_verificar):
            st.success("🎯 Coincide: el texto es íntegro.")
        else:
            st.error("⚠️ No coincide: el texto fue modificado o el hash es distinto.")
    else:
        st.warning("Completa ambos campos para verificar.")

st.write("Timestamp:", time.time())
st.write("Ejemplo JSON:", json.dumps({"ok": True, "msg": "listo"}))

