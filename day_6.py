#!/usr/bin/env python


def locate_marker(stream: list | tuple, marker_length: int):
    _chain: list = list(stream[:marker_length - 1])
    _packet: str | int
    for _packet in stream[marker_length - 1:]:
        _chain.append(_packet)
        _detector = set(_chain[-marker_length:])
        if len(_detector) == marker_length:
            return _chain


with open("data.txt", "r") as file:
    data = tuple(file.read())

print("Length to start-of-packet marker: "
      f"{len(locate_marker(data, 4))}")
print("Length to start-of-message marker: "
      f"{len(locate_marker(data, 14))}")
