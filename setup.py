#!/usr/bin/env python

# $Id: setup.py,v 1.1 2002/06/21 18:10:49 jgoerzen Exp $

# IMAP synchronization
# Module: installer
# COPYRIGHT #
# Copyright (C) 2002 - 2018 John Goerzen & contributors
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301  USA

from distutils.core import setup, Command
import offlineimap
import logging
from test.OLItest import TextTestRunner, TestLoader, OLITestLib


class TestCommand(Command):
    """runs the OLI testsuite"""
    description = """Runs the test suite. In order to execute only a single
        test, you could also issue e.g. 'python -m unittest
        test.tests.test_01_basic.TestBasicFunctions.test_01_olistartup' on the
        command line."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        logging.basicConfig(format='%(message)s')
        # set credentials and OfflineImap command to be executed:
        OLITestLib(cred_file='./test/credentials.conf', cmd='./offlineimap.py')
        suite = TestLoader().discover('./test/tests')
        TextTestRunner(verbosity=2, failfast=True).run(suite)


setup(name="offlineimap",
      version=offlineimap.__version__,
      description=offlineimap.__description__,
      long_description=offlineimap.__description__,
      author=offlineimap.__author__,
      author_email=offlineimap.__author_email__,
      url=offlineimap.__homepage__,
      packages=['offlineimap', 'offlineimap.folder',
                'offlineimap.repository', 'offlineimap.ui',
                'offlineimap.utils'],
      scripts=['bin/offlineimap'],
      license=offlineimap.__copyright__ + ", Licensed under the GPL version 2",
      cmdclass={'test': TestCommand},
      install_requires=['distro', 'imaplib2>=3.5', 'rfc6555', 'gssapi[kerberos]', 'portalocker[cygwin]', 'urllib3~=1.25.9', 'keyring']
      )
