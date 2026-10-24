import os

# one thread per worker process: the run is parallel across processes
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

from .cli import main  # noqa: E402

if __name__ == "__main__":
    main()
