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
