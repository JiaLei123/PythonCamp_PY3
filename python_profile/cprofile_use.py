import cProfile

from python_profile.benchmark import benchmark

pr = cProfile.Profile()
pr.enable()

benchmark()

pr.disable()
pr.print_stats(sort='time')