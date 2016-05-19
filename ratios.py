#!/usr/bin/python
# encoding: utf-8

import sys
import csv
from workflow import Workflow

def main(wf):
  args = wf.args
  with open('ratios.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
      wf.add_item(', '.join(row), u'Item subtitle')

  wf.send_feedback()


if __name__ == '__main__':
  # Create a global `Workflow` object
  wf = Workflow()
  # Call your entry function via `Workflow.run()` to enable its helper
  # functions, like exception catching, ARGV normalization, magic
  # arguments etc.
  sys.exit(wf.run(main))
