#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""{{PROJECT_NAME}} - メイン処理スクリプト"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# プロジェクトルートパスの取得
ROOT_DIR = Path(__file__).resolve().parent
DATA_INPUT_DIR = ROOT_DIR / "data" / "input"
DATA_OUTPUT_DIR = ROOT_DIR / "data" / "output"
CONFIG_DIR = ROOT_DIR / "config"

# 環境変数の読み込み (.env)
load_dotenv(ROOT_DIR / ".env")


def main():
    print(f"[{Path(__file__).stem}] 処理を開始します: {{PROJECT_NAME}}")
    DATA_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    # ここにメイン処理を記述
    print(f"[{Path(__file__).stem}] 処理が正常に完了しました。")


if __name__ == "__main__":
    main()
