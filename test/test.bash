#!/bin/bash
# SPDX-FileCopyrightText: 2024 Ryusei Fujimura
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

timeout 10 ros2 launch calendar_data talk_listen.launch.py > /tmp/calendar.log

cat /tmp/calendar.log | grep -A 10 "September 2025"
