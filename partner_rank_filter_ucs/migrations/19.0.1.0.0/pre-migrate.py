"""Pre-migrate customer_vendor_ucs 17.x → 19.0.1.0.0."""
import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    if version:
        _logger.info("Pre-migrate customer_vendor_ucs from %s", version)
