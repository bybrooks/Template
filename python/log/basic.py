import logging

from rich.logging import RichHandler

logging.basicConfig(
    level=logging.INFO,
    handlers=[RichHandler(markup=True, rich_tracebacks=True)],  # 色付きログ
)
logger = logging.getLogger(__name__)
