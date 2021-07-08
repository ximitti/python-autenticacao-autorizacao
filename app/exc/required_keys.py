from http import HTTPStatus

# -------------------------------------


class RequiredKeysError(Exception):
    def __init__(self, payload: dict, key_list: list) -> None:

        print(key_list)

        self.message = (
            {
                "error": {
                    "blank_fields": key_list,
                    "received_values": payload,
                }
            },
            HTTPStatus.BAD_REQUEST,
        )

        super().__init__(self.message)
