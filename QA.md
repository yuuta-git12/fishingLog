# 作成中に発生したエラー一覧

## Docker

### Error response from daemon: Conflict. The container name・・・・
- `docker compose up -d`実行時に発生
- 自分のDocker環境に同じ名前のコンテナが存在している場合に発生するエラー
- 対処方法：
  - コンテナの名前を変更する
  - 名前が重複しているコンテナを削除する[`docker rm コンテナID`(コンテナが停止している場合に有効)]
```
Error response from daemon: Conflict. The container name "/app" is already in use by container "8b0ccef2da9d43b43da132f21fb50eff028483baf814ef8b1431156cf61047d1". You have to remove (or rename) that container to be able to reuse that name.
```
### docker compose up -d で起動したコンテナがすぐに停止する。
- `docker compose up -d`でコンテナを起動してもすぐに停止する。
- 確認事項
  - `docker ps`をしても起動しているコンテナ一覧に表示されない。
  - `docker compose logs`でコマンドの実行ログを確認
  - 表示されたエラー
    ```
    ModuleNotFoundError: No module named 'djangopj'
    ```
- 原因：
  - djangoのプロジェクトを作成していなかったことが原因?