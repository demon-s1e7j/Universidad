#!/bin/sh

javac $1.java && echo "Termino de compilar" && java $1 < input.in
