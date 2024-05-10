
        if request.get("intent") is None:
            return self._error(
                "intent", "Missing intent parameter in request", "intent"
            )

        intent = request.get("intent")
        if intent is None:
            return self._error(
                "intent", "Missing intent parameter in request", "intent"
            )

 