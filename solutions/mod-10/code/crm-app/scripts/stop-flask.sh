#!/usr/bin/env bash

kill -15 $(pgrep --uid $(id -u labs) flask)
