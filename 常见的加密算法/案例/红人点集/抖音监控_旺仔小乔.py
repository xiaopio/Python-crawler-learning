import time
from pprint import pprint

import requests

cookies = {
    'enter_pc_once': '1',
    'UIFID_TEMP': '1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee64740fbe9f64265e8cc0c6a24a49d2c9dfcc27bbe0e26d5d0df1affc62bf744a34c91cecc38215362424e9c0df56fddf5521ca7295d88532c55add194674b1cb9a07daa02d2612ef4edc06355da0b5f59f594',
    'hevc_supported': 'true',
    'strategyABtestKey': '%221753847217.904%22',
    'is_dash_user': '1',
    'volume_info': '%7B%22volume%22%3A0.6%2C%22isMute%22%3Atrue%7D',
    'passport_csrf_token': '712d3e367df201f55b59e630d67b4c63',
    'passport_csrf_token_default': '712d3e367df201f55b59e630d67b4c63',
    'bd_ticket_guard_client_web_domain': '2',
    '__security_mc_1_s_sdk_crypt_sdk': 'dc0f74d3-45ce-85a1',
    'sdk_source_info': '7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6a716c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f2737353c35373732313d36303234272927676c715a75776a716a666a69273f2763646976602778',
    'bit_env': 'pMDOywlennt3XSIJEx_ablPyzisry0FG1Yf_FReUTLhQAV5XACe-mWTjUQh1V4m9bmRcAEqhkSXJM-Ms9uTqHuSEsXv6WSIMukaglrHHwJT3fYbKWPpgIe_DtI2xeqpG8Jnro7kgp6VMVY5LUK_P0fNglidLu0YuJ73zinfeCIuLlGKssyJeEB3RJs24z9YsJfVIZ2aXkCf_A5kZIdmBUBvy24GwZHiKNUxHcsnBwmF7dK8U25VMAvF58nuNwSQeW9Am2czpE2YwVW4SF11PRvQ24fQkN6wER-Smjpxv2Ie_ufX0AV0PaKglaw5JAowXhsswKZWcIIC9233bBbfQBKW-uPriz4rLv7hZ1lYnH_JBuagEIecN0sFy40IkcUZt_mivELKIgQv6x4QTlgkBmEXR8Lt1vwvAN1nqmkxf0f2Qiv5wy5CN_iSN8RZi5Q3IqQnhbvlESbIpJfnHrLlHDJnpzqADSbBjNPeQnaj8fu01YmlgvESPcgCwg5tjQ-ho',
    'gulu_source_res': 'eyJwX2luIjoiYTlmMjU3NzAxMWQ2OTIyYjc5NWQ5Zjk3NjY1OWVkOTNkMGQ2NjBjMWZhMmNkYzdjMGI4NmI5YTU2YjlhYmU1OCJ9',
    'passport_auth_mix_state': '5lt3ceo0zocb5rdppsdwzygq37imfaq1gkz55o71on7llcsf',
    'passport_assist_user': 'CkHvzWDAGJ6TUxq1rARRSw7v5FcPUJq_S62HHspzu-dXW-b3mRKnLcqtHRwtYt7bKR8s1vV9_wuO0QEyCZ86t6R7nRpKCjwAAAAAAAAAAAAAT0u54ZFN2JW7DBZjmBJD89WNEet95NO9fHbrEn-26exFmJ3XZw5YtB_fwHopaPvPh0cQvYz4DRiJr9ZUIAEiAQOrrgf0',
    'n_mh': 'f7POOEKDXAGvn8fDFrjyy_4xHL1EaK7JzMwpuJwbnhg',
    'sid_guard': '9eb526a7ffa0e0ae16f8bc3168c628a9%7C1753847232%7C5184000%7CSun%2C+28-Sep-2025+03%3A47%3A12+GMT',
    'uid_tt': '8b591390921f99217b2112d6adad2ca1',
    'uid_tt_ss': '8b591390921f99217b2112d6adad2ca1',
    'sid_tt': '9eb526a7ffa0e0ae16f8bc3168c628a9',
    'sessionid': '9eb526a7ffa0e0ae16f8bc3168c628a9',
    'sessionid_ss': '9eb526a7ffa0e0ae16f8bc3168c628a9',
    'session_tlb_tag': 'sttt%7C2%7CnrUmp_-g4K4W-LwxaMYoqf_________LG-p9MTt9PtamsI6eCr1NCI79u9H5xYjh22TPs-LEFf0%3D',
    'is_staff_user': 'false',
    'sid_ucp_v1': '1.0.0-KGUyNTJmMzVjNjFiNjQzYTI2ODBiZWZkYjA0NDcwMjUxOTA1OTkzYmYKIQiNrODZl4yyBhDAq6bEBhjvMSAMMMro3ogGOAdA9AdIBBoCaGwiIDllYjUyNmE3ZmZhMGUwYWUxNmY4YmMzMTY4YzYyOGE5',
    'ssid_ucp_v1': '1.0.0-KGUyNTJmMzVjNjFiNjQzYTI2ODBiZWZkYjA0NDcwMjUxOTA1OTkzYmYKIQiNrODZl4yyBhDAq6bEBhjvMSAMMMro3ogGOAdA9AdIBBoCaGwiIDllYjUyNmE3ZmZhMGUwYWUxNmY4YmMzMTY4YzYyOGE5',
    'login_time': '1753847233129',
    '_bd_ticket_crypt_cookie': '3fd808ee4840bffeff0da7c8f84d4026',
    '__security_mc_1_s_sdk_sign_data_key_web_protect': '64726287-4be5-a5c9',
    '__security_mc_1_s_sdk_cert_key': '969c2de7-4754-ba3a',
    '__security_server_data_status': '1',
    'UIFID': '1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee64740fbe9f64265e8cc0c6a24a49d2c9dfcc27bbe0e26d5d0df1affc62bf744a34c9162790a3a27d45975691656f68c29afdaeca6df90c4d5c59ae7c8274bd054c0f7364450014267091a7ad7764b4bd5342971d1c65196fc1c58be11fcf780819b0a6553aecf7e97dde38b6d647ab263086045ac5d48e01c8fd199a045bdcf758c6463fbc544cc1afb3724d495bdf7de96f7455eb5fd0e1f9b4cec040cb7e2e04e2c',
    'stream_player_status_params': '%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22',
    'SelfTabRedDotControl': '%5B%7B%22id%22%3A%227526174577727113279%22%2C%22u%22%3A6%2C%22c%22%3A0%7D%5D',
    'FOLLOW_LIVE_POINT_INFO': '%22MS4wLjABAAAAaUOulUqNRkX7zNVUbsUIBhUD4Yl2YsnCfjfJeir_niDgUFiPs9a4l7WYtrI-BMKC%2F1753891200000%2F0%2F1753847235058%2F0%22',
    'biz_trace_id': 'a88a9d97',
    'publish_badge_show_info': '%220%2C0%2C0%2C1753847244732%22',
    'stream_recommend_feed_params': '%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22',
    'bd_ticket_guard_client_data': 'eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSnFFU0lXQ3hrTlRGQ2lqOTF0UlVjc2pSYmppRGxFWnRhYzEyMXFJTUJNTW1ubXJSL1V6ZUxXTU9rRjJnSlUwcnpaMGtoRjhyOXprYlc4eitqRSt5Q2M9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D',
    'ttwid': '1%7C2g225d6Au-kkYrdDlCGK_NW4NrQrFsRI9YEAIV3zI2M%7C1753847286%7Cfeb256781692187dfb7e081f80428eb4506ae1bcc18706fc34a06873fed199d9',
    'playRecommendGuideTagCount': '1',
    'totalRecommendGuideTagCount': '1',
    'IsDouyinActive': 'true',
    'home_can_add_dy_2_desktop': '%220%22',
    'odin_tt': '2d9165af9ce3a245b267dad6be1d0c7238054250c378091cbd2baa47596a69985b8011b93650136d59885b84ddb6ac01b1ec3b05e806dbe826e92ef5cbf18c7d',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'origin': 'https://www.douyin.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.douyin.com/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'uifid': '1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee64740fbe9f64265e8cc0c6a24a49d2c9dfcc27bbe0e26d5d0df1affc62bf744a34c9162790a3a27d45975691656f68c29afdaeca6df90c4d5c59ae7c8274bd054c0f7364450014267091a7ad7764b4bd5342971d1c65196fc1c58be11fcf780819b0a6553aecf7e97dde38b6d647ab263086045ac5d48e01c8fd199a045bdcf758c6463fbc544cc1afb3724d495bdf7de96f7455eb5fd0e1f9b4cec040cb7e2e04e2c',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': 'enter_pc_once=1; UIFID_TEMP=1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee64740fbe9f64265e8cc0c6a24a49d2c9dfcc27bbe0e26d5d0df1affc62bf744a34c91cecc38215362424e9c0df56fddf5521ca7295d88532c55add194674b1cb9a07daa02d2612ef4edc06355da0b5f59f594; hevc_supported=true; strategyABtestKey=%221753847217.904%22; is_dash_user=1; volume_info=%7B%22volume%22%3A0.6%2C%22isMute%22%3Atrue%7D; passport_csrf_token=712d3e367df201f55b59e630d67b4c63; passport_csrf_token_default=712d3e367df201f55b59e630d67b4c63; bd_ticket_guard_client_web_domain=2; __security_mc_1_s_sdk_crypt_sdk=dc0f74d3-45ce-85a1; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6a716c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f2737353c35373732313d36303234272927676c715a75776a716a666a69273f2763646976602778; bit_env=pMDOywlennt3XSIJEx_ablPyzisry0FG1Yf_FReUTLhQAV5XACe-mWTjUQh1V4m9bmRcAEqhkSXJM-Ms9uTqHuSEsXv6WSIMukaglrHHwJT3fYbKWPpgIe_DtI2xeqpG8Jnro7kgp6VMVY5LUK_P0fNglidLu0YuJ73zinfeCIuLlGKssyJeEB3RJs24z9YsJfVIZ2aXkCf_A5kZIdmBUBvy24GwZHiKNUxHcsnBwmF7dK8U25VMAvF58nuNwSQeW9Am2czpE2YwVW4SF11PRvQ24fQkN6wER-Smjpxv2Ie_ufX0AV0PaKglaw5JAowXhsswKZWcIIC9233bBbfQBKW-uPriz4rLv7hZ1lYnH_JBuagEIecN0sFy40IkcUZt_mivELKIgQv6x4QTlgkBmEXR8Lt1vwvAN1nqmkxf0f2Qiv5wy5CN_iSN8RZi5Q3IqQnhbvlESbIpJfnHrLlHDJnpzqADSbBjNPeQnaj8fu01YmlgvESPcgCwg5tjQ-ho; gulu_source_res=eyJwX2luIjoiYTlmMjU3NzAxMWQ2OTIyYjc5NWQ5Zjk3NjY1OWVkOTNkMGQ2NjBjMWZhMmNkYzdjMGI4NmI5YTU2YjlhYmU1OCJ9; passport_auth_mix_state=5lt3ceo0zocb5rdppsdwzygq37imfaq1gkz55o71on7llcsf; passport_assist_user=CkHvzWDAGJ6TUxq1rARRSw7v5FcPUJq_S62HHspzu-dXW-b3mRKnLcqtHRwtYt7bKR8s1vV9_wuO0QEyCZ86t6R7nRpKCjwAAAAAAAAAAAAAT0u54ZFN2JW7DBZjmBJD89WNEet95NO9fHbrEn-26exFmJ3XZw5YtB_fwHopaPvPh0cQvYz4DRiJr9ZUIAEiAQOrrgf0; n_mh=f7POOEKDXAGvn8fDFrjyy_4xHL1EaK7JzMwpuJwbnhg; sid_guard=9eb526a7ffa0e0ae16f8bc3168c628a9%7C1753847232%7C5184000%7CSun%2C+28-Sep-2025+03%3A47%3A12+GMT; uid_tt=8b591390921f99217b2112d6adad2ca1; uid_tt_ss=8b591390921f99217b2112d6adad2ca1; sid_tt=9eb526a7ffa0e0ae16f8bc3168c628a9; sessionid=9eb526a7ffa0e0ae16f8bc3168c628a9; sessionid_ss=9eb526a7ffa0e0ae16f8bc3168c628a9; session_tlb_tag=sttt%7C2%7CnrUmp_-g4K4W-LwxaMYoqf_________LG-p9MTt9PtamsI6eCr1NCI79u9H5xYjh22TPs-LEFf0%3D; is_staff_user=false; sid_ucp_v1=1.0.0-KGUyNTJmMzVjNjFiNjQzYTI2ODBiZWZkYjA0NDcwMjUxOTA1OTkzYmYKIQiNrODZl4yyBhDAq6bEBhjvMSAMMMro3ogGOAdA9AdIBBoCaGwiIDllYjUyNmE3ZmZhMGUwYWUxNmY4YmMzMTY4YzYyOGE5; ssid_ucp_v1=1.0.0-KGUyNTJmMzVjNjFiNjQzYTI2ODBiZWZkYjA0NDcwMjUxOTA1OTkzYmYKIQiNrODZl4yyBhDAq6bEBhjvMSAMMMro3ogGOAdA9AdIBBoCaGwiIDllYjUyNmE3ZmZhMGUwYWUxNmY4YmMzMTY4YzYyOGE5; login_time=1753847233129; _bd_ticket_crypt_cookie=3fd808ee4840bffeff0da7c8f84d4026; __security_mc_1_s_sdk_sign_data_key_web_protect=64726287-4be5-a5c9; __security_mc_1_s_sdk_cert_key=969c2de7-4754-ba3a; __security_server_data_status=1; UIFID=1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee64740fbe9f64265e8cc0c6a24a49d2c9dfcc27bbe0e26d5d0df1affc62bf744a34c9162790a3a27d45975691656f68c29afdaeca6df90c4d5c59ae7c8274bd054c0f7364450014267091a7ad7764b4bd5342971d1c65196fc1c58be11fcf780819b0a6553aecf7e97dde38b6d647ab263086045ac5d48e01c8fd199a045bdcf758c6463fbc544cc1afb3724d495bdf7de96f7455eb5fd0e1f9b4cec040cb7e2e04e2c; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; SelfTabRedDotControl=%5B%7B%22id%22%3A%227526174577727113279%22%2C%22u%22%3A6%2C%22c%22%3A0%7D%5D; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAaUOulUqNRkX7zNVUbsUIBhUD4Yl2YsnCfjfJeir_niDgUFiPs9a4l7WYtrI-BMKC%2F1753891200000%2F0%2F1753847235058%2F0%22; biz_trace_id=a88a9d97; publish_badge_show_info=%220%2C0%2C0%2C1753847244732%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSnFFU0lXQ3hrTlRGQ2lqOTF0UlVjc2pSYmppRGxFWnRhYzEyMXFJTUJNTW1ubXJSL1V6ZUxXTU9rRjJnSlUwcnpaMGtoRjhyOXprYlc4eitqRSt5Q2M9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; ttwid=1%7C2g225d6Au-kkYrdDlCGK_NW4NrQrFsRI9YEAIV3zI2M%7C1753847286%7Cfeb256781692187dfb7e081f80428eb4506ae1bcc18706fc34a06873fed199d9; playRecommendGuideTagCount=1; totalRecommendGuideTagCount=1; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22; odin_tt=2d9165af9ce3a245b267dad6be1d0c7238054250c378091cbd2baa47596a69985b8011b93650136d59885b84ddb6ac01b1ec3b05e806dbe826e92ef5cbf18c7d',
}

