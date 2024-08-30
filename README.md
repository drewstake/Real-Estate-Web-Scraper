# Real Estate Web Scraper

This project is a web scraper designed to extract and analyze real estate data from websites. It allows users to input a website URL, scrape relevant property details, and parse specific information such as price, address, square footage, and more. The scraper is equipped to handle CAPTCHA challenges using BrightData and utilizes Llama 3.1 from Ollama for advanced parsing.

## Features

- Scrape real estate data from various websites.
- Extract specific property details including price, address, square footage, and more.
- Handle CAPTCHA challenges using BrightData.
- Advanced data parsing with Llama 3.1 (via Ollama).
- User-friendly interface built with Streamlit.

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- **Python 3.8+**: Required to run the scripts.
- **Git**: Version control system to clone the repository.

## Getting Started

### 1. Clone the Repository

Clone the repository to your local machine using Git:

\```bash
git clone https://github.com/drewstake/Real-Estate-Web-Scraper.git
cd Real-Estate-Web-Scraper
\```

### 2. Set Up a Virtual Environment (Optional but Recommended)

It is recommended to create and activate a virtual environment to isolate your dependencies:

\```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS and Linux
python3 -m venv venv
source venv/bin/activate
\```

### 3. Install the Required Dependencies

Install the necessary Python packages by running:

\```bash
pip install -r requirements.txt
\```

### 4. Install BrightData for CAPTCHA Solving

This project uses BrightData to handle CAPTCHA challenges. Follow the instructions on the [BrightData website](https://brightdata.com/) to set up an account and install the necessary tools.

Ensure that you configure the CAPTCHA solver in your scraping script (`scrape.py`) with the correct API credentials.

### 5. Install and Set Up Ollama with Llama 3.1

Download and install Ollama from the [Ollama GitHub repository](https://github.com/ollama/ollama).

After installation, run the following command to download Llama 3.1:

\```bash
ollama run llama3.1
\```

Ensure that Llama 3.1 is set up and accessible in your environment.

### 6. Run the Streamlit App

Now you're ready to run the application:

\```bash
streamlit run main.py
\```

### 7. Use the Application

1. Open the app in your web browser using the URL provided in your terminal (usually `http://localhost:8501`).
2. Enter the URL of the real estate website you want to scrape.
3. Describe the specific details you want to extract in the text area provided.
4. Click "Scrape Site" and "Parse Content" to get the extracted data.

## Project Structure

- `main.py`: The main application file that runs the Streamlit app.
- `scrape.py`: Contains functions for scraping and cleaning web content, including CAPTCHA handling using BrightData.
- `parse.py`: Handles parsing of the scraped content using Llama 3.1 from Ollama.
- `requirements.txt`: Lists all the Python dependencies required for the project.

## Troubleshooting

- If you encounter any issues with scraping, make sure the target website is accessible and that CAPTCHA challenges are being properly handled by BrightData.
- Ensure that Llama 3.1 is correctly installed and accessible in your environment through Ollama.

## Contributing

Feel free to fork this repository and contribute. Please submit a pull request if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
