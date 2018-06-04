# -*- coding:utf-8 -*


class Commands(object):

  TEXT = 'text'
  TAG_NAME = 'tag_name'
  CLICK = 'click'
  CLEAR = 'clear'
  SEND_KEYS = 'send_keys'
  ENTER = 'ENTER'
  HOME = 'HOME'
  BACK = 'BACK'


class Tests(object):

  GET_MEMORY_STATUS = 'test_get_memory_status'
  BLUETOOTH_DISABLE = 'test_bluetooth_disable'
  BLUETOOTH_ENABLE = 'test_bluetooth_enable'
  WLAN_DISABLE = 'test_wlan_disable'
  WLAN_ENABLE = 'test_wlan_enable'
  CANDY_CRUSH= 'test_candy_crush'
  TAKE_PICTURE = 'test_take_picture'
  SMS_MO = 'test_SMS_MO'
  MMS_MO = 'test_MMS_MO'
  MULTI_LAYERS = 'test_multi_layers_no_reset'
  TEN_WEBSITES = 'test_ten_websites'
  MUSIC_PLAYBACK = 'test_music_palyback'
  MUSIC_NETWORK = 'test_music_network'
  VIDEO_PLAYBACK = 'test_video_playback'
  VIDEO_NETWORK = 'test_video_network'
  MOVILTE = 'test_MOViLTE'
  MOVOLTE = 'test_MOVoLTE'
  MTVOLTE = 'test_MTVoLTE'
  VO2VI2VO = 'test_Vo2Vi2Vo'


class C_Location(object):
  
  BTN_ALLOW = "//*[contains(@resource-id, 'id/permission_allow_button')]"
  BTN_DENY = "//*[contains(@resource-id, 'id/permission_deny_button')]"


class C_Settings(object):
  
  APP = [
    'Settings',               # App Name
    "com.android.settings",   # App Package
    ".Settings"               # App Activity
  ]

  PATH_NAVIGATE_UP = "//*[contains(@content-desc, 'Navigate up')]"
  PATH_MEMORY = "//*[contains(@text, 'Storage')]"
  PATH_BLUETOOTH = "//*[contains(@text, 'Connected devices')]"
  PATH_WLAN = "//*[contains(@text, 'Network & Internet')]"


class C_Memorry(object):
  
  PREFIX = 'test_get_memory_status'
  ROOT_PATH = "android.support.v7.widget.RecyclerView[@index=0]/android.widget.LinearLayout[@index=0]/android.widget.LinearLayout[@index=0]"
  PATH_DONUT = "//*[contains(@resource-id, 'id/donut')]"
  PATH_TOTAL_MEMORY = "//{0}/android.widget.TextView[@index=1]".format(ROOT_PATH)
  PATH_USED= "//{0}/android.widget.TextView[@index=0]".format(ROOT_PATH)

  PATH_USED_C = "//android.support.v7.widget.RecyclerView[@index=0]/android.widget.LinearLayout[@index=1]/android.widget.TextView[@index=0]"
  PATH_TOTAL_C = "//android.support.v7.widget.RecyclerView[@index=0]/android.widget.LinearLayout[@index=1]/android.widget.TextView[@index=1]"


class C_Bluetooth(object):
  
  PATH_BLUETOOTH_INDEX = "//*[contains(@text, 'Bluetooth') and contains(@resource-id, 'id/title')]"
  PREFIX_D = "test_bluetooth_disable"
  PREFIX_E = "test_bluetooth_enable"
  HEADSET_NAME = "MIX2-FEC"
  BLUETOOTH_ENABLED = "ON"
  BLUETOOTH_DISABLED = "OFF"

  PATH_SWITCH_BLUETOOTH = "//*[contains(@resource-id, 'id/switch_widget') and contains(@index, 1)]"

  PATH_DEVICES_1ST_SETTINGS = "//android.support.v7.widget.RecyclerView[@index=0]/android.widget.LinearLayout[@index=2]/android.widget.LinearLayout[@index=2]/android.widget.ImageView[@index=0]"
  PATH_BTN_FOGET = "//*[contains(@text, 'FORGET')]"
  PATH_BTN_OK = "//*[contains(@text, 'OK')]"
  PATH_PAIR_NEW_DEVICE = "//*[contains(@text, 'Pair new device')]"

  PATH_HEADSET = "//*[contains(@text, '{0}')]".format(HEADSET_NAME)
  PATH_CHECKBOX_PAIR_ALLOW = "//*[contains(@resource-id, 'id/phonebook_sharing_message_confirm_pin')]"
  PATH_BTN_PAIR = "//*[contains(@text, 'PAIR')]"
  PATH_BTN_CANCEL = "//*[contains(@text, 'CANCEL')]"
  PATH_AVAILABLE_DEVICES = "//*[contains(@text, 'Available devices')]"
  PATH_PAIRED_DEVICE = "//*[contains(@text, 'Paired devices')]"


