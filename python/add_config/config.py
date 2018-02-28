import configparser


def read_config():
    # cp = configparser.SafeConfigParser()
    cp = configparser.RawConfigParser()
    print('cp_no_read', cp)
    cp.read("test.conf")
    print('cp_read', cp)
    sections = cp.sections()
    print('sections', sections)
    res_bitbucket_org = cp.options('bitbucket.org')
    print('res_bitbucket_org', res_bitbucket_org)
    print(type(res_bitbucket_org))

    print(cp['bitbucket.org']['User'])

    print(cp['topsecret.server.com'])

    m = cp['DEFAULT']
    print(m['CompressionLevel'])
    print(float(m['CompressionLevel']))  # convert the type of origin data

    #  you can use a section’s get() method to provide fallback values
    print('number', m.get('CompressionLevel'))

    print(cp.get('topsecret.server.com', 'Port'))


def write_config():
    cf = configparser.ConfigParser()
    cf['db'] = {
        'host': '10.149.3.130',
        'port': '3306',
        'user': 'root',
        'passwd': 'root',
    }
    cf['ftp'] = {}
    cf['ssh'] = {
        'host': '',
        'port': '22',
        'time': '3600',
        'write': 'yes',
    }

    with open('exp.cfg', 'w') as configfile:
        cf.write(configfile)





if __name__ == '__main__':
    # read_config()
    write_config()