#!/bin/bash
pids=$(pgrep play) 
kill -9 $pids
