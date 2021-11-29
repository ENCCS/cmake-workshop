from ._pyaccount import ffi, lib

# we change names to obtain a more pythonic API
new = lib.account_new
free = lib.account_free
deposit = lib.account_deposit
withdraw = lib.account_withdraw
get_balance = lib.account_get_balance

__version__ = "0.0"

__all__ = [
    "__version__",
    "new",
    "free",
    "deposit",
    "withdraw",
    "get_balance",
]
