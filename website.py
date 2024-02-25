import streamlit as st

def main():
    st.title("About Project")

    st.markdown("""
        ### About
        PROJECT NAME is an open source software to be used by students who attend school districts that use StudentVUE by Synergy. 
        This project is built for HackTJ to make the lives of students easier. Our mission is to make a system that enables students to 
        calculate their grades anywhere on the go. With our technology, students can allocate their time to classes that need it most 
        and avoid wasting valuable effort.

        ### How to Use
        To use our program, start by clicking [on this link](https://github.com/JasonGrace2282/hacktj24). Scroll down and follow the 
        installation instructions below and run "main.py".

        To use our program, start by clicking on the link above. Follow the installation instructions below and run "main.py". Next, enter 
        in your Username and Password. Then enter in the domain of your studentvue website. For example, if you attend Fairfax County 
        Schools, you would enter the domain "sisstudent.fcps.edu/SVUE".

        Then, you choose a subject to simulate grades for. Once you've done that, you can view your grades normally, or you can add custom 
        assignments to simulate your grades. To do this, click the plus sign and then fill out the simulated grade's name, points possible, 
        points earned, and weight category. This will give you a new simulated grade that will factor into your class grade average.

        This feature helps our users to figure out their grades before their teachers put them into the gradebook, or work out scenarios and 
        strategize where to allocate your time when you study to make sure you can spread out your attention to where it's important.
    
        ### 
        ### 
        More info about [HackTJ](https://hacktj.org)

    """)

if __name__ == "__main__":
    main()