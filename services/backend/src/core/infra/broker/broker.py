from src.core.config.settings import settings
from taskiq import InMemoryBroker
from taskiq.brokers.inmemory_broker import InmemoryResultBackend
from taskiq.middlewares import SimpleRetryMiddleware
from taskiq_aio_pika.broker import AioPikaBroker
from taskiq_pipelines import PipelineMiddleware
from taskiq_redis import RedisAsyncResultBackend

broker = AioPikaBroker(settings.rabbitmq_url)
rbackend = RedisAsyncResultBackend(
    settings.redis_url, result_ex_time=settings.taskiq_result_ex_time
)


if settings.env == "pytest":
    broker = InMemoryBroker()
    rbackend = InmemoryResultBackend()

broker = broker.with_result_backend(rbackend).with_middlewares(
    SimpleRetryMiddleware(), PipelineMiddleware()
)
