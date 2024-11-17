run:
	ollama serve &
	streamlit run app.py

streamlit:
	streamlit run app.py

ollama:
	ollama serve

# make sure to pull the models declared in the model_type
pull-model:
	@read -p "Enter the name of the template to download: " model_name; \
	ollama pull $$model_name