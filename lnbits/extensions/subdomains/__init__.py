import asyncio

from fastapi import APIRouter

from lnbits.db import Database
from lnbits.helpers import template_renderer
from lnbits.tasks import catch_everything_and_restart

db = Database("ext_subdomains")

subdomains_ext: APIRouter = APIRouter(prefix="/subdomains", tags=["subdomains"])


def subdomains_renderer():
    return template_renderer(["lnbits/extensions/subdomains/templates"])


from .tasks import wait_for_paid_invoices
from .views import *  # noqa
from .views_api import *  # noqa


def subdomains_start():
    loop = asyncio.get_event_loop()
    loop.create_task(catch_everything_and_restart(wait_for_paid_invoices))
