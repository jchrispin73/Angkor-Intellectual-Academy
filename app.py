import streamlit as st
import random

st.set_page_config(page_title="AIKH Early Years GPT Demo", layout="centered")

st.title("🧢 AIKH Teacher Assistant - Early Years Edition")
st.subheader("Lesson ideas and plans powered by Hats on Top")

# Select options
level = st.selectbox("Select your level:", ["K2", "K3"])
lesson_type = st.selectbox("What would you like to generate?", [
    "Full Lesson Plan",
    "Storytime Activity",
    "Song or Rhyme",
    "Circle Time Questions",
    "Worksheet or Craft Idea"
])
theme = st.text_input("Topic or Theme (e.g., Animals, Feelings, Colours):")

if st.button("Generate Lesson Idea"):
    # Placeholder responses – these will later use GPT logic with Hats on Top insights
    if not theme:
        st.warning("Please enter a theme to personalise your lesson.")
    else:
        ideas = {
            "Full Lesson Plan": f"**{level} Lesson Plan on '{theme}'**\n\n1. Welcome Song\n2. Introduction to the theme with flashcards\n3. Story from Hats on Top\n4. Movement game: Act like a {theme.lower()}!\n5. Worksheet or coloring\n6. Goodbye song",
            "Storytime Activity": f"**Storytime: '{theme} Friends'**\n\nRead a short story featuring animals or characters showing the theme '{theme}'. Ask children what they see and feel. Repeat key words together.",
            "Song or Rhyme": f"**The {theme} Song**\n\n(To the tune of 'Twinkle Twinkle')\n\n{theme} here, {theme} there,\nI see {theme} everywhere!\nIn my book and on the mat,\nLook — it’s on my teacher’s hat!",
            "Circle Time Questions": f"**Circle Time Talk – Theme: {theme}**\n\n1. What's your favourite {theme}?\n2. Can you show me how a {theme.lower()} moves?\n3. What color is your {theme.lower()}?\n4. Do you feel happy when you see a {theme.lower()}?",
            "Worksheet or Craft Idea": f"**Craft: My {theme} Hat**\n\nMake a fun paper hat shaped like a {theme.lower()}. Let kids decorate with colors, stickers, or googly eyes. Encourage them to wear it during story time."
        }

        st.markdown(ideas[lesson_type])
        st.info("This content is based on Hats on Top themes and early years classroom strategies.")

st.markdown("---")
st.caption("Demo created for Angkor International Academy | Powered by Streamlit + GPT")
