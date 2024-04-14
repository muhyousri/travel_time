From python:3.11-slim

RUN useradd -ms /bin/bash admin
RUN chown -R admin:admin /home/admin
COPY main.py requirments.txt ./
RUN chmod +x main.py
ENV TZ=Europe/Dublin
RUN pip install -r requirments.txt
USER admin
ENTRYPOINT ["./main.py"]
