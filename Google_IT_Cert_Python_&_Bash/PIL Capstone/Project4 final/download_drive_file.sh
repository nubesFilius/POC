#!/bin/bash

# First parameter is the ID, second parameter is the filename
FILEID=$1
FILENAME=$2

# This script downloads the drive file with the given ID and saves it with the given name

COOKIE_FILE=$(mktemp cookiesXXXX.txt)

# First get the confirmation prompt because the file is too big
# Originally in Linux with wget = curl is for MAC
CONFIRM=$(curl -L ${COOKIE_FILE} "https://docs.google.com/uc?export=download&id=${FILEID}" | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')

# Then download the file using the confirmation prompt
curl -L ${COOKIE_FILE} -o "https://docs.google.com/uc?export=download&confirm=${CONFIRM}&id=${FILEID}" -O ${FILENAME}

# Finally, delete the cookie file
rm ${COOKIE_FILE}