class C_WLAN(object):

  PATH_WLAN_INDEX = "//android.widget.RelativeLayout[@index=1]/android.widget.TextView[@index=0]"
  PREFIX_D = 'test_wlan_disable'
  PREFIX_E = 'test_wlan_enable'
  AP_POINT_NAME = "CTS_2.4G"
  # password must be number
  AP_PASSWORD = "173925239"
  WLAN_ENABLED = "ON"
  WLAN_DISABLED = "OFF"

  PATH_SWITCH_WLAN = "//*[contains(@resource-id, 'id/switch_widget') and contains(@index, 1)]"
  
  PATH_AP_POINT = "//*[contains(@text, '{0}')]".format(AP_POINT_NAME)
  PATH_AP_CONNECTED = "//*[contains(@resource-id, 'id/summary') and contains(@text, 'Connected')]"
  PATH_AP_FORGET = "//*[contains(@resource-id, 'id/forget_button')]"
  PATH_ET_PW = "//*[contains(@resource-id, 'id/password')]"
  PATH_CHECKBOX_PW_SHOW = "//*[contains(@resource-id, 'id/show_password')]"
  PATH_BTN_CANCEL = "//*[contains(@resource-id, 'id/button2') and contains(@text, 'CANCEL')]"
  PATH_BTN_CONNECT = "//*[contains(@resource-id, 'id/button1') and contains(@text, 'CONNECT')]"
  PATH_ADD_NETWORK = "//*[contains(@text, 'Add network')]"
  PATH_ET_SSID = "//*[contains(@resource-id, 'id/ssid')]"
  PATH_SPINNER_SECURITY = "//*[contains(@resource-id, 'id/security')]"
  PATH_NONE_SECURITY = "//*[contains(@resource-id, 'id/text1') and contains(@text, 'None')]"
  PATH_WEP_SECURITY = "//*[contains(@resource-id, 'id/text1') and contains(@text, 'WEP')]"
  PATH_WPA_SECURITY = "//*[contains(@resource-id, 'id/text1') and contains(@text, 'WPA/WPA2 PSK')]"
  PATH_EAP_SECURITY = "//*[contains(@resource-id, 'id/text1') and contains(@text, '802.1x EAP')]"
  PATH_BTN_SAVE = "//*[contains(@resource-id, 'id/button1') and contains(@text, 'SAVE')]"
  PATH_WLAN_STATUS = "//android.support.v7.widget.RecyclerView[@index=0]/android.widget.LinearLayout[@index=0]/android.widget.LinearLayout[@index=0]/android.widget.RelativeLayout[@index=1]/android.widget.TextView[@index=1]"


class C_CandyCrush(object):
  
  APP = [
    "CandyCrush",
    "com.king.candycrushsaga",
    ".CandyCrushSagaActivity"
  ]
  
  PREFIX = 'test_candy_crush'
  LOGIN_CLOSE_X = 575
  LOGIN_CLOSE_Y = 500
  SETTINGS_X = 25
  SETTINGS_Y = 1150


