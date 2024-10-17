# Makefile for Stable Diffusion Web App

# Define Python version and virtual environment name
PYTHON_VERSION = 3.9.13
VENV_NAME = image-gen-webapp-venv


# Create virtual environment using pyenv
pyenv-setup:
	pyenv install $(PYTHON_VERSION) --skip-existing
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME) || echo "Virtual environment already exists."
	pyenv local $(VENV_NAME)

# Install dependencies
install:
	pip install --upgrade pip
	pip install -r requirements.txt

# Download the model
download-model:
	python download_model.py

# Run the application
run:
	streamlit run app.py

# Clean the environment
clean:
	pyenv uninstall -f $(VENV_NAME)
	rm -rf __pycache__
