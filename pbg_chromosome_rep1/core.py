"""build_core() — register all wrappers, types, adapters, stubs for chromosome-rep1."""
from process_bigraph import allocate_core


def build_core():
    core = allocate_core()
    # /pbg-pull-processes will populate this with core.register_link(...) calls.
    return core
