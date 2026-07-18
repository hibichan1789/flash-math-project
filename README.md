# フラッシュ数学アプリ

## 必要な環境
- Docker Desktop
- Visual Studio Code
- Dev Containers拡張機能

## セットアップ方法
### これは絶対に行ってください
```bash
cp setup-git.sh.example setup-git.sh
```
setup-git.shの中のyour-nameとsample.@example.comを自分の名前とメールアドレスに書き換える  

### devconainerを開く
VSCodeでこのリポジトリを開き、左下の **><** のアイコンをクリックし、"Reopen in Container"を選択することでdevcontainerを開くことができる  

### Azure Functionsの環境と実行方法
#### 以下のコマンドはすべてdevcontainer内のbackendディレクトリで実行する必要がある  
```bash
cd workspace/backend
```
#### pythonの仮想環境を作成しライブラリのインストールのため下のコマンドを実行する
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
#### local.settings.json.exampleをlocal.settings.jsonにコピーして環境変数の設定をする
```bash
cp local.settings.json.example local.settings.json
```
#### azurite を使ってローカルでAzure Functionsを実行するために下のコマンドを実行する
```bash
azurite --silent
```
#### 別ターミナルでazure functionsをローカルで実行するために下のコマンドを実行する
```bash
func start --python
```

### Azure Login方法
#### 以下のコマンドを実行してログインしサブスクリプションの選択を数字でする
```bash
az login
```
#### サブスクリプションの確認
```bash
az account show
```
### Azure Functions デプロイ方法
```bash
func azure
```

## 学んだこと
コンテナにgitを入れるときに権限問題が発生した,それの解決のためにdevcontainer.jsonにremoteUserの設定を入れた  
git initをしたときにデフォルトではmasterブランチが作られるためdockerfile内に
```Dockerfile
RUN git config --global init.defaultBranch main
```
をいれることでdevcontainer内でgit initをしたときにmainブランチが作られるようにした  
```bash
git commit -m "first commit"
```
をするときに初回はemailとnameの設定が必要になるためdevcontainerを開いて初回実行するときは
```bash
git config --global user.email "your-email@example.com"
git config --global user.name "Your Name"
```
を実行する必要がある  
このコマンドも打つのがめんどくさそうであるが、セキュリティ上の理由でdevcontainer.jsonに入れることはできないため、初回実行時に手動で打つ必要がある

AzureFunctionsのプロジェクト作成するために
```bash
cd workspace/backend
func init --python
```
を実行しプロジェクトの作成をする

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
を実行しライブラリのインストールをする