"""
pip install asyncio aiohttp
pip install --upgrade certifi



"""
from typing import Iterable
from itertools import islice
import asyncio
import json
import os
import pickle
import time

import aiohttp
from aiohttp import ClientTimeout

from concurrent.futures import ThreadPoolExecutor

import asyncio
import ssl
import sys

import ssl

ssl_context = ssl._create_unverified_context()
ssl_context.set_ciphers('DEFAULT@SECLEVEL=1')


SSL_PROTOCOLS = (asyncio.sslproto.SSLProtocol,)
try:
    import uvloop.loop
except ImportError:
    pass
else:
    SSL_PROTOCOLS = (*SSL_PROTOCOLS, uvloop.loop.SSLProtocol)


def get_domains(limit=None, checked= {}):
    with open(path, "r") as f:
        ss_domains = json.load(f)
    if limit:
        domains = ss_domains["false"][:limit]
    else:
        domains = ss_domains["false"]
    return ["http://" + d for d in domains if "http://" + d  not in checked]


async def download_site(session, ssl_context, url):
    async with session.get(
        url, timeout=ClientTimeout(total=None, sock_connect=5, sock_read=5), ssl=ssl_context
    ) as response:
        code = response.status
    return url, code


async def download_all_sites(sites, ssl_context):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.create_task(download_site(session, ssl_context, url))
            tasks.append(task)
        responses = await asyncio.gather(*tasks, return_exceptions=True)
    return responses


def batch(dataset: Iterable, batch_size: int) -> Iterable:
    """Creates batches from an iterable.

    Args:
        dataset (Iterable): Your dataset you want to batch given as an iterable (e.g. a list).
        batch_size (int): Your desired batch size

    Returns:
        Iterable: An iterable of tuples of size equal to batch_size.

    Example:
        >>> batches = batch([1,2, 3, 4, 5], 2)
        >>> print(list(batches))
        [(1, 2), (3, 4), (5,)]
    """

    iterable_dataset = iter(dataset)
    while True:
        chunk = tuple(islice(iterable_dataset, batch_size))
        if not chunk:
            break
        yield chunk




def ignore_aiohttp_ssl_eror(loop):
    """Ignore aiohttp #3535 / cpython #13548 issue with SSL data after close

    There is an issue in Python 3.7 up to 3.7.3 that over-reports a
    ssl.SSLError fatal error (ssl.SSLError: [SSL: KRB5_S_INIT] application data
    after close notify (_ssl.c:2609)) after we are already done with the
    connection. See GitHub issues aio-libs/aiohttp#3535 and
    python/cpython#13548.

    Given a loop, this sets up an exception handler that ignores this specific
    exception, but passes everything else on to the previous exception handler
    this one replaces.

    Checks for fixed Python versions, disabling itself when running on 3.7.4+
    or 3.8.

    """
    if sys.version_info >= (3, 7, 4):
        return

    orig_handler = loop.get_exception_handler()

    def ignore_ssl_error(loop, context):
        if context.get("message") in {
            "SSL error in data received",
            "Fatal error on transport",
        }:
            # validate we have the right exception, transport and protocol
            exception = context.get('exception')
            protocol = context.get('protocol')
            if (
                isinstance(exception, ssl.SSLError)
                and exception.reason == 'KRB5_S_INIT'
                and isinstance(protocol, SSL_PROTOCOLS)
            ):
                if loop.get_debug():
                    asyncio.log.logger.debug('Ignoring asyncio SSL KRB5_S_INIT error')
                return
        if orig_handler is not None:
            orig_handler(loop, context)
        else:
            loop.default_exception_handler(context)
    loop.set_exception_handler(ignore_ssl_error)


if __name__ == "__main__":


    path = os.path.join(
        "/work/netarkivet-cleaned/safe_search_domains.json"
    )

    save_path = os.path.join(
        "/work/netarkivet-cleaned/safe_search_domains_safe.pkl"
    )

    DNSes = {"cleanweb": "185.228.168.10", # 185.228.169.11
                "google public DNS": "8.8.8.8",}

    for DNS in DNSes:
        print("Running DNS", DNS)
        cmd = f"""sudo sh -c 'echo \"nameserver {DNSes[DNS]}\" > /etc/resolv.conf'"""
        os.system(cmd)

        if os.path.isfile(save_path):
            with open(save_path, "rb") as f:
                output = pickle.load(f)
            checked = set(output[DNS].keys())
        else:
            output = {}
            output["cleanweb"] = {}
            output["google public DNS"] = {}
            checked = set()
        print("len checked", len(checked))


        for i, sites in enumerate(batch(get_domains(limit=None, checked =checked), 10000)):
            print(i)
            start_time = time.time()
            loop = asyncio.get_event_loop()
            ignore_aiohttp_ssl_eror(loop)
            loop.set_default_executor(ThreadPoolExecutor(100))
            t = loop.run_until_complete(download_all_sites(sites, ssl_context))

            duration = time.time() - start_time
            print(f"\tDownloaded {len(sites)} sites in {duration} seconds")

            # append to output pickle
            for d, status in zip(sites, t):
                output[DNS][d] = isinstance(status, tuple)

            # l = [d for d in output[DNS]]
            # print(sum(l))
            # print(len(l))
            with open(save_path, "wb") as f:
                pickle.dump(output, f)

    print("checking unsafe sites")
    domains = {d: (output["google public DNS"][d], c) for d, c in output["cleanweb"].items()}
    unsafe_sites = [t for t, c in domains.items() if c[0] is True and c[1] is False]
    output["unsafe_sites"] = unsafe_sites

    with open(save_path, "wb") as f:
        pickle.dump(output, f)



    cmd = f"""sudo sh -c 'echo \"nameserver {DNSes["cleanweb"]}\" > /etc/resolv.conf'"""
    os.system(cmd)

    print("doing a 10 iter check")
    output["unsafe_sites_double_checked"] = output["unsafe_sites"]
    for i in range(10):
        print(i)
        loop = asyncio.get_event_loop()
        ignore_aiohttp_ssl_eror(loop)
        loop.set_default_executor(ThreadPoolExecutor(100))
        t = loop.run_until_complete(download_all_sites(output["unsafe_sites_double_checked"], ssl_context))
        print(len(output["unsafe_sites_double_checked"]))
        print(output["unsafe_sites_double_checked"][:10])
        output["unsafe_sites_double_checked"] = [site for dom, site in zip(t, output["unsafe_sites_double_checked"]) if not isinstance(dom, tuple)]
    with open(save_path, "wb") as f:
        pickle.dump(output, f)

    print("done")
    print(output["unsafe_sites_double_checked"][:10])