from typing import TypedDict, Any, Optional


class HttpResponse(TypedDict):
    statusCode: int
    body: Any


class HttpRequest(TypedDict):
    body: Optional[Any]
