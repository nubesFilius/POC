#!/usr/bin/env python

import subprocess, os
from multiprocessing import Pool

src = "../data/prod/"
dest = "../data/prod_backup/"

for directories in os.walk("../data/prod/", topdown=True):
    for files in directories:
        #print(files)

subprocess.call(["rsync", "-arq", src, dest])

def run(task):
  # Do something with task here
    print("Handling {}".format(task))
if __name__ == "__main__":
  tasks = ['task1', 'task2', 'task3']
  # Create a pool of specific number of CPUs
  p = Pool(len(tasks))
  # Start each task within the pool
  p.map(run, tasks)
