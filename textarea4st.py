import streamlit as st
import pandas as pd

st.title("Alastair's Test Template")
#st.sidebar.title('Navigation')
nav=st.sidebar.radio('Navigation',['Home','Other','Yet Another'])

if nav == 'Home':
    st.write('Home Page')
    st.write('Just A Blank Page - well sort of blank')
    st.write('Well no, actually')


    st.header("Line Chart")
    
    data = {"a":[23, 12, 78, 4, 54], "b":[0, 13 ,88, 1, 3], 
    "c":[45, 2, 546, 67, 56]}
    
    df = pd.DataFrame(data)
    df
    st.line_chart(data=df)    
    
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
    st.markdown("### Python code embedded")
    st.code("""import pandas as pd
    pd.read_csv(my_csv_file)
    """)

    # Preformatted text
    st.text("Some text")

    # LaTeX
    st.markdown("### algebraic notation")
    st.latex("x = 2^2")

    # Divider
    st.text('Text above divider')
    st.divider()
    st.text('Text below divider')

    #st.write
    st.write('Some text')

if nav == 'Other':

    data = {"a":[23, 12, 78, 4, 54], "b":[0, 13 ,88, 1, 3], 
    "c":[45, 2, 546, 67, 56]}
    st.write('Other Page')
    st.write('Just A Blank Page')

    st.button("Click me")
    #st.download_button("Download file", data)
    #st.link_button("Go to gallery", url)
    #st.page_link("app.py", label="Home")
    st.data_editor("Edit data", data)
    st.checkbox("I agree")
    st.toggle("Enable")
    st.radio("Pick one", ["cats", "dogs"])
    st.selectbox("Pick one", ["cats", "dogs"])
    st.multiselect("Buy", ["milk", "apples", "potatoes"])
    st.slider("Pick a number", 0, 100)
    st.select_slider("Pick a size", ["S", "M", "L"])
    st.text_input("First name")
    st.number_input("Pick a number", 0, 10)
    st.text_area("Text to translate")
    st.date_input("Your birthday")
    st.time_input("Meeting time")
    st.file_uploader("Upload a CSV")
    st.camera_input("Take a picture")
    st.color_picker("Pick a color")

        # Sidebar section
    with st.sidebar:
      st.subheader('This is a Sidebar')
      st.write('Button with Balloons 🎈')
      if st.button('Click me!✨'):
        st.balloons()
      else:
        st.write(' ')
    


if nav == 'Yet Another':
    st.write('Yet Another Page')

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
