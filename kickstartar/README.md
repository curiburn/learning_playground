# kickstarter

## 構築

1. devcontainer をビルド
2. データセットをダウンロード

```sh
cd learning_playground/kickstarter
curl --output "data/kickstarter.csv" "「API - CSV Data」より取得できるURL"
```

## テスト

```sh
python -m unittest discover tests -v
```

## 構成メモ

- transforms: データの変形処理をまとめたモジュール
  - columns: 特定のカラムを作成する処理、`pd.DataFrame -> pd.Series`な関数を記載する
  - dataframe: 特定のデータフレームを作成する処理、`pd.DataFrame -> pd.DataFrame`な関数を記載する
- tests: 主に transforms の動作チェック
- profilings: プロファイリングを実施する ipynb 置き場。
- edas: EDA を行う ipynb 置き場
