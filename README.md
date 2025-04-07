# My Local GPT Chat Application

This is a simple Streamlit-based application that uses the LangChain library and the Ollama language models to provide a conversational chatbot interface. The app allows users to configure various parameters for the model via a sidebar and interact with the chatbot in real-time

## Features

* Interactive GPT chat interface with previous messages displayed.
* Model parameter customization via Streamlit sidebar, allowing the adjustment of various language model settings such as temperature, top-k, and top-p.
* Real-time streaming of the model’s responses.

## Prerequisites

* Ollama local model: pull your favorite models [here](https://ollama.com/library).
* Python 3.9 or higher

### Usage

1.	**Clone the repository:**
```bash
git clone https://github.com:userID/local-chatbot.git
cd local-chatbot
```

2.	**Download dependencies:**
```bash
pip install -r requirements.txt
```

2.	**Run:**
```bash
make run
```

3. **Open your browser and navigate to ```http://localhost:8501``` to access the chat interface.**

## Customization

You can customize the behavior of the language model by adjusting the parameters in the sidebar. These parameters include:

* Model type
* Temperature
* Mirostat settings (eta, tau)
* Context size
* Top-K, Top-P
* And more…

Refer to the sidebar in the app for more details.

## Files

* ```app.py```: The main application file that runs the Streamlit app.
* ```scripts/sidebar.py```: Contains the logic for the sidebar configuration and model instantiation.
* ```Makefile```: Contains shortcuts for running the application.

### Contribution
If you’d like to contribute to the development of this project, please feel free to submit a pull request or open an issue

## License

This project is licensed under the MIT License.
