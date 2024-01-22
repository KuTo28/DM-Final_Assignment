set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

_:
  @just --list

merge shard_path :
  @python ./data/merge.py {{shard_path}} heart_data.csv

shard file_path n_shards:
  @python ./data/shard.py {{file_path}} {{n_shards}}

clean file_path cleaned_path:
  @python ./data/clean.py {{file_path}} {{cleaned_path}}