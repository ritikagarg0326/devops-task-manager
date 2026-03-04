import random
import os
import subprocess
import re

def break_nginx_backend():
    path = "nginx/default.conf"
    with open(path, "r") as f:
        content = f.read()
    content = content.replace("auth-service", "wrong-service")
    with open(path, "w") as f:
        f.write(content)

def break_auth_port():
    path = "auth-service/app.py"
    with open(path, "r") as f:
        content = f.read()
    content = re.sub(r"port=PORT", "port=9999", content)
    with open(path, "w") as f:
        f.write(content)

def break_mongo_connection():
    path = ".env"
    with open(path, "r") as f:
        content = f.read()
    content = content.replace("mongo", "badmongo")
    with open(path, "w") as f:
        f.write(content)

def break_requirements_build():
    path = "auth-service/requirements.txt"
    with open(path, "a") as f:
        f.write("\nthispackagedoesnotexist123\n")

def delete_profile_route():
    path = "auth-service/app.py"
    with open(path, "r") as f:
        lines = f.readlines()
    lines = [line for line in lines if "/profile" not in line]
    with open(path, "w") as f:
        f.writelines(lines)

def corrupt_nginx_config():
    path = "nginx/default.conf"
    with open(path, "a") as f:
        f.write("\ninvalid_directive_here;\n")

failures = [
    break_nginx_backend,
    break_auth_port,
    break_mongo_connection,
    break_requirements_build,
    delete_profile_route,
    corrupt_nginx_config,
]

random.choice(failures)()

print("🔥 Failure injected.")