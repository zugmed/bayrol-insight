#!/usr/bin/env python3

"""
Bayrol Insight

Minimal proof of concept.
"""

from config import VERSION, CLIENT_NAME, BROKER, PORT


def main():

    print("=" * 40)
    print(CLIENT_NAME)
    print(f"Version {VERSION}")
    print("=" * 40)

    print(f"Broker : {BROKER}")
    print(f"Port   : {PORT}")

    print()
    print("Starting...")


if __name__ == "__main__":
    main()