import matplotlib.pyplot as plt
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from urllib.parse import urlparse


class Server(BaseHTTPRequestHandler):
    def do_GET(self):               # dyskusja klient-serwer metodą GET - co mu odpowiadamy/wysyłamy
        self.send_response(200)     #kod oznaczający 'jest OK'
        self.send_header('content-type', 'image/html') #co będziemy wysyłać
        self.end_headers()
        query = urlparse(self.path).query #bierzemy to co jest po katalogach, szczegoly zapytania
        qc = dict(q.split("=") for q in query.split("&")) #tworzy słownik rozbijając zapytanie
        print(len(qc))
        if len(qc) > 0:
            tri = Triangle(float(qc['a']), float(qc['t']), float(qc['fi']))
            tri.create_traj()

        print(qc)
        dane = '<img src=../pliki_pyri.jpg>'


        self.wfile.write(bytes(dane, "utf8"))  # wyślij do przeglądarki tekst, jako bajty, kodowanie utf-8
        return qc


class Triangle:

    def __init__(self, a, t, fi):
        plt.axis([0, 8, -a, a])
        self.a = a
        self.t = t
        self.fi = fi
        self.trajectory = []

    def create_traj(self):
        xes = []
        yes = []

        xes.append(self.fi)
        yes.append(self.a)
        for i in range(int(16/self.t + 1)):
            yes.append(yes[i] * -1)
            xes.append(xes[i] + self.t/2)

        xes.insert(0, (xes[0] - self.t/2))
        yes.insert(0, (yes[0] * -1))
        plt.plot(xes, yes)
        plt.show()
        plt.savefig('plik.jpg')




def run_server():
    server_addres = ('127.0.0.1', 80)
    httpd = HTTPServer(server_addres, Server)
    print('Server is working')
    httpd.serve_forever()
    #httpd.timeout = 30
    #httpd.handle_timeout()


run_server()
