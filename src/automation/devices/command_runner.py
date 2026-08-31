from __future__ import annotations

import shutil
import subprocess
from typing import Sequence
import time
from automation.devices.command_result import (CommandResult,)

class CommandRunner:

    @staticmethod
    def exists(command: str,) -> bool:
        return shutil.which(command) is not None

    @staticmethod
    def which(command: str,):
        return shutil.which(command)

    @staticmethod
    def run(command: Sequence[str],*,timeout: int | None = None,cwd: str | None = None,):
        start = time.perf_counter()
        completed = subprocess.run(command,capture_output=True,text=True,timeout=timeout,cwd=cwd,)
        elapsed = time.perf_counter() - start
        return CommandResult(success=completed.returncode == 0,stdout=completed.stdout,stderr=completed.stderr,returncode=completed.returncode,execution_time=elapsed,)

    @staticmethod
    def start(command: Sequence[str],*,cwd: str | None = None,):
        return subprocess.Popen(command,cwd=cwd,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,)

    @staticmethod
    def shell(command: str,*,timeout: int | None = None,cwd: str | None = None,):
        start = time.perf_counter()
        completed = subprocess.run(command,shell=True,capture_output=True,text=True,timeout=timeout,cwd=cwd,)
        elapsed = time.perf_counter() - start
        return CommandResult(success=completed.returncode == 0,stdout=completed.stdout,stderr=completed.stderr,returncode=completed.returncode,execution_time=elapsed,)

    @staticmethod
    def check(command: Sequence[str],):
        subprocess.run(command,check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,)
        completed = subprocess.run(command,check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,)
        return CommandResult(success=True,returncode=completed.returncode,)

    def __repr__(self):
        return "<CommandRunner>"
