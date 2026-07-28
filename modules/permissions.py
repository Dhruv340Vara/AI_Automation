import os
import stat

def get_permissions(path):
    try:
        mode=os.stat(path).st_mode
        return {
            "success":True,
            "permissions":oct(stat.S_IMODE(mode))
        }
    except Exception as e:
        return {
            "success":False,
            "error":str(e)
        }

def set_permissions(path,permission):
    try:
        os.chmod(path,int(permission,8))
        return {
            "success":True,
            "permissions":permission
        }
    except Exception as e:
        return {
            "success":False,
            "error":str(e)
        }
