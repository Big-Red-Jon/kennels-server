from http.server import BaseHTTPRequestHandler, HTTPServer
from units.request import get_all_units, get_single_unit
from factions import get_all_factions, get_single_faction
from unitType import get_all_unitTypes, get_single_unitType
from defense_dice import get_all_defense_dice, get_single_defense_dice
from lists import get_all_lists, get_single_list, create_list, delete_list
from keywords import get_all_keywords, get_single_keyword
import json


class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]
        id = None
        try:
            id = int(path_params[2])
        except IndexError:
            pass
        except ValueError:
            pass

        return (resource, id)

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        self._set_headers(200)
        response = {}

        (resource, id) = self.parse_url(self.path)

        if resource == "lists":
            if id is not None:
                response = f"{get_single_list(id)}"

            else:
                response = f"{get_all_lists()}"

        if resource == "units":
            if id is not None:
                response = f"{get_single_unit(id)}"

            else:
                response = f"{get_all_units()}"

        if resource == "factions":
            if id is not None:
                response = f"{get_single_faction(id)}"
            else:
                response = f"{get_all_factions()}"

        if resource == "unitTypes":
            if id is not None:
                response = f"{get_single_unitType(id)}"
            else:
                response = f"{get_all_unitTypes()}"

        if resource == "defense_dice":
            if id is not None:
                response = f"{get_single_defense_dice(id)}"
            else:
                response = f"{get_all_defense_dice()}"

        if resource == "keywords":
            if id is not None:
                response = f"{get_single_keyword(id)}"
            else:
                response = f"{get_all_keywords()}"

        self.wfile.write(f"{response}".encode())

    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)

        new_list = None

        if resource == "lists":
            new_list = create_list(post_body)

        self.wfile.write(f"{new_list}".encode())

    def do_PUT(self):
        self.do_POST()

    def do_DELETE(self):
        self._set_headers(204)
        (resource, id) = self.parse_url(self.path)
        if resource == "lists":
            delete_list(id)

        self.wfile.write("".encode())


def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
