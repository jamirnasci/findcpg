import sys
import os

def findCpg(sequence, window_size, min_gc, min_obs_exp):
  result = []
  i = 0
  while i < len(sequence) - window_size:
    c_count  = 0
    g_count  = 0
    cg_count = 0
    start = i
    end = i + window_size

    window = sequence[start:i + window_size]

    for j in range(0, len(window)):
      if window[j] == 'C':
        c_count += 1
      if window[j] == 'G':
        g_count += 1
      if j < len(window) - 1:
        if window[j] == 'C' and window[j+1] == 'G' :
          cg_count += 1
    gc_content = (c_count + g_count) * 100 / window_size
    obs_exp = cg_count  / ((c_count * g_count) / window_size)

    if gc_content > min_gc and obs_exp > min_obs_exp:
      result.append(
        {
          "start":start + 1,
          "end":end,
          "obs_exp": obs_exp,
          "gc_content":gc_content
        }
      )
      i += window_size
    else:
      i += 1
  return result

if __name__ == '__main__':
  if len(sys.argv) < 4:
    print("Missing args, usage:")
    print("CpG.py <sequence file> <min gc content> <min obs/exp> <window size>")
  else:
    file_path = sys.argv[1]
    min_gc = float(sys.argv[2])
    min_obs_exp = float(sys.argv[3])
    min_window = int(sys.argv[4])

    sequence = ''
    with open(file_path, 'r') as sequence_file:
      lines = sequence_file.readlines()

      for line in lines:
        if line[0] != '>':
          sequence += line.replace('\n', '')
    
    res = findCpg(sequence, min_window, min_gc, min_obs_exp)
    x = []
    gc_array = []
    obs_exp_array = []

    for result in res:
      print("Obs/Exp: {}\tGC Content: {}\tstart: {}\tend: {}".
            format(result["obs_exp"], result["gc_content"], result["start"], result["end"]))