params = {
    'device_platform': 'webapp',
    'aid': '6383',
    'channel': 'channel_pc_web',
    'publish_video_strategy_type': '2',
    'source': 'channel_pc_web',
    'sec_user_id': 'MS4wLjABAAAACdtHOv8XS_X_PTuqJ3WReO4ka7pBWg7fmzG4wjiIZVkUKFOVtbhizl9GkpdOJ-O1',
    'personal_center_strategy': '1',
    'profile_other_record_enable': '1',
    'land_to': '1',
    'update_version_code': '170400',
    'pc_client_type': '1',
    'pc_libra_divert': 'Windows',
    'support_h265': '1',
    'support_dash': '1',
    'cpu_core_num': '16',
    'version_code': '170400',
    'version_name': '17.4.0',
    'cookie_enabled': 'true',
    'screen_width': '1536',
    'screen_height': '864',
    'browser_language': 'zh-CN',
    'browser_platform': 'Win32',
    'browser_name': 'Chrome',
    'browser_version': '138.0.0.0',
    'browser_online': 'true',
    'engine_name': 'Blink',
    'engine_version': '138.0.0.0',
    'os_name': 'Windows',
    'os_version': '10',
    'device_memory': '8',
    'platform': 'PC',
    'downlink': '10',
    'effective_type': '4g',
    'round_trip_time': '50',
    'webid': '7532716363392255488',
    'uifid': '1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee64740fbe9f64265e8cc0c6a24a49d2c9dfcc27bbe0e26d5d0df1affc62bf744a34c9162790a3a27d45975691656f68c29afdaeca6df90c4d5c59ae7c8274bd054c0f7364450014267091a7ad7764b4bd5342971d1c65196fc1c58be11fcf780819b0a6553aecf7e97dde38b6d647ab263086045ac5d48e01c8fd199a045bdcf758c6463fbc544cc1afb3724d495bdf7de96f7455eb5fd0e1f9b4cec040cb7e2e04e2c',
    'msToken': 'Ri9PunFyr6BesMpHoP7TvYTt1S4jx6Uw0avEH37DPFeTH3Cgy7tIcfqGyBG7jR3ytyLdigoGSvQ37w23WDGHCt4cpDT1nrXgYjTcrgOoo0nmBzGxfgsW18EeIWecSeByKB9LK7swbu_Kusu-MUgvJV4nJNN0hbT94p5Dp_hGML_8',
    'a_bogus': 'dJsfhetExpWjFVKGYCGz972lW1g/NBuy1HixWNrPS5aDOZFTUmPAwNb3bxKQsq88uYBziFI7EjlMbdnc04X0ZHrkumkkSu4SOT/VVUso8qq6TUT/EHfxezUzowBFUOiNaQ9WiI8RWs0r2nxR9r5uABZae5F9Q5jgbNBCpZb9jDC8psgTIo2ACrJWvq6=',
    'verifyFp': 'verify_mdpfcl7h_DD6um8TF_tCqk_48SZ_9HXf_6VL1PcCnoBrt',
    'fp': 'verify_mdpfcl7h_DD6um8TF_tCqk_48SZ_9HXf_6VL1PcCnoBrt',
}

from datetime import datetime


def get_current_time():
    # 获取当前时间
    current_time = datetime.now()
    # 格式化时间为 "yyyy年-mm月-dd日 时-分-秒" 格式
    formatted_time = current_time.strftime("%Y年%m月%d日 %H:%M:%S")
    # 打印结果
    print(formatted_time)




def get_now_follower_count():
    response = requests.get(
        'https://www-hj.douyin.com/aweme/v1/web/user/profile/other/',
        params=params,
        cookies=cookies,
        headers=headers,
    ).json()
    # pprint(response)
    nick_name = response["user"]["nickname"]
    max_follower_count = response["user"]["max_follower_count"]
    mplatform_followers_count = response["user"]["mplatform_followers_count"]
    get_current_time()
    print(f'用户名：\t\t\t{nick_name}\n最多关注人数：\t{max_follower_count}\n实时关注人数：\t{mplatform_followers_count}\n掉粉人数:\t\t{max_follower_count - mplatform_followers_count}')



while True:
    mp = get_now_follower_count()
    time.sleep(10)