class C_Maps(object):

  APP = [
    "GoogleMaps",
    "com.google.android.apps.maps",
    "com.google.android.maps.MapsActivity"
  ]

  PREFIX = 'test_multi_layers_no_reset'
  # //android.widget.RelativeLayout[@index=0]/android.widget.Button[@index=1]
  PATH_PAGE_SKIP = "//*[contains(@text, 'SKIP')]"
  PATH_PAGE_SIGN_IN_PATH = "//*[contains(@text, 'SIGN IN')]"
  PATH_NAV_MENU = "//*[contains(@resource-id, 'id/search_omnibox_menu_button')]"
  PATH_NAV_TYPES = "//android.support.v4.widget.DrawerLayout[@index=0]/android.widget.FrameLayout[@index=1]/android.widget.ListView[@index=0]/android.widget.ToggleButton"
  PATH_BTN_MYLOCATIONBT = "//*[contains(@resource-id, 'id/mylocation_button')]"
  PATH_BTN_DIRECTIONS = "//*[contains(@resource-id, 'id/on_map_directions_button')]"
  PATH_BTN_COMPASS = "//*[contains(@content-desc, 'Layers button')]"
  PATH_MAP_TYPE_ROOT1 = "android.widget.LinearLayout[@index=0]/android.widget.LinearLayout[@index=2]"
  PATH_MAP_TYPE_ROOT2 = "android.widget.LinearLayout[@index=0]/android.widget.LinearLayout[@index=5]"
  PATH_MAP_TYPE_DEFAULT = "//{0}/android.widget.LinearLayout[@index=0]/android.widget.TextView[@index=1]".format(PATH_MAP_TYPE_ROOT1)
  PATH_MAP_TYPE_SATELLITE = "//{0}/android.widget.LinearLayout[@index=1]/android.widget.TextView[@index=1]".format(PATH_MAP_TYPE_ROOT1)
  PATH_MAP_TYPE_TERRAIN = "//{0}/android.widget.LinearLayout[@index=2]/android.widget.TextView[@index=1]".format(PATH_MAP_TYPE_ROOT1)
  PATH_MAP_TYPE_TRANSIT = "//{0}/android.widget.LinearLayout[@index=0]/android.widget.TextView[@index=1]".format(PATH_MAP_TYPE_ROOT2)
  PATH_MAP_TYPE_TRAFFIC = "//{0}/android.widget.LinearLayout[@index=1]/android.widget.TextView[@index=1]".format(PATH_MAP_TYPE_ROOT2)
  PATH_MAP_TYPE_BICYCLING = "//{0}/android.widget.LinearLayout[@index=2]/android.widget.TextView[@index=1]".format(PATH_MAP_TYPE_ROOT2)
  PATH_BTN_CLOSE_COMPASS = "//*[contains(@content-desc, 'Close menu')]"


class C_Music(object):
  
  APP = [
    "GoogleMusic",
    "com.google.android.music",
    ".ui.HomeActivity"
  ]

  PREFIX = 'test_music_palyback'
  PLAY_MINUTES = 3
  PATH_BTN_MENU = "//*[contains(@content-desc, 'Show navigation drawer') and contains(@index, 0)]"
  PATH_NAV_LISTEN_NOW = "//*[contains(@text, 'Listen Now')]"
  PATH_NAV_MUSIC_LIBRARY = "//*[contains(@text, 'Music library')]"
  PATH_BTN_ADD_ACCOUNT = "//*[contains(@resource-id, 'id/add_account_button')]"
  PATH_BTN_SKIP = "//*[contains(@resource-id, 'id/skip_button')]"
  PATH_SHUFFLE_ALL = "//*[contains(@resource-id, 'id/play_card') and contains(@index, 0)]"
  PATH_BTN_PAUSE_PLAY = "//*[contains(@resource-id, 'id/play_pause_header')]"
  # pause->content-desc:play    play->content-desc:pause
  STATUS_PLAYING = "Pause"
  STATUS_PAUSED = "Play"


class C_Video(object):
  
  APP = [
    "Video",
    "com.android.music",
    ".VideoBrowserActivity"
  ]

  PREFIX = 'test_video_playback'
  PLAY_MINUTES = 3
  PATH_VIDEOS = "//*[contains(@resource-id, 'id/text1')]"
  PATH_SELECT_PLAY = "//*[contains(@text, 'Video player')]"
  PATH_BTN_ONCE = "//*[contains(@resource-id, 'id/button_once')]"
  PATH_BTN_ALWAYS = "//*[contains(@resource-id, 'id/button_always')]"
  PATH_START_OVER = "//*[contains(@resource-id, 'id/button2') and contains(@text, 'START OVER')]"
  PATH_RESUME_PLAYING = "//*[contains(@resource-id, 'id/button1') and contains(@text, 'RESUME PLAYING')]"


