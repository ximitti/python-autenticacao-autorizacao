from http import HTTPStatus

# -------------------------------------


class AllowedKeysError(Exception):
    def __init__(self, payload: dict, key_list: list) -> None:

        self.message = (
            {
                "error": {
                    "allowed_keys": key_list,
                    "received_keys": list(payload.keys()),
                }
            },
            HTTPStatus.BAD_REQUEST,
        )

        super().__init__(self.message)
