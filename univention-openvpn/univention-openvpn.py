from univention.admin.hook import simpleHook


class univentionOpenVpn(simpleHook):

    @staticmethod
    def unmap(value, encoding=()):
        """
        >>> univentionOpenVpn.unmap([b'uid=join-backup,cn=users,dc=w2k12,dc=test:10.200.7.66', b'uid=Administrator,cn=users,dc=w2k12,dc=test:10.200.7.11'])
        [['uid=join-backup,cn=users,dc=w2k12,dc=test', '10.200.7.66'], ['uid=Administrator,cn=users,dc=w2k12,dc=test', '10.200.7.11']]
        """
        return [x.decode(*encoding).split(':', 1) for x in value]

    @staticmethod
    def map(value, encoding=()):
        """
        >>> univentionOpenVpn.map([['uid=join-backup,cn=users,dc=w2k12,dc=test', '10.200.7.66'], ['uid=Administrator,cn=users,dc=w2k12,dc=test', '10.200.7.11']])
        [b'uid=join-backup,cn=users,dc=w2k12,dc=test:10.200.7.66', b'uid=Administrator,cn=users,dc=w2k12,dc=test:10.200.7.11']
        """
        return [':'.join(x).encode(*encoding) for x in value]
