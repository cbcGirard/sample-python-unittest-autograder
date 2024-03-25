
echo "Executing in $1"
. $1/py-version.sh

if [ "$PY_VERSION" != "3" ]; then
    apt-add-repository ppa:deadsnakes/ppa -y
    apt-get update
    apt-get install -y python${PY_VERSION} python${PY_VERSION}-{dev,distutils}
else
    apt-get install -y python3 python3-pip python3-dev
    apt-get update
fi
