# titanicやってみる
## 構築

### データセットの用意
```sh
$ mkdir data
$ cd data
$ kaggle competitions download -c titanic
$ unzip titanic.zip
```

### sshのエージェント
https://code.visualstudio.com/docs/remote/containers#_sharing-git-credentials-with-your-container

### ipynbを扱うときの注意
1. run allしてからcommitする
2. 必要な変分以外はcommitしない
    - 確認で実行し直すだけであれば、`checkout -f`等で変分を消す
