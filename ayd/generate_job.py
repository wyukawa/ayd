#!/usr/bin/env python
# encoding: utf-8

import os
import zipfile
import yaml
import shutil

import logging

from cliff.command import Command

class Generate_Job(Command):

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Generate_Job, self).get_parser(prog_name)
        parser.add_argument('--jobyaml', required=True)
        parser.add_argument('--propertyfile')
        parser.add_argument('--outputdir', required=True)
        return parser

    def take_action(self, parsed_args):
        jobyaml = parsed_args.jobyaml
        if os.path.exists(jobyaml) == False:
            raise Exception("%s doesn't exist" % (jobyaml))

        outputdir = parsed_args.outputdir
        if os.path.exists(outputdir):
            raise Exception("%s already exists" % (outputdir))
        os.mkdir(outputdir)

        with open(jobyaml, "r") as f:
            y = yaml.load(f)
            zipfile_path = os.path.join(outputdir, os.path.basename(f.name) + ".zip")
            zip = zipfile.ZipFile(zipfile_path, "w", zipfile.ZIP_DEFLATED)

            if parsed_args.propertyfile:
                propertyfile = parsed_args.propertyfile
                if os.path.exists(propertyfile) == False:
                    raise Exception("%s doesn't exist" % (propertyfile))
                shutil.copy(propertyfile, outputdir)
                p = os.path.join(outputdir, os.path.basename(propertyfile))
                zip.write(p)
                os.remove(p)

            for flow_name, flow_content in y.items():
                self.log.debug("flow_name=%s, flow_content=%s" % (flow_name, flow_content))
                flow_dir = os.path.join(outputdir, flow_name)
                os.mkdir(flow_dir)
                job_file_name = flow_name + ".job"
                job_file_path = os.path.join(flow_dir, job_file_name)
                with open(job_file_path, "w") as o:
                    for k, v in flow_content.items():
                        if v is None:
                            raise Exception("%s at %s has no value" % (k, flow_name))
                        if k == "type" or k == "dependencies" or k == "retries" or k == "retry.backoff" or k[0:7] == "command":
                            o.write(k + "=" + str(v))
                            o.write("\n")
          
                zip.write(job_file_path)
                os.remove(job_file_path)
                os.rmdir(flow_dir)
