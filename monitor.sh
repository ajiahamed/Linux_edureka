#!/usr/bin/env bash

# Define color codes
COLOR_RESET="\e[0m"
COLOR_HEADER="\e[1;34m"
COLOR_CPU="\e[1;31m"
COLOR_MEMORY="\e[1;32m"
COLOR_DISK="\e[1;33m"
COLOR_NETWORK="\e[1;35m"
COLOR_USERS="\e[1;36m"

# Function to print headers in color
print_header() {
    echo -e "${COLOR_HEADER}$1${COLOR_RESET}"
}

# Function to print command output in a specific color
print_output() {
    local color=$1
    shift
    echo -e "${color}$@${COLOR_RESET}"
}

# CPU Load
print_header "CPU Load:"
print_output "$COLOR_CPU" "$(uptime)"

# Memory Usage
print_header "Memory Usage:"
print_output "$COLOR_MEMORY" "$(free -h)"

# Disk Usage
print_header "Disk Usage:"
print_output "$COLOR_DISK" "$(df -h)"

# Network Usage
print_header "Network Usage:"
print_output "$COLOR_NETWORK" "$(netstat -i)"

# Active Logged In Users
print_header "Active Logged In Users:"
print_output "$COLOR_USERS" "$(who)"

