#!/bin/bash

PIXOO_REST_URL="http://localhost:5000"

SCREEN_SIZE_X=64
SCREEN_SIZE_Y=64

MAX_SCREEN_VALUE_X=$((SCREEN_SIZE_X - 1))
MAX_SCREEN_VALUE_Y=$((SCREEN_SIZE_Y - 1))

function progress_bar() {

  # Fill screen with black
  curl -s -X POST \
    -H "Content-Type: application/json" \
    -d '{"r":0,"g":0,"b":0,"push_immediately":false}' \
    "${PIXOO_REST_URL}/draw/fill"

  # Calculate progress bar dimensions
  local TOP_LEFT_Y=$(printf "%.0f\n" "$((MAX_SCREEN_VALUE_Y - (SCREEN_SIZE_Y * ${1} / 100)))")

  # Draw red progress rectangle
  curl -s -X POST \
    -H "Content-Type: application/json" \
    -d "{\"top_left_x\":0,\"top_left_y\":${TOP_LEFT_Y},\"bottom_right_x\":${MAX_SCREEN_VALUE_X},\"bottom_right_y\":${MAX_SCREEN_VALUE_Y},\"r\":255,\"g\":0,\"b\":0,\"push_immediately\":false}" \
    "${PIXOO_REST_URL}/draw/rectangle"

  # Draw percentage text
  curl -s -X POST \
    -H "Content-Type: application/json" \
    -d "{\"text\":\"${1} %\",\"x\":0,\"y\":0,\"r\":255,\"g\":255,\"b\":255,\"push_immediately\":true}" \
    "${PIXOO_REST_URL}/draw/text"

}

for i in {1..100}; do

  # do something meaningful here ...

  progress_bar ${i} > /dev/null

  sleep 1

done
