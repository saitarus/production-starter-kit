# 標準作業ディレクトリ・テンプレート

このディレクトリは、Webアプリケーション開発およびAIエージェント共同作業における**標準体制（公開分離・多層防御・ルート汚染防止）**のベーステンプレートです。

## ディレクトリ構成
```text
├── AGENTS.md        # プロジェクト固有ルール・構成定義
├── .gitignore       # 標準除外設定（node_modules, .env, *.sqlite, *.log, OSゴミ）
├── .env.example     # 環境変数サンプル
├── public/          # 公開Web画面（HTML, JS, CSS, 画像, 多層防御.htaccess）
├── server/          # バックエンドAPI（直接アクセス遮断.htaccess）
├── config/          # 設定ファイル・サービス定義（直接アクセス遮断.htaccess）
├── data/            # データベース領域（直接アクセス遮断.htaccess）
├── scripts/         # 配備・ビルド・運用スクリプト
├── test_scripts/    # テスト・検証スクリプト
└── archive/         # 旧資産・旧ドキュメント退避用（直接アクセス遮断.htaccess）
```

## 新規プロジェクトの作成方法
同じフォルダの `create-standard-workspace.ps1` を使用してください。

```powershell
# 例: 新規プロジェクト「204_my_project」を作成
d:\LANCERS\_template_workspace\create-standard-workspace.ps1 -ProjectName "204_my_project"
```
自動的に以下が行われます：
1. `d:\LANCERS\<ProjectName>` の作成
2. テンプレート一式（多層防御 .htaccess 群を含む）のコピー
3. `AGENTS.md` のプロジェクト名・日付の自動置換
4. `git init` および初回初期コミット
