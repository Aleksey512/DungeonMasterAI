python_sources(
    name="lib", sources=["**/*.py"], resolve=parametrize("default", "gateway")
)
python_tests(
    name="tests",
    sources=["**/test_*.py"],
    dependencies=[":lib"],
)

python_distribution(
    name="dist",
    wheel=True,
    sdist=True,
    provides=setup_py(
        name="mediators",
        version="0.0.1",
        description="Mediators lib.",
    ),
)
