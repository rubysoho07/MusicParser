import unittest
import json

from MusicParser.parser import MusicParser, AllMusicParser, BugsParser, NaverMusicParser, MelonParser


class TestMusicParser(unittest.TestCase):
    """
    Test for Music Parser.

    Example 1, 2 are for Korean music sites. (Bugs, Melon, Naver)
    Example 1: Crying Nut/No Brain - 96
    Example 2: Pink Floyd - The Wall

    Example 3, 4 are for AllMusic.
    Example 3: The Smashing Pumpkins - Mellon Collie and the Infinite Sadness
    Example 4: Various Artists - Judgment Night OST
    """
    bugs_example_1 = "http://music.bugs.co.kr/album/450734"
    bugs_example_2 = "https://music.bugs.co.kr/album/8000460"
    melon_example_1 = "http://www.melon.com/album/detail.htm?albumId=2281828"
    melon_example_2 = "http://www.melon.com/album/detail.htm?albumId=2661487"
    naver_music_example_1 = "http://music.naver.com/album/index.nhn?albumId=451880"
    naver_music_example_2 = "http://music.naver.com/album/index.nhn?albumId=12873"
    all_music_example_3 = "http://www.allmusic.com/album/mellon-collie-and-the-infinite-sadness-mw0000645152"
    all_music_example_4 = "http://www.allmusic.com/album/judgment-night-mw0000101514"

    bugs_parser = None
    naver_music_parser = None
    melon_parser = None
    all_music_parser = None

    @classmethod
    def setUpClass(cls):
        """Configuration before test."""
        cls.bugs_parser = BugsParser()
        cls.naver_music_parser = NaverMusicParser()
        cls.melon_parser = MelonParser()
        cls.all_music_parser = AllMusicParser()

    def test_check_input(self):
        """Check input URL is valid and return correct URL and parser object to parse."""
        bugs_result, self.bugs_parser = MusicParser.check_input(self.bugs_example_1)
        self.assertEqual(bugs_result, self.bugs_example_1)
        self.assertNotEqual(self.bugs_parser, None)

        melon_result, self.melon_parser = MusicParser.check_input(self.melon_example_1)
        self.assertEqual(melon_result, self.melon_example_1)
        self.assertNotEqual(self.melon_parser, None)

        naver_music_result, self.naver_music_parser = MusicParser.check_input(self.naver_music_example_1)
        self.assertEqual(naver_music_result, self.naver_music_example_1)
        self.assertNotEqual(self.naver_music_parser, None)

        all_music_result, self.all_music_parser = MusicParser.check_input(self.all_music_example_3)
        self.assertEqual(all_music_result, self.all_music_example_3)
        self.assertNotEqual(self.all_music_parser, None)

    def test_to_dict_from_base_parser(self):
        parser = MusicParser()

        parse_result = parser.to_dict(self.bugs_example_1)

        self.assertEqual(parse_result['artist'], "크라잉넛(Crying Nut), 노브레인(No Brain)")
        self.assertEqual(parse_result['album_title'], "96")

    def test_to_json_from_base_parser(self):
        parser = MusicParser()

        parse_result = parser.to_json(self.bugs_example_1)

        dict_result = json.loads(parse_result)

        self.assertEqual(dict_result['artist'], "크라잉넛(Crying Nut), 노브레인(No Brain)")
        self.assertEqual(dict_result['album_title'], "96")

    def test_check_album_cover_pattern(self):
        """Check album cover patterns from music information sites."""
        naver_pattern = "http://musicmeta.phinf.naver.net/album/000/645/645112.jpg?type=r204Fll&v=20160623150347"
        melon_pattern = "http://cdnimg.melon.co.kr/cm/album/images/006/23/653/623653.jpg"
        bugs_pattern = "https://image.bugsm.co.kr/album/images/200/5712/571231.jpg"
        all_music_pattern = "https://cps-static.rovicorp.com/3/JPG_500/MI0002/416/MI0002416076.jpg?partner=allrovi.com"

        naver_result = MusicParser._check_album_cover_pattern(naver_pattern)
        self.assertEqual(naver_result, True)

        melon_result = MusicParser._check_album_cover_pattern(melon_pattern)
        self.assertEqual(melon_result, True)

        bugs_result = MusicParser._check_album_cover_pattern(bugs_pattern)
        self.assertEqual(bugs_result, True)

        all_music_result = MusicParser._check_album_cover_pattern(all_music_pattern)
        self.assertEqual(all_music_result, True)

        error_result = MusicParser._check_album_cover_pattern("http://music.bugs.co.kr/album/450734")
        self.assertEqual(error_result, False)

    def test_naver_parser_to_dict(self):
        """ Test to parse album information from Naver Music as a dict. """
        result1 = self.naver_music_parser.to_dict(self.naver_music_example_1)
        self.assertEqual(result1['artist'], "크라잉넛(CRYING NUT), 노브레인")
        self.assertEqual(result1['album_title'], "96")

        result2 = self.naver_music_parser.to_dict(self.naver_music_example_2)
        self.assertEqual(result2['artist'], "Pink Floyd")
        self.assertIn("The Wall", result2['album_title'])

    def test_naver_parser_to_json(self):
        """ Test to parse album information from Naver Music as a JSON string. """
        json1 = self.naver_music_parser.to_json(self.naver_music_example_1)

        result1 = json.loads(json1, encoding='utf-8')
        self.assertEqual(result1['artist'], "크라잉넛(CRYING NUT), 노브레인")
        self.assertEqual(result1['album_title'], "96")

        json2 = self.naver_music_parser.to_json(self.naver_music_example_2)

        result2 = json.loads(json2, encoding='utf-8')
        self.assertEqual(result2['artist'], "Pink Floyd")
        self.assertIn("The Wall", result2['album_title'])

    def test_melon_parser_to_dict(self):
        """ Test to parse album information from Melon as a dict. """
        result1 = self.melon_parser.to_dict(self.melon_example_1)
        self.assertEqual(result1['artist'], "크라잉넛 (CRYING NUT), 노브레인")
        self.assertEqual(result1['album_title'], "96")

        result2 = self.melon_parser.to_dict(self.melon_example_2)
        self.assertEqual(result2['artist'], "Pink Floyd")
        self.assertIn("The Wall", result2['album_title'])

    def test_melon_parser_to_json(self):
        """ Test to parse album information from Melon as a JSON string. """
        json1 = self.melon_parser.to_json(self.melon_example_1)
        result1 = json.loads(json1, encoding='utf-8')
        self.assertEqual(result1['artist'], "크라잉넛 (CRYING NUT), 노브레인")
        self.assertEqual(result1['album_title'], "96")

        json2 = self.melon_parser.to_json(self.melon_example_2)
        result2 = json.loads(json2, encoding='utf-8')
        self.assertEqual(result2['artist'], "Pink Floyd")
        self.assertIn("The Wall", result2['album_title'])

    def test_bugs_parser_to_dict(self):
        """ Test to parse album information from Bugs as a dict. """
        result1 = self.bugs_parser.to_dict(self.bugs_example_1)
        self.assertEqual(result1['artist'], "크라잉넛(Crying Nut), 노브레인(No Brain)")
        self.assertEqual(result1['album_title'], "96")

        result2 = self.bugs_parser.to_dict(self.bugs_example_2)
        self.assertEqual(result2['artist'], "Pink Floyd(핑크 플로이드)")
        self.assertIn("The Wall", result2['album_title'])

    def test_bugs_parser_to_json(self):
        """ Test to parse album information from Bugs as a JSON string. """
        json1 = self.bugs_parser.to_json(self.bugs_example_1)
        result1 = json.loads(json1, encoding='utf-8')
        self.assertEqual(result1['artist'], "크라잉넛(Crying Nut), 노브레인(No Brain)")
        self.assertEqual(result1['album_title'], "96")

        json2 = self.bugs_parser.to_json(self.bugs_example_2)
        result2 = json.loads(json2, encoding='utf-8')
        self.assertEqual(result2['artist'], "Pink Floyd(핑크 플로이드)")
        self.assertIn("The Wall", result2['album_title'])

    def test_allmusic_parser_to_dict(self):
        """ Test to parse album information from AllMusic as a dict. """
        result3 = self.all_music_parser.to_dict(self.all_music_example_3)
        self.assertEqual(result3['artist'], "The Smashing Pumpkins")
        self.assertEqual(result3['album_title'], "Mellon Collie and the Infinite Sadness")

        result4 = self.all_music_parser.to_dict(self.all_music_example_4)
        self.assertEqual(result4['artist'], "Original Soundtrack")
        self.assertEqual(result4['album_title'], "Judgment Night")

    def test_allmusic_parser_to_json(self):
        """ Test to parse album information from AllMusic as a JSON string. """
        json3 = self.all_music_parser.to_json(self.all_music_example_3)
        result3 = json.loads(json3, encoding='utf-8')
        self.assertEqual(result3['artist'], "The Smashing Pumpkins")
        self.assertEqual(result3['album_title'], "Mellon Collie and the Infinite Sadness")

        json4 = self.all_music_parser.to_json(self.all_music_example_4)
        result4 = json.loads(json4, encoding='utf-8')
        self.assertEqual(result4['artist'], "Original Soundtrack")
        self.assertEqual(result4['album_title'], "Judgment Night")
