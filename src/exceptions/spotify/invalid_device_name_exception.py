class InvalidDeviceNameException(Exception):
    def __init__(self) -> None:
        super().__init__('Spotify: Invalid device name, verify in .env')
