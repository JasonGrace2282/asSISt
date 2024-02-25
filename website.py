import streamlit as st

def main():
    progress_bar = st.progress(0)
    status_text = st.empty()
    chart = st.line_chart(np.random.randn(10, 2))

    for i in range(100):
        # Update progress bar.
        progress_bar.progress(i + 1)

        new_rows = np.random.randn(10, 2)

        # Update status text.
        status_text.text(
        'The latest random number is: %s' % new_rows[-1, 1])

    # Append data to the chart.
    chart.add_rows(new_rows)

    # Pretend we're doing some computation that takes time.
    time.sleep(0.1)

status_text.text('Done!')
st.balloons()
    
    st.title("About Project")

    # About Section
    st.markdown("""
        **<font color=blue>About</font>**

        *<font color=purple>PROJECT NAME</font>* is an open source software designed for students attending school districts that use **StudentVUE by Synergy**. 
        This project, built for *<font color=blue>HackTJ</font>*, aims to simplify students' lives by providing a system to calculate grades on the go. 
        Our mission is to empower students to allocate their time efficiently to classes that need it most, avoiding wasted effort.
    """, unsafe_allow_html=True)

    # How to Use Section
    st.markdown("""
        **<font color=green>How to Use</font>**

        To use our program, follow these steps:

        1. Click [<font color=green>this link</font>](https://github.com/JasonGrace2282/hacktj24) to access the project on GitHub.
        2. Scroll down and follow the installation instructions below.
        3. Run "main.py".

        Once the program is running, enter your **Username**, **Password**, and the domain of your studentvue website (e.g., "sisstudent.fcps.edu/SVUE").

        Next, choose a subject to simulate grades for. You can view your grades normally or add custom assignments to simulate your grades. 
        To add custom assignments, click the plus sign and fill out the simulated grade's name, points possible, points earned, and weight category. 
        This will create a new simulated grade that factors into your class grade average.

        This feature helps users to anticipate their grades before teachers input them into the gradebook. It also allows for scenario planning and 
        strategizing study time allocation based on grade priorities.
    """, unsafe_allow_html=True)

    # HackTJ Section
    st.markdown("""
        **<font color=red>More info about [HackTJ](https://hacktj.org)</font>**
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()