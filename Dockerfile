FROM debian:10
ENV TZ="America/Mexico_City"
RUN apt update && apt install tzdata -y

# Install systemd, jq, and Python
RUN apt-get update && \
    apt-get install -y systemd jq python3 python3-pip && \
    apt-get clean

COPY convert.sh /usr/local/bin/convert_journal.sh
COPY hex_to_string.py /code/

RUN chmod +x /usr/local/bin/convert_journal.sh

# logs directory
WORKDIR /logs  

# Default command
CMD ["/usr/local/bin/convert_journal.sh"]