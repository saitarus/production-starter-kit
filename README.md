# Production Starter Kit 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Security: Defense in Depth](https://img.shields.io/badge/Security-Defense%20in%20Depth-green.svg)](docs/SECURITY_STANDARDS.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/saitarus/production-starter-kit/pulls)

**実稼働品質（プロダクションレディ）な開発環境を即座に立ち上げるための標準テンプレート＆セキュリティ基盤**

A production-ready starter kit and boilerplate framework designed for high-security, maintainable Web and Python application development.

---

## 🌟 主な特徴 (Features)

1. **多層防御セキュリティ (Defense in Depth)**
   - Web公開ディレクトリ（`public/`）の厳格な分離
   - サブディレクトリごとの `.htaccess` による機密ファイル・スクリプト遮断
   - `.env` などの環境変数・シークレット漏洩を未然に防ぐ厳格な `.gitignore`
2. **AI エージェント協調開発規約 (AI-Ready Standards)**
   - `AGENTS.md` による AI コーディングアシスタント向けの明確なコンテキスト設定
   - 「ルート汚染防止」「ゴール駆動の検証義務」「ピンポイント修正」の実践
3. **充実した GitHub 運用キット (GitHub Flow & CI)**
   - GitHub Actions による自動テスト・Lint ワークフロー
   - Issue テンプレート（Bug Report / Feature Request）
   - Pull Request テンプレート & Dependabot による依存関係自動監視

---

## 📁 ディレクトリ構成 (Architecture)

```text
production-starter-kit/
├── .github/                      # GitHub 運用設定
│   ├── ISSUE_TEMPLATE/           # Issue テンプレート（Bug / Feature）
│   ├── workflows/                # CI / CD ワークフロー
│   ├── dependabot.yml            # 依存関係更新設定
│   └── pull_request_template.md  # PR テンプレート
├── docs/
│   └── SECURITY_STANDARDS.md     # セキュリティ・アーキテクチャ標準書
├── templates/
│   ├── python/                   # Python アプリケーション用テンプレート
│   │   ├── config/               # 設定ファイル格納
│   │   ├── data/                 # 入出力データ分離領域 (input/output)
│   │   ├── test_scripts/         # テスト・検証用スクリプト群
│   │   ├── .env.example          # 環境変数サンプル
│   │   ├── AGENTS.md             # AI協調・開発規約
│   │   ├── main.py               # エントリーポイント
│   │   └── requirements.txt      # 依存パッケージ
│   └── web/                      # Web アプリケーション用テンプレート
│       ├── public/               # ★ 唯一の Web 公開ディレクトリ (DocumentRoot)
│       │   ├── index.html
│       │   ├── app.js
│       │   ├── style.css
│       │   └── .htaccess         # 拡張子・ドットファイル遮断
│       ├── server/               # バックエンドロジック (アクセス拒否 .htaccess 付)
│       ├── data/                 # SQLite / データ (アクセス拒否 .htaccess 付)
│       ├── config/               # サービス設定 (アクセス拒否 .htaccess 付)
│       ├── scripts/              # ビルド・配備スクリプト
│       ├── test_scripts/         # 検証スクリプト
│       └── AGENTS.md             # 開発規約
├── .editorconfig                 # コーディング規約
├── .gitattributes                # 改行コード自動制御
├── .gitignore                    # グローバル機密遮断ルール
├── LICENSE                       # MIT ライセンス
└── README.md                     # 本ドキュメント
```

---

## 🚀 クイックスタート (Quick Start)

### 1. リポジトリのクローンまたはテンプレート利用

```bash
git clone https://github.com/saitarus/production-starter-kit.git my-project
cd my-project
```

### 2. Python プロジェクトの開始

```bash
# テンプレートディレクトリへ移動（または新規ワークスペースへコピー）
cd templates/python

# 仮想環境の作成と有効化
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 依存パッケージのインストール
pip install -r requirements.txt

# 環境変数の設定
cp .env.example .env

# 実行
python main.py
```

### 3. Web プロジェクトの開始（Apache / Docker / 静的ホスティング）

Web サーバー（Apache, Nginx, LiteSpeed 等）の DocumentRoot を `templates/web/public/` に設定して起動します。

---

## 🛡️ セキュリティ規準のハイライト

詳細な仕様は [docs/SECURITY_STANDARDS.md](docs/SECURITY_STANDARDS.md) をご覧ください。

- **公開領域の最小化**: `public/` のみがブラウザから到達可能。上位階層のソースコードや設定ファイルは物理的に遮断されます。
- **機密拡張子の拒否**: `.sql`, `.json`, `.env`, `.sh`, `.log`, `.bak` 等へのダイレクトアクセスを Web サーバーレイヤーで拒絶します。
- **データ・ログの漏洩防止**: `data/output/` や `test_scripts/` の実体ファイルは Git 管理外とし、本番環境やリモートリポジトリへの偶発的な流出をブロックします。

---

## 📄 ライセンス (License)

本プロジェクトは [MIT License](LICENSE) のもとで公開されています。商用・個人利用を問わず、自由にご活用いただけます。
