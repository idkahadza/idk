import streamlit as st

# Initialize the website's memory trackers
if "step" not in st.session_state:
    st.session_state.step = 1

# --- STEP 1 ---
if st.session_state.step == 1:
    st.write("Hallo!")
    answer1 = st.text_input("Say Hallo back!", key="hallo_input")
    
    if answer1:
        if answer1.strip() == "Hallo":
            st.write("Hallo! Who are you?")
            if st.button("Continue", key="btn1"):
                st.session_state.step = 2
                st.rerun()
        else:
            st.write("Meanie! Say it back!")

# --- STEP 2 ---
elif st.session_state.step == 2:
    answer2 = st.text_input("To verify your identity, please enter the code", key="code_input")
    
    if answer2:
        clean_code = answer2.strip()
        if clean_code == "YXL00PNOKOEI":
            st.session_state.step = 3
            st.rerun()
        elif clean_code == "NOA02NOAKINC":
            st.session_state.step = 5
            st.rerun()
        else:
            st.write("Incorrect code. Please try again.")

# --- STEP 3 ---
elif st.session_state.step == 3:
    st.write("Azure! Welcome! Happy Birthday!")
    answer3 = st.text_input("When is your birthday?", key="bday_input")
    
    if answer3:
        if answer3.strip() == "October 9":
            st.write("Azure! Sorry for the inconvenience!")
            if st.button("Continue", key="btn3"):
                st.session_state.step = 4
                st.rerun()
        else:
            st.write("Incorrect date. Please try again.")

# --- STEP 4 ---
elif st.session_state.step == 4:
    answer4 = st.text_input("Wanna know some cool fact? (Type anything except No)", key="fact_input")
    
    if answer4:
        if answer4.strip() == "No":
            st.write("I see, visit this later!")
        else:
            st.write("It is 1 year since we met!, time flies!")
            st.write("If you are Azure, please DM me for your gift, \n\nIf you are Timey, thank you for trying this out!")

# --- STEP 5 ---
elif st.session_state.step == 5:
    st.write("Timey! Welcome! Happy Birthday!")
    st.write("If you are Azure, please DM me for your gift, \n\nIf you are Timey, thank you for trying this out!")
