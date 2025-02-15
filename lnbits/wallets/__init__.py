# flake8: noqa

from .cliche import ClicheWallet
from .cln import CoreLightningWallet  # legacy .env support
from .cln import CoreLightningWallet as CLightningWallet
from .eclair import EclairWallet
from .fake import FakeWallet
from .lnbits import LNbitsWallet
from .lndgrpc import LndWallet
from .lndrest import LndRestWallet
from .lnpay import LNPayWallet
from .lntxbot import LntxbotWallet
from .opennode import OpenNodeWallet
from .spark import SparkWallet
from .void import VoidWallet
