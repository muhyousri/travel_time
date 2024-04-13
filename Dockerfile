From python:3.11-slim

RUN useradd -ms /bin/bash admin
COPY main.py requirments.txt ./
RUN chmod +x main.py
RUN pip install -r requirments.txt
USER admin
CMD ["./main.py"]
