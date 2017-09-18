#!/usr/bin/python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import re
import sys
import argparse
from collections import deque
from pathlib import Path
from graphviz import Digraph
from terminal_files import terminal_files
from media_cpp_files import media_cpp_files

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

def includes_in(d, f):
  # Not a valid file?.
  if not Path(src_dir + d + f).is_file():
    print("WARNING: includes_in({},{}) can't find file".format(d,f))
    return []
  includes = []
  with open(src_dir + d + f) as f:
    r = re.compile(r'#\s*include\s*"(.*)"')
    for line in f:
      for x in r.findall(line):
        if Path(src_dir + obj_dir_includes + x).is_file():
          includes += [(obj_dir_includes, x)]
        elif Path(src_dir + d + x).is_file():
          includes += [(d, x)]
  return includes

def friendly_name(header_name):
  # print("friendly_name({})=".format(header_name))
  if header_name.startswith(obj_dir_includes):
    return header_name[len(obj_dir_includes):]
  else:
    return header_name

def is_terminal_header(header_friendly_name):
  return (header_friendly_name.startswith("js") or
          header_friendly_name.startswith("mozilla/ipc/") or
          header_friendly_name.startswith("mozilla/dom/") or
          header_friendly_name in terminal_files or
          header_friendly_name.startswith("nsI") or
          re.match(".*String.h", header_friendly_name) or
          re.match(".*Hashtable.h", header_friendly_name)
          )




src_dir = "/home/cpearce/src/firefox/"
obj_dir_includes = "obj-x86_64-pc-linux-gnu/dist/include/"


output_graph_file_prefix = "output"

headers = set()

# Add files to this list to add roots of the include graph to
# generate.
minimal_import_cpp_files = [
  # ("dom/media/","XiphExtradata.cpp"),
  # ("xpcom/threads/", "nsThread.cpp"),
  # ("xpcom/threads/", "Mutex.h"),
# ("dom/media/","MediaDataDemuxer.h"),
  # ("dom/media/","AudioStream.h"),
  # ("dom/media/","MediaFormatReader.cpp"),
  ("dom/media/","MediaDecoderStateMachine.cpp"),
  # ("dom/media/platforms/agnostic/", "WAVDecoder.cpp"),

  # ("mozglue/misc/", "TimeStamp.cpp"),
  # ("mozglue/misc/", "TimeStamp_darwin.cpp"),
  # ("mozglue/misc/", "TimeStamp.h"),
  # ("mozglue/misc/", "TimeStamp_posix.cpp"),
  # ("mozglue/misc/", "TimeStamp_windows.cpp"),
  # ("mozglue/misc/", "TimeStamp_windows.h"),
]

# Hot edges are those that are known to pull in lots of
# subsystems which we don't want to import into gecko-media.
def is_hot_edge(friendly_name):
  return friendly_name.startswith("js/");
  # hot_edges = [
  #   "nsCOMPtr.h",
  #   "nsISupports.h",
  #   "nsISupportsImpl.h",
  #   "mozilla/mozalloc.h"
  # ]


q = deque(minimal_import_cpp_files)

m = dict()

while len(q) > 0:
  # x = q.pop()
  (u,v) = q.pop()
  includes = includes_in(u,v)
  # print("{} includes {}".format(u+v, includes))
  m[friendly_name(u+v)] = includes

  for (d,f) in filter(lambda x: x[0]+x[1] not in headers, includes):
    if Path(src_dir + d + f).is_file():
      headers.add(d + f)
    header = friendly_name(d+f)
    if not is_terminal_header(header):# and header not in includes:
      q.append((d, f))
    else:
      m[header] = []

dot = Digraph(comment="Include graph for header", format='svg')

for (header, includes) in m.items():
  color = "lightgray" if is_terminal_header(friendly_name(header) ) else "white"
  dot.attr("node", fillcolor=color, style="filled")
  dot.node(friendly_name(header))

for (header, includes) in m.items():
  if not is_terminal_header(header):
    for (d,f) in includes:
      target_name = friendly_name(d+f)
      if is_hot_edge(target_name):
        dot.attr("edge", color="red", penwidth="4")
      else:
        dot.attr("edge", color="black", penwidth="1")
      dot.edge(friendly_name(header), target_name);
dot.render(filename=output_graph_file_prefix)


for header in sorted(m.keys()):
  print(header)