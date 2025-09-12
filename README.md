# LLM Chat CLI

## Overview
LLM Chat CLI is a command-line interface application that allows users to interact with a large language model (LLM) by sending prompts and receiving responses. This project serves as a simple yet effective way to leverage LLM capabilities directly from the terminal.

## Project Structure
```
llm-chat-cli
├── src
│   ├── main.py          # Entry point of the application
│   ├── llm_client.py    # Contains the LLMClient class for API interactions
│   └── utils.py         # Utility functions for input validation and formatting
├── requirements.txt      # Lists project dependencies
├── .gitignore            # Specifies files to ignore in version control
└── README.md             # Documentation for the project
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd llm-chat-cli
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To start the application, run the following command in your terminal:
```
python src/main.py
```

You will be prompted to enter your question. Type your question and press Enter. The application will send your prompt to the LLM and display the response.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.