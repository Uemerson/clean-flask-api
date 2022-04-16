from src.presentation.protocols.http import HttpRequest, HttpResponse


class Controller:
    def handle(self, http_request: HttpRequest) -> HttpResponse: ...
