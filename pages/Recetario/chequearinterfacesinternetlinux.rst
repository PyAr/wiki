
Si te esta pasa que necesitas saber porque placa de red tenes internet en Gnu/Linux con Python ? bueno, por ahi esto te sirve 🙂

::

    import socket

    DEBUG = True

    def list_net_devices():
        '''
        Lista todas las placas de red.
            Retorna:
                Lista con diccionarios, cada diccionario de la lista tiene
                como key el nombre de la iface asignada y los valores del 
                diccionario son los datos correspondiente a la interfaz de red
        '''
        fh = open('/proc/net/dev', 'r')
        lines = fh.readlines()
        fh.close()

        ifaces = []
        for line in lines:
            if ':' in line:
                iface_name, iface_data = line.split(':')
                new_iface = {}
                # limpiamos iface_data ...
                data = []
                for item in iface_data.strip().split(' '):
                    if item != '':
                        data.append(item)
                new_iface[iface_name.strip()] = data
                ifaces.append(new_iface)

        return ifaces

    def info_net_device(device):
        '''
        Devuelve informacion de un dispositivo de red en particular
            Argumentos:
                device(str)
            Retorna:
                Diccionario siendo la clave el device solicitado y
                los datos como values.
                None en caso de no encontrarse el dispositivo de red.
            Funciones:
                list_net_devices
        '''
        if not isinstance(device, str):
            raise Exception, 'el device debe ser un string, obtuve %s' % repr(device)

        devices = list_net_devices()
        info_iface = {}
        for iface in devices:
            kw = iface.keys().pop()
            if kw == device:
                info_iface[kw] = iface[kw]
                return info_iface
        return None

    def route_net_devices():
        '''
        Devuelve las rutas asignadas a los dispositivos de red
            Retorna:
                Diccionario siendo la clave el dispositivo de red y su
                value la ip de la ruta por defecto como string.
        '''
        fh = open('/proc/net/route', 'r')
        lines = fh.readlines()
        fh.close()
        devices = {}

        for line in lines:
            if line.split('\t')[0] != 'Iface':
                iface = line.split('\t')[0]
                hexgw = line.split('\t')[2]
                gw = '%s.%s.%s.%s' % (int(hexgw[6:8], 16),
                                      int(hexgw[4:6], 16),
                                      int(hexgw[2:4], 16),
                                      int(hexgw[:2], 16),
                                      )
                devices[iface] = gw
        return devices

    def ip_port_open(ip,port):
        '''
        Chequea si un puerto en una ip dada se encuentra abierto o no.
            Argumentos:
                ip(str)
                port(int)
            Retorna:
                True(bool), si el puerto en la ip dada esta abierto
                False(bool), si el puerto en la ip dada no esta abierto
        '''
        if not isinstance(ip, str):
            raise Exception, 'la ip debe ser un string, obtuve %s' % repr(ip)
        if not isinstance(port, int):
            raise Exception, 'el puerto debe ser un int, obtuve %s' % repr(port)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, int(port)))
            s.shutdown(2)
            return True
        except:
            return False

    def host_port_open(hostname, port):
        '''
        Chequea si un puerto en un host dado se encuentra abierto o no.
            Argumentos:
                hostname(str)
                port(int)
            Retorna:
                True(bool), si el puerto en el hostname dado esta abierto
                False(bool), si el puerto en el hostname dado no esta abierto
            Funciones:
                ip_port_open
        '''
        if not isinstance(hostname, str):
            raise Exception, 'el hostname debe ser un string, obtuve %s' % repr(hostname)
        if not isinstance(port, int):
            raise Exception, 'el puerto debe ser un int, obtuve %s' % repr(port)

        ip = socket.gethostbyname(hostname)
        return ip_port_open(ip, port)

    def dns_working(domain):
        '''
        Chequea si podemos resolver un dominio, por lo tanto, si funcionan los DNS
        Argumentos:
            domain(str)
        Retorna:
            True(bool) en caso de poder resolver el dominio
            False(bool) en caso de no poder resolver el dominio
        '''
        if not isinstance(domain, str):
            raise Exception, 'el domain debe ser un string'

        try:
            socket.gethostbyname(domain)
            return True
        except Exception:
            return False

    def gateway_recheable(dest_addr=None, inet=None):
        '''
        Chequea si tenemos conexion contra el gateway pasado como parametro.
        Si el gateway bloquea los paquetes icmp, este metodo no funciona.
            Argumentos:
                gateway(str)
            Retorna:
                True(bool) si el gateway es recheable
                False(bool) si el gateways no es recheable
        '''

        if not isinstance(dest_addr, str):
            raise Exception, 'gateway debe ser una ip como string'

        def create_sockets(ttl):
            """
            Sockets necesarios para el traceroute, enviamos por udp y
            recibimos por icmp. Al usar icmp, precisamos permisos de super
            administrador.
                Argumentos:
                    ttl(int) TimeToLive, campo que se setea en el paquete
                    y cual se decrementa en 1 a medida que pasa por cada
                    host / router
                Retorna:
                    recv_socket, socket icmp en el que se escuchan datos
                    send_socket, socket udp por el cual se envian datos
                Funciones:
                    dns_working
            """
            icmp = socket.getprotobyname('icmp')
            udp = socket.getprotobyname('udp')
            timeout = 2

            recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
            recv_socket.settimeout(timeout)
            send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
            send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
            return recv_socket, send_socket

        ttl = 1
        port = 33434
        recheable = False
        remote_host = 'google.com'    # host usado para comprobar internet

        try:
            if dest_addr is not None:
                recv_socket, send_socket = create_sockets(ttl)
                recv_socket.bind(("", port))
                send_socket.sendto("", (dest_addr, port))
                _, curr_addr = recv_socket.recvfrom(512)
                curr_addr = curr_addr[0]
                send_socket.close()
                recv_socket.close()
                if curr_addr == dest_addr:
                    recheable = True

            if inet is True:
                max_hops = 30
                max_hops_failures = 20
                failures = 0
                accerted_hops = 0

                if not dns_working(remote_host):
                    return False
                dest_addr = socket.gethostbyname(remote_host)

                while True:
                    recv_socket, send_socket = create_sockets(ttl)
                    recv_socket.bind(("", port))
                    send_socket.sendto("", (remote_host, port))
                    try:
                        _, curr_addr = recv_socket.recvfrom(512)
                        curr_addr = curr_addr[0]
                        if curr_addr is not None:
                            accerted_hops += 1
                            if curr_addr == dest_addr:
                                recheable = True
                                send_socket.close()
                                recv_socket.close()
                                break
                        else:
                            failures += 1

                    except Exception, ex:
                        failures += 1

                    if DEBUG:
                        print 'ttl: %s chost: %s rhost: %s failures: %s accerts: %s' % (ttl,
                                                                                        curr_addr,
                                                                                        dest_addr,
                                                                                        failures,
                                                                                        accerted_hops)

                    ttl += 1
                    send_socket.close()
                    recv_socket.close()

                    if failures >= max_hops_failures:
                        recheable = False
                        break

        except Exception, ex:
            recheable = False

        return recheable


