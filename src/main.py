import langchain_helper as lch
import streamlit as st 

st.title("Pets name generator")

user_animal_type = st.sidebar.selectbox("What is your pet?", ("Cat","Dog", "Bird", "Hamster", "Snake", "Rabbit"))

if user_animal_type == "Cat":
    pet_color = st.sidebar.text_area(label="What color is your cat? Press CTRL+ENTER", max_chars = 15)

if user_animal_type == "Dog":
    pet_color = st.sidebar.text_area(label="What color is your dog? ress CTRL+ENTER", max_chars = 15)

if user_animal_type == "Bird":
    pet_color = st.sidebar.text_area(label="What color is your bird? ress CTRL+ENTER", max_chars = 15)

if user_animal_type == "Hamster":
    pet_color = st.sidebar.text_area(label="What color is your hamster? ress CTRL+ENTER", max_chars = 15)

if user_animal_type == "Snake":
    pet_color = st.sidebar.text_area(label="What color is your snake? ress CTRL+ENTER", max_chars = 15)

if user_animal_type == "Rabbit":
    pet_color = st.sidebar.text_area(label="What color is your rabbit? ress CTRL+ENTER", max_chars = 15)

if pet_color:
    response = lch.generate_pet_name(user_animal_type, pet_color)
    st.text(response)