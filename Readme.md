# PDF and CSV Reader

This application allows you to upload and analyze PDF and CSV files using a web interface.

## Dependencies

Before running the application, make sure you have the following dependencies installed:

- langchain: A library for working with language models and embeddings.
- streamlit: A framework for building web applications.
- pandas: A library for data manipulation and analysis.

You can install the dependencies by running the following command:

```shell
pip install langchain streamlit pandas
```

## How to Use

1. **Upload a File**: Click the "Upload a file" button and select a PDF or CSV file from your computer.

2. **Ask a Question (PDF)**: If you uploaded a PDF file, you can enter a question in the "Ask a Question about the Uploaded PDF" input box and click Enter. The application will use artificial intelligence to provide an answer based on the content of the PDF.

3. **View Document Similarity (PDF)**: The application also performs a document similarity search based on your question. The most similar page from the PDF will be displayed.

4. **View CSV Data**: If you uploaded a CSV file, the application will display the entire content of the CSV file in a table format. You can scroll through the data to explore its contents.

5. **Filter Data (CSV)**: To filter the CSV data, use the sidebar on the left. Select one or more columns to filter by, and the application will display the filtered data based on your selection. If no filters are applied, the original CSV data will be shown.

**Note:** Before using the application, make sure you have the necessary dependencies installed. You can install them by following the installation instructions in the [repository](https://github.com).

## API Keys

To use this application, you need to set up API keys:

- **OpenAI API Key**: Insert your OpenAI API key in the code to enable the artificial intelligence-based question-answering functionality.

- **SerpAPI Key**: Insert your SerpAPI key in the code if you want to include additional features or services.

Make sure to replace the placeholders `'Insert OpenAI API Key Here'` and `'Insert Serpai API Key Here'` with your actual API keys.

## Running the Application

To run the application:

1. Clone the repository from GitHub.

2. Install the necessary dependencies by following the installation instructions in the repository.

3. Open the command line or terminal and navigate to the project directory.

4. Run the following command: `streamlit run your_app.py`

Replace `your_app.py` with the actual filename of the Python script containing the code for the application.

Enjoy exploring and analyzing your PDF and CSV files with this user-friendly application!