Ejemplitos de como se usa:

::

    In [8]: # chequeamos conexion contra la db

    In [9]: host_port_open('gondor.airtrack.ovz', 3306)
    Out[9]: True

    In [10]: # http de googl ...

    In [11]: host_port_open('www.google.com', 80)
    Out[11]: True

    In [12]: host_port_open('www.google.com', 81)
    Out[12]: False

    In [15]: # pedimos el gateway de la eth1 ...

    In [16]: route_net_devices()
    Out[16]: {'eth1': '192.168.1.1', 'eth2': '0.0.0.0', 'lo': '0.0.0.0'}

    In [17]: # aha ... ahora veamos si tenemos conexion contra ese gw ...

    In [18]: gateway_recheable(route_net_devices()['eth1'])
    Out[18]: True

    In [19]: # y nos da internet ese gw ? ...

    In [20]: gateway_recheable(route_net_devices()['eth1'], inet=True)
    ttl: 1 chost: 192.168.1.1 rhost: 209.85.195.104 failures: 0 accerts: 1
    ttl: 2 chost: 192.168.1.1 rhost: 209.85.195.104 failures: 1 accerts: 1
    ttl: 3 chost: 192.168.1.1 rhost: 209.85.195.104 failures: 2 accerts: 1
    ttl: 4 chost: 192.168.1.1 rhost: 209.85.195.104 failures: 3 accerts: 1
    ttl: 5 chost: 192.168.1.1 rhost: 209.85.195.104 failures: 4 accerts: 1
    ttl: 6 chost: 200.89.165.213 rhost: 209.85.195.104 failures: 4 accerts: 2
    ttl: 7 chost: 200.89.165.194 rhost: 209.85.195.104 failures: 4 accerts: 3
    ttl: 8 chost: 200.89.165.194 rhost: 209.85.195.104 failures: 5 accerts: 3
    ttl: 9 chost: 200.89.165.194 rhost: 209.85.195.104 failures: 6 accerts: 3
    ttl: 10 chost: 200.49.159.254 rhost: 209.85.195.104 failures: 6 accerts: 4
    ttl: 11 chost: 209.85.251.28 rhost: 209.85.195.104 failures: 6 accerts: 5
    ttl: 12 chost: 209.85.251.6 rhost: 209.85.195.104 failures: 6 accerts: 6
    Out[20]: True


-------------------------



  CategoryRecetas_

.. _categoryrecetas: /pages/categoryrecetas.html
