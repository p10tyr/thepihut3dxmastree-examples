#!/bin/bash

DIRECTORY="$(dirname "$0")"
DIRECTORY="$(cd "$DIRECTORY" && pwd)"

function select_file() {
    local options=()
    local file
    local i=0
    while read -r file; do
        options+=("$i" "$file")
        ((i++))
    done < <(find "$DIRECTORY" -type f -name "*.py" | sort)

    local cmd=(dialog --menu "Choose file" 22 76 16)
    local choice
    while true; do
        choice=$("${cmd[@]}"  "${options[@]}" 2>&1 >/dev/tty)
        [[ -z "$choice" ]] && return 0
        python "${options[$choice*2+1]}"
    done
}

select_file
