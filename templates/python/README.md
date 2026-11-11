# {{PROJECT_NAME}}

Pythonスクリプト標準構成テンプレートから生成されたプロジェクトです。

## セットアップと実行

```bash
# 1. 仮想環境の作成と有効化
python -m venv .venv
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Mac / Linux:
source .venv/bin/activate

# 2. 依存パッケージのインストール
pip install -r requirements.txt

# 3. 実行
python main.py
```

## ディレクトリ構成
```text
├── AGENTS.md        # プロジェクト規約（AIエージェント行動規範）
├── .gitignore       # Python標準除外設定
├── .env.example     # 環境変数サンプル
├── requirements.txt # 依存ライブラリ
├── main.py          # メイン処理
├── config/          # 設定ファイル
├── data/            # 入力（input/）および出力（output/）データ
├── test_scripts/    # テスト・検証用スクリプト
└── archive/         # 旧スクリプト退避用
```