class C_Dialer(object):
  
  APP = [
    "Dialer",
    "com.android.dialer",
    ".app.DialtactsActivity"
    ]
  
  CALL_TIME = 3

  PREFIX = 'test_dialer'
  PHONE_NUM = "13621872145"
  REF_PHONE_NUM = "14782305348"

  ID_BTN_FLOAT = "com.android.dialer:id/floating_action_button"
  ID_BTN_DIALPAD_FLOAT = "com.android.dialer:id/dialpad_floating_action_button"
  ID_BTN_END_CALL = "com.android.dialer:id/incall_end_call"
  ID_BTN_DELETE = "com.android.dialer:id/deleteButton"

  ID_CONTACTGRID_STATUS = "com.android.dialer:id/contactgrid_status_text"

  ID_VOLUME_BOOST = "com.android.dialer:id/volumeBoost"
  PATH_MUTE = "//*[contains(@resource-id, 'id/incall_first_button') and contains(@text, 'Mute')]"
  PATH_KEYPAD = "//*[contains(@resource-id, 'id/incall_second_button') and contains(@text, 'Keypad')]"
  PATH_SPEAKER = "//*[contains(@resource-id, 'id/incall_third_button') and contains(@text, 'Speaker')]"
  PATH_ADD_CALL = "//*[contains(@resource-id, 'id/incall_fourth_button') and contains(@text, 'Add call')]"
  PATH_ADD_CALL = "//*[contains(@resource-id, 'id/incall_fifth_button') and contains(@text, 'Hold')]"

  ID_DIALPAD_BACK = "com.android.dialer:id/dialpad_back"
  PATH_SWAP_CALL = "//*[contains(@resource-id, 'id/incall_fourth_button') and contains(@text, 'Swap')]"

  ID_SWIPE_TO_ANSWER = "com.android.dialer:id/incoming_swipe_to_answer_container"
  ID_CALL_PUCK = "com.android.dialer:id/incoming_call_puck_bg"

  ID_KEY_ZERO = "com.android.dialer:id/zero"
  ID_KEY_ONE = "com.android.dialer:id/one"
  ID_KEY_TWO = "com.android.dialer:id/two"
  ID_KEY_THREE = "com.android.dialer:id/three"
  ID_KEY_FOUR = "com.android.dialer:id/four"
  ID_KEY_FIVE = "com.android.dialer:id/five"
  ID_KEY_SIX = "com.android.dialer:id/six"
  ID_KEY_SEVEN = "com.android.dialer:id/seven"
  ID_KEY_EIGHT = "com.android.dialer:id/eight"
  ID_KEY_NINE = "com.android.dialer:id/nine"
  ID_KEY_STAR = "com.android.dialer:id/star"
  ID_KEY_POUND = "com.android.dialer:id/pound"

  def number(self, key):
    return{
      '0': "com.android.dialer:id/zero",
      '1': "com.android.dialer:id/one",
      '2': "com.android.dialer:id/two",
      '3': "com.android.dialer:id/three",
      '4': "com.android.dialer:id/four",
      '5': "com.android.dialer:id/five",
      '6': "com.android.dialer:id/six",
      '7': "com.android.dialer:id/seven",
      '8': "com.android.dialer:id/eight",
      '9': "com.android.dialer:id/nine"
    }.get(key, "Please confirm if the keycode is valid.")


class C_Tune(object):
  
  APP = [
    "TuneInRadio",
    "tunein.player",
    "tunein.ui.actvities.TuneInHomeActivity"
  ]
  
  PREFIX = "test_music_network"
  CLOSE_HOMEPAGE_X = 607
  CLOSE_HOMEPAGE_Y = 68
  PATH_HOMEPAGE = "//*[contains(@resource-id, 'id/webview)]"
  PLAY_MINUTES = 3
  PATH_NAV = "//*[contains(@content-desc, 'Open navigation drawer')]"
  PATH_BTN_SEARCH = "//*[contains(@resource-id, 'id/action_bar_search')]"
  PATH_ET_SEARCH = "//*[contains(@resource-id, 'id/search_src_text')]"
  PATH_MUSIC_1ST = "//*[contains(@resource-id, 'id/view_model_list')]/android.widget.FrameLayout[@index=1]"
  PATH_BTN_PROFILE_PLAY = "//*[contains(@resource-id, 'id/profile_primary_button')]"
  # id/mini_player_button_pause
  # id/mini_player_button_play
  # id/mini_player_button_stop
  # Navigate up


