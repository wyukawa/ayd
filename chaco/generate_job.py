#!/usr/bin/env python
# encoding: utf-8

import os
import logging

from cliff.command import Command

class Generate_Job(Command):

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Generate_Job, self).get_parser(prog_name)
        parser.add_argument('--outputdir', required=True)
        return parser

    def take_action(self, parsed_args):
        outputdir = parsed_args.outputdir
        if os.path.exists(outputdir):
           raise Exception("%s already exists" % (outputdir))
