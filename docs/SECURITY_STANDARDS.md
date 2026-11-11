# Security & Architecture Standards

本ドキュメントは、実稼働（プロダクション）環境におけるセキュリティ、アーキテクチャ分離、および AI エージェント共同開発時の運用規準を定義したものです。

---

## 1. ディレクトリ分離原則（Public Directory Separation）

Web アプリケーションにおいて、ソースコード全体を Web 公開ルート（DocumentRoot）に配置することは、重大な脆弱性（ソースコード漏洩、`.env` 露出、バックアップファイルの不正取得など）の最大の原因となります。

```
[Repository Root]
├── .env.example          # 環境変数テンプレート（秘密情報は含めない）
├── .gitignore            # 機密除外定義
├── server/               # バックエンド処理（非公開エリア）
│   └── .htaccess         # 直アクセス拒否 (Deny from all)
├── data/                 # SQLite / 一時データ（非公開エリア）
│   └── .htaccess         # 直アクセス拒否 (Deny from all)
├── config/               # 設定テンプレート（非公開エリア）
│   └── .htaccess         # 直アクセス拒否 (Deny from all)
└── public/               # ★ 唯一の DocumentRoot ★
    ├── index.html
    ├── app.js
    ├── style.css
    └── .htaccess         # ドットファイル遮断・拡張子防御
```

- **原則**: DocumentRoot には必ず `public/` のみを指定する。
- **効果**: 万一 Web サーバーの設定不備があっても、親階層にある設定ファイルやデータベースファイルへの直接アクセスを物理的に遮断します。

---

## 2. 多層防御（Defense in Depth: `.htaccess`）

Apache / LiteSpeed 環境下において、仮に DocumentRoot がリポジトリルートに誤設定された場合でも情報漏洩を防ぐため、サブディレクトリ単位でアクセス制御を二重に施します。

### 非公開ディレクトリ（`server/`, `data/`, `config/`, `archive/`）
```apache
<IfModule mod_authz_core.c>
    Require all denied
</IfModule>
<IfModule !mod_authz_core.c>
    Order deny,allow
    Deny from all
</IfModule>
```

### 公開ディレクトリ（`public/`）
```apache
# 1. ディレクトリインデックス（ファイル一覧表示）の無効化
Options -Indexes

# 2. ドット隠しファイル（.env, .git等）へのアクセス遮断
<FilesMatch "^\.">
    Require all denied
</FilesMatch>

# 3. センシティブな拡張子への直接アクセス拒否
<FilesMatch "\.(sql|json|sh|env|md|log|bak|old|yml|yaml)$">
    Require all denied
</FilesMatch>
```

---

## 3. 機密情報のライフサイクル管理

1. **`.env` の Git 追跡禁止**:
   - `.env` は `.gitignore` に厳格に指定し、コミットに絶対に含めない。
   - 代わりに、ダミー値と説明を記載した `.env.example` のみをリポジトリで管理する。
2. **ログ出力時のサニタイズ**:
   - 認証トークン、パスワード、クレジットカード情報、個人情報はログファイルへ出力しない。
3. **CI/CD シークレットの保護**:
   - 本番デプロイ用の API キー・SSH 秘密鍵は GitHub Actions Secrets 等の暗号化ストレージで管理する。

---

## 4. AI エージェント（Pair Programming）協調規準

AI エージェント（Copilot, Codex, Claude Code, Antigravity 等）を活用した開発において、プロジェクトの整合性を保つためのルール：

- **ゴール駆動の検証義務**: コード変更後は必ずテスト・構文チェックを実行し、エラーがないことを検証してから完了とする。
- **外科手術的ピンポイント修正**: 指示された場所以外の無断リファクタリング、フォーマット整形、不要なコード変更は行わない。
- **ルート汚染の防止**: 一時スクリプトや生成データはルート直下に放置せず、`test_scripts/` や `data/output/` へ配置する。
