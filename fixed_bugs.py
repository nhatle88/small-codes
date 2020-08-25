# Can't open webcam
# https://stackoverflow.com/questions/45944962/you-might-be-loading-two-sets-of-qt-binaries-into-the-same-process
pip uninstall opencv-python
pip install opencv-python-headless
