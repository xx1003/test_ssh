FROM python:3.10-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache -r requirements.txt
CMD ['streamlit', 'run', 'app/app.py', '--server.port=8501', '--server.address=0.0.0.0']