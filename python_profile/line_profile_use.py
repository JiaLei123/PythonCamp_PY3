import sys
import line_profiler
from python_profile.benchmark import benchmark, primise

pr = line_profiler.LineProfiler(benchmark, primise)
pr.enable()

benchmark()

pr.disable()
pr.print_stats(sys.stdout)