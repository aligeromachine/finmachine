from machine.tools.model import Payload, WidgetRange


def to_payload(rng: list[WidgetRange]) -> list[Payload]:
    return [Payload(**it.model_dump()) for it in rng]
