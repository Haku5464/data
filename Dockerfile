FROM python:3.8

WORKDIR /dashboard

COPY ./ ./

# Install dependencies and launch streamlit app.py
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port", "8501"]