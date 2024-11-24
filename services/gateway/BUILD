python_sources(
    name="python",
    resolve="gateway",
    sources=["**/*.py"],
)
python_tests(
    name="tests",
    sources=["**/test_*.py"],
    resolve="gateway",
)
poetry_requirements(name="poetry", resolve="gateway")
pex_binary(
    name="bin",
    resolve="gateway",
    execution_mode="venv",
    entry_point="gateway.application.api.main",
)
