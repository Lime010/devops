FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
COPY templates ./templates
ENV APP_TITLE="조서빈의 DevOps 방명록" THEME_COLOR="#16a34a"
EXPOSE 5000
CMD ["python", "app.py"]
