import httpx


def send(phone):
    resp = httpx.post('192.', data={'phone': phone})
    print(resp.status_code)
