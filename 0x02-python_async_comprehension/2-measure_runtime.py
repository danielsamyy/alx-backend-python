#!/usr/bin/env python3
"""
    This Module contains basic async practices
"""
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ This Function measures the runtime of async comprehension

    Returns:
        float: _description_
    """
    coroutine = [async_comprehension() for i in range(4)]
    start_time = time()
    await asyncio.gather(*coroutine)
    end_time = time()
    return end_time - start_time
