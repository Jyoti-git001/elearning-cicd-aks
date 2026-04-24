import requests
import sys
import argparse

ENDPOINTS = {
    "staging":    "http://staging.elearning.example.com",
    "production": "http://elearning.example.com",
}

def run_smoke_tests(env):
    base_url = ENDPOINTS.get(env)
    if not base_url:
        print(f"Unknown environment: {env}")
        sys.exit(1)

    tests = [
        ("Health check - frontend", f"{base_url}/health"),
        ("Home page",               f"{base_url}/"),
        ("Courses endpoint",        f"{base_url}/courses"),
    ]

    failed = 0
    for name, url in tests:
        try:
            resp = requests.get(url, timeout=10)
            status = "PASS" if resp.status_code == 200 else "FAIL"
            if resp.status_code != 200:
                failed += 1
            print(f"[{status}] {name} — HTTP {resp.status_code}")
        except Exception as e:
            print(f"[FAIL] {name} — {e}")
            failed += 1

    print(f"\n{len(tests) - failed}/{len(tests)} tests passed.")
    if failed > 0:
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", default="staging")
    args = parser.parse_args()
    run_smoke_tests(args.env)
