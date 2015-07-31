#!/usr/bin/env python
# encoding: utf-8

import os
import yaml

import logging

from cliff.command import Command

class Migrate(Command):

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Migrate, self).get_parser(prog_name)
        parser.add_argument('--jobdir', required=True)
        parser.add_argument('--outputyaml', required=True)
        return parser

    def take_action(self, parsed_args):
        jobdir = parsed_args.jobdir
        if os.path.exists(jobdir) == False:
            raise Exception("%s doesn't exist" % (jobdir))

        outputyaml = parsed_args.outputyaml
        if os.path.exists(outputyaml):
            raise Exception("%s already exists" % (outputyaml))

        with open(outputyaml, "w") as o:
            for dirpath, dirnames, filenames in os.walk(jobdir):
                for filename in filenames:
                    if filename.endswith(".job"):
                        with open(os.path.join(dirpath, filename), "r") as f:
                            dict = {}
                            lines = f.read().split("\n")
                            for line in lines:
                                kv = line.split("=")
                                if len(kv) == 2 and len(kv[1]) > 0:
                                    dict[kv[0]] = kv[1]
                            o.write(yaml.dump({filename.rstrip(".job"):dict}, default_flow_style=False))
                            o.write("\n")
