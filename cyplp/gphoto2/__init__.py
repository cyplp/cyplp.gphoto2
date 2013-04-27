"""
Class for pilot gphoto2
"""
import os.path
import logging
import subprocess


class GPhoto2(object):
    """
    Class for pilot gphoto2
    """

    def __init__(self, gphoto2Path='/usr/bin/gphoto2', logger='gphoto2'):
        """
        Constructor.
        :param gphoto2Path: path to the gphoto2 binary.

        if gphoto2 isn't found, an exception is raises.
        """
        if not os.path.isfile(gphoto2Path):
            raise IOError("gphoto2 not found at %s" % gphoto2Path)
        self._gphoto2 = gphoto2Path

        self._logger = logging.getLogger(logger)
        self._logger.info('init done')


    def initCamera(self):
        """
        init the camera.

        execute gphoto2 --auto-detect.
        """
        self._logger.debug("init camera")
        subprocess.check_call("%s --auto-detect" % self._gphoto2,
                              shell=True)

    def takePicture(self, filename, retry=3):
        """
        Take a picture.

        :param retry: number of retry.

        execute gphoto2 --capture-image
        """
        # TODO all sort of thing like, retry, exception reinit
        subprocess.check_call("%s --capture-image-and-download --filename %s" % (self._gphoto2, filename),
                              shell=True)

