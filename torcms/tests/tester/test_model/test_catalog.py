# -*- coding:utf-8 -*-
from torcms.model.catalog_model import MCatalog
from torcms.model.category_model import MCategory
from torcms.model.post2catalog_model import MPost2Catalog
from torcms.model.post_model import MPost


class TestMCatalog:
    def setup_method(self):
        print('setup 方法执行于本类中每条用例之前')
        self.post_id = 'r42w2'
        self.slug = 'huohuohuo'
        self.tag_id = 'xx00'
        self.add_message()

    def add_message(self, **kwargs):
        post_data = {
            'name': kwargs.get('name', 'category'),
            'slug': kwargs.get('slug', self.slug),
            'order': kwargs.get('order', '0'),
            'kind': kwargs.get('kind1', '1'),
            'pid': kwargs.get('pid', '0000'),
        }
        tf = MCategory.add_or_update(self.tag_id, post_data)
        assert tf == self.tag_id
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
            'valid': kwargs.get('valid', 0),
        }
        post_id = kwargs.get('post_id', self.post_id)

        tt = MPost.add_or_update(post_id, p_d)
        assert tt == post_id
        MPost2Catalog.add_record(self.post_id, self.tag_id)

    def test_query_by_slug(self):
        aa = MCatalog.query_by_slug(self.slug)
        assert aa
        tf = False
        for i in aa:
            if i.uid == self.post_id:
                tf = True
        assert tf

    def test_query_all(self):
        aa = MCatalog.query_all()
        assert aa
        tf = False
        for i in aa:
            if i.slug == self.slug:
                tf = True
        assert tf

    def teardown_method(self):
        print("function teardown")
        post = MPost.get_by_uid(self.post_id)
        if post:
            MPost.delete(self.post_id)
        cate = MPost.get_by_uid(self.tag_id)
        if cate:
            MCategory.delete(self.tag_id)
        MPost2Catalog.remove_relation(self.post_id, self.tag_id)
