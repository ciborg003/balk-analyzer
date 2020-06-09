import asyncio
import subprocess
import os
import sys
import _thread as thread
import pyansys

async def command():
    file_name = "D:\\master degree\cell-analyzer\\researches\\28-01-2020 10-56-36\\1\\file.rst"
    print(file_name)
    res = pyansys.read_binary(file_name)
    res.plot_nodal_solution(0, 'x', label='Displacement')
    return True

asyncio.
asyncio.run(command())

print("hello")
