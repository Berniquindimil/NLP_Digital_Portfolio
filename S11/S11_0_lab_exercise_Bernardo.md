# Create an Emotion-Based Chatbot with Ollama, Open WebUI, and Streamlit

## 1. **Prerequisites**
Before you begin, make sure you have the following installed:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Streamlit](https://streamlit.io/)
- [Python 3](https://www.python.org/)

## 2. **Set Up Ollama with Docker**

### 2.1. Create a Docker Container for Ollama

1. **Download and configure the Ollama and Docker image**.

2. **Copy paste Ollama on Docker Container**:
   Do a copy of the "Quick Start with Docker" link that is in the Open WebUI. And then, paste on the Docker terminal. The link is:
   ```bash
   docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main