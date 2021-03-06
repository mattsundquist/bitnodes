#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# tests.py - Dummy data and tests for bitnodes.
#
# Copyright (c) 2013 Addy Yeow Chin Heng <ayeowch@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
Dummy data and tests for bitnodes.
"""

import time

"""
Graph layout for DUMMY_NETWORK_A:
    1.1.1.1
        2.2.2.2
            4.4.4.4
                10.10.10.10
                11.11.11.11
                    13.13.13.13
                        14.14.14.14
                            15.15.15.15
                                16.16.16.16
                                    22.22.22.22
                                17.17.17.17
                            18.18.18.18
                                4.4.4.4
                                5.5.5.5
                            19.19.19.19
                            20.20.20.20
                                21.21.21.21
                12.12.12.12
        3.3.3.3
            5.5.5.5
                7.7.7.7
                    9.9.9.9
                8.8.8.8
            6.6.6.6
        16.16.16.16
"""
DUMMY_NETWORK_A = {
    "1.1.1.1": [{"ip": "2.2.2.2"}, {"ip": "3.3.3.3"}, {"ip": "16.16.16.16"}, ],
    "2.2.2.2": [{"ip": "4.4.4.4"}, ],
    "3.3.3.3": [{"ip": "5.5.5.5"}, {"ip": "6.6.6.6"}, ],
    "4.4.4.4": [{"ip": "10.10.10.10"}, {"ip": "11.11.11.11"}, {"ip": "12.12.12.12"}, ],
    "5.5.5.5": [{"ip": "7.7.7.7"}, {"ip": "8.8.8.8"}, ],
    "6.6.6.6": [],
    "7.7.7.7": [{"ip": "9.9.9.9"}, ],
    "8.8.8.8": [],
    "9.9.9.9": [],
    "10.10.10.10": [],
    "11.11.11.11": [{"ip": "13.13.13.13"}, ],
    "12.12.12.12": [],
    "13.13.13.13": [{"ip": "14.14.14.14"}, ],
    "14.14.14.14": [{"ip": "15.15.15.15"}, {"ip": "18.18.18.18"}, {"ip": "19.19.19.19"}, {"ip": "20.20.20.20"}, ],
    "15.15.15.15": [{"ip": "16.16.16.16"}, {"ip": "17.17.17.17"}, ],
    "16.16.16.16": [{"ip": "22.22.22.22"}, ],
    "17.17.17.17": [],
    "18.18.18.18": [{"ip": "4.4.4.4"}, {"ip": "5.5.5.5"}, ],
    "19.19.19.19": [],
    "20.20.20.20": [{"ip": "21.21.21.21"}, ],
    "21.21.21.21": [],
    "22.22.22.22": [],
}

DUMMY_SEEDS_A = {
    1: "1.1.1.1",
    2: "2.2.2.2",
    3: "3.3.3.3",
    4: "4.4.4.4",
    5: "5.5.5.5",
    6: "6.6.6.6",
}

"""
DUMMY_NETWORK_B was created using gephi's random graph generation with
100 nodes and 511 edges.
"""
DUMMY_NETWORK_B = {
    "5.2.7.4": [{"ip": "5.2.6.2"}, {"ip": "5.2.8.8"}, {"ip": "5.2.0.5"}, {"ip": "5.2.1.0"}, {"ip": "5.2.0.1"}, {"ip": "5.1.9.9"}, ],
    "5.2.7.5": [{"ip": "5.2.7.9"}, {"ip": "5.2.2.8"}, {"ip": "5.2.9.1"}, {"ip": "5.2.7.1"}, {"ip": "5.2.7.3"}, {"ip": "5.2.0.7"}, {"ip": "5.2.0.4"}, {"ip": "5.2.1.7"}, {"ip": "5.2.4.7"}, {"ip": "5.1.9.7"}, {"ip": "5.2.5.4"}, {"ip": "5.2.0.8"}, ],
    "5.2.7.6": [{"ip": "5.2.2.5"}, {"ip": "5.2.3.3"}, {"ip": "5.2.7.8"}, {"ip": "5.2.2.8"}, {"ip": "5.2.1.0"}, {"ip": "5.2.4.5"}, {"ip": "5.2.5.6"}, {"ip": "5.2.5.4"}, {"ip": "5.2.2.1"}, ],
    "5.2.7.7": [{"ip": "5.2.2.5"}, {"ip": "5.2.3.3"}, {"ip": "5.2.3.7"}, {"ip": "5.2.6.8"}, {"ip": "5.2.8.4"}, {"ip": "5.2.2.6"}, {"ip": "5.2.4.2"}, {"ip": "5.2.8.6"}, {"ip": "5.2.0.5"}, {"ip": "5.2.0.3"}, {"ip": "5.2.0.0"}, {"ip": "5.2.5.0"}, ],
    "5.2.7.0": [{"ip": "5.2.2.5"}, {"ip": "5.2.3.2"}, {"ip": "5.2.4.5"}, {"ip": "5.2.8.3"}, {"ip": "5.2.4.2"}, {"ip": "5.2.1.7"}, {"ip": "5.2.0.0"}, {"ip": "5.1.9.9"}, {"ip": "5.2.5.6"}, ],
    "5.2.7.1": [{"ip": "5.2.6.0"}, {"ip": "5.2.6.5"}, {"ip": "5.2.1.6"}, {"ip": "5.2.2.0"}, {"ip": "5.2.2.1"}, {"ip": "5.2.7.5"}, {"ip": "5.2.3.8"}, {"ip": "5.2.8.5"}, {"ip": "5.2.8.2"}, {"ip": "5.1.9.5"}, {"ip": "5.2.0.1"}, {"ip": "5.2.5.0"}, ],
    "5.2.7.2": [{"ip": "5.2.3.2"}, {"ip": "5.2.2.1"}, {"ip": "5.2.2.3"}, {"ip": "5.2.3.9"}, {"ip": "5.2.8.2"}, {"ip": "5.2.5.6"}, {"ip": "5.2.4.8"}, {"ip": "5.2.5.0"}, ],
    "5.2.7.3": [{"ip": "5.2.6.0"}, {"ip": "5.2.2.5"}, {"ip": "5.2.8.8"}, {"ip": "5.2.3.6"}, {"ip": "5.2.7.5"}, {"ip": "5.2.8.7"}, {"ip": "5.2.8.4"}, {"ip": "5.2.8.3"}, {"ip": "5.2.8.0"}, {"ip": "5.2.4.3"}, {"ip": "5.2.1.7"}, {"ip": "5.2.5.8"}, {"ip": "5.2.5.4"}, ],
    "5.2.7.8": [{"ip": "5.2.3.2"}, {"ip": "5.2.2.0"}, {"ip": "5.2.6.8"}, {"ip": "5.2.7.6"}, {"ip": "5.2.1.3"}, {"ip": "5.2.8.6"}, {"ip": "5.2.4.1"}, {"ip": "5.2.4.6"}, {"ip": "5.2.1.6"}, {"ip": "5.2.1.4"}, ],
    "5.2.7.9": [{"ip": "5.2.6.3"}, {"ip": "5.2.3.9"}, {"ip": "5.2.3.8"}, {"ip": "5.2.4.5"}, {"ip": "5.2.1.2"}, {"ip": "5.2.7.5"}, {"ip": "5.2.5.8"}, {"ip": "5.2.5.6"}, ],
    "5.2.6.7": [{"ip": "5.2.2.7"}, {"ip": "5.2.6.5"}, {"ip": "5.2.8.7"}, {"ip": "5.2.8.2"}, {"ip": "5.1.9.2"}, {"ip": "5.2.1.4"}, {"ip": "5.1.9.8"}, {"ip": "5.2.1.9"}, {"ip": "5.2.0.9"}, ],
    "5.2.6.6": [{"ip": "5.2.6.3"}, {"ip": "5.2.8.9"}, {"ip": "5.2.8.7"}, {"ip": "5.2.8.1"}, {"ip": "5.2.4.5"}, {"ip": "5.2.1.8"}, {"ip": "5.2.5.3"}, ],
    "5.2.6.5": [{"ip": "5.2.2.0"}, {"ip": "5.2.6.7"}, {"ip": "5.2.9.1"}, {"ip": "5.2.8.5"}, {"ip": "5.2.7.1"}, {"ip": "5.2.0.6"}, {"ip": "5.1.9.3"}, {"ip": "5.2.0.0"}, {"ip": "5.2.5.5"}, {"ip": "5.2.0.9"}, ],
    "5.2.6.4": [{"ip": "5.2.2.5"}, {"ip": "5.2.2.3"}, {"ip": "5.2.1.0"}, {"ip": "5.2.8.3"}, {"ip": "5.2.4.1"}, {"ip": "5.2.4.6"}, {"ip": "5.2.4.8"}, {"ip": "5.2.5.2"}, ],
    "5.2.6.3": [{"ip": "5.2.7.9"}, {"ip": "5.2.6.6"}, {"ip": "5.2.8.9"}, {"ip": "5.2.8.5"}, {"ip": "5.2.0.7"}, {"ip": "5.2.1.1"}, {"ip": "5.1.9.5"}, {"ip": "5.2.1.5"}, {"ip": "5.2.1.8"}, {"ip": "5.2.5.2"}, {"ip": "5.2.0.8"}, {"ip": "5.2.4.7"}, ],
    "5.2.6.2": [{"ip": "5.2.2.5"}, {"ip": "5.2.2.6"}, {"ip": "5.2.8.6"}, {"ip": "5.2.7.4"}, {"ip": "5.2.8.5"}, {"ip": "5.1.9.4"}, {"ip": "5.2.0.3"}, {"ip": "5.2.5.6"}, ],
    "5.2.6.1": [{"ip": "5.2.3.0"}, {"ip": "5.2.2.2"}, {"ip": "5.2.8.7"}, {"ip": "5.2.4.5"}, {"ip": "5.2.5.5"}, {"ip": "5.2.0.8"}, ],
    "5.2.6.0": [{"ip": "5.2.3.7"}, {"ip": "5.2.8.2"}, {"ip": "5.2.8.4"}, {"ip": "5.2.9.0"}, {"ip": "5.2.7.1"}, {"ip": "5.2.7.3"}, {"ip": "5.2.8.1"}, {"ip": "5.1.9.2"}, ],
    "5.2.6.9": [{"ip": "5.2.2.4"}, {"ip": "5.2.1.4"}, {"ip": "5.2.2.6"}, {"ip": "5.2.2.5"}, {"ip": "5.2.8.9"}, {"ip": "5.2.2.8"}, {"ip": "5.2.9.0"}, {"ip": "5.2.8.2"}, {"ip": "5.2.8.0"}, {"ip": "5.1.9.3"}, {"ip": "5.2.0.2"}, {"ip": "5.1.9.5"}, {"ip": "5.2.8.7"}, {"ip": "5.2.2.3"}, ],
    "5.2.6.8": [{"ip": "5.2.3.0"}, {"ip": "5.2.3.3"}, {"ip": "5.2.2.7"}, {"ip": "5.2.7.8"}, {"ip": "5.2.2.3"}, {"ip": "5.2.8.4"}, {"ip": "5.2.7.7"}, {"ip": "5.2.8.2"}, {"ip": "5.2.0.6"}, {"ip": "5.2.0.7"}, {"ip": "5.2.1.6"}, {"ip": "5.2.1.5"}, {"ip": "5.1.9.9"}, {"ip": "5.2.9.1"}, {"ip": "5.2.5.2"}, {"ip": "5.2.5.1"}, {"ip": "5.2.4.7"}, ],
    "5.2.5.2": [{"ip": "5.2.3.0"}, {"ip": "5.2.6.3"}, {"ip": "5.2.6.4"}, {"ip": "5.2.8.8"}, {"ip": "5.2.6.8"}, {"ip": "5.2.8.4"}, {"ip": "5.2.9.0"}, {"ip": "5.2.8.3"}, {"ip": "5.2.8.0"}, {"ip": "5.2.1.1"}, {"ip": "5.1.9.8"}, {"ip": "5.2.2.0"}, {"ip": "5.2.1.8"}, ],
    "5.2.5.3": [{"ip": "5.2.3.0"}, {"ip": "5.2.2.7"}, {"ip": "5.2.2.1"}, {"ip": "5.2.6.6"}, {"ip": "5.2.8.0"}, {"ip": "5.2.4.5"}, {"ip": "5.2.4.9"}, ],
    "5.2.5.0": [{"ip": "5.2.2.8"}, {"ip": "5.2.7.7"}, {"ip": "5.2.7.1"}, {"ip": "5.2.7.2"}, {"ip": "5.1.9.5"}, {"ip": "5.2.4.4"}, {"ip": "5.2.1.6"}, ],
    "5.2.5.1": [{"ip": "5.1.9.6"}, {"ip": "5.2.8.8"}, {"ip": "5.2.3.6"}, {"ip": "5.2.6.8"}, {"ip": "5.1.9.2"}, {"ip": "5.2.1.0"}, {"ip": "5.2.1.5"}, {"ip": "5.1.9.7"}, {"ip": "5.1.9.8"}, {"ip": "5.2.5.4"}, ],
    "5.2.5.6": [{"ip": "5.2.3.1"}, {"ip": "5.2.6.2"}, {"ip": "5.2.7.6"}, {"ip": "5.2.7.9"}, {"ip": "5.2.8.6"}, {"ip": "5.2.3.8"}, {"ip": "5.2.9.0"}, {"ip": "5.2.7.0"}, {"ip": "5.2.2.9"}, {"ip": "5.2.7.2"}, {"ip": "5.2.4.2"}, {"ip": "5.2.1.1"}, {"ip": "5.2.8.0"}, {"ip": "5.2.8.7"}, {"ip": "5.2.8.1"}, {"ip": "5.1.9.7"}, {"ip": "5.2.1.6"}, ],
    "5.2.5.7": [{"ip": "5.2.8.8"}, {"ip": "5.2.8.6"}, {"ip": "5.2.8.0"}, {"ip": "5.2.0.6"}, {"ip": "5.2.0.2"}, {"ip": "5.2.4.5"}, {"ip": "5.2.4.8"}, ],
    "5.2.5.4": [{"ip": "5.2.3.1"}, {"ip": "5.1.9.6"}, {"ip": "5.2.2.2"}, {"ip": "5.2.7.5"}, {"ip": "5.2.7.6"}, {"ip": "5.2.7.3"}, {"ip": "5.2.4.3"}, {"ip": "5.2.4.7"}, {"ip": "5.2.0.0"}, {"ip": "5.2.1.8"}, {"ip": "5.2.5.1"}, ],
    "5.2.5.5": [{"ip": "5.2.3.0"}, {"ip": "5.2.3.2"}, {"ip": "5.2.6.5"}, {"ip": "5.2.2.3"}, {"ip": "5.2.8.6"}, {"ip": "5.2.6.1"}, {"ip": "5.2.8.3"}, {"ip": "5.2.8.1"}, {"ip": "5.2.1.7"}, {"ip": "5.2.0.9"}, ],
    "5.2.5.8": [{"ip": "5.2.7.9"}, {"ip": "5.2.2.1"}, {"ip": "5.2.9.1"}, {"ip": "5.2.0.5"}, {"ip": "5.2.7.3"}, {"ip": "5.2.8.1"}, {"ip": "5.1.9.3"}, {"ip": "5.2.4.7"}, {"ip": "5.2.4.8"}, {"ip": "5.2.8.4"}, ],
    "5.2.5.9": [{"ip": "5.2.2.4"}, {"ip": "5.2.3.1"}, {"ip": "5.2.3.2"}, {"ip": "5.2.8.4"}, {"ip": "5.2.0.6"}, {"ip": "5.2.1.2"}, {"ip": "5.2.0.3"}, ],
    "5.2.4.9": [{"ip": "5.2.3.7"}, {"ip": "5.2.3.9"}, {"ip": "5.2.8.4"}, {"ip": "5.2.9.0"}, {"ip": "5.2.1.3"}, {"ip": "5.2.0.2"}, {"ip": "5.1.9.8"}, {"ip": "5.2.5.3"}, ],
    "5.2.4.8": [{"ip": "5.2.2.0"}, {"ip": "5.2.8.6"}, {"ip": "5.2.1.4"}, {"ip": "5.2.7.2"}, {"ip": "5.2.5.8"}, {"ip": "5.2.5.7"}, {"ip": "5.2.6.4"}, ],
    "5.2.4.5": [{"ip": "5.2.2.0"}, {"ip": "5.2.6.1"}, {"ip": "5.2.7.9"}, {"ip": "5.2.6.6"}, {"ip": "5.2.0.7"}, {"ip": "5.2.9.1"}, {"ip": "5.2.7.6"}, {"ip": "5.2.7.0"}, {"ip": "5.2.1.2"}, {"ip": "5.2.1.6"}, {"ip": "5.2.4.4"}, {"ip": "5.1.9.7"}, {"ip": "5.2.5.7"}, {"ip": "5.1.9.9"}, {"ip": "5.2.5.3"}, {"ip": "5.2.4.7"}, ],
    "5.2.4.4": [{"ip": "5.2.3.6"}, {"ip": "5.2.9.1"}, {"ip": "5.2.8.0"}, {"ip": "5.2.8.1"}, {"ip": "5.2.4.2"}, {"ip": "5.2.4.5"}, {"ip": "5.1.9.8"}, {"ip": "5.2.5.0"}, ],
    "5.2.4.7": [{"ip": "5.2.3.1"}, {"ip": "5.2.6.3"}, {"ip": "5.2.3.6"}, {"ip": "5.2.7.5"}, {"ip": "5.2.3.8"}, {"ip": "5.2.5.8"}, {"ip": "5.2.0.7"}, {"ip": "5.2.0.3"}, {"ip": "5.2.4.5"}, {"ip": "5.2.5.4"}, {"ip": "5.2.6.8"}, ],
    "5.2.4.6": [{"ip": "5.2.3.3"}, {"ip": "5.2.6.4"}, {"ip": "5.2.7.8"}, {"ip": "5.2.2.6"}, {"ip": "5.1.9.7"}, {"ip": "5.2.2.0"}, ],
    "5.2.4.1": [{"ip": "5.2.6.4"}, {"ip": "5.2.7.8"}, {"ip": "5.2.8.8"}, {"ip": "5.2.8.7"}, {"ip": "5.2.8.2"}, {"ip": "5.2.0.6"}, {"ip": "5.1.9.2"}, {"ip": "5.1.9.4"}, {"ip": "5.2.2.1"}, ],
    "5.2.4.0": [{"ip": "5.2.1.7"}, {"ip": "5.2.1.1"}, {"ip": "5.2.8.7"}, {"ip": "5.2.0.2"}, {"ip": "5.2.0.9"}, ],
    "5.2.4.3": [{"ip": "5.2.3.1"}, {"ip": "5.2.3.4"}, {"ip": "5.2.7.3"}, {"ip": "5.2.1.3"}, {"ip": "5.2.0.7"}, {"ip": "5.2.0.5"}, {"ip": "5.2.0.1"}, {"ip": "5.2.5.4"}, ],
    "5.2.4.2": [{"ip": "5.2.3.2"}, {"ip": "5.2.2.0"}, {"ip": "5.2.4.4"}, {"ip": "5.2.8.4"}, {"ip": "5.2.7.0"}, {"ip": "5.1.9.2"}, {"ip": "5.1.9.4"}, {"ip": "5.2.0.0"}, {"ip": "5.2.5.6"}, {"ip": "5.2.7.7"}, {"ip": "5.2.0.9"}, ],
    "5.2.3.8": [{"ip": "5.2.2.7"}, {"ip": "5.2.7.9"}, {"ip": "5.2.3.7"}, {"ip": "5.2.8.5"}, {"ip": "5.2.7.1"}, {"ip": "5.2.2.9"}, {"ip": "5.2.8.0"}, {"ip": "5.1.9.4"}, {"ip": "5.2.1.6"}, {"ip": "5.2.5.6"}, {"ip": "5.2.0.8"}, {"ip": "5.2.4.7"}, ],
    "5.2.3.9": [{"ip": "5.2.3.1"}, {"ip": "5.2.3.0"}, {"ip": "5.2.7.9"}, {"ip": "5.2.2.1"}, {"ip": "5.2.9.0"}, {"ip": "5.2.7.2"}, {"ip": "5.2.8.1"}, {"ip": "5.2.4.9"}, ],
    "5.2.3.0": [{"ip": "5.2.6.1"}, {"ip": "5.2.3.2"}, {"ip": "5.2.3.4"}, {"ip": "5.2.3.7"}, {"ip": "5.2.6.8"}, {"ip": "5.2.0.5"}, {"ip": "5.2.3.9"}, {"ip": "5.2.1.0"}, {"ip": "5.2.5.5"}, {"ip": "5.2.5.3"}, {"ip": "5.2.5.2"}, {"ip": "5.2.0.9"}, ],
    "5.2.3.1": [{"ip": "5.2.3.5"}, {"ip": "5.2.8.8"}, {"ip": "5.2.8.9"}, {"ip": "5.2.3.9"}, {"ip": "5.2.8.4"}, {"ip": "5.2.8.2"}, {"ip": "5.2.4.3"}, {"ip": "5.2.1.1"}, {"ip": "5.2.4.7"}, {"ip": "5.2.5.9"}, {"ip": "5.2.1.4"}, {"ip": "5.2.5.6"}, {"ip": "5.2.5.4"}, ],
    "5.2.3.2": [{"ip": "5.2.3.0"}, {"ip": "5.1.9.6"}, {"ip": "5.2.3.6"}, {"ip": "5.2.7.0"}, {"ip": "5.2.7.2"}, {"ip": "5.2.4.2"}, {"ip": "5.2.0.5"}, {"ip": "5.2.5.9"}, {"ip": "5.2.5.5"}, {"ip": "5.2.7.8"}, ],
    "5.2.3.3": [{"ip": "5.2.3.5"}, {"ip": "5.2.0.1"}, {"ip": "5.2.2.2"}, {"ip": "5.2.6.8"}, {"ip": "5.2.7.7"}, {"ip": "5.2.7.6"}, {"ip": "5.2.0.6"}, {"ip": "5.1.9.2"}, {"ip": "5.2.4.6"}, {"ip": "5.2.1.6"}, {"ip": "5.1.9.7"}, {"ip": "5.1.9.8"}, ],
    "5.2.3.4": [{"ip": "5.2.3.0"}, {"ip": "5.2.2.3"}, {"ip": "5.2.8.2"}, {"ip": "5.2.8.3"}, {"ip": "5.2.8.1"}, {"ip": "5.2.4.3"}, {"ip": "5.1.9.7"}, {"ip": "5.2.1.8"}, ],
    "5.2.3.5": [{"ip": "5.2.3.1"}, {"ip": "5.2.3.3"}, {"ip": "5.2.2.0"}, {"ip": "5.2.3.7"}, {"ip": "5.2.0.3"}, {"ip": "5.1.9.5"}, ],
    "5.2.3.6": [{"ip": "5.2.3.2"}, {"ip": "5.2.7.3"}, {"ip": "5.2.1.3"}, {"ip": "5.2.1.0"}, {"ip": "5.2.4.7"}, {"ip": "5.2.4.4"}, {"ip": "5.2.5.1"}, ],
    "5.2.3.7": [{"ip": "5.2.6.0"}, {"ip": "5.2.3.0"}, {"ip": "5.2.2.6"}, {"ip": "5.2.3.5"}, {"ip": "5.2.2.3"}, {"ip": "5.2.3.8"}, {"ip": "5.2.7.7"}, {"ip": "5.2.9.0"}, {"ip": "5.2.0.3"}, {"ip": "5.1.9.7"}, {"ip": "5.2.4.9"}, ],
    "5.2.2.9": [{"ip": "5.2.2.3"}, {"ip": "5.2.8.6"}, {"ip": "5.2.3.8"}, {"ip": "5.2.8.0"}, {"ip": "5.2.0.7"}, {"ip": "5.2.1.0"}, {"ip": "5.2.1.7"}, {"ip": "5.1.9.5"}, {"ip": "5.2.5.6"}, ],
    "5.2.2.8": [{"ip": "5.2.8.9"}, {"ip": "5.2.7.5"}, {"ip": "5.2.6.9"}, {"ip": "5.2.7.6"}, {"ip": "5.2.8.0"}, {"ip": "5.2.1.2"}, {"ip": "5.2.1.1"}, {"ip": "5.1.9.4"}, {"ip": "5.1.9.6"}, {"ip": "5.1.9.9"}, {"ip": "5.2.0.2"}, {"ip": "5.2.5.0"}, ],
    "5.2.2.3": [{"ip": "5.2.2.5"}, {"ip": "5.2.2.7"}, {"ip": "5.2.6.4"}, {"ip": "5.2.3.4"}, {"ip": "5.2.3.7"}, {"ip": "5.2.6.8"}, {"ip": "5.2.6.9"}, {"ip": "5.2.9.0"}, {"ip": "5.2.2.9"}, {"ip": "5.2.7.2"}, {"ip": "5.1.9.4"}, {"ip": "5.2.5.5"}, {"ip": "5.2.0.9"}, ],
    "5.2.2.2": [{"ip": "5.2.6.1"}, {"ip": "5.2.3.3"}, {"ip": "5.2.2.0"}, {"ip": "5.2.8.4"}, {"ip": "5.2.0.2"}, {"ip": "5.2.5.4"}, {"ip": "5.2.0.8"}, {"ip": "5.2.0.9"}, ],
    "5.2.2.1": [{"ip": "5.2.2.7"}, {"ip": "5.2.7.6"}, {"ip": "5.2.3.9"}, {"ip": "5.2.9.1"}, {"ip": "5.2.5.8"}, {"ip": "5.2.7.1"}, {"ip": "5.2.7.2"}, {"ip": "5.2.1.2"}, {"ip": "5.2.4.1"}, {"ip": "5.1.9.4"}, {"ip": "5.2.0.1"}, {"ip": "5.2.1.8"}, {"ip": "5.2.5.3"}, ],
    "5.2.2.0": [{"ip": "5.2.3.5"}, {"ip": "5.2.7.8"}, {"ip": "5.2.2.2"}, {"ip": "5.2.9.1"}, {"ip": "5.2.4.5"}, {"ip": "5.2.7.1"}, {"ip": "5.2.4.2"}, {"ip": "5.2.0.5"}, {"ip": "5.2.4.6"}, {"ip": "5.1.9.5"}, {"ip": "5.2.0.1"}, {"ip": "5.2.4.8"}, {"ip": "5.2.5.2"}, {"ip": "5.2.6.5"}, ],
    "5.2.2.7": [{"ip": "5.2.2.6"}, {"ip": "5.2.9.0"}, {"ip": "5.2.2.1"}, {"ip": "5.2.2.3"}, {"ip": "5.2.6.8"}, {"ip": "5.2.3.8"}, {"ip": "5.2.9.1"}, {"ip": "5.2.6.7"}, {"ip": "5.2.1.1"}, {"ip": "5.1.9.8"}, {"ip": "5.2.5.3"}, ],
    "5.2.2.6": [{"ip": "5.2.6.2"}, {"ip": "5.2.2.7"}, {"ip": "5.2.3.7"}, {"ip": "5.2.6.9"}, {"ip": "5.2.7.7"}, {"ip": "5.2.1.3"}, {"ip": "5.2.0.4"}, {"ip": "5.1.9.4"}, {"ip": "5.1.9.5"}, {"ip": "5.2.1.4"}, {"ip": "5.2.4.6"}, {"ip": "5.2.9.1"}, {"ip": "5.2.0.8"}, ],
    "5.2.2.5": [{"ip": "5.2.1.4"}, {"ip": "5.2.6.2"}, {"ip": "5.2.6.4"}, {"ip": "5.2.2.3"}, {"ip": "5.2.6.9"}, {"ip": "5.2.7.7"}, {"ip": "5.2.7.6"}, {"ip": "5.2.7.0"}, {"ip": "5.2.8.0"}, {"ip": "5.2.0.5"}, {"ip": "5.1.9.4"}, {"ip": "5.2.7.3"}, {"ip": "5.1.9.7"}, ],
    "5.2.2.4": [{"ip": "5.2.6.9"}, {"ip": "5.2.0.6"}, {"ip": "5.2.0.7"}, {"ip": "5.2.0.4"}, {"ip": "5.2.0.2"}, {"ip": "5.2.5.9"}, {"ip": "5.2.8.7"}, ],
    "5.2.9.0": [{"ip": "5.2.6.0"}, {"ip": "5.2.2.7"}, {"ip": "5.2.3.7"}, {"ip": "5.2.2.3"}, {"ip": "5.2.3.9"}, {"ip": "5.2.6.9"}, {"ip": "5.2.8.3"}, {"ip": "5.2.0.5"}, {"ip": "5.2.1.4"}, {"ip": "5.2.5.6"}, {"ip": "5.2.1.9"}, {"ip": "5.2.4.9"}, {"ip": "5.2.5.2"}, {"ip": "5.2.0.8"}, ],
    "5.2.9.1": [{"ip": "5.2.2.6"}, {"ip": "5.2.2.7"}, {"ip": "5.2.2.0"}, {"ip": "5.2.1.5"}, {"ip": "5.2.6.8"}, {"ip": "5.2.0.1"}, {"ip": "5.2.7.5"}, {"ip": "5.2.4.4"}, {"ip": "5.2.4.5"}, {"ip": "5.2.5.8"}, {"ip": "5.2.2.1"}, {"ip": "5.2.6.5"}, ],
    "5.2.1.6": [{"ip": "5.2.3.3"}, {"ip": "5.2.7.8"}, {"ip": "5.2.6.8"}, {"ip": "5.2.3.8"}, {"ip": "5.2.1.4"}, {"ip": "5.2.7.1"}, {"ip": "5.2.8.6"}, {"ip": "5.2.0.4"}, {"ip": "5.1.9.3"}, {"ip": "5.2.0.0"}, {"ip": "5.2.4.5"}, {"ip": "5.1.9.8"}, {"ip": "5.2.5.6"}, {"ip": "5.2.1.8"}, {"ip": "5.1.9.7"}, {"ip": "5.2.0.8"}, {"ip": "5.2.5.0"}, ],
    "5.2.1.7": [{"ip": "5.2.7.5"}, {"ip": "5.2.2.9"}, {"ip": "5.2.8.0"}, {"ip": "5.2.7.0"}, {"ip": "5.2.4.0"}, {"ip": "5.2.7.3"}, {"ip": "5.1.9.9"}, {"ip": "5.2.5.5"}, ],
    "5.2.1.4": [{"ip": "5.2.3.1"}, {"ip": "5.2.2.5"}, {"ip": "5.2.2.6"}, {"ip": "5.2.7.8"}, {"ip": "5.2.6.7"}, {"ip": "5.2.8.7"}, {"ip": "5.2.8.4"}, {"ip": "5.2.9.0"}, {"ip": "5.2.8.1"}, {"ip": "5.2.1.6"}, {"ip": "5.2.6.9"}, {"ip": "5.1.9.9"}, {"ip": "5.2.4.8"}, ],
    "5.2.1.5": [{"ip": "5.2.6.3"}, {"ip": "5.2.6.8"}, {"ip": "5.2.9.1"}, {"ip": "5.2.8.5"}, {"ip": "5.2.0.2"}, {"ip": "5.2.0.3"}, {"ip": "5.2.5.1"}, {"ip": "5.2.0.9"}, ],
    "5.2.1.2": [{"ip": "5.2.7.9"}, {"ip": "5.2.2.1"}, {"ip": "5.2.8.6"}, {"ip": "5.2.2.8"}, {"ip": "5.2.1.3"}, {"ip": "5.2.0.2"}, {"ip": "5.2.5.9"}, {"ip": "5.2.4.5"}, ],
    "5.2.1.3": [{"ip": "5.2.2.6"}, {"ip": "5.2.7.8"}, {"ip": "5.2.1.2"}, {"ip": "5.2.3.6"}, {"ip": "5.2.4.3"}, {"ip": "5.2.0.4"}, {"ip": "5.2.0.2"}, {"ip": "5.2.0.3"}, {"ip": "5.1.9.8"}, {"ip": "5.2.4.9"}, ],
    "5.2.1.0": [{"ip": "5.2.3.0"}, {"ip": "5.2.7.6"}, {"ip": "5.2.6.4"}, {"ip": "5.2.3.6"}, {"ip": "5.2.7.4"}, {"ip": "5.2.8.5"}, {"ip": "5.2.2.9"}, {"ip": "5.2.0.1"}, {"ip": "5.1.9.7"}, {"ip": "5.2.5.1"}, ],
    "5.2.1.1": [{"ip": "5.2.3.1"}, {"ip": "5.2.2.7"}, {"ip": "5.2.8.8"}, {"ip": "5.2.2.8"}, {"ip": "5.2.4.0"}, {"ip": "5.2.6.3"}, {"ip": "5.2.5.6"}, {"ip": "5.2.5.2"}, ],
    "5.2.1.8": [{"ip": "5.2.6.3"}, {"ip": "5.2.3.4"}, {"ip": "5.2.6.6"}, {"ip": "5.2.8.5"}, {"ip": "5.2.0.2"}, {"ip": "5.2.1.6"}, {"ip": "5.1.9.4"}, {"ip": "5.2.5.4"}, {"ip": "5.2.5.2"}, {"ip": "5.2.2.1"}, ],
    "5.2.1.9": [{"ip": "5.2.8.6"}, {"ip": "5.2.9.0"}, {"ip": "5.1.9.7"}, {"ip": "5.2.0.5"}, {"ip": "5.2.6.7"}, ],
    "5.1.9.9": [{"ip": "5.2.6.8"}, {"ip": "5.2.7.4"}, {"ip": "5.2.8.4"}, {"ip": "5.2.4.5"}, {"ip": "5.2.2.8"}, {"ip": "5.2.7.0"}, {"ip": "5.2.0.4"}, {"ip": "5.2.1.7"}, {"ip": "5.2.1.4"}, {"ip": "5.1.9.7"}, {"ip": "5.2.0.8"}, ],
    "5.1.9.8": [{"ip": "5.2.3.3"}, {"ip": "5.2.2.7"}, {"ip": "5.2.6.7"}, {"ip": "5.2.8.9"}, {"ip": "5.2.8.6"}, {"ip": "5.2.8.5"}, {"ip": "5.2.1.3"}, {"ip": "5.2.0.5"}, {"ip": "5.2.1.6"}, {"ip": "5.2.4.4"}, {"ip": "5.2.4.9"}, {"ip": "5.2.5.2"}, {"ip": "5.2.5.1"}, ],
    "5.1.9.5": [{"ip": "5.2.2.6"}, {"ip": "5.2.6.3"}, {"ip": "5.2.2.0"}, {"ip": "5.2.6.9"}, {"ip": "5.2.7.1"}, {"ip": "5.2.2.9"}, {"ip": "5.2.3.5"}, {"ip": "5.2.5.0"}, ],
    "5.1.9.4": [{"ip": "5.2.2.5"}, {"ip": "5.2.2.6"}, {"ip": "5.2.2.1"}, {"ip": "5.2.2.3"}, {"ip": "5.2.3.8"}, {"ip": "5.2.4.2"}, {"ip": "5.2.2.8"}, {"ip": "5.2.6.2"}, {"ip": "5.2.8.3"}, {"ip": "5.2.0.6"}, {"ip": "5.2.4.1"}, {"ip": "5.2.1.8"}, ],
    "5.1.9.7": [{"ip": "5.2.2.5"}, {"ip": "5.2.3.3"}, {"ip": "5.1.9.3"}, {"ip": "5.2.3.4"}, {"ip": "5.2.3.7"}, {"ip": "5.2.7.5"}, {"ip": "5.2.1.0"}, {"ip": "5.2.4.6"}, {"ip": "5.2.1.6"}, {"ip": "5.2.4.5"}, {"ip": "5.1.9.9"}, {"ip": "5.2.5.6"}, {"ip": "5.2.1.9"}, {"ip": "5.2.5.1"}, ],
    "5.1.9.6": [{"ip": "5.2.5.4"}, {"ip": "5.2.0.4"}, {"ip": "5.2.3.2"}, {"ip": "5.2.2.8"}, {"ip": "5.2.5.1"}, ],
    "5.1.9.3": [{"ip": "5.2.6.5"}, {"ip": "5.2.6.9"}, {"ip": "5.2.5.8"}, {"ip": "5.2.8.3"}, {"ip": "5.2.0.5"}, {"ip": "5.2.1.6"}, {"ip": "5.1.9.7"}, ],
    "5.1.9.2": [{"ip": "5.2.6.0"}, {"ip": "5.2.3.3"}, {"ip": "5.2.4.1"}, {"ip": "5.2.6.7"}, {"ip": "5.2.8.7"}, {"ip": "5.2.4.2"}, {"ip": "5.2.0.5"}, {"ip": "5.2.5.1"}, ],
    "5.2.8.9": [{"ip": "5.2.3.1"}, {"ip": "5.2.6.3"}, {"ip": "5.2.6.6"}, {"ip": "5.2.6.9"}, {"ip": "5.2.2.8"}, {"ip": "5.2.0.4"}, {"ip": "5.2.0.2"}, {"ip": "5.2.0.3"}, {"ip": "5.1.9.8"}, ],
    "5.2.8.8": [{"ip": "5.2.3.1"}, {"ip": "5.2.7.4"}, {"ip": "5.2.7.3"}, {"ip": "5.2.1.1"}, {"ip": "5.2.4.1"}, {"ip": "5.2.0.2"}, {"ip": "5.2.8.7"}, {"ip": "5.2.5.7"}, {"ip": "5.2.5.2"}, {"ip": "5.2.5.1"}, ],
    "5.2.8.1": [{"ip": "5.2.6.0"}, {"ip": "5.2.3.4"}, {"ip": "5.2.6.6"}, {"ip": "5.2.3.9"}, {"ip": "5.2.8.4"}, {"ip": "5.2.1.4"}, {"ip": "5.2.4.4"}, {"ip": "5.2.5.8"}, {"ip": "5.2.5.6"}, {"ip": "5.2.5.5"}, ],
    "5.2.8.0": [{"ip": "5.2.2.5"}, {"ip": "5.2.6.9"}, {"ip": "5.2.0.1"}, {"ip": "5.2.2.8"}, {"ip": "5.2.2.9"}, {"ip": "5.2.7.3"}, {"ip": "5.2.0.6"}, {"ip": "5.2.0.4"}, {"ip": "5.2.0.5"}, {"ip": "5.2.1.7"}, {"ip": "5.2.4.4"}, {"ip": "5.2.3.8"}, {"ip": "5.2.5.7"}, {"ip": "5.2.5.6"}, {"ip": "5.2.5.3"}, {"ip": "5.2.5.2"}, ],
    "5.2.8.3": [{"ip": "5.2.9.0"}, {"ip": "5.2.6.4"}, {"ip": "5.2.3.4"}, {"ip": "5.2.8.7"}, {"ip": "5.2.8.5"}, {"ip": "5.2.7.0"}, {"ip": "5.2.7.3"}, {"ip": "5.1.9.3"}, {"ip": "5.1.9.4"}, {"ip": "5.2.5.5"}, {"ip": "5.2.5.2"}, ],
    "5.2.8.2": [{"ip": "5.2.6.0"}, {"ip": "5.2.3.1"}, {"ip": "5.2.3.4"}, {"ip": "5.2.6.7"}, {"ip": "5.2.6.8"}, {"ip": "5.2.6.9"}, {"ip": "5.2.7.1"}, {"ip": "5.2.7.2"}, {"ip": "5.2.4.1"}, {"ip": "5.2.0.3"}, {"ip": "5.2.0.1"}, ],
    "5.2.8.5": [{"ip": "5.2.6.2"}, {"ip": "5.2.6.3"}, {"ip": "5.2.6.5"}, {"ip": "5.2.3.8"}, {"ip": "5.2.7.1"}, {"ip": "5.2.8.3"}, {"ip": "5.2.1.0"}, {"ip": "5.2.1.5"}, {"ip": "5.1.9.8"}, {"ip": "5.2.1.8"}, ],
    "5.2.8.4": [{"ip": "5.2.6.0"}, {"ip": "5.2.3.1"}, {"ip": "5.2.2.2"}, {"ip": "5.2.6.8"}, {"ip": "5.2.7.7"}, {"ip": "5.2.1.4"}, {"ip": "5.2.7.3"}, {"ip": "5.2.8.1"}, {"ip": "5.2.4.2"}, {"ip": "5.2.5.9"}, {"ip": "5.2.5.8"}, {"ip": "5.1.9.9"}, {"ip": "5.2.4.9"}, {"ip": "5.2.5.2"}, ],
    "5.2.8.7": [{"ip": "5.2.2.4"}, {"ip": "5.2.6.1"}, {"ip": "5.2.8.8"}, {"ip": "5.2.6.6"}, {"ip": "5.2.6.7"}, {"ip": "5.2.6.9"}, {"ip": "5.2.8.3"}, {"ip": "5.2.7.3"}, {"ip": "5.2.0.7"}, {"ip": "5.2.4.0"}, {"ip": "5.2.4.1"}, {"ip": "5.2.0.2"}, {"ip": "5.2.1.4"}, {"ip": "5.1.9.2"}, {"ip": "5.2.5.6"}, ],
    "5.2.8.6": [{"ip": "5.2.6.2"}, {"ip": "5.2.7.8"}, {"ip": "5.2.7.7"}, {"ip": "5.2.5.7"}, {"ip": "5.2.2.9"}, {"ip": "5.2.1.2"}, {"ip": "5.2.1.6"}, {"ip": "5.2.4.8"}, {"ip": "5.1.9.8"}, {"ip": "5.2.5.6"}, {"ip": "5.2.5.5"}, {"ip": "5.2.1.9"}, ],
    "5.2.0.1": [{"ip": "5.2.3.3"}, {"ip": "5.2.2.0"}, {"ip": "5.2.2.1"}, {"ip": "5.2.0.7"}, {"ip": "5.2.7.4"}, {"ip": "5.2.9.1"}, {"ip": "5.2.8.2"}, {"ip": "5.2.8.0"}, {"ip": "5.2.7.1"}, {"ip": "5.2.4.3"}, {"ip": "5.2.1.0"}, ],
    "5.2.0.0": [{"ip": "5.2.0.6"}, {"ip": "5.2.6.5"}, {"ip": "5.2.7.7"}, {"ip": "5.2.7.0"}, {"ip": "5.2.4.2"}, {"ip": "5.2.1.6"}, {"ip": "5.2.5.4"}, ],
    "5.2.0.3": [{"ip": "5.2.6.2"}, {"ip": "5.2.3.5"}, {"ip": "5.2.1.5"}, {"ip": "5.2.3.7"}, {"ip": "5.2.8.9"}, {"ip": "5.2.7.7"}, {"ip": "5.2.8.2"}, {"ip": "5.2.1.3"}, {"ip": "5.2.4.7"}, {"ip": "5.2.5.9"}, ],
    "5.2.0.2": [{"ip": "5.2.2.4"}, {"ip": "5.2.1.8"}, {"ip": "5.2.2.2"}, {"ip": "5.2.8.8"}, {"ip": "5.2.8.9"}, {"ip": "5.2.6.9"}, {"ip": "5.2.2.8"}, {"ip": "5.2.1.3"}, {"ip": "5.2.1.2"}, {"ip": "5.2.4.0"}, {"ip": "5.2.1.5"}, {"ip": "5.2.8.7"}, {"ip": "5.2.5.7"}, {"ip": "5.2.4.9"}, ],
    "5.2.0.5": [{"ip": "5.2.3.0"}, {"ip": "5.2.3.2"}, {"ip": "5.2.2.0"}, {"ip": "5.2.2.5"}, {"ip": "5.2.7.4"}, {"ip": "5.2.7.7"}, {"ip": "5.2.9.0"}, {"ip": "5.2.8.0"}, {"ip": "5.2.4.3"}, {"ip": "5.1.9.2"}, {"ip": "5.1.9.3"}, {"ip": "5.2.5.8"}, {"ip": "5.1.9.8"}, {"ip": "5.2.1.9"}, ],
    "5.2.0.4": [{"ip": "5.2.2.4"}, {"ip": "5.2.1.3"}, {"ip": "5.2.2.6"}, {"ip": "5.2.8.9"}, {"ip": "5.2.7.5"}, {"ip": "5.2.8.0"}, {"ip": "5.2.0.6"}, {"ip": "5.2.1.6"}, {"ip": "5.1.9.6"}, {"ip": "5.1.9.9"}, ],
    "5.2.0.7": [{"ip": "5.2.2.4"}, {"ip": "5.2.6.3"}, {"ip": "5.2.7.5"}, {"ip": "5.2.8.7"}, {"ip": "5.2.4.5"}, {"ip": "5.2.2.9"}, {"ip": "5.2.4.3"}, {"ip": "5.2.4.7"}, {"ip": "5.2.0.1"}, {"ip": "5.2.6.8"}, ],
    "5.2.0.6": [{"ip": "5.2.2.4"}, {"ip": "5.2.3.3"}, {"ip": "5.2.6.5"}, {"ip": "5.2.0.0"}, {"ip": "5.2.6.8"}, {"ip": "5.2.8.0"}, {"ip": "5.2.0.4"}, {"ip": "5.2.4.1"}, {"ip": "5.1.9.4"}, {"ip": "5.2.5.9"}, {"ip": "5.2.5.7"}, ],
    "5.2.0.9": [{"ip": "5.2.3.0"}, {"ip": "5.2.6.5"}, {"ip": "5.2.2.2"}, {"ip": "5.2.6.7"}, {"ip": "5.2.2.3"}, {"ip": "5.2.4.2"}, {"ip": "5.2.4.0"}, {"ip": "5.2.1.5"}, {"ip": "5.2.5.5"}, ],
    "5.2.0.8": [{"ip": "5.2.6.1"}, {"ip": "5.2.2.6"}, {"ip": "5.2.6.3"}, {"ip": "5.2.2.2"}, {"ip": "5.2.7.5"}, {"ip": "5.2.3.8"}, {"ip": "5.2.9.0"}, {"ip": "5.2.1.6"}, {"ip": "5.1.9.9"}, ],
}

DUMMY_SEEDS_B = {
    1: "5.2.4.0",
    2: "5.1.9.6",
    3: "5.2.0.4",
    4: "5.2.3.0",
    5: "5.2.7.8",
    6: "5.2.2.0",
    7: "5.2.8.4",
    8: "5.2.0.8",
}

DUMMY_NETWORK = DUMMY_NETWORK_B

DUMMY_SEEDS = DUMMY_SEEDS_B


def dummy_getaddr(node):
    """
    Returns adjacent nodes based on the dummy network.
    """
    time.sleep(0.2)
    return DUMMY_NETWORK.get(node, [])
