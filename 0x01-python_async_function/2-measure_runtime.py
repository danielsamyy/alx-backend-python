#!/usr/bin/env python3
"""
    This Module contains the basics for async practices
    Author: Peter Ekwere
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ This function measures the execution time of wait n

    Args:
        n (int): an integer
        max_delay (int): an integer

    Returns:
        float: time / n
    """
    start_time = time.time()
    result = asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    result = (end_time - start_time) / n
    return result
