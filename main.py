import asyncio
import websockets
import base64
import time

from camera_pi import Camera

from config import ws_algorithm_server_url


def main():
    camera = Camera()
    while True:
        try:
            asyncio.get_event_loop().run_until_complete(get_and_send_img(camera))
        except Exception as e:
            print(e)
        time.sleep(20)


async def get_and_send_img(camera: Camera):
    async with websockets.connect(ws_algorithm_server_url) as websocket:
        img_bytes = camera.get_frame()
        img_str = img_bytes

        await websocket.send(img_str)


if __name__ == '__main__':
    main()