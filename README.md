## Run:

### With socks5 proxy:
```
docker run -it --name no-sticker-gif --restart always -v $(pwd)/docker/db:/db -e API_ID=XXXXX -e API_HASH=XXXXXXXXXXXXXXXXXXXXXXXXXXXX -e PROXY=true -e PROXY_IP=XXX.XXX.XXX.XXX -e PROXY_PORT=XXXXX ghcr.io/doorbash/telegram-no-sticker-gif:latest
```

### Without proxy:
```
docker run -it --name no-sticker-gif --restart always -v $(pwd)/docker/db:/db -e API_ID=XXXXX -e API_HASH=XXXXXXXXXXXXXXXXXXXXXXXXXXXX ghcr.io/doorbash/telegram-no-sticker-gif:latest
```

## Usage:
Send any sticker/gif you have problem with to yourself to add it to database. Send again to remove.