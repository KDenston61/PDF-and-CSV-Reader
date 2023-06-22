# Import os to set API key
import os
# Import OpenAI as main LLM service
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
# Bring in streamlit for UI/app interface
import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo
)
import pandas as pd
from io import StringIO

# Set API key for OpenAI Service
# Can substitute this with other LLM providers
os.environ['OPENAI_API_KEY'] = 'Insert OpenAI API Key Here'

# Set SerpAPI key
serpapi_key = 'Insert Serpai API Key Here'

# Create instance of OpenAI LLM
llm = OpenAI(temperature=0.9)
embeddings = OpenAIEmbeddings()

st.title('PDF and CSV Reader')
# Create a text input box for the user
prompt = st.text_input('Ask a Question about the Uploaded PDF')

# Add an upload button for files in the Streamlit app
uploaded_file = st.file_uploader("Upload a file", type=["pdf", "csv"])

# If a file is uploaded
if uploaded_file:
    file_extension = uploaded_file.name.split(".")[-1].lower()

    if file_extension == "pdf":
        # Load the PDF document from the uploaded file
        pdf_data = uploaded_file.read()

        # Create a temporary file name
        temp_filename = "uploaded_file.pdf"

        # Save the uploaded file as a temporary PDF file
        with open(temp_filename, "wb") as file:
            file.write(pdf_data)

        # Create and load PDF Loader with the uploaded file
        loader = PyPDFLoader(temp_filename)

        # Split pages from the PDF
        pages = loader.load_and_split()

        # Load documents into vector database aka ChromaDB
        store = Chroma.from_documents(pages, embeddings, collection_name='uploaded_pdf')

        # Create vectorstore info object - metadata repo?
        vectorstore_info = VectorStoreInfo(
            name="uploaded_pdf",
            description="uploaded PDF document",
            vectorstore=store
        )

        # Convert the document store into a langchain toolkit
        toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)

        # Add the toolkit to an end-to-end LC
        agent_executor = create_vectorstore_agent(
            llm=llm,
            toolkit=toolkit,
            verbose=True
        )

        # If the user hits enter
        if prompt:
            # Then pass the prompt to the LLM
            response = agent_executor.run(prompt)
            # ...and write it out to the screen
            st.write(response)

            # With a streamlit expander
            with st.expander('Document Similarity Search'):
                # Find the relevant pages
                search = store.similarity_search_with_score(prompt)
                # Write out the first
                st.write(search[0][0].page_content)

    elif file_extension == "csv":
        # Read the raw CSV file data
        raw_data = uploaded_file.read()

        # Load the CSV data as a Pandas DataFrame
        csv_data = pd.read_csv(StringIO(raw_data.decode()))

        # Display the entire CSV document
        st.write("CSV Document:")
        st.dataframe(csv_data.style)

        # Display basic statistical information about the data
        st.write("Description of the Data:")
        st.write(csv_data.describe())

        # Get filter options from the columns
        filter_options = csv_data.columns.tolist()

        # Add sidebar filter
        selected_filters = st.sidebar.multiselect("Filter by Column(s)", filter_options)

        # Apply filters to the data
        filtered_data = csv_data[selected_filters]

        # Display the filtered data
        if len(selected_filters) > 0:
            st.write("Filtered Data:")
            st.dataframe(filtered_data)
        else:
            st.write("No filters applied.")


else:
    st.write("Please upload a PDF or CSV file.")
