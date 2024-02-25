import streamlit as st

def main():
    st.set_page_config(page_title="asSISt")

    # Display the title within the Streamlit app
    st.title("asSISt")

    # Page content without background color
    st.markdown(
        """
        <style>
            .w3-top {
                position: fixed;
                width: 100%;
                top: 0;
                z-index: 1000;
            }
            .w3-bar {
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            .w3-bar-item {
                padding: 8px 16px;
            }
            h1 {
                color: #4CAF50; /* Green color for h1 */
            }
            h2 {
                color: #2196F3; /* Blue color for h2 */
            }
            p {
                color: #FF9800; /* Orange color for paragraphs */
            }
            ol {
                color: #E91E63; /* Pink color for ordered lists */
            }
            footer {
                color: #000; /* Black color for footer text */
            }
        </style>
        <div style="padding: 20px;">
            <div class="w3-top">
                <div class="w3-bar w3-white w3-wide w3-padding w3-card">
                    <span class="w3-bar-item w3-button"><b>asSISt</b></span>
                </div>
            </div>
            <div class="w3-content" style="max-width:1564px">
                <div class="w3-container w3-padding-32" id="about">
                    <h1>About</h1>
                    <p>
                        <font color="purple">asSISt</font> is an open source software designed for students attending school districts that use
                        <strong>StudentVUE by Synergy</strong>. This project, built for <font color="purple">HackTJ</font>, aims to simplify students' lives by
                        providing a system to calculate grades on the go. Our mission is to empower students to allocate their time efficiently to
                        classes that need it most, avoiding wasted effort.
                    </p>
                    <h2>How to Use</h2>
                    <p>
                        To use our program, follow these steps:
                        <ol>
                            <li>Click <a href="https://github.com/JasonGrace2282/hacktj24" target="_blank">this link</a> to access the project on GitHub.</li>
                            <li>Scroll down and follow the installation instructions below.</li>
                            <li>Run "main.py".</li>
                        </ol>
                        Once the program is running, enter your <strong>Username</strong>, <strong>Password</strong>, and the domain of your studentvue website
                        (e.g., "sisstudent.fcps.edu/SVUE").
                        <br>
                        <br>
                        Next, choose a subject to simulate grades for. You can view your grades normally and add custom assignments to simulate your grades.
                        To add custom assignments, click the plus sign and fill out the simulated grade's name, points possible, points earned, and weight
                        category. This will create a new simulated grade that factors into your class grade average.
                        <br>
                        <br>
                        This feature helps users to anticipate their grades before teachers input them into the gradebook. It also allows for scenario
                        planning and strategizing study time allocation based on grade priorities.
                    </p>
                </div>
            </div>
        </div>
        """
        , unsafe_allow_html=True
    )
    # About Section
    st.markdown("""
        **<font color=purple>About</font>**

        *<font color=purple>asSISt</font>* is an open source software designed for students attending school districts that use **StudentVUE by Synergy**. 
        This project, built for *<font color=purple>HackTJ</font>*, aims to simplify students' lives by providing a system to calculate grades on the go. 
        Our mission is to empower students to allocate their time efficiently to classes that need it most, avoiding wasted effort.
    """, unsafe_allow_html=True)

    # How to Use Section
    st.markdown("""
        **<font color=green>How to Use</font>**

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

    # Footer
    st.markdown(
        """
        <footer class="w3-center w3-black w3-padding-16">
            <p style="font-size: 16px;">More info about <a href="https://hacktj.org" target="_blank" class="w3-hover-text-purple">HackTJ</a></p>
        </footer>
        """
        , unsafe_allow_html=True
    )

    st.markdown("""





""")




if __name__ == "__main__":
    main()