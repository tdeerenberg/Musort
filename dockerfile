# Musort - Docker installation
# Copyright (C) 2023 tdeerenberg
#
# Sources on github:
# https://github.com/tdeerenberg/Musort
#
# Licensed under the GNU General Public License v3.0 (GPLv3)
# Copyright (C) 2023 tdeerenberg
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


FROM python:3.11

# Update and upgrade packages
RUN apt-get update && apt-get upgrade -y

# Set working directory
WORKDIR /opt/musort/

# Copy project
COPY ./src/config.py /opt/musort/config.py
COPY ./src/variables.py /opt/musort/variables.py
COPY ./src/tinytag.py /opt/musort/tinytag.py
COPY ./src/musort.py /opt/musort/musort.py

# docker run --name musort --rm -it musort --help
ENTRYPOINT ["python3", "musort.py"]
