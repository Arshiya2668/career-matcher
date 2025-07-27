import streamlit as st
import random

st.set_page_config(page_title="Career Matcher", layout="centered")

# Career data and weights
careers = {
    "Software Developer": {"tech": 5, "creativity": 2, "people": 1, "leadership": 2, "design": 1},
    "Graphic Designer": {"tech": 2, "creativity": 5, "people": 2, "leadership": 1, "design": 5},
    "Teacher": {"tech": 2, "creativity": 2, "people": 5, "leadership": 4, "design": 1},
    "Entrepreneur": {"tech": 3, "creativity": 3, "people": 3, "leadership": 5, "design": 2},
    "UX Designer": {"tech": 3, "creativity": 4, "people": 3, "leadership": 2, "design": 5}
}

career_plans = {
    "Software Developer": ["Learn Python basics", "Build projects on GitHub", "Master data structures", "Apply for internships"],
    "Graphic Designer": ["Learn Photoshop/Illustrator", "Design posters/logos", "Create portfolio website", "Work with clients"],
    "Teacher": ["Get teaching certification", "Volunteer to teach", "Develop communication skills", "Apply to schools"],
    "Entrepreneur": ["Identify a business idea", "Study marketing/finance", "Build MVP", "Pitch to investors"],
    "UX Designer": ["Learn Figma and UX basics", "Analyze apps/websites", "Design case studies", "Apply for UX roles"]
}

recommended_subjects = {
    "Software Developer": ["Computer Science", "Mathematics", "Data Structures"],
    "Graphic Designer": ["Design", "Digital Art", "Visual Communication"],
    "Teacher": ["Education", "Psychology", "Subject Expertise"],
    "Entrepreneur": ["Business", "Marketing", "Finance"],
    "UX Designer": ["UI/UX Design", "Human-Computer Interaction", "Behavioral Psychology"]
}

personality_colors = {
    "Logical Thinker": "blue",
    "Creative Mind": "red",
    "People Person": "green",
    "Leader Type": "orange",
    "Visual Thinker": "purple"
}

# Dark mode check
is_dark = st.get_option("theme.base") == "dark"
text_class = "dark-text" if is_dark else "light-text"
st.markdown(f"""
<style>
.dark-text {{ color: white; font-size: 18px; }}
.light-text {{ color: black; font-size: 18px; }}
.tip {{ font-size: 14px; color: gray; margin-bottom: 10px; }}
.question-label {{ font-size: 20px; font-weight: bold; color: {'white' if is_dark else 'black'}; }}
body {{
    background-image: url('https://i.pinimg.com/originals/41/11/4f/41114f0a8d8705081671a27c4c1101be.jpg');
    background-size: cover;
}}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🎯 Career Matcher")

# Name input
name = st.text_input("Enter your name to begin:")
if name:
    st.markdown(f"<p class='{text_class}'>Welcome, <b>{name}</b>! Please rate the following:</p>", unsafe_allow_html=True)

    # Questions with styling
    st.markdown("<div class='question-label'>1. Interest in Technology</div>", unsafe_allow_html=True)
    tech = st.slider("", 1, 5, key="tech_slider")
    st.markdown("<div class='tip'>Tip: Do you enjoy working with software, hardware, or tools?</div>", unsafe_allow_html=True)

    st.markdown("<div class='question-label'>2. Creative Thinking</div>", unsafe_allow_html=True)
    creativity = st.slider("", 1, 5, key="creativity_slider")
    st.markdown("<div class='tip'>Tip: Are you good at coming up with ideas or designing things?</div>", unsafe_allow_html=True)

    st.markdown("<div class='question-label'>3. Comfort Working with People</div>", unsafe_allow_html=True)
    people = st.slider("", 1, 5, key="people_slider")
    st.markdown("<div class='tip'>Tip: Do you enjoy teamwork, teaching, or talking to people?</div>", unsafe_allow_html=True)

    st.markdown("<div class='question-label'>4. Leadership Ability</div>", unsafe_allow_html=True)
    leadership = st.slider("", 1, 5, key="leadership_slider")
    st.markdown("<div class='tip'>Tip: Do you like managing projects or leading teams?</div>", unsafe_allow_html=True)

    st.markdown("<div class='question-label'>5. Eye for Design</div>", unsafe_allow_html=True)
    design = st.slider("", 1, 5, key="design_slider")
    st.markdown("<div class='tip'>Tip: Are you interested in layouts, UI, or how things look?</div>", unsafe_allow_html=True)

    # Time Period
    st.subheader("Select your time period:")
    start_year = st.number_input("From Year", min_value=2000, max_value=2029, value=2025, step=1)
    end_year = st.number_input("To Year", min_value=start_year, max_value=2030, value=2027, step=1)
    st.markdown("<div class='tip'>Tip: Think about your past experiences</div>", unsafe_allow_html=True)

    # Show matches
    if st.button("Show My Matches"):
        scores = {}
        for career, weights in careers.items():
            scores[career] = (
                weights["tech"] * tech +
                weights["creativity"] * creativity +
                weights["people"] * people +
                weights["leadership"] * leadership +
                weights["design"] * design
            )

        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        top_career = sorted_scores[0][0]

        st.subheader("Your Best Matches")
        for career, score in sorted_scores:
            st.markdown(f"<p class='{text_class}'><b>{career}</b> — Match Score: {score}</p>", unsafe_allow_html=True)

        st.markdown(f"<p class='{text_class}'>📆 Time Period: <b>{start_year} to {end_year}</b></p>", unsafe_allow_html=True)

        # Personality Tag + Color
        max_trait = max([(tech, "Logical Thinker"), (creativity, "Creative Mind"), (people, "People Person"),
                         (leadership, "Leader Type"), (design, "Visual Thinker")])[1]
        color = personality_colors[max_trait]
        st.markdown(f"<p style='color:{color}; font-size:20px;'>🧠 Personality Tag: <b>{max_trait}</b></p>", unsafe_allow_html=True)

        # Recommended Subjects
        st.markdown(f"<p class='{text_class}'><b>📘 Subjects to Focus On for {top_career}:</b></p>", unsafe_allow_html=True)
        for subj in recommended_subjects[top_career]:
            st.markdown(f"<p class='{text_class}'>• {subj}</p>", unsafe_allow_html=True)

        # Year-by-year plan
        st.markdown(f"<p class='{text_class}'><b>📅 Year-by-Year Plan for {top_career}:</b></p>", unsafe_allow_html=True)
        for i, year in enumerate(range(start_year, end_year + 1)):
            if i < len(career_plans[top_career]):
                st.markdown(f"<p class='{text_class}'>{year}: {career_plans[top_career][i]}</p>", unsafe_allow_html=True)

        # Motivational quote
        quote = random.choice([
            "💡 Choose a job you love, and you’ll never work a day in your life.",
            "🚀 The future depends on what you do today.",
            "🌟 Your career will be as great as your passion.",
            "🎯 Success doesn’t come from what you do occasionally, it comes from what you do consistently.",
            "💪 Believe in yourself and all that you are."
        ])
        st.markdown(f"<br><i>{quote}</i>", unsafe_allow_html=True)