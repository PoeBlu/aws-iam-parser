#!/usr/bin/env python3

import sys
import json

# Get these from curl -s http://169.254.169.254/latest/meta-data/iam/security-credentials/<profile_name>
iam_security_creds = json.loads(sys.stdin.read())

print(f"export AWS_ACCESS_KEY_ID={iam_security_creds['AccessKeyId']}")
print(f"export AWS_SECRET_ACCESS_KEY={iam_security_creds['SecretAccessKey']}")
print(f"export AWS_SESSION_TOKEN={iam_security_creds['Token']}")