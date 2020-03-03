import uuid
from hashlib import md5


def random_md5() -> str:
    """
    生成UUID并区哈希 -> 生成随机哈希
    :return: 生成的哈希
    """
    return md5(uuid.uuid4().bytes).hexdigest()

