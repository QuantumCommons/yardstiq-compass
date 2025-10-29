from yardstiq.core import (
    provider,
    Backend,
    Benchmark,
    BackendProvider,
    BenchmarkProvider,
)


@provider("compass")
class CompassProvider(BackendProvider, BenchmarkProvider):
    """Compass backend provider for Yardstiq."""

    def get_backend(self, name: str) -> Backend:
        if name == "aer":
            return AerLocalBackend()
        elif name == "qsim":
            return QSimLocalBackend()
        else:
            raise ValueError(f"Unknown backend: {name}")

    def get_benchmark(self, name: str) -> Benchmark:
        if name == "vqe":
            return VQEBenchmark()
        else:
            raise ValueError(f"Unknown benchmark: {name}")
