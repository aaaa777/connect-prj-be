FROM debian:11

COPY ./requirements.txt /app/

RUN apt update && apt install -y python3 python3-pip\
 && mkdir -p /app/files && cd /app \
 && pip install -r requirements.txt

RUN apt update \
 && apt install -y net-tools curl git wget nano build-essential 

COPY ./main.py /app/

WORKDIR /workspace

RUN git clone https://github.com/aaaa777/connect-prj-be.git

RUN wget https://aka.ms/vscode-server-launcher/aarch64-unknown-linux-gnu \
 && chmod +x aarch64-unknown-linux-gnu && mkdir -p /usr/local/lib/vscode-server \
 && mv aarch64-unknown-linux-gnu /usr/local/lib/vscode-server/ \
 && ln -s /usr/local/lib/vscode-server/aarch64-unknown-linux-gnu /usr/local/bin/vscode-server

COPY --chmod=755 start.sh /workspace/

CMD ["./start.sh"]
# && code-server \
#  --install-extension ms-python.python \
#  --install-extension ms-ceintl.vscode-language-pack-ja
