# -*- coding:utf-8 -*-
import unittest

from torcms.model.collect_model import MCollect
from torcms.model.post_model import MPost


class TestMCollect:
    def setup_method(self):
        print('setup 方法执行于本类中每条用例之前')
        self.user_id = 'pppp'
        self.post_id = '90953'
        self.post_id_new = '90955'
        self.add_mess()

    def add_message(self, **kwargs):
        p_d = {
            'title': kwargs.get('title', 'iiiii'),
            'cnt_md': kwargs.get('cnt_md', 'grgr'),
            'time_create': kwargs.get('time_create', '1992'),
            'time_update': kwargs.get('time_update', '1996070600'),
            'user_name': kwargs.get('user_name', 'yuanyuan'),
            'view_count': kwargs.get('view_count', 1),
            'logo': kwargs.get('logo', 'prprprprpr'),
            'memo': kwargs.get('memo', ''),
            'order': kwargs.get('order', '1'),
            'keywords': kwargs.get('keywords', ''),
            'extinfo': kwargs.get('extinfo', {}),
            'kind': kwargs.get('kind2', '1'),
            'valid': kwargs.get('valid', 1),
        }
        post_id = kwargs.get('post_id', self.post_id)

        tf = MPost.add_or_update(post_id, p_d)
        assert tf == post_id

    def test_add_or_update(self):
        user_id = self.user_id
        app_id = self.post_id
        MCollect.add_or_update(user_id, app_id)
        tt = MCollect.get_by_signature(user_id, app_id)
        assert tt
        a = MCollect.get_by_signature(user_id, app_id)

        assert a != None

    def add_mess(self):
        self.add_message()
        MCollect.add_or_update(self.user_id, self.post_id)
        tt = MCollect.get_by_signature(self.user_id, self.post_id)
        assert tt
        a = MCollect.query_pager_by_all(self.user_id)
        tf = False
        for i in a:
            if i.post_id == self.post_id:
                tf = True
        assert tf

    def test_query_recent(self):
        user_id = self.user_id
        a = MCollect.query_recent(user_id)

        assert a[0].post_id == self.post_id

    def test_get_by_signature(self):
        user_id = self.user_id

        a = MCollect.get_by_signature(user_id, self.post_id)

        assert a != None

    def test_count_of_user(self):
        user_id = self.user_id
        b = MCollect.count_of_user(user_id)

        self.add_message(post_id=self.post_id_new)
        MCollect.add_or_update(self.user_id, self.post_id_new)

        a = MCollect.count_of_user(user_id)

        assert a == b + 1

    def test_query_pager_by_all(self):
        user_id = self.user_id

        a = MCollect.query_pager_by_all(user_id)
        tf = False
        for i in a:
            if i.post_id == self.post_id:
                tf = True
        assert tf

    def test_query_pager_by_userid(self):
        user_id = self.user_id

        a = MCollect.query_pager_by_userid(user_id, '1')
        tf = False
        for i in a:
            if i.post_id == self.post_id:
                tf = True
        assert tf

    def test_remove_collect(self):
        MCollect.remove_collect(self.user_id, self.post_id)
        rec = MCollect.get_by_signature(self.user_id, self.post_id)
        assert rec == None

    def teardown_method(self):
        print("function teardown")
        tt = MPost.get_by_uid(self.post_id)
        tt1 = MPost.get_by_uid(self.post_id_new)
        if tt:
            MPost.delete(self.post_id)
        if tt1:
            MPost.delete(self.post_id_new)
