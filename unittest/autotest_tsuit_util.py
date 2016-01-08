#!/usr/bin/env python3
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-

import os
import time
import shutil
import tempfile
import unittest
from util import util

class TestPyroServer(unittest.TestCase):

    def setUp(self):
        self.serverPort = util.getFreeTcpPort()

        buf = ""
        buf += "from gi.repository import GLib\n"
        buf += "sys.path.append(\"../src\")\n"
        buf += "from util import util\n"
        buf += "\n"
        buf += "class ServiceObject:\n"
        buf += "    def method(self):\n"
        buf += "        return 100\n"
        buf += "\n"
        buf += "mainloop = GLib.MainLoop()\n"
        buf += "\n"
    	buf += "pyroServer = util.PyroServer(%d)\n" % (port)
        buf += "pyroServer.register(\"main\", ServiceObject())\n"
        buf += "pyroServer.attach(mainloop)\n"
        buf += "\n"
        buf += "mainloop.run()\n"
        with open("./_test_server.py", "w") as f:
            f.write(buf)

        proc = subprocess.Open("python3 ./_test_server.py", shell=True, universal_newlines=True)
        time.sleep(1)

    def runTest(self):
        obj = Pyro4.Proxy("PYRO:main@localhost:%d" % (self.serverPort))
        assertEqual(obj.method(), 100)

    def tearDown(self):
        proc.terminate()
        proc.wait()
        os.unlink("./_test_server.py")
