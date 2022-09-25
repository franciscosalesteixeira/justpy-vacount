import argparse
from src.voiceactor import VA

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "username", help="username to use", type=str
    )
    args = parser.parse_args()
    v = VA(args.username)
    v.output()
