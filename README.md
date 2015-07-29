# ayd

ayd generates Azkaban Job Zip File based on Azkaban YAML DSL.

##Prerequisites
Python 2.7

##Required Python Libraries
* cliff
* PyYAML

##Install
```
pip install ayd
```

Usage
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
ayd generateJob --jobyaml aaa.yaml --outputdir aaa
```

then, aaa/aaa.yaml.zip is generated.

If you upload aaa/aaa.yaml.zip, Azkaban Job is the following.

![ayd](screenshot/azkaban_job.png)
