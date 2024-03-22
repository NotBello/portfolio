import streamlit as st

st.set_page_config(page_title="My Portfolio")



with st.container():
    st.header("Hello there, I'm Venujan Malaiyandi :wave:")
    st.write('A cyber-security student at the crossroads of offensive security, IoT and machine learning')

value = 30
st.progress(value, text="Website Development Progress: 30%")

st.write("---")
with st.container():
    st.title("My Projects")
    st.header("SSH Brute Forcer - Offensive Pentesting Tool")
    st.write("I created a console based bruteforcing application for knocking down your SSH port :)")
    st.write("Though you still need a good list")
    st.write("Libraries Used: pexpect")
    st.write("Language Used: Python 3")
    st.link_button("Repo", "https://github.com/NotBello/ssh-brute")

    st.header("Automated SSH Command Parser")
    st.write("As a proof of concept for future program, I created an automation program in python to login into target hosts via ssh and pass terminal commands.")
    st.write("Libraries Used: pexpect")
    st.write("Language Used: Python 3")
    st.link_button("Repo", "https://github.com/NotBello/automated-ssh-command-passer")

    st.header("Custom Vulnerability Scanner")
    st.write("I wanted to know how smart was your average nmap tool. And so I created my own. Listens for the server banner and compares it with a list of vulnerable services and versions")
    st.write("To get the best of this tool, populate the list with the common vulnerable services.")
    st.write("Libraries Used: socket, os, sys")
    st.write("Language Used: Python 2")
    st.link_button("Repo", "https://github.com/NotBello/vulnerability-scanner")

    st.header("Port Scanner")
    st.write("I wanted to know how smart was your average nmap tool. And so I created my own. Listens for the server banner and compares it with a list of vulnerable services and versions")
    st.write("To get the best of this tool, populate the list with the common vulnerable services.")
    st.write("Libraries Used: socket, os, sys")
    st.write("Language Used: Python 2")
    st.link_button("Repo", "https://github.com/NotBello/vulnerability-scanner")

    st.header("Network Analysis on Vulnerable networks")
    st.write("Conducted on analysis in behavior on SDN networks under attack, based on real life topologies. Setup labs using mininet and onos controller")
    st.write("Softwares Involved: mininet, onos controller, iperf, jperf, low orbit ion cannon")

with st.container():    
    st.title("My Tech Stack")
    st.header("Offensive Security :skull_and_crossbones:")
    st.write("""
            - Enumeration
                - Nmap
                - WireShark
            - SQL exploit
                - SQLmap
            - Directory enumeration
                - dirbuster
                - gobuster
                - Hydra
            - Web penetration
                - Burp Suite
                - Zaproxy (OWASP)
                - wp\-scan
            - Server listening
                - NetCat
            - Windows Priviledge Escalation
                - Winpeas    
             """)

    st.header("Machine Learning :brain:")   
    st.write("""
            - Classic Machine Learning
                - Linear Regression
                - Linear Classification
                - Polynomial Regression
                - Support Vector Machines
                - K-Nearest Neighbours
                - Decision Trees
                - Random Forest Tree Clustering
                - Kmeans Clustering
                - Agglomerative Hierarchical Clustering
                - DBSCAN
            - Feature Selection
            - Hyper Parameter Tuning
            """)
             
    st.header("Data Analytics :bar_chart:")   
    st.write("""
            - Database
                - Microsoft SQL Server 19,22
                - PostgreSQL
                - MySQL
                - Oracle DB
                - Microsoft Excel
            - Database management
                - SQL Server Management Studio 19
                - Dbeaver
                - PgAdmin
            - Database migration
                - Talend
                - Apache Nifi
            - Dashboarding
                - PowerBI
                - Apache SuperSet
            """)

    st.header("Programming :gear:")   
    st.write("""
            - Programming Paradigms
                - Functional Programming
                - Object Oriented Development

            - Programming Langauges
                - Python
                - C#
                - C++
                - Java
                - ASM x86

            """)

    st.header("Web dev :computer:")
    st.write("""
                - HTML 5
                - Bootstrap CSS
                - Vanila JS
                - Python 
             """)
    

with st.container():
    st.write("---")
    st.title("About Me")
    st.write("""
                Greetings! I'm Venujan Malaiyandi, but you may know me as 'Bello'. I hail from the vibrant lands of Sri Lanka but spent my formative years soaking in the bustling energy of Chennai. With a passion for continuous learning and exploration, I've eagerly delved into the realm of technology, honing my skills and nurturing my curiosity every step of the way.

During my undergraduate journey, my focus has been on the intriguing intersection of offensive web security and classical machine learning techniques, with a burgeoning interest in the depths of deep learning. My ultimate aim? To seamlessly blend offensive security practices with the power of deep learning algorithms.

Alongside my academic pursuits, I've eagerly pursued certifications in diverse areas such as AR/VR, SEO, and administration, all in a quest to discover where my true passion lies within the vast landscape of technology.

But wait, there's more! I'm absolutely captivated by the world of autonomous systems, UAVs, and drones—particularly within the realm of defense technology.

With boundless enthusiasm and a relentless drive for innovation, I'm excited to embark on this journey of exploration, discovery, and creation within the ever-evolving tech landscape. Let's connect and discover the endless possibilities together
             """)
    email_address = "venujan42@gmail.com"
    email_link = f"[Let's connect and discover the endless possibilities together!](mailto:{email_address})"
    st.markdown(email_link, unsafe_allow_html=True)


st.write("---")
