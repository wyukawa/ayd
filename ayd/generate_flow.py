#!/usr/bin/env python
# encoding: utf-8

import os
import yaml

import logging

from cliff.command import Command

class Generate_Flow(Command):

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Generate_Flow, self).get_parser(prog_name)
        parser.add_argument('--flowyaml', required=True)
        parser.add_argument('--outputdir', required=True)
        return parser

    def take_action(self, parsed_args):
        flowyaml = parsed_args.flowyaml
        if os.path.exists(flowyaml) == False:
            raise Exception("%s doesn't exist" % (flowyaml))

        outputdir = parsed_args.outputdir
        if os.path.exists(outputdir):
            raise Exception("%s already exists" % (outputdir))
        os.mkdir(outputdir)

        with open(flowyaml, "r") as f:
            y = yaml.load(f)
            for job_name, job_content in y.items():
                self.log.debug("job_name=%s, job_content=%s" % (job_name, job_content))
                job_dir = os.path.join(outputdir, job_name)
                os.mkdir(job_dir)
                job_file_name = job_name + ".job"
                job_file_path = os.path.join(job_dir, job_file_name)
                with open(job_file_path, "w") as o:
                    for k, v in job_content.items():
                        if v is None:
                            raise Exception("%s at %s has no value" % (k, job_name))
                        if k == "type" or k == "dependencies" or k == "retries" or k == "retry.backoff" or k[0:7] == "command":
                            o.write(k + "=" + str(v))
                            o.write("\n")
