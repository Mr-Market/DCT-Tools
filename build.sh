echo "DCTtools Installer v1.0"
echo "Installing prerequisites "
sudo apt-get install python3-pip -y 
echo "Installing dependencies "
sudo pip3 install -r requirements.txt 
mkdir build
cd build
cython3 ../dcttools.py --embed -o dcttools.c --verbose
if [ $? -eq 0 ]; then
    echo [SUCCESS] C code Generated
else
    echo [ERROR] cython3 was unable to generate C code. Build failed.
    exit 1
fi
gcc -Os -I /usr/include/python3.8 -o dcttools dcttools.c -lpython3.8 -lpthread -lm -lutil -ldl
if [ $? -eq 0 ]; then
    echo [SUCCESS] Static Binary Compiled
else
    echo [ERROR] Build failed
    exit 1
fi
sudo cp -r dcttools /usr/bin/
if [ $? -eq 0 ]; then
    echo [SUCCESS] Binary copied to /usr/bin 
else
    echo [ERROR] Copy Failed. Unable to copy
    exit 1
fi