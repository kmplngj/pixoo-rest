#!/bin/bash

PIXOO_REST_URL="http://localhost:5000"

function swipe() {
  local R=${1}
  local G=${2}
  local B=${3}

  # Swipe from center (32,32) to right edge
  for i in {-1..64}; do
    curl -s -X POST \
      -H "Content-Type: application/json" \
      -d "{\"start_x\":32,\"start_y\":32,\"stop_x\":${i},\"stop_y\":-1,\"r\":${R},\"g\":${G},\"b\":${B},\"push_immediately\":true}" \
      "${PIXOO_REST_URL}/draw/line"
  done

  # Swipe to bottom edge
  for i in {0..64}; do
    curl -s -X POST \
      -H "Content-Type: application/json" \
      -d "{\"start_x\":32,\"start_y\":32,\"stop_x\":64,\"stop_y\":${i},\"r\":${R},\"g\":${G},\"b\":${B},\"push_immediately\":true}" \
      "${PIXOO_REST_URL}/draw/line"
  done

  # Swipe to left edge
  for i in {63..-1}; do
    curl -s -X POST \
      -H "Content-Type: application/json" \
      -d "{\"start_x\":32,\"start_y\":32,\"stop_x\":${i},\"stop_y\":64,\"r\":${R},\"g\":${G},\"b\":${B},\"push_immediately\":true}" \
      "${PIXOO_REST_URL}/draw/line"
  done

  # Swipe to top edge
  for i in {63..0}; do
    curl -s -X POST \
      -H "Content-Type: application/json" \
      -d "{\"start_x\":32,\"start_y\":32,\"stop_x\":-1,\"stop_y\":${i},\"r\":${R},\"g\":${G},\"b\":${B},\"push_immediately\":true}" \
      "${PIXOO_REST_URL}/draw/line"
  done

}

swipe 0 255 0 > /dev/null
