#!/bin/bash
# Copyright 2022 Marcos Gómez de Quero Santos
# See LICENSE for details.
# Author: Marcos Gome de Quero (@iSkYrIsE on GitHub)


sudo python3 -m pip install pip --upgrade
sudo python3 -m pip install -r requirements.txt
sudo python3 -m pip install . --upgrade
sudo beer_recognition_api