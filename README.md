# フラッシュ数学アプリ

## 学んだこと
コンテナにgitを入れるときに権限問題が発生した,それの解決のためにdevcontainer.jsonにremoteUserの設定を入れた  
git initをしたときにデフォルトではmasterブランチが作られるためdockerfile内に
```Dockerfile
RUN git config --global init.defaultBranch main
```
をいれることでdevcontainer内でgit initをしたときにmainブランチが作られるようにした

