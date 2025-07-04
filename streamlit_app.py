import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# Initialize session state variables
if "number_to_guess" not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

st.write("I have selected a number between 1 and 100. Can you guess it?")

# Input from user
guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    if not st.session_state.game_over:
        st.session_state.attempts += 1
        if guess < st.session_state.number_to_guess:
            st.warning("Too low! Try again.")
        elif guess > st.session_state.number_to_guess:
            st.warning("Too high! Try again.")
        else:
            st.success(f"🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts.")
            st.session_state.game_over = True

if st.session_state.game_over:
    if st.button("Play Again"):
        # Reset the game
        st.session_state.number_to_guess = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.experimental_rerun()
