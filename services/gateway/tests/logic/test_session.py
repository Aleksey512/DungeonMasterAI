# type:ignore
import pytest
from gateway.logic import TypedContainer
from gateway.logic.commands.test.commands import SessionTestCommand
from gateway.logic.mediators.base import BaseMediator


@pytest.mark.asyncio
async def test_session(mediator: BaseMediator, container: TypedContainer):
    sessions = await mediator.handle_command(SessionTestCommand())
    assert len(sessions) == 2
    assert id(sessions[0]) == id(sessions[1])

    new_mediator = container.resolve(BaseMediator)
    new_sessions = await new_mediator.handle_command(SessionTestCommand())
    assert len(new_sessions) == 2
    assert id(new_sessions[0]) == id(new_sessions[1])
    assert hash(sessions) != hash(new_sessions)
