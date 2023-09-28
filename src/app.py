import logging

logger = logging.getLogger(__name__)


def handler(event, context):
    logger.debug(f"Event: {event}")
    logger.debug(f"Context: {context}")

    # force out-of-memory and timeout errors
    # b = bytearray(10000)
    # while len(b) < 512000000:
    #     b += bytearray(10000)
