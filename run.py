import os
import time

from pyarr import RadarrAPI
from pyarr.exceptions import PyarrUnauthorizedError
from vulcan_utils.logger import Logger

logger = Logger(name="radarr-rss-sync")
host_url = os.environ.get("HOST_URL")
api_key = os.environ.get("API_KEY")
interval = int(os.environ.get("INTERVAL", 900))


def init_client(host_url: str, api_key: str) -> RadarrAPI | None:
    """
    Initialize the RadarrAPI client with the given host URL and API key.

    Args:
        host_url (str): The URL of the Radarr host.
        api_key (str): The API key for authentication.

    Returns:
        RadarrAPI | None: The initialized RadarrAPI client or None if initialization fails.
    """

    try:
        return RadarrAPI(host_url=host_url, api_key=api_key)
    except PyarrUnauthorizedError as e:
        logger.error(
            "Failed to authorize: Verify API_KEY environment variable")
        logger.error(e)
    except ConnectionRefusedError as e:
        logger.error("Failed to connect: Verify HOST_URL environment variable")
        logger.error(e)
    except Exception as e:
        logger.error(e)


def rss_sync(client: RadarrAPI) -> None:
    """
    Perform RSS synchronization using the provided RadarrAPI client.

    Args:
        client (RadarrAPI): The RadarrAPI client to use for synchronization.

    Returns:
        None
    """

    try:
        client.post_command(name="RssSync")
        logger.info("RSS Sync successful")
    except Exception as e:
        logger.error(f"RSS Sync failed: {e}")


client = init_client(host_url, api_key)
if client:
    while True:
        rss_sync(client=client)
        time.sleep(interval)
