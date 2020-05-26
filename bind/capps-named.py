import os
import docker

base = os.path.dirname(os.path.realpath(__file__))
gid = os.stat('tconfig').st_gid

dr_client = docker.from_env()

server = dr_client.containers.run(
    'capps-bind:test',
    volumes={f'{base}/tconfig/': {'bind': '/etc/bind', 'mode': 'rw'}},
    ports={'53/tcp': 1053, '53/udp': 1053},
    user=f'root:{gid}',
    detach=True,
    remove=True
)

print(server.id)

#server.stop()
