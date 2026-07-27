#!/usr/bin/env bash

set -euo pipefail

readonly DEVICE_ADDRESS="10.1.0.29"
readonly STATUS_ENDPOINT="Switch.GetStatus?id=0"

if [[ $# -ne 1 ]]; then
  echo "Użycie: $0 {włącz|wyłącz|przełącz|status}" >&2
  exit 2
fi

case "$1" in
  włącz)
    endpoint="Switch.Set?id=0&on=true"
    should_read_status=true
    ;;
  wyłącz)
    endpoint="Switch.Set?id=0&on=false"
    should_read_status=true
    ;;
  przełącz)
    endpoint="Switch.Toggle?id=0"
    should_read_status=true
    ;;
  status)
    endpoint="$STATUS_ENDPOINT"
    should_read_status=false
    ;;
  *)
    echo "Nieznana akcja: $1. Użyj: włącz, wyłącz, przełącz lub status." >&2
    exit 2
    ;;
esac

curl --fail --silent --show-error "http://${DEVICE_ADDRESS}/rpc/${endpoint}"

if [[ "$should_read_status" == true ]]; then
  printf '\n'
  curl --fail --silent --show-error "http://${DEVICE_ADDRESS}/rpc/${STATUS_ENDPOINT}"
fi