class C_Messaging(object):

  APP = [
    "Messaging",
    "com.android.mms",
    ".ui.ConversationList"
  ]

  PREFIX = 'test_SMS_M*'
  PREFIX_O = 'test_SMS_MO'
  PREFIX_T = 'test_SMS_MT'
  PHONE_NUM = "13621872145"
  REF_PHONE_NUM = "14782305348"
  DEFAULT_MSG = "Something you want to send."
  DEFAULT_SUBJECT = "Subject"
  PATH_BTN_EXIT = "//*[contains(@resource-id, 'id/exit')]"
  PATH_BTN_NEXT = "//*[contains(@resource-id, 'id/next')]"
  PATH_BTN_MMS_SEARCH = "//*[contains(@resource-id, 'id/search')]"
  PATH_MORE_OPTIONS = "//*[contains(@content-desc, 'More options')]"
  PATH_NAVIGATE_UP = "//*[contains(@content-desc, 'Navigate up')]"
  PATH_BTN_CREATE = "//*[contains(@resource-id, 'id/create')]"
  PATH_RECIPIENTS = "//*[contains(@resource-id, 'id/recipients_editor')]"
  PATH_RECIPIENTS_PICKER = "//*[contains(@resource-id, 'id/recipients_picker')]"
  PATH_TEXT_EDITOR = "//*[contains(@resource-id, 'id/embedded_text_editor')]"
  PATH_BTN_SEND_SMS = "//*[contains(@resource-id, 'id/send_button_sms')]"
  PATH_BTN_SEND_MMS = "//*[contains(@resource-id, 'id/send_button_mms')]"
  PATH_ADD_ATTACH = "//*[contains(@resource-id, 'id/add_attachment_first')]"
  PATH_ATTACH_SUBJECT = "//*[contains(@resource-id, 'id/attachment_selector_image')]"
  PATH_ET_SUBJECT = "//*[contains(@resource-id, 'id/subject')]"


class C_Camera(object):
  
  APP = [
    "Camera",
    "org.codeaurora.snapcam",
    "com.android.camera.CameraLauncher"
  ]

  PREFIX = 'test_take_picture'
  PATH_BTN_OK = "//*[contains(@text, 'OK')]"
  PATH_BTN_YES = "//*[contains(@text, 'Yes')]"
  PATH_SHUTTER = "//*[contains(@resource-id, 'id/shutter_button')]"
  PATH_CAMERA_SWITCHER = "//*[contains(@resource-id, 'id/camera_switcher')]"
  PATH_PHOTO_SWITCHER = "//*[contains(@content-desc, 'Switch to photo')]"
  PATH_VIDEO_SWITCHER = "//*[contains(@content-desc, 'Switch to video')]"
  PATH_PANORAMA_SWITCHER = "//*[contains(@content-desc, 'Switch to panorama')]"


class C_Browser(object):
  
  APP = [
    'GoogleChrome',
    "com.android.chrome",
    "org.chromium.chrome.browser.ChromeTabbedActivity"
  ]

  PREFIX = 'test_ten_websites'
  PATH_CHECKBOX_SEND_REPORT = "//*[contains(@resource-id, 'id/send_report_checkbox')]"
  PATH_BTN_TERMS_ACCEPT = "//*[contains(@resource-id, 'id/terms_accept')]"
  PATH_BTN_NEGATIVE = "//*[contains(@resource-id, 'id/negative_button')]"
  PATH_BTN_POSITIVE = "//*[contains(@resource-id, 'id/positive_button')]"
  PATH_BTN_CHANGE_SEARCH = "//*[contains(@resource-id, 'id/button_primary')]"
  PATH_BTN_UNCHANGE_SEARCH = "//*[contains(@resource-id, 'id/button_secondary')]"
  PATH_SEARCH_BOX = "//*[contains(@resource-id, 'id/search_box_text')]"
  PATH_URL_BAR = "//*[contains(@resource-id, 'id/url_bar')]"
  PATH_BTN_URL_BAR_DELETE = "//*[contains(@resource-id, 'id/delete_button')]"

  SITES = [
    "https://www.bing.com",
    "https://www.google.com",
    "https://www.facebook.com",
    "https://mobile.twitter.com",
    "https://m.youtube.com",
    "https://www.wikipedia.org",
    "https://m.ebay.com",
    "https://www.amazon.com",
    "https://dribbble.com/",
    "https://www.baidu.com"
  ]

class C_Youtube(object):
  
  APP = [
    "Youtube",
    "com.google.android.youtube",
    "com.google.android.apps.youtube.app.application.Shell$HomeActivity"
  ]
  
  PREFIX = 'test_video_network'
  PLAY_MINUTES = 3
  PATH_HOME_1ST_VIDEO = "//*[contains(@resource-id, 'id/results')]/android.widget.FrameLayout[@index=0]/android.widget.LinearLayout[@index=0]"
  PATH_HOME_VIDEOS = "//*[contains(@resource-id, 'id/event_item')]"
