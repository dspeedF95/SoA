#!/usr/bin/env bash
# Original file from Girl Life ecv - Cat

set -Eexo pipefail

# Set those lines to fit your setup.
# This is where glife.qsp will be copied. If you don't want to move it just comment (#) the line below.
#DESTDIR=../SOB

# The file that will be generated or open
QSPFILE=SOA_EE.qsp

#######################################################################

./txtmerge.py main SOA_EE.txt
if [[ "$OSTYPE" == "linux-gnu" ]] || [[ "$OSTYPE" == "linux-musl" ]]; then
	./txt2gam.linux SOA_EE.txt "${QSPFILE}" 1> /dev/null
elif [[ "$OSTYPE" == "darwin"* ]]; then
	./txt2gam.mac SOA_EE.txt "${QSPFILE}" 1> /dev/null
elif [[ "$OSTYPE" == "msys" ]]; then
	if [[ "$MSYSTEM_CARCH" == "x86_64" ]]; then
		./txt2gam64.exe SOA_EE.txt "${QSPFILE}" 1> /dev/null
	else
		./txt2gam.exe SOA_EE.txt "${QSPFILE}" 1> /dev/null
	fi
else
	echo "Unsupported Operating System"
	exit 1
fi
if [ -d "${DESTDIR}" ]; then
	cp --reflink=auto "${QSPFILE}" "${DESTDIR}"
fi

