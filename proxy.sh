set -e

python3 "${PWD%/}/change_IP.py" & python3 "${PWD%/}/send_request.py"