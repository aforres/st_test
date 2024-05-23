import streamlit as st

st.title('DRAFT ONLY Resources News')
#st.sidebar.title('Navigation')
nav=st.sidebar.radio('Navigation',['Home','Agriculture','Energy'])

if nav == 'Home':
    st.write('Home')
    st.write('Just A Blank Page - see Energy')
    
    # Header
    st.header("Main header")

    # Subheader
    st.subheader("This is a subheader")

    # Markdown
    st.markdown("This is markdown **text**")
    st.markdown("# Header1")
    st.markdown("## Header 2")
    st.markdown("### Header 3")

    # Caption
    st.caption("This is a caption")

    # Code block
    st.code("""import pandas as pd
    pd.read_csv(my_csv_file)
    """)

    # Preformatted text
    st.text("Some text")

    # LaTeX
    st.latex("x = 2^2")

    # Divider
    st.text('Text above divider')
    st.divider()
    st.text('Text below divider')

    #st.write
    st.write('Some text')

if nav == 'Agriculture':
    st.write('Agriculture')
    st.write('Just A Blank Page - see Energy')
    


if nav == 'Energy':
    st.write('Energy')

    st.subheader("Work Underway to Upgrade High-Voltage Power System in Northwest Ohio")

    st.markdown("Monday - May 13: (RWE) - American Transmission Systems, Inc. (ATSI), a subsidiary of " 
    "FirstEnergy Corp. (NYSE: FE), has started construction to upgrade a 138-kilovolt " 
    "substation in Lucas County's Springfield Township and reconfigure connecting high-voltage " 
    "power lines. The combined work will enhance reliability for nearly 23,000 customers of " 
    "Toledo Edison in the area. \n\n" 

    "ATSI will expand the substation on company-owned property by "
    "17,870 square feet, a 58% increase in the size of its footprint, to install new equipment "
    "– including new automated devices – that will allow the company to enhance and reorganize "
    "the existing transmission lines. This will help reduce the number of power outages that "
    "customers experience and make it easier for the station to be maintained without power "
    "interruptions. \n\n"
                
    "Carl Bridenbaugh, FirstEnergy's Vice President of Transmission: 'This "
    "upgrade to our substation and connecting lines will help prevent outages for thousands of " 
    "Toledo Edison customers in northwest Ohio while providing us with the flexibility we need "
    "to provide safe, reliable power in the future.' ATSI also will upgrade more than 10 miles "
    "of existing transmission lines that connect to the substation and construct a one-mile "
    "section of new line. The new configuration will eliminate potential sources of service "
    "interruptions. "
    ,
        )
