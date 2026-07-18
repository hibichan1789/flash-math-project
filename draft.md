# フラッシュ数学構想

ただの整数の足し算引き算じゃおもん無いから、積分とか微分とかのものの解の和を答え合わせできるアプリ  
割と実用的であると考えられる

## 目的
React(SPA)の復習、超軽量アプリの作成練習、DevContainer開発練習、テストコード(Unit Testのみ)、CI/CDの練習

## 構成
- フロントエンド  
Vite TypeScript React Tailwind CSS Static Web Apps(最初は側だけめっちゃ軽くだけ作ってgithub actionsでCI/CDの練習をしたいかも)
- バックエンド  
Python Azure Functions(サーバーレスでいきたいし、数学計算)
- DB  
CosmosDB(RDBを使うまでもないのでは)
- 開発環境  
開発環境はDevcontainerを用いてAzureFunctionsのみDockerコンテナで開発する

## フォルダ構成最終目標案
```
flash-math-project/
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.ts
│
├── backend/
│   ├── host.json
│   ├── local.settings.json    # ローカルの環境変数が入るGit管理しない
│   ├── requirements.txt
│   ├── function_app.py
│   │
│   ├── api/
│   │   ├── question.py
│   │   ├── answer.py
│   │   └── health.py           # 動作確認用
│   │
│   ├── services/
│   │   ├── generator.py
│   │   ├── checker.py
│   │   └── score_service.py
│   │
│   ├── domain/
│   │   ├── models.py
│   │   ├── enums.py
│   │   └── exceptions.py
│   │
│   ├── infrastructure/
│   │   ├── cosmos.py       
│   │   └── settings.py     # 環境変数をここで読み込み定数に入れておく
│   │
│   ├── tests/
│   │   ├── test_generator.py
│   │   ├── test_checker.py
│   │   └── test_score.py
│   │
│   └── shared/
│       ├── utils.py
│       └── constants.py
│
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
│
├── .github/
│   └── workflows/
│       ├── frontend.yml
│       └── backend.yml
│
└── README.md
```

最初は認証とかは緩めに行きたいかもしれない
のちのちEntraID認証とかを入れたいかもしれない