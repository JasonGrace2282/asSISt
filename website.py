import streamlit as st

def main():
    st.title("asSISt")

    # About Section
    st.markdown("""
        **<font color=purple>About</font>**

        *<font color=purple>asSISt</font>* is an open source software designed for students attending school districts that use **StudentVUE by Synergy**. 
        This project, built for *<font color=purple>HackTJ</font>*, aims to simplify students' lives by providing a system to calculate grades on the go. 
        Our mission is to empower students to allocate their time efficiently to classes that need it most, avoiding wasted effort.
    """, unsafe_allow_html=True)

    # How to Use Section
    st.markdown("""
        **<font color=blue>How to Use</font>**

        To use our program, follow these steps:

        1. Click [<font color=blue>this link</font>](https://github.com/JasonGrace2282/hacktj24) to access the project on GitHub.
        2. Scroll down and follow the installation instructions below.
        3. Run "main.py".

        Once the program is running, enter your **Username**, **Password**, and the domain of your studentvue website (e.g., "sisstudent.fcps.edu/SVUE").

        Next, choose a subject to simulate grades for. You can view your grades normally and add custom assignments to simulate your grades. 
        To add custom assignments, click the plus sign and fill out the simulated grade's name, points possible, points earned, and weight category. 
        This will create a new simulated grade that factors into your class grade average.

        This feature helps users to anticipate their grades before teachers input them into the gradebook. It also allows for scenario planning and 
        strategizing study time allocation based on grade priorities.
    """, unsafe_allow_html=True)

    # HackTJ Section
    st.markdown("""
        **<font color=black>More info about [HackTJ](https://hacktj.org)</font>**
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()