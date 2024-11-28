resources(name="alembic", sources=["alembic.ini", "migrations/script.py.mako"])
python_sources(
    name="python_sources",
    resolve="gateway",
    sources=["**/*.py"],
    dependencies=[
        ":poetry",
    ],
)
python_tests(
    name="tests",
    sources=["**/test_*.py"],
    resolve="gateway",
    dependencies=[":python_sources"],
)
poetry_requirements(name="poetry", resolve="gateway")

pex_binary(
    name="main",
    resolve="gateway",
    execution_mode="venv",
    layout="packed",
    dependencies=[":python_sources", ":alembic"],
    entry_point="gateway.manage",
)
