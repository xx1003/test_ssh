# api만 관리하는 도커파일
FROM python:3.10-slim

# 내가 만드는 건데, docker compose 파일의 volumes 부분의 ./app:/app 여기에 : 뒷부분이 컨테이너 app 부분이니까 둘이 같아야 함 뭔말?
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ['uvicorn', 'api:app', '--host', '0.0.0.0', '--port', '8000']