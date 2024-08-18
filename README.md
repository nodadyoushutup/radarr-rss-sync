
# Radarr RSS Sync

This project provides RSS synchronization with Radarr using the `pyarr` library. The application is designed to run as a Docker container and can be configured to perform RSS sync at a specified interval.

## Prerequisites

- Docker installed on your system.
- A Radarr instance running and accessible.
- Radarr API key for authentication.

## Environment Variables

The script uses the following environment variables:

- `HOST_URL`: The URL of the Radarr host.
- `API_KEY`: The API key for Radarr authentication.
- `INTERVAL` (optional): The interval (in seconds) between RSS sync operations. Defaults to 900 seconds (15 minutes) if not specified.

## Docker Setup

To run this application in a Docker container, follow these steps:

### Using Docker Compose

You can use Docker Compose to manage the container. Here's an example `docker-compose.yaml` file:

```yaml
services:
  radarr-rss-sync:
    image: ghcr.io/nodadyoushutup/radarr-rss-sync:latest
    environment:
      - HOST_URL=http://192.168.1.100:7878
      - API_KEY=1234567890abcdef1234567890abcdef
      - INTERVAL=900 # (Optional)
    restart: always
```

Replace the environment variables with your actual Radarr host URL, API key, and desired sync interval.

To start the service, simply run:

```bash
docker-compose up -d
```

### Without Docker Compose

If you prefer not to use Docker Compose, you can run the container directly with Docker:

```bash
docker run -d \
  --name radarr-rss-sync \
  -e HOST_URL=<your_radarr_host_url> \
  -e API_KEY=<your_radarr_api_key> \
  -e INTERVAL=<sync_interval_in_seconds> \
  radarr-rss-sync
```

Replace `<your_radarr_host_url>`, `<your_radarr_api_key>`, and `<sync_interval_in_seconds>` with your Radarr host URL, API key, and desired sync interval, respectively.

## Troubleshooting

- **Authorization Errors:** Ensure that the `API_KEY` is correct and that Radarr is properly configured to accept the key.
- **Connection Errors:** Verify that the `HOST_URL` is correct and accessible from within the Docker container.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
