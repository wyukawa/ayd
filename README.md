# chaco

chaco generates Azkaban Job File based on Azkaban YAML DSL.

chaco is derived from ```The Story on a Seashore for Chaco``` of ```Southern All Stars```.

```Southern All Stars``` is the Japanese famous rock band.

##Prerequisites
Python 2.7

##Required Python Libraries
* cliff
* PyYAML

##Install
```
pip install chaco
```

Usage
----------

```
$ chaco -h
usage: chaco [--version] [-v] [--log-file LOG_FILE] [-q] [-h] [--debug]

genereate Azkaban Job File

optional arguments:
  --version            show program's version number and exit
  -v, --verbose        Increase verbosity of output. Can be repeated.
  --log-file LOG_FILE  Specify a file to log output. Disabled by default.
  -q, --quiet          suppress output except warnings and errors
  -h, --help           show this help message and exit
  --debug              show tracebacks on errors

Commands:
  complete       print bash completion command
  generateJob
  help           print detailed help for another command
```

```
$ chaco generateJob
usage: chaco generateJob [-h] --jobyaml JOBYAML [--propertyfile PROPERTYFILE]
                         --outputdir OUTPUTDIR
chaco generateJob: error: argument --jobyaml is required
```

Example
----------

* aaa.yaml

```
foo:
  type: command
  command: echo "foo"
  retries: 1
  retry.backoff: 300000

bar:
  type: command
  command: echo "bar"
  dependencies: foo
  retries: 1
  retry.backoff: 300000

hoge:
  type: command
  dependencies: foo
  command: echo "hoge"
  command.1: echo "hoge1"
  retries: 2
  retry.backoff: 30000

piyo:
  type: command
  dependencies: bar, hoge
  command: echo "piyo"
  retries: 1
  retry.backoff: 300000
```

* execute
```
chaco generateJob --jobyaml aaa.yaml --outputdir aaa
```

then, aaa/aaa.yaml.zip is generated.

If you upload aaa/aaa.yaml.zip, Azkaban Job is the following.

![chaco](screenshot/azkaban_job.png)
