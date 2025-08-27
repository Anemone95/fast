#!/usr/bin/env python3
import resource

from simurun.launcher import main

# Set maximum heap size (e.g., 500 MB)
max_heap_size = 30 * 1024 * 1024 * 1024  # 500 MB in bytes

# Set memory limit
resource.setrlimit(resource.RLIMIT_AS, (max_heap_size, max_heap_size))

if __name__ == '__main__':
    main()
