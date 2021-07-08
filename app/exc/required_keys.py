from http import HTTPStatus

# -------------------------------------


class RequiredKeysError(Exception):
    def __init__(self, payload: dict, key_list: list) -> None:

        self.message = (
            {
                "error": {
                    "blank_fields": key_list,
                    "received_values": dict(payload.values()),
                }
            },
            HTTPStatus.BAD_REQUEST,
        )

        super().__init__(self.message)
