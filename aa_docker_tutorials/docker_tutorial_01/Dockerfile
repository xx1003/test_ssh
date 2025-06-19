# Dokerfile 새롭게 만들기

# Docker-Compose.yml

FROM python:3.10-slim

WORKDIR /app

# 이 파일을 app다가 복사하겠다
COPY requirements.txt .
RUN pip install -r requirements.txt

# 현재 디렉터리에 있는 모든 파일을 app에 다 복사?
COPY . .

# streamlit과 관련이 있는 포트번호
EXPOSE 8501

# 서버 포트번호 생김..?
CMD ['streamlit', 'run', 'app.py', '--server.port=8501', '--server.address=0.0.0.0']