set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

_:
  @echo "Use just --list to see all available recipes"

merge shard_path:
  @python ./data/merge.py {{shard_path}}

shard file_path n_shards:
  @python ./data/shard.py {{file_path}} {{n_shards}}

clean file_path:
  @python ./data/clean.py {{file_path}}