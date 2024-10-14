#!/usr/bin/env bash

# create blog project directories
mkdir -p "$HOME"/blog
mkdir -p "$HOME"/blog/blog-tests
mkdir -p "$HOME"/blog/blog-tests/all
mkdir -p "$HOME"/blog/blog-tests/by-function
mkdir -p "$HOME"/blog/check
mkdir -p "$HOME"/blog/check/no-check
cd "$HOME"/blog || exit
pwd
ls -l ./*
