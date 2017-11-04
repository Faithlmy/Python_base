#!/usr/bin/env python
"""
1. connect server
2. output your path
3. input your path
4. create folder
5. create file
6. operation file
"""

import os
import paramiko

class Operation_file(object):

    def __init__(self, host, port, username, password):
        """
        initialize some parameters
        :param host:
        :param port:
        :param username:
        :param password:
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.ssh = None

    def get_host(self):
        try:
            ssh = paramiko.SSHClient
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            ssh.connect(
                hostname=self.host,
                port=self.port,
                username=self.username,
                password=self.password,
            )
            self.ssh = ssh
            return self.ssh
        except Exception as e:
            print("connect error: ", e)

    def create_file(self):
        """
        create  your file
        :return:
        """
        path = os.getcwd()
        return path

    def create_folder(self):
        """
        create your folder
        :return:
        """
        pass

    def close_connection(self):
        """
        close some coonection
        :return:
        """
        pass

if __name__ == "__main__":
    host = "10.132.37.126"
    port = 22
    username = "root"
    password = "nxkAdmin!"
    conn = Operation_file(
        host=host,
        port=port,
        username=username,
        password=password,
    )
    print(conn)

    # op = Operation_file()
    # path = op.create_file()
    # print(path)