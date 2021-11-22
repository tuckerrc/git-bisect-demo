#!/usr/bin/env bash

cp bisect_tests.example.py bisect_tests.py
cp bisect_test.example.sh bisect_test.sh

git bisect start
git bisect bad 51ae82c
git bisect good 32558cc
