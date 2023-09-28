#!/usr/bin/env bash

QUEUE_URL="$1"

aws sqs send-message-batch --queue-url "${QUEUE_URL}" --entries file://./events/batch.json
