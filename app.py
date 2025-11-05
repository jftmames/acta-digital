import streamlit as st
st.title("Acta Digital")
st.write("Esta es tu primera app en Streamlit.")
import hashlib, time, json


st.title("Acta Digital — Import Test")

st.write("✅ Librerías importadas:")
st.code("streamlit, hashlib, time, json")

# --- Función de verificación ---
def verify_hash(text, original_hash):
    return get_hash(text) == original_hash

st.subheader("🔍 Verificar autenticidad de un acta")

texto_verificar = st.text_area("Introduce el texto a verificar:")
hash_verificar = st.text_input("Introduce el hash original:")

if st.button("Verificar"):
    if verify_hash(texto_verificar, hash_verificar):
        st.success("✅ El texto coincide con el hash. El acta es íntegra.")
    else:
        st.error("⚠️ El texto no coincide. El acta ha sido modificada o el hash es incorrecto.")


st.write("Timestamp:", time.time())
st.write("Ejemplo JSON:", json.dumps({"ok": True, "msg": "listo"}))

