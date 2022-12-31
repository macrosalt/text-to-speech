def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

def read_non_empty_lines(addr):
  f = open(addr, "r")
  res = []
  for line in nonblank_lines(f):
    res.append(line)
  return res
  



