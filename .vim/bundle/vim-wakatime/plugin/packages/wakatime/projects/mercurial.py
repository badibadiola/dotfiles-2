# -*- coding: utf-8 -*-
"""
    wakatime.projects.mercurial
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Information about the mercurial project for a given file.

    :copyright: (c) 2013 Alan Hamlett.
    :license: BSD, see LICENSE for more details.
"""

import logging
import os
import sys

from .base import BaseProject
from ..compat import u, open


log = logging.getLogger('WakaTime')


class Mercurial(BaseProject):

    def process(self):
        self.configDir = self._find_hg_config_dir(self.path)
        return self.configDir is not None

    def name(self):
        if self.configDir:
            return u(os.path.basename(os.path.dirname(self.configDir)))
        return None

    def branch(self):
        if self.configDir:
            branch_file = os.path.join(self.configDir, 'branch')
            try:
                with open(branch_file, 'r', encoding='utf-8') as fh:
                    return u(fh.readline().strip().rsplit('/', 1)[-1])
            except UnicodeDecodeError:
                try:
                    with open(branch_file, 'r', encoding=sys.getfilesystemencoding()) as fh:
                        return u(fh.readline().strip().rsplit('/', 1)[-1])
                except:
                    log.exception("Exception:")
            except IOError:
                log.exception("Exception:")
        return u('default')

    def _find_hg_config_dir(self, path):
        path = os.path.realpath(path)
        if os.path.isfile(path):
            path = os.path.split(path)[0]
        if os.path.isdir(os.path.join(path, '.hg')):
            return os.path.join(path, '.hg')
        split_path = os.path.split(path)
        if split_path[1] == '':
            return None
        return self._find_hg_config_dir(split_path[0])
