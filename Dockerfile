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

RUN type -p curl >/dev/null || apt install curl -y \
 && curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
 && chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
 && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
 && apt update \
 && apt install gh -y

COPY --chmod=755 start.sh /workspace/

CMD ["./start.sh"]
# && code-server \
#  --install-extension ms-python.python \
#  --install-extension ms-ceintl.vscode-language-pack-ja
