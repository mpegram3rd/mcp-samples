import json
import math
import random
from json import JSONDecodeError


class NoAAService:
    """
    Support for the No as a Service MCP
    """
    def __init__(self):
        self.reasons = self._load_reasons()

    def _load_reasons(self):
        """
        Loads the `reasons.json` file as a list.
        :return: An array of "no" responses
        """
        try:
            with open("data/no-reasons.json", "r") as garbage_in:
                reasons = json.load(garbage_in)
                return reasons

        except FileNotFoundError:
            print(f"Could not find `reasons.json`.")
            raise
        except JSONDecodeError:
            print(f"`reasons.json` was not valid JSON.")
            raise

    def get_reason(self):
        """
        Returns a random reason from the loaded reasons list.
        :return: A string containing a random reason.
        """
        return self.reasons[math.floor(random.random() * len(self.reasons))]
