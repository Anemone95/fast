#!/usr/bin/env python3
import resource

from simurun.launcher import main
max_heap_size = 30 * 1024 * 1024 * 1024  # 30GB

# Set memory limit
resource.setrlimit(resource.RLIMIT_AS, (max_heap_size, max_heap_size))
if __name__ == '__main__':
    main()
