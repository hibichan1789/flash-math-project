# .devcontainer/Dockerfile
FROM mcr.microsoft.com/devcontainers/python:3.11

# 開発に必要なツールとNode.jsのインストール
RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    && curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*



# 実行ユーザーをrootからvscodeに変更
USER vscode

# 作業ディレクトリ
WORKDIR /workspace

# npmのグローバルインストール先をユーザーのホームディレクトリに変更してPATHを更新
# 権限エラー回避のため、 npmのグローバルインストール先をユーザーのホームディレクトリに変更している
RUN mkdir -p /home/vscode/.npm-global \
    && npm config set prefix '/home/vscode/.npm-global' \
    && echo 'export PATH=/home/vscode/.npm-global/bin:$PATH' >> /home/vscode/.bashrc

# Azure Functions Core ToolsとAzuriteのインストール
RUN npm install -g \
    npm@latest \
    azure-functions-core-tools@4 \
    azurite

# デフォルトコマンド
CMD ["sleep", "infinity"]