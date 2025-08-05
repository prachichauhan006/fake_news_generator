import streamlit as st
from utils.generate_news import generate_news
from tts_engine import speak_text

st.set_page_config(page_title="Fake News Generator", page_icon="🗞️")

st.title("📰 Fake News Headline Generator")
st.subheader("Generate your own fake news headline and story")

category = st.selectbox("Select a category", ["sports", "politics", "bollywood"])

# Use session_state to remember the news
if "headline" not in st.session_state:
    st.session_state.headline = ""
    st.session_state.paragraph = ""

# Generate button
if st.button("📝 Generate Fake News"):
    headline, paragraph = generate_news(category)
    st.session_state.headline = headline
    st.session_state.paragraph = paragraph

# Show news if available
if st.session_state.headline:
    st.markdown(f"### 🗞️ {st.session_state.headline}")
    st.write(st.session_state.paragraph)

    # Speak button
    if st.button("🔊 Speak This News"):
        speak_text(st.session_state.headline + ". " + st.session_state.paragraph)
