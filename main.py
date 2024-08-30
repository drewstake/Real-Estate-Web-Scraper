import streamlit as st
from scrape import (scrape_website, split_dom_content, clean_body_content, extract_body_content)
from parse import parse_with_ollama

# Set the title of the Streamlit app
st.title("Real Estate Web Scraper")

# Input box for the user to enter a website URL
url = st.text_input("Enter a website URL: ")

# Button to trigger the scraping process
if st.button("Scrape Site"):
    st.write("Scraping the website")

    # Scrape the website content
    result = scrape_website(url)
    # Extract body content from the HTML
    body_content = extract_body_content(result)
    # Clean the body content (remove scripts, styles, etc.)
    cleaned_content = clean_body_content(body_content)

    # Store the cleaned DOM content in session state
    st.session_state.dom_content = cleaned_content

    # Expandable section to view the cleaned DOM content
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

# Check if there is content stored in session state
if "dom_content" in st.session_state:
    # Text area for the user to describe what they want to parse from the content
    parse_description = st.text_area("Describe what you want to parse?")

    # Button to trigger the parsing process
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            # Split the DOM content into chunks to handle large content
            dom_chunks = split_dom_content(st.session_state.dom_content)
            # Parse the content using the description provided by the user
            result = parse_with_ollama(dom_chunks, parse_description)
            # Display the parsed results
            st.write(result)
