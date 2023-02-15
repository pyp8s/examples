# pyp8s examples

Here you can find a few simple usage examples.

Prepare environment:

1. Make sure you have Python 3.6+ installed
1. Install pyp8s `python3 -m pip install pyp8s`
1. Run an example `python3 examples/pyp8s_ticker.py`

## Ticker

A tiny application that counts seconds from the startup.

[pyp8s_ticker.py](https://github.com/pyp8s/examples/blob/master/examples/pyp8s_ticker.py)


## Eternity

In this example we only start the metrics server. Nothing else changes.

[pyp8s_eternity.py](https://github.com/pyp8s/examples/blob/master/examples/pyp8s_eternity.py)


## Workarounds

A few workarounds on how to make python accept things that are legal for Prometheus metrics, but cause syntax error in Python.

[pyp8s_workarounds.py](https://github.com/pyp8s/examples/blob/master/examples/pyp8s_workarounds.py)
