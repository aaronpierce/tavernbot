import sys

def is_linux():
	return True if sys.platform == 'linux' else False

def dotenv_path():
	if is_linux():
		return b'\\root\\docker-pyhton\\tavernbot\\.env'
	else:
		return '.env'