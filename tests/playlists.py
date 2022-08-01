# coding: utf-8
# Copyright 2014 Globo.com Player authors. All rights reserved.
# Use of this source code is governed by a MIT License
# license that can be found in the LICENSE file.

from os.path import dirname, abspath, join

TEST_HOST = 'http://localhost:8112'

SIMPLE_PLAYLIST = '''
#EXTM3U
#EXT-X-TARGETDURATION:5220
#EXTINF:5220,
http://media.example.com/entire.ts
#EXT-X-ENDLIST
'''

SIMPLE_PLAYLIST_WITH_ZERO_DURATION = '''
#EXTM3U
#EXT-X-TARGETDURATION:5220
#EXTINF:0,
http://media.example.com/entire1.ts
#EXTINF:5220,
http://media.example.com/entire2.ts
#EXT-X-ENDLIST
'''

SIMPLE_PLAYLIST_WITH_VERY_SHORT_DURATION = '''
#EXTM3U
#EXT-X-TARGETDURATION:5220
#EXTINF:5220,
http://media.example.com/entire1.ts
#EXTINF:5218.5,
http://media.example.com/entire2.ts
#EXTINF:0.000011,
http://media.example.com/entire3.ts
#EXT-X-ENDLIST
'''

SIMPLE_PLAYLIST_WITH_START_NEGATIVE_OFFSET = '''
#EXTM3U
#EXT-X-TARGETDURATION:5220
#EXT-X-START:TIME-OFFSET=-2.0
#EXTINF:5220,
http://media.example.com/entire.ts
#EXT-X-ENDLIST
'''

SIMPLE_PLAYLIST_WITH_START_PRECISE = '''
#EXTM3U
#EXT-X-TARGETDURATION:5220
#EXT-X-START:TIME-OFFSET=10.5,PRECISE=YES
#EXTINF:5220,
http://media.example.com/entire.ts
#EXT-X-ENDLIST
'''

SIMPLE_PLAYLIST_FILENAME = abspath(
    join(dirname(__file__), 'playlists/simple-playlist.m3u8'))

SIMPLE_PLAYLIST_URI = TEST_HOST + '/simple.m3u8'
TIMEOUT_SIMPLE_PLAYLIST_URI = TEST_HOST + '/timeout_simple.m3u8'
REDIRECT_PLAYLIST_URI = TEST_HOST + '/path/to/redirect_me'


PLAYLIST_WITH_NON_INTEGER_DURATION = '''
#EXTM3U
#EXT-X-TARGETDURATION:5220.5
#EXTINF:5220.5,
http://media.example.com/entire.ts
'''

SLIDING_WINDOW_PLAYLIST = '''
#EXTM3U
#EXT-X-TARGETDURATION:8
#EXT-X-MEDIA-SEQUENCE:2680

#EXTINF:8,
https://priv.example.com/fileSequence2680.ts
#EXTINF:8,
https://priv.example.com/fileSequence2681.ts
#EXTINF:8,
https://priv.example.com/fileSequence2682.ts
'''

PLAYLIST_WITH_ENCRYPTED_SEGMENTS = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:7794
#EXT-X-TARGETDURATION:15

#EXT-X-KEY:METHOD=AES-128,URI="https://priv.example.com/key.php?r=52"

#EXTINF:15,
http://media.example.com/fileSequence52-1.ts
#EXTINF:15,
http://media.example.com/fileSequence52-2.ts
#EXTINF:15,
http://media.example.com/fileSequence52-3.ts
'''

PLAYLIST_WITH_SESSION_ENCRYPTED_SEGMENTS = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:7794
#EXT-X-TARGETDURATION:15

#EXT-X-SESSION-KEY:METHOD=AES-128,URI="https://priv.example.com/key.php?r=52"

#EXTINF:15,
http://media.example.com/fileSequence52-1.ts
#EXTINF:15,
http://media.example.com/fileSequence52-2.ts
#EXTINF:15,
http://media.example.com/fileSequence52-3.ts
'''

VARIANT_PLAYLIST = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=1280000
http://example.com/low.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
http://example.com/mid.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=7680000
http://example.com/hi.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=65000,CODECS="mp4a.40.5,avc1.42801e"
http://example.com/audio-only.m3u8
'''

VARIANT_PLAYLIST_WITH_CC_SUBS_AND_AUDIO = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=7680000,CLOSED-CAPTIONS="cc",SUBTITLES="sub",AUDIO="aud"
http://example.com/with-cc-hi.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=65000,CLOSED-CAPTIONS="cc",SUBTITLES="sub",AUDIO="aud"
http://example.com/with-cc-low.m3u8
'''

VARIANT_PLAYLIST_WITH_NONE_CC_AND_AUDIO = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=7680000,CLOSED-CAPTIONS=NONE,SUBTITLES="sub",AUDIO="aud"
http://example.com/with-cc-hi.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=65000,CLOSED-CAPTIONS=NONE,SUBTITLES="sub",AUDIO="aud"
http://example.com/with-cc-low.m3u8
'''

VARIANT_PLAYLIST_WITH_VIDEO_CC_SUBS_AND_AUDIO = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=7680000,CLOSED-CAPTIONS="cc",SUBTITLES="sub",AUDIO="aud",VIDEO="vid"
http://example.com/with-everything-hi.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=65000,CLOSED-CAPTIONS="cc",SUBTITLES="sub",AUDIO="aud",VIDEO="vid"
http://example.com/with-everything-low.m3u8
'''

VARIANT_PLAYLIST_WITH_AVERAGE_BANDWIDTH = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1280000,AVERAGE-BANDWIDTH=1252345
http://example.com/low.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000,AVERAGE-BANDWIDTH=2466570
http://example.com/mid.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=7680000,AVERAGE-BANDWIDTH=7560423
http://example.com/hi.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=65000,AVERAGE-BANDWIDTH=63005,CODECS="mp4a.40.5,avc1.42801e"
http://example.com/audio-only.m3u8
'''

VARIANT_PLAYLIST_WITH_VIDEO_RANGE = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,VIDEO-RANGE=SDR
http://example.com/sdr.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,VIDEO-RANGE=PQ
http://example.com/hdr.m3u8
'''

VARIANT_PLAYLIST_WITH_HDCP_LEVEL = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,HDCP-LEVEL=NONE
http://example.com/none.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,HDCP-LEVEL=TYPE-0
http://example.com/type0.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,HDCP-LEVEL=TYPE-1
http://example.com/type1.m3u8
'''

VARIANT_PLAYLIST_WITH_BANDWIDTH_FLOAT = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=1280000.0
http://example.com/low.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000.4
http://example.com/mid.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=7680000.6
http://example.com/hi.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=65000,CODECS="mp4a.40.5,avc1.42801e"
http://example.com/audio-only.m3u8
'''

VARIANT_PLAYLIST_WITH_IFRAME_PLAYLISTS = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=800000,RESOLUTION=624x352,CODECS="avc1.4d001f, mp4a.40.5"
video-800k.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1200000,CODECS="avc1.4d001f, mp4a.40.5"
video-1200k.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=400000,CODECS="avc1.4d001f, mp4a.40.5"
video-400k.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=150000,CODECS="avc1.4d001f, mp4a.40.5"
video-150k.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=64000,CODECS="mp4a.40.5"
video-64k.m3u8
#EXT-X-I-FRAME-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=151288,RESOLUTION=624x352,CODECS="avc1.4d001f",URI="video-800k-iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=193350,CODECS="avc1.4d001f",URI="video-1200k-iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=83598,CODECS="avc1.4d001f",URI="video-400k-iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=38775,CODECS="avc1.4d001f",URI="video-150k-iframes.m3u8"
'''

VARIANT_PLAYLIST_WITH_ALT_IFRAME_PLAYLISTS_LAYOUT = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=800000,RESOLUTION=624x352,CODECS="avc1.4d001f, mp4a.40.5"
video-800k.m3u8
#EXT-X-I-FRAME-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=151288,RESOLUTION=624x352,CODECS="avc1.4d001f",URI="video-800k-iframes.m3u8"
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1200000,CODECS="avc1.4d001f, mp4a.40.5"
video-1200k.m3u8
#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=193350,CODECS="avc1.4d001f",URI="video-1200k-iframes.m3u8"
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=400000,CODECS="avc1.4d001f, mp4a.40.5"
video-400k.m3u8
#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=83598,CODECS="avc1.4d001f",URI="video-400k-iframes.m3u8"
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=150000,CODECS="avc1.4d001f, mp4a.40.5"
video-150k.m3u8
#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=38775,CODECS="avc1.4d001f",URI="video-150k-iframes.m3u8"
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=64000,CODECS="mp4a.40.5"
video-64k.m3u8
'''

IFRAME_PLAYLIST = '''
#EXTM3U
#EXT-X-VERSION:4
#EXT-X-TARGETDURATION:10
#EXT-X-PLAYLIST-TYPE:VOD
#EXT-X-I-FRAMES-ONLY
#EXTINF:4.12,
#EXT-X-BYTERANGE:9400@376
segment1.ts
#EXTINF:3.56,
#EXT-X-BYTERANGE:7144@47000
segment1.ts
#EXTINF:3.82,
#EXT-X-BYTERANGE:10340@1880
segment2.ts
#EXT-X-ENDLIST
'''

# reversing byterange and extinf from IFRAME.
IFRAME_PLAYLIST2 = '''
#EXTM3U
#EXT-X-VERSION:4
#EXT-X-TARGETDURATION:10
#EXT-X-PLAYLIST-TYPE:VOD
#EXT-X-I-FRAMES-ONLY
#EXT-X-BYTERANGE:9400@376
#EXTINF:4.12,
segment1.ts
#EXT-X-BYTERANGE:7144@47000
#EXTINF:3.56,
segment1.ts
#EXT-X-BYTERANGE:10340@1880
#EXTINF:3.82,
segment2.ts
#EXT-X-ENDLIST
'''

PLAYLIST_USING_BYTERANGES = '''
#EXTM3U
#EXT-X-VERSION:4
#EXT-X-TARGETDURATION:11
#EXTINF:10,
#EXT-X-BYTERANGE:76242@0
segment.ts
#EXTINF:10,
#EXT-X-BYTERANGE:83442@762421
segment.ts
#EXTINF:10,
#EXT-X-BYTERANGE:69864@834421
segment.ts
#EXT-X-ENDLIST
'''

PLAYLIST_WITH_ENCRYPTED_SEGMENTS_AND_IV = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:82400
#EXT-X-ALLOW-CACHE:NO
#EXT-X-VERSION:2
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key.bin", IV=0X10ef8f758ca555115584bb5b3c687f52
#EXT-X-TARGETDURATION:8
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXTINF:8,
../../../../hls/streamNum82402.ts
#EXTINF:8,
../../../../hls/streamNum82403.ts
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts
'''

PLAYLIST_WITH_SESSION_ENCRYPTED_SEGMENTS_AND_IV = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:82400
#EXT-X-ALLOW-CACHE:NO
#EXT-X-VERSION:2
#EXT-X-SESSION-KEY:METHOD=AES-128,URI="/hls-key/key.bin", IV=0X10ef8f758ca555115584bb5b3c687f52
#EXT-X-TARGETDURATION:8
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXTINF:8,
../../../../hls/streamNum82402.ts
#EXTINF:8,
../../../../hls/streamNum82403.ts
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts
'''

PLAYLIST_WITH_ENCRYPTED_SEGMENTS_AND_IV_SORTED = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:82400
#EXT-X-ALLOW-CACHE:NO
#EXT-X-VERSION:2
#EXT-X-TARGETDURATION:8
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key.bin", IV=0X10ef8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXTINF:8,
../../../../hls/streamNum82402.ts
#EXTINF:8,
../../../../hls/streamNum82403.ts
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts
'''

PLAYLIST_WITH_SESSION_ENCRYPTED_SEGMENTS_AND_IV_SORTED = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:82400
#EXT-X-ALLOW-CACHE:NO
#EXT-X-VERSION:2
#EXT-X-TARGETDURATION:8
#EXT-X-SESSION-KEY:METHOD=AES-128,URI="/hls-key/key.bin", IV=0X10ef8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXTINF:8,
../../../../hls/streamNum82402.ts
#EXTINF:8,
../../../../hls/streamNum82403.ts
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts
'''

PLAYLIST_WITH_ENCRYPTED_SEGMENTS_AND_IV_WITH_MULTIPLE_KEYS = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:82400
#EXT-X-ALLOW-CACHE:NO
#EXT-X-VERSION:2
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key.bin",IV=0X10ef8f758ca555115584bb5b3c687f52
#EXT-X-TARGETDURATION:8
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXTINF:8,
../../../../hls/streamNum82402.ts
#EXTINF:8,
../../../../hls/streamNum82403.ts
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key2.bin",IV=0Xcafe8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts
'''

PLAYLIST_WITH_ENCRYPTED_SEGMENTS_AND_IV_WITH_MULTIPLE_KEYS_SORTED = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:82400
#EXT-X-ALLOW-CACHE:NO
#EXT-X-VERSION:2
#EXT-X-TARGETDURATION:8
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key.bin",IV=0X10ef8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXTINF:8,
../../../../hls/streamNum82402.ts
#EXTINF:8,
../../../../hls/streamNum82403.ts
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key2.bin",IV=0Xcafe8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts
'''

PLAYLIST_WITH_MULTIPLE_KEYS_UNENCRYPTED_AND_ENCRYPTED = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:82400
#EXT-X-ALLOW-CACHE:NO
#EXT-X-VERSION:2
#EXT-X-TARGETDURATION:8
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key.bin",IV=0X10ef8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXTINF:8,
../../../../hls/streamNum82402.ts
#EXTINF:8,
../../../../hls/streamNum82403.ts
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key2.bin",IV=0Xcafe8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts
'''

PLAYLIST_WITH_MULTIPLE_KEYS_UNENCRYPTED_AND_ENCRYPTED_UPDATED = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:82400
#EXT-X-ALLOW-CACHE:NO
#EXT-X-VERSION:2
#EXT-X-TARGETDURATION:8
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key0.bin",IV=0Xcafe8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key.bin",IV=0X10ef8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXTINF:8,
../../../../hls/streamNum82402.ts
#EXTINF:8,
../../../../hls/streamNum82403.ts
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key2.bin",IV=0Xcafe8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts
'''

PLAYLIST_WITH_MULTIPLE_KEYS_UNENCRYPTED_AND_ENCRYPTED_NONE = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:82400
#EXT-X-ALLOW-CACHE:NO
#EXT-X-VERSION:2
#EXT-X-TARGETDURATION:8
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key.bin",IV=0X10ef8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXTINF:8,
../../../../hls/streamNum82402.ts
#EXTINF:8,
../../../../hls/streamNum82403.ts
#EXT-X-KEY:METHOD=NONE,URI=""
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key2.bin",IV=0Xcafe8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts

'''

PLAYLIST_WITH_MULTIPLE_KEYS_UNENCRYPTED_AND_ENCRYPTED_NONE_AND_NO_URI_ATTR = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:82400
#EXT-X-ALLOW-CACHE:NO
#EXT-X-VERSION:2
#EXT-X-TARGETDURATION:8
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key.bin",IV=0X10ef8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82400.ts
#EXTINF:8,
../../../../hls/streamNum82401.ts
#EXTINF:8,
../../../../hls/streamNum82402.ts
#EXTINF:8,
../../../../hls/streamNum82403.ts
#EXT-X-KEY:METHOD=NONE
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts
#EXT-X-KEY:METHOD=AES-128,URI="/hls-key/key2.bin",IV=0Xcafe8f758ca555115584bb5b3c687f52
#EXTINF:8,
../../../../hls/streamNum82404.ts
#EXTINF:8,
../../../../hls/streamNum82405.ts

'''

PLAYLIST_WITH_KEYFORMAT_AND_KEYFORMATVERSIONS='''#EXTM3U
#EXT-X-VERSION:5
#EXT-X-TARGETDURATION:8
#EXT-X-KEY:METHOD=SAMPLE-AES,URI="skd://someuri",KEYFORMAT="com.apple.streamingkeydelivery",KEYFORMATVERSIONS="1"
#EXTINF:8,
segment.ts
'''

SIMPLE_PLAYLIST_WITH_QUOTED_TITLE = '''
#EXTM3U
#EXT-X-TARGETDURATION:5220
#EXTINF:5220,"A sample title"
http://media.example.com/entire.ts
#EXT-X-ENDLIST
'''

SIMPLE_PLAYLIST_WITH_UNQUOTED_TITLE = '''
#EXTM3U
#EXT-X-TARGETDURATION:5220
#EXTINF:5220,A sample unquoted title
http://media.example.com/entire.ts
#EXT-X-ENDLIST
'''

SIMPLE_PLAYLIST_WITH_RESOLUTION = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=445000,RESOLUTION=512x288,CODECS="avc1.77.30, mp4a.40.5"
index_0_av.m3u8?e=b471643725c47acd
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=45000,CODECS="mp4a.40.5"
index_0_a.m3u8?e=b471643725c47acd
'''

SIMPLE_PLAYLIST_WITH_VOD_PLAYLIST_TYPE = '''
#EXTM3U
#EXT-X-PLAYLIST-TYPE:VOD
#EXTINF:180.00000,
some_video.ts
#EXT-X-ENDLIST
'''

SIMPLE_PLAYLIST_WITH_INDEPENDENT_SEGMENTS = '''
#EXTM3U
#EXT-X-INDEPENDENT-SEGMENTS
#EXTINF:180.00000,
some_video.ts
#EXT-X-ENDLIST
'''

SIMPLE_PLAYLIST_WITH_EVENT_PLAYLIST_TYPE = '''
#EXTM3U
#EXT-X-PLAYLIST-TYPE:EVENT
#EXTINF:180.00000,
some_video.ts
#EXT-X-ENDLIST
'''

SIMPLE_PLAYLIST_WITH_PROGRAM_DATE_TIME = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:50116
#EXT-X-TARGETDURATION:3
#EXT-X-PROGRAM-DATE-TIME:2014-08-13T13:36:33+00:00
#EXTINF:3,
g_50116.ts
#EXTINF:3,
g_50117.ts
#EXTINF:3,
g_50118.ts
#EXTINF:3,
g_50119.ts
#EXTINF:3,
g_50120.ts
#EXTINF:3,
g_50121.ts
#EXTINF:3,
g_50122.ts
#EXTINF:3,
g_50123.ts

'''

# The playlist fails if parsed as strict, but otherwise passes
SIMPLE_PLAYLIST_MESSY = '''
#EXTM3U
#EXT-X-TARGETDURATION:5220
#EXTINF:5220,
http://media.example.com/entire.ts
JUNK
#EXT-X-ENDLIST
'''

# The playlist fails if parsed as strict, but otherwise passes
SIMPLE_PLAYLIST_TITLE_COMMA = '''
#EXTM3U
#EXTINF:5220,Title with a comma, end
http://media.example.com/entire.ts
#EXT-X-ENDLIST
'''

# Playlist with EXTINF record not ending with comma
SIMPLE_PLAYLIST_COMMALESS_EXTINF = '''
#EXTM3U
#EXT-X-TARGETDURATION:5220
#EXTINF:5220
http://media.example.com/entire.ts
#EXT-X-ENDLIST
'''

DISCONTINUITY_PLAYLIST_WITH_PROGRAM_DATE_TIME = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:50116
#EXT-X-TARGETDURATION:3
#EXT-X-PROGRAM-DATE-TIME:2014-08-13T13:36:33.000+00:00
#EXTINF:3,
g_50116.ts
#EXTINF:3,
g_50117.ts
#EXTINF:3,
g_50118.ts
#EXTINF:3,
g_50119.ts
#EXTINF:3,
g_50120.ts
#EXT-X-DISCONTINUITY
#EXT-X-PROGRAM-DATE-TIME:2014-08-13T13:36:55.000+00:00
#EXTINF:3,
g_50121.ts
#EXTINF:3,
g_50122.ts
#EXTINF:3,
g_50123.ts

'''

PLAYLIST_WITH_PROGRAM_DATE_TIME_WITHOUT_DISCONTINUITY = '''
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:6
#EXT-X-PLAYLIST-TYPE:EVENT
#EXT-X-MEDIA-SEQUENCE:50
#EXT-X-PROGRAM-DATE-TIME:2019-06-10T00:05:00.000Z
#EXTINF:6.000,
manifest_1_50.ts?m=1559946393
#EXT-X-PROGRAM-DATE-TIME:2019-06-10T00:05:06.000Z
#EXTINF:6.000,
manifest_1_51.ts?m=1559946393
#EXT-X-PROGRAM-DATE-TIME:2019-06-10T00:05:12.000Z
#EXTINF:6.000,
manifest_1_52.ts?m=1559946393
#EXT-X-ENDLIST
'''

CUE_OUT_PLAYLIST = '''
#EXTM3U
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:143474331
#EXT-X-VERSION:3
#EXTINF:10,
#EXT-X-PROGRAM-DATE-TIME:2015-06-18T23:22:10Z
1432451707508/ts/71737/sequence143474338.ts
#EXT-X-CUE-OUT-CONT
#EXTINF:10,
#EXT-X-PROGRAM-DATE-TIME:2015-06-18T23:22:20Z
1432451707508/ts/71737/sequence143474339.ts
#EXT-X-CUE-OUT-CONT
#EXTINF:10,
#EXT-X-PROGRAM-DATE-TIME:2015-06-18T23:22:30Z
1432451707508/ts/71737/sequence143474340.ts
#EXT-OATCLS-SCTE35:/DA5AAAAAAAA/wCABQb+aDhDgAAjAhdDVUVJQAAAV3+fCAgAAAAAIxDjqDUCAAAIQ1VFSQAAAABSV+PX
#EXT-X-CUE-IN
#EXTINF:10,
#EXT-X-PROGRAM-DATE-TIME:2015-06-18T23:22:40Z
1432451707508/ts/71737/sequence143474341.ts
'''

CUE_OUT_ELEMENTAL_PLAYLIST = '''
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:47224
#EXTINF:10.000,
master2500_47224.ts
#EXTINF:10.000,
master2500_47225.ts
#EXTINF:2.040,
master2500_47226.ts
#EXT-OATCLS-SCTE35:/DAlAAAAAAAAAP/wFAUAAAABf+//wpiQkv4ARKogAAEBAQAAQ6sodg==
#EXT-X-CUE-OUT:50.000
#EXTINF:7.960,
master2500_47227.ts
#EXT-X-CUE-OUT-CONT:ElapsedTime=7.960,Duration=50,SCTE35=/DAlAAAAAAAAAP/wFAUAAAABf+//wpiQkv4ARKogAAEBAQAAQ6sodg==
#EXTINF:10.000,
master2500_47228.ts
#EXT-X-CUE-OUT-CONT:ElapsedTime=17.960,Duration=50,SCTE35=/DAlAAAAAAAAAP/wFAUAAAABf+//wpiQkv4ARKogAAEBAQAAQ6sodg==
#EXTINF:10.000,
master2500_47229.ts
#EXT-X-CUE-OUT-CONT:ElapsedTime=27.960,Duration=50,SCTE35=/DAlAAAAAAAAAP/wFAUAAAABf+//wpiQkv4ARKogAAEBAQAAQ6sodg==
#EXTINF:10.000,
master2500_47230.ts
#EXT-X-CUE-OUT-CONT:ElapsedTime=37.960,Duration=50,SCTE35=/DAlAAAAAAAAAP/wFAUAAAABf+//wpiQkv4ARKogAAEBAQAAQ6sodg==
#EXTINF:10.000,
master2500_47231.ts
#EXT-X-CUE-OUT-CONT:ElapsedTime=47.960,Duration=50,SCTE35=/DAlAAAAAAAAAP/wFAUAAAABf+//wpiQkv4ARKogAAEBAQAAQ6sodg==
#EXTINF:2.040,
master2500_47232.ts
#EXT-X-CUE-IN
#EXTINF:7.960,
master2500_47233.ts
#EXTINF:7.960,
master2500_47234.ts
'''

CUE_OUT_ENVIVIO_PLAYLIST = '''
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:11
#EXT-X-MEDIA-SEQUENCE:399703
#EXTINF:10.0000,
20160914T080055-master804-199/1703.ts
#EXTINF:10.0000,
20160914T080055-master804-199/1704.ts
#EXTINF:5.1200,
20160914T080055-master804-199/1705.ts
#EXT-X-CUE-OUT:DURATION=366,ID=16777323,CUE="/DAlAAAENOOQAP/wFAUBAABrf+//N25XDf4B9p/gAAEBAQAAxKni9A=="
#EXTINF:10.0000,
20160914T080055-master804-199/1706.ts
#EXT-X-CUE-SPAN:TIMEFROMSIGNAL=PT10S,ID=16777323
#EXTINF:10.0000,
20160914T080055-master804-199/1707.ts
#EXT-X-CUE-SPAN:TIMEFROMSIGNAL=PT20S,ID=16777323
#EXTINF:10.0000,
20160914T080055-master804-199/1708.ts
#EXT-X-CUE-SPAN:TIMEFROMSIGNAL=PT30S,ID=16777323
#EXTINF:10.0000,
20160914T080055-master804-199/1709.ts
#EXT-X-CUE-IN:ID=16777323
#EXTINF:10.0000,
20160914T080055-master804-199/1710.ts
'''

CUE_OUT_INVALID_PLAYLIST = '''#EXTM3U
#EXT-X-TARGETDURATION:6
#EXT-X-CUE-OUT:INVALID
#EXTINF:5.76, no desc
0.aac
#EXT-X-CUE-OUT-CONT
#EXTINF:5.76
1.aac
'''

CUE_OUT_NO_DURATION_PLAYLIST = '''#EXTM3U
#EXT-X-TARGETDURATION:6
#EXT-X-CUE-OUT
#EXTINF:5.76,
0.aac
#EXTINF:5.76,
1.aac
#EXT-X-CUE-IN
#EXTINF:5.76,
2.aac
'''

CUE_OUT_WITH_DURATION_PLAYLIST = '''#EXTM3U
#EXT-X-TARGETDURATION:6
#EXT-X-CUE-OUT:11.52
#EXTINF:5.76,
0.aac
#EXTINF:5.76,
1.aac
#EXT-X-CUE-IN
#EXTINF:5.76,
2.aac
'''

CUE_OUT_WITH_DURATION_KEY_PLAYLIST = '''#EXTM3U
#EXT-X-TARGETDURATION:6
#EXT-X-CUE-OUT:DURATION=11.52
#EXTINF:5.76,
0.aac
#EXTINF:5.76,
1.aac
#EXT-X-CUE-IN
#EXTINF:5.76,
2.aac
'''

MULTI_MEDIA_PLAYLIST = '''#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA:URI="chinese/ed.ttml",TYPE=SUBTITLES,GROUP-ID="subs",LANGUAGE="zho",NAME="Chinese",AUTOSELECT=YES,FORCED=NO
#EXT-X-MEDIA:URI="french/ed.ttml",TYPE=SUBTITLES,GROUP-ID="subs",LANGUAGE="fra",ASSOC-LANGUAGE="fra",NAME="French",AUTOSELECT=YES,FORCED=NO,CHARACTERISTICS="public.accessibility.transcribes-spoken-dialog,public.accessibility.describes-music-and-sound"
#EXT-X-MEDIA:TYPE=CLOSED-CAPTIONS,GROUP-ID="cc",LANGUAGE="sp",NAME="CC2",AUTOSELECT=YES,INSTREAM-ID="CC2"
#EXT-X-MEDIA:URI="en/chunklist_w370587926_b160000_ao_slen_t64RW5nbGlzaA==.m3u8",TYPE=AUDIO,GROUP-ID="aac",LANGUAGE="en",NAME="English",DEFAULT=YES,AUTOSELECT=YES
#EXT-X-MEDIA:URI="sp/chunklist_w370587926_b160000_ao_slsp_t64U3BhbmlzaA==.m3u8",TYPE=AUDIO,GROUP-ID="aac",LANGUAGE="sp",NAME="Spanish",DEFAULT=NO,AUTOSELECT=YES
#EXT-X-MEDIA:URI="com/chunklist_w370587926_b160000_ao_slen_t64Q29tbWVudGFyeSAoZW5nKQ==.m3u8",TYPE=AUDIO,GROUP-ID="aac",LANGUAGE="en",NAME="Commentary (eng)",DEFAULT=NO,AUTOSELECT=NO
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2962000,RESOLUTION=1280x720,CODECS="avc1.66.30",AUDIO="aac",SUBTITLES="subs"
1280/chunklist_w370587926_b2962000_vo_slen_t64TWFpbg==.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1427000,RESOLUTION=768x432,CODECS="avc1.66.30",AUDIO="aac",SUBTITLES="subs"
768/chunklist_w370587926_b1427000_vo_slen_t64TWFpbg==.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=688000,RESOLUTION=448x252,CODECS="avc1.66.30",AUDIO="aac",SUBTITLES="subs"
448/chunklist_w370587926_b688000_vo_slen_t64TWFpbg==.m3u8
'''

MAP_URI_PLAYLIST = '''#EXTM3U
#EXT-X-TARGETDURATION:2
#EXT-X-VERSION:7
#EXT-X-MEDIA-SEQUENCE:1
#EXT-X-PLAYLIST-TYPE:VOD
#EXT-X-INDEPENDENT-SEGMENTS
#EXT-X-MAP:URI="fileSequence0.mp4"
'''

MAP_URI_PLAYLIST_WITH_BYTERANGE = '''#EXTM3U
#EXT-X-TARGETDURATION:2
#EXT-X-VERSION:7
#EXT-X-MEDIA-SEQUENCE:1
#EXT-X-PLAYLIST-TYPE:VOD
#EXT-X-INDEPENDENT-SEGMENTS
#EXT-X-MAP:URI="main.mp4",BYTERANGE="812@0"
#EXTINF:1,
segment_link1.mp4
#EXT-X-MAP:URI="main2.mp4",BYTERANGE="912@0"
#EXTINF:1,
segment_link2.mp4
'''

MULTIPLE_MAP_URI_PLAYLIST = '''#EXTM3U
#EXT-X-TARGETDURATION:6
#EXT-X-VERSION:7
#EXT-X-MEDIA-SEQUENCE:1
#EXT-X-PLAYLIST-TYPE:VOD
#EXT-X-INDEPENDENT-SEGMENTS
#EXT-X-KEY:URI="key.bin",METHOD=AES-128
#EXT-X-MAP:URI="init1.mp4"
#EXTINF:5,
segment1.mp4
#EXTINF:5,
segment2.mp4
#EXT-X-MAP:URI="init3.mp4"
#EXTINF:5,
segment3.mp4
'''

MEDIA_WITHOUT_URI_PLAYLIST = '''#EXTM3U
#EXT-X-VERSION:4
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio-aacl-312",NAME="English",LANGUAGE="en",AUTOSELECT=YES,DEFAULT=YES,CHANNELS="2"
#EXT-X-STREAM-INF:BANDWIDTH=364000,AVERAGE-BANDWIDTH=331000,CODECS="mp4a.40.2",AUDIO="audio-aacl-312",SUBTITLES="textstream"
ch001-audio_312640_eng=312000.m3u8
'''

SIMPLE_PLAYLIST_WITH_DISCONTINUITY_SEQUENCE = '''#EXTM3U
#EXT-X-TARGETDURATION:5220
#EXT-X-DISCONTINUITY-SEQUENCE:123
#EXTINF:5220,
http://media.example.com/entire.ts
#EXT-X-ENDLIST
'''

SIMPLE_PLAYLIST_WITH_CUSTOM_TAGS = '''#EXTM3U
#EXT-X-MOVIE: million dollar baby
#EXT-X-TARGETDURATION:5220
#EXTINF:5220,
http://media.example.com/entire.ts
#EXT-X-ENDLIST
'''

IPTV_PLAYLIST_WITH_CUSTOM_TAGS = '''#EXTM3U
#EXTVLCOPT:video-filter=invert
#EXTGRP:ExtGroup1
#EXTINF:-1 timeshift="0" catchup-days="7" catchup-type="flussonic" tvg-id="channel1" group-title="Group1",Channel1
#EXTVLCOPT:param2=value2
http://str00.iptv.domain/7331/mpegts?token=longtokenhere
'''

LOW_LATENCY_DELTA_UPDATE_PLAYLIST = '''#EXTM3U
# Following the example above, this playlist is a response to: GET https://example.com/2M/waitForMSN.php?_HLS_msn=273&_HLS_part=3&_HLS_report=../1M/waitForMSN.php&_HLS_report=../4M/waitForMSN.php&_HLS_skip=YES
#EXT-X-TARGETDURATION:4
#EXT-X-VERSION:9
#EXT-X-SERVER-CONTROL:CAN-BLOCK-RELOAD=YES,PART-HOLD-BACK=1.0,CAN-SKIP-UNTIL=12.0
#EXT-X-PART-INF:PART-TARGET=0.33334
#EXT-X-MEDIA-SEQUENCE:266
#EXT-X-SKIP:SKIPPED-SEGMENTS=3
#EXTINF:4.00008,
fileSequence269.ts
#EXTINF:4.00008,
fileSequence270.ts
#EXT-X-PART:DURATION=0.33334,URI="filePart271.0.ts"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.1.ts"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.2.ts"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.3.ts"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.4.ts",INDEPENDENT=YES
#EXT-X-PART:DURATION=0.33334,URI="filePart271.5.ts"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.6.ts"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.7.ts"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.8.ts",INDEPENDENT=YES
#EXT-X-PART:DURATION=0.33334,URI="filePart271.9.ts"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.10.ts"
#EXT-X-PART:DURATION=0.33334,URI="filePart271.11.ts"
#EXTINF:4.00008,
fileSequence271.ts
#EXT-X-PROGRAM-DATE-TIME:2019-02-14T02:14:00.106Z
#EXT-X-PART:DURATION=0.33334,URI="filePart272.a.ts"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.b.ts"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.c.ts"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.d.ts"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.e.ts"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.f.ts",INDEPENDENT=YES
#EXT-X-PART:DURATION=0.33334,URI="filePart272.g.ts"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.h.ts"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.i.ts"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.j.ts"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.k.ts"
#EXT-X-PART:DURATION=0.33334,URI="filePart272.l.ts"
#EXTINF:4.00008,
fileSequence272.ts
#EXT-X-PART:DURATION=0.33334,URI="filePart273.0.ts",INDEPENDENT=YES
#EXT-X-PART:DURATION=0.33334,URI="filePart273.1.ts"
#EXT-X-PART:DURATION=0.33334,URI="filePart273.2.ts"
#EXT-X-PART:DURATION=0.33334,URI="filePart273.3.ts"
#EXT-X-PRELOAD-HINT:TYPE=PART,URI="filePart273.4.ts"

#EXT-X-RENDITION-REPORT:URI="../1M/waitForMSN.php",LAST-MSN=273,LAST-PART=3
#EXT-X-RENDITION-REPORT:URI="../4M/waitForMSN.php",LAST-MSN=273,LAST-PART=3
'''

LOW_LATENCY_WITH_PRELOAD_AND_BYTERANGES_PLAYLIST = '''
#EXTM3U
#EXTINF:4.08,
fs270.mp4
#EXT-X-PART:DURATION=1.02,URI="fs271.mp4",BYTERANGE=20000@0
#EXT-X-PART:DURATION=1.02,URI="fs271.mp4",BYTERANGE=23000@20000
#EXT-X-PART:DURATION=1.02,URI="fs271.mp4",BYTERANGE=18000@43000
#EXT-X-PRELOAD-HINT:TYPE=PART,URI="fs271.mp4",BYTERANGE-START=61000,BYTERANGE-LENGTH=20000
'''

RELATIVE_PLAYLIST_FILENAME = abspath(join(dirname(__file__), 'playlists/relative-playlist.m3u8'))

RELATIVE_PLAYLIST_URI = TEST_HOST + '/path/to/relative-playlist.m3u8'

CUE_OUT_PLAYLIST_FILENAME = abspath(join(dirname(__file__), 'playlists/cue_out.m3u8'))

CUE_OUT_PLAYLIST_URI = TEST_HOST + '/path/to/cue_out.m3u8'

VARIANT_PLAYLIST_WITH_FRAME_RATE = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1280000,FRAME-RATE=25
http://example.com/low.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000,FRAME-RATE=50
http://example.com/mid.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=7680000,FRAME-RATE=60
http://example.com/hi.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=65000,FRAME-RATE=12.5,CODECS="mp4a.40.5,avc1.42801e"
http://example.com/audio-only.m3u8
'''

VARIANT_PLAYLIST_WITH_ROUNDABLE_FRAME_RATE = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=65000,FRAME-RATE=12.54321,CODECS="mp4a.40.5,avc1.42801e"
http://example.com/audio-only.m3u8
'''

VARIANT_PLAYLIST_WITH_ROUNDED_FRAME_RATE = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=65000,FRAME-RATE=12.543,CODECS="mp4a.40.5,avc1.42801e"
http://example.com/audio-only.m3u8
'''

SESSION_DATA_PLAYLIST = '''#EXTM3U
#EXT-X-VERSION:4
#EXT-X-SESSION-DATA:DATA-ID="com.example.value",VALUE="example",LANGUAGE="en"
'''

MULTIPLE_SESSION_DATA_PLAYLIST = '''#EXTM3U
#EXT-X-VERSION:4
#EXT-X-SESSION-DATA:DATA-ID="com.example.value",VALUE="example",LANGUAGE="en"
#EXT-X-SESSION-DATA:DATA-ID="com.example.value",VALUE="example",LANGUAGE="ru"
#EXT-X-SESSION-DATA:DATA-ID="com.example.value",VALUE="example",LANGUAGE="de"
#EXT-X-SESSION-DATA:DATA-ID="com.example.title",URI="title.json"
'''

VERSION_PLAYLIST = '''#EXTM3U
#EXT-X-VERSION:4
'''

PLAYLIST_WITH_NEGATIVE_MEDIA_SEQUENCE = '''
#EXTM3U
#EXT-X-TARGETDURATION:5220
#EXT-X-MEDIA-SEQUENCE:-2680
#EXTINF:5220,
http://media.example.com/entire.ts
#EXT-X-ENDLIST
'''

DATERANGE_SIMPLE_PLAYLIST = '''
#EXTM3U
#EXT-X-PROGRAM-DATE-TIME:2016-06-13T11:15:15Z
#EXT-X-DATERANGE:ID="ad3",START-DATE="2016-06-13T11:15:00Z",DURATION=20,X-AD-URL="http://ads.example.com/beacon3",X-AD-ID="1234"
#EXTINF:10,
ad3.1.ts
#EXTINF:10,
ad3.2.ts
'''

DATERANGE_SCTE35_OUT_AND_IN_PLAYLIST = '''
#EXTM3U
# adapted from https://tools.ietf.org/html/rfc8216#section-8.10
#EXT-X-PROGRAM-DATE-TIME:2014-03-05T11:15:00Z
#EXT-X-DATERANGE:ID="splice-6FFFFFF0",START-DATE="2014-03-05T11:15:00Z",PLANNED-DURATION=59.993,SCTE35-OUT=0xFC002F0000000000FF000014056FFFFFF000E011622DCAFF000052636200000000000A0008029896F50000008700000000
#EXTINF:10,
ad3.1.ts
#EXTINF:10,
ad3.2.ts
#EXTINF:10,
ad3.3.ts
#EXTINF:10,
ad3.4.ts
#EXTINF:10,
ad3.5.ts
#EXTINF:10,
ad3.6.ts
#EXT-X-DATERANGE:ID="splice-6FFFFFF0",DURATION=59.993,SCTE35-IN=0xFC002A0000000000FF00000F056FFFFFF000401162802E6100000000000A0008029896F50000008700000000
#EXTINF:10,
prog.1.ts
'''

DATERANGE_ENDDATE_SCTECMD_PLAYLIST = '''
#EXTM3U
#EXT-X-PROGRAM-DATE-TIME:2020-03-11T10:51:00Z
#EXT-X-DATERANGE:ID="test_id",START-DATE="2020-03-11T10:51:00Z",CLASS="test_class",END-DATE="2020-03-11T10:52:00Z",DURATION=60,SCTE35-CMD=0xFCINVALIDSECTION
#EXTINF:10,
prog.1.ts
'''

DATERANGE_IN_PART_PLAYLIST = '''
#EXTM3U
#EXT-X-PROGRAM-DATE-TIME:2020-03-10T07:48:00Z
#EXT-X-PART:DURATION=1,URI="filePart271.a.ts"
#EXT-X-PART:DURATION=1,URI="filePart271.b.ts"
#EXT-X-DATERANGE:ID="test_id",START-DATE="2020-03-10T07:48:02Z",CLASS="test_class",END-ON-NEXT=YES
#EXT-X-PART:DURATION=1,URI="filePart271.c.ts"
'''

GAP_PLAYLIST = '''
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:14
#EXT-X-VERSION:7
#EXT-X-TARGETDURATION:10
#EXTINF:9.84317,
fileSequence14.ts
#EXTINF:8.75875,
#EXT-X-GAP
missing-Sequence15.ts
#EXTINF:9.88487,
#EXT-X-GAP
missing-Sequence16.ts
#EXTINF:9.09242,
fileSequence17.ts
'''

GAP_IN_PARTS_PLAYLIST = '''
#EXTM3U
#EXT-X-PART:DURATION=1,URI="filePart271.a.ts"
#EXT-X-PART:DURATION=1,URI="filePart271.b.ts",GAP=YES
#EXT-X-GAP
#EXT-X-PART:DURATION=1,URI="filePart271.c.ts"
'''

PLAYLIST_WITH_SLASH_IN_QUERY_STRING = '''
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:5
#EXT-X-MEDIA-SEQUENCE:10599
#EXT-X-PROGRAM-DATE-TIME:2020-08-05T13:51:49.000+00:00
#EXTINF:5.0000,
testvideo-1596635509-4769390994-a0e3087c.ts?hdntl=exp=1596678764~acl=/*~data=hdntl~hmac=12345&
#EXTINF:5.0000,
testvideo-1596635514-4769840994-a0e00878.ts?hdntl=exp=1596678764~acl=/*~data=hdntl~hmac=12345&
#EXTINF:5.0000,
testvideo-1596635519-4770290994-a0e5087d.ts?hdntl=exp=1596678764~acl=/*~data=hdntl~hmac=12345&
#EXTINF:5.0000,
'''

VARIANT_PLAYLIST_WITH_IFRAME_AVERAGE_BANDWIDTH = '''
#EXTM3U
#EXT-X-STREAM-INF:BANDWIDTH=800000,RESOLUTION=624x352,CODECS="avc1.4d001f, mp4a.40.5"
video-800k.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=1200000,CODECS="avc1.4d001f, mp4a.40.5"
video-1200k.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=400000,CODECS="avc1.4d001f, mp4a.40.5"
video-400k.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=150000,CODECS="avc1.4d001f, mp4a.40.5"
video-150k.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=64000,CODECS="mp4a.40.5"
video-64k.m3u8
#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=151288,RESOLUTION=624x352,CODECS="avc1.4d001f",URI="video-800k-iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=193350,AVERAGE_BANDWIDTH=155000,CODECS="avc1.4d001f",URI="video-1200k-iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=83598,AVERAGE_BANDWIDTH=65000,CODECS="avc1.4d001f",URI="video-400k-iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=38775,AVERAGE_BANDWIDTH=30000,CODECS="avc1.4d001f",URI="video-150k-iframes.m3u8"
'''

VARIANT_PLAYLIST_WITH_IFRAME_VIDEO_RANGE = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,VIDEO-RANGE=SDR
http://example.com/sdr.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,VIDEO-RANGE=PQ
http://example.com/hdr-pq.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,VIDEO-RANGE=HLG
http://example.com/hdr-hlg.m3u8
#EXT-X-I-FRAME-STREAM-INF:VIDEO_RANGE=SDR,URI="http://example.com/sdr-iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:VIDEO_RANGE=PQ,URI="http://example.com/hdr-pq-iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:VIDEO_RANGE=HLG,URI="http://example.com/hdr-hlg-iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:URI="http://example.com/unknown-iframes.m3u8"
'''

VARIANT_PLAYLIST_WITH_IFRAME_HDCP_LEVEL = '''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,HDCP-LEVEL=NONE
http://example.com/none.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,HDCP-LEVEL=TYPE-0
http://example.com/type0.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,HDCP-LEVEL=TYPE-1
http://example.com/type1.m3u8
#EXT-X-I-FRAME-STREAM-INF:HDCP-LEVEL=NONE,URI="http://example.com/none-iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:HDCP-LEVEL=TYPE-0,URI="http://example.com/type0-iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:HDCP-LEVEL=TYPE-1,URI="http://example.com/type1-iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:URI="http://example.com/unknown-iframes.m3u8"
'''

DELTA_UPDATE_SKIP_DATERANGES_PLAYLIST = '''#EXTM3U
#EXT-X-VERSION:10
#EXT-X-TARGETDURATION:6
#EXT-X-SERVER-CONTROL:CAN-SKIP-UNTIL=36,CAN-SKIP-DATERANGES=YES
#EXT-X-MEDIA-SEQUENCE:1
#EXT-X-MAP:URI="init.mp4"
#EXT-X-SKIP:SKIPPED-SEGMENTS=16,RECENTLY-REMOVED-DATERANGES="1"
#EXTINF:4.00000,
segment16.mp4
#EXTINF:4.00000,
segment17.mp4
#EXTINF:4.00000,
segment18.mp4
#EXTINF:4.00000,
segment19.mp4
#EXTINF:4.00000,
segment20.mp4
#EXTINF:4.00000,
segment21.mp4
#EXT-X-DATERANGE:ID="P"
#EXT-X-DATERANGE:ID="Q"
'''

BITRATE_PLAYLIST = '''
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-INDEPENDENT-SEGMENTS
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:55119
#EXT-X-PROGRAM-DATE-TIME:2020-07-21T08:14:29.379Z
#EXT-X-BITRATE:1674
#EXTINF:9.600,
test1.ts
#EXT-X-BITRATE:1625
#EXTINF:9.600,
test2.ts
'''

CONTENT_STEERING_PLAYLIST = '''
#EXTM3U
#EXT-X-CONTENT-STEERING:SERVER-URI="/steering?video=00012",PATHWAY-ID="CDN-A"
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="A",NAME="English",DEFAULT=YES,URI="eng.m3u8",LANGUAGE="en"
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="B",NAME="ENGLISH",DEFAULT=YES,URI="https://b.example.com/content/videos/video12/eng.m3u8",LANGUAGE="en"
#EXT-X-STREAM-INF:BANDWIDTH=1280000,AUDIO="A",PATHWAY-ID="CDN-A"
low/video.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=7680000,AUDIO="A",PATHWAY-ID="CDN-A"
hi/video.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=1280000,AUDIO="B",PATHWAY-ID="CDN-B"
https://backup.example.com/content/videos/video12/low/video.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=7680000,AUDIO="B",PATHWAY-ID="CDN-B"
https://backup.example.com/content/videos/video12/hi/video.m3u8
#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=193350,CODECS="avc1.4d001f",URI="video-1200k-iframes.m3u8",PATHWAY-ID="CDN-A"
#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=193350,CODECS="avc1.4d001f",URI="https://backup.example.com/content/videos/video12/video-1200k-iframes.m3u8",PATHWAY-ID="CDN-B"
'''

VARIANT_PLAYLIST_WITH_STABLE_VARIANT_ID = '''
#EXT-X-STREAM-INF:BANDWIDTH=1280000,STABLE-VARIANT-ID="eb9c6e4de930b36d9a67fbd38a30b39f865d98f4a203d2140bbf71fd58ad764e"
http://example.com/type0.m3u8
'''

VARIANT_PLAYLIST_WITH_IFRAME_STABLE_VARIANT_ID = '''
#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=128000,STABLE-VARIANT-ID="415901312adff69b967a0644a54f8d00dc14004f36bc8293737e6b4251f60f3f",URI="http://example.com/type0-iframes.m3u8"
'''

VARIANT_PLAYLIST_WITH_STABLE_RENDITION_ID = '''
#EXT-X-MEDIA:TYPE=AUDIO,NAME="audio-aac-eng",STABLE-RENDITION-ID="a8213e27c12a158ea8660e0fe8bdcac6072ca26d984e7e8603652bc61fdceffa",URI="http://example.com/eng.m3u8"
'''

del abspath, dirname, join
