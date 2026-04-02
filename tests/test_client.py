import textwrap

from gui_executor.client import MyClient
from gui_executor.kernel import MyKernel


def test_kernel_info():
    kernel = MyKernel()
    client = MyClient(kernel)
    with client:
        client.wait_for_ready()
        info = client.get_kernel_info()
        print(info)
        protocol_version = info["protocol_version"]
        major, minor, *_ = (int(part) for part in protocol_version.split("."))
        assert major == 5
        assert minor >= 3


def test_run_snippet_long_running_waits_for_reply_and_keeps_client_usable():
    kernel = MyKernel()
    # Keep timeouts short so this test exercises repeated queue.Empty polling.
    client = MyClient(kernel, timeout=0.1)

    long_snippet = textwrap.dedent(
        """
        import time
        print("start")
        time.sleep(2.0)
        print("done")
        """
    )

    with client:
        out = client.run_snippet(long_snippet)
        assert "start" in out
        assert "done" in out

        # The client should still be synchronized for the next execution.
        assert client.run_snippet("1 + 1") == "2"
