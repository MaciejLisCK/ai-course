import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import stop_reasons


class StopReasonsTests(unittest.TestCase):
    def test_no_api_key_returns_demo_output(self):
        os.environ.pop("ANTHROPIC_API_KEY", None)
        result = stop_reasons.build_output()
        self.assertIn("demo", result.lower())
        self.assertIn("Kim jesteś", result)


if __name__ == "__main__":
    unittest.main()
