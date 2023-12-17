set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

help:
	@Write-Host "Available targets:"
	@Write-Host "  help      : Display this help message"
	@Write-Host "  merge     : Run the merge script on the data"
	@Write-Host "  shard     : Run the shard script on the data"
	@Write-Host "  clean     : Run the clean script on the data"

merge:
  @python ./data/merge.py

shard:
  @python ./data/shard.py

clean:
  @python ./data/clean.py