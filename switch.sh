#! /bash/sh

# Autorun USB switcher
# Initial run: sudo chmod +x switch.sh
# Use command: bash switch.sh

source ~/venv/usb/bin/activate
cd Python
streamlit run USBswitcher.py
