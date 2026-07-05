import streamlit as st
from deep_translator import GoogleTranslator

def load_css():
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.set_page_config(
    page_title="AI Language Translation Tool",
    page_icon="🌍",
    layout="wide"
)


if "history" not in st.session_state:
    st.session_state.history = []


st.sidebar.title("🌍 AI Translator")

st.sidebar.markdown("---")

st.sidebar.header("👩‍💻 Developer")

st.sidebar.info("""
**Bhuvi Kataria**

CodeAlpha AI Internship Project
""")

st.sidebar.markdown("---")

st.sidebar.header("✨ Features")

st.sidebar.success("✔ Auto Detect Language")
st.sidebar.success("✔ 25+ Languages")
st.sidebar.success("✔ Translation History")
st.sidebar.success("✔ Download Translation")
st.sidebar.success("✔ Character Counter")
st.sidebar.success("✔ Clear Text")
st.sidebar.success("✔ Beautiful UI")

st.sidebar.markdown("---")

st.sidebar.write("Made with ❤️ using Python & Streamlit")


st.title("🌍 AI Language Translation Tool")

st.write(
    "Translate text into multiple languages instantly using Artificial Intelligence."
)

st.markdown("---")

languages = {
    "Auto Detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Italian": "it",
    "Russian": "ru",
    "Arabic": "ar",
    "Bengali": "bn",
    "Punjabi": "pa",
    "Urdu": "ur",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml",
    "Gujarati": "gu",
    "Marathi": "mr",
    "Kannada": "kn",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Turkish": "tr",
    "Korean": "ko",
    "Greek": "el",
    "Thai": "th",
    "Vietnamese": "vi"
}


text = st.text_area(
    "📝 Enter Text",
    height=180,
    placeholder="Type or paste your text here..."
)

st.caption(f"Characters : {len(text)}")


col1, col2 = st.columns(2)

with col1:

    source = st.selectbox(
        "🌐 Source Language",
        list(languages.keys())
    )

with col2:

    target = st.selectbox(
        "🌎 Target Language",
        list(languages.keys()),
        index=2
    )


button1, button2 = st.columns(2)

with button1:

    translate = st.button(
        "🔄 Translate",
        use_container_width=True
    )

with button2:

    clear = st.button(
        "🗑 Clear",
        use_container_width=True
    )


if clear:

    st.session_state.history = []

    st.rerun()


if translate:

    if text.strip() == "":

        st.warning("⚠ Please enter some text.")

    elif source == target and source != "Auto Detect":

        st.warning("⚠ Source and Target languages cannot be the same.")

    else:
        
        try:

            translated = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)


            st.success("✅ Translation Successful!")


            st.text_area(
                "📄 Translated Text",
                translated,
                height=180
            )


            st.download_button(
                label="📥 Download Translation",
                data=translated,
                file_name="translated_text.txt",
                mime="text/plain",
                use_container_width=True
            )


            st.session_state.history.insert(
                0,
                {
                    "source": source,
                    "target": target,
                    "original": text,
                    "translated": translated
                }
            )

        except Exception:

            st.error(
                "❌ Something went wrong.\n\nPlease check your internet connection and try again."
            )


st.markdown("---")

st.subheader("🕒 Translation History")

if len(st.session_state.history) == 0:

    st.info("No translations yet.")

else:

    for i, item in enumerate(st.session_state.history, start=1):

        with st.expander(
            f"{i}. {item['source']} ➜ {item['target']}"
        ):

            st.markdown("### 📝 Original Text")

            st.write(item["original"])

            st.markdown("### 🌍 Translated Text")

            st.write(item["translated"])


st.markdown("---")

st.markdown(
    """
    <div style='text-align:center; font-size:18px;'>

    ❤️ Made by <b>Bhuvi Kataria</b>

    <br><br>

    🚀 CodeAlpha Artificial Intelligence Internship Project

    <br><br>

    Python • Streamlit • Deep Translator

    </div>
    """,
    unsafe_allow_html=True
)