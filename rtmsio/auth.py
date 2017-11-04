import hashlib
from typing import Dict


def sign(params: Dict[str, str], secret: str) -> str:
    """Compute signature

    See https://www.rememberthemilk.com/services/api/authentication.rtm

    Parameters
    ----------
    params : Dict
        Arguments that will be passed the network call

    secret : str
        Your secret

    Returns
    -------
    sig : str
        Computed signature as required by RTM
    """

    p = secret + ''.join(f'{k}{v}' for k, v in sorted(params.items()))
    return hashlib.md5(p.encode('utf-8')).hexdigest()